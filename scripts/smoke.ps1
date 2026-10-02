# Smoke autenticado (JWT local) com espera da saga.
# Uso: .\scripts\smoke.ps1
#      .\scripts\smoke.ps1 -BaseUrl http://localhost:11001
param(
    [string]$BaseUrl = "http://localhost:11001",
    [string]$QaUser = "qa",
    [string]$QaPass = "qa123",
    [string]$AdminUser = "admin",
    [string]$AdminPass = "admin123",
    [int]$TimeoutSec = 60
)
$ErrorActionPreference = "Stop"

function Invoke-Json {
    param(
        [string]$Method,
        [string]$Uri,
        [object]$Body = $null,
        [string]$Token = $null
    )
    $headers = @{ Accept = "application/json" }
    if ($Token) { $headers.Authorization = "Bearer $Token" }

    $params = @{
        Method      = $Method
        Uri         = $Uri
        Headers     = $headers
        ContentType = "application/json"
    }
    if ($null -ne $Body) {
        $params.Body = ($Body | ConvertTo-Json -Depth 6 -Compress)
    }
    return Invoke-RestMethod @params
}

function Get-StatusCode {
    param(
        [string]$Method,
        [string]$Uri,
        [string]$Token = $null,
        [string]$Body = $null
    )
    try {
        $headers = @{ Accept = "application/json" }
        if ($Token) { $headers.Authorization = "Bearer $Token" }
        $params = @{
            Method          = $Method
            Uri             = $Uri
            Headers         = $headers
            ContentType     = "application/json"
            UseBasicParsing = $true
        }
        if ($Body) { $params.Body = $Body }
        $resp = Invoke-WebRequest @params
        return [int]$resp.StatusCode
    } catch {
        $resp = $_.Exception.Response
        if ($null -eq $resp) { throw }
        return [int]$resp.StatusCode
    }
}

function Wait-OrderStatus {
    param(
        [string]$OrderId,
        [string]$Token,
        [string]$Expected
    )
    $deadline = (Get-Date).AddSeconds($TimeoutSec)
    $last = $null
    do {
        $last = Invoke-Json -Method GET -Uri "$BaseUrl/api/orders/$OrderId" -Token $Token
        Write-Host ("      poll {0} -> {1}" -f $OrderId, $last.status)
        if ($last.status -eq $Expected) { return $last }
        if ($last.status -eq "CONFIRMED" -or $last.status -eq "CANCELLED") {
            throw "Estado final inesperado: $($last.status) (esperado $Expected). motivo=$($last.statusReason)"
        }
        Start-Sleep -Seconds 1
    } while ((Get-Date) -lt $deadline)
    throw "Timeout de ${TimeoutSec}s esperando $Expected; ultimo=$($last.status)"
}

Write-Host "==> Smoke StudyShop ($BaseUrl)" -ForegroundColor Cyan

Write-Host "`n[1/9] GET /api/health (publico)"
$health = Invoke-Json -Method GET -Uri "$BaseUrl/api/health"
Write-Host ("  overall={0}" -f $health.overall)
if ($health.overall -ne "UP") {
    Write-Host "Health DEGRADED/DOWN - abortando." -ForegroundColor Yellow
    exit 1
}

Write-Host "`n[2/9] GET /api/products sem token (esperado 401)"
$codeAnon = Get-StatusCode -Method GET -Uri "$BaseUrl/api/products"
Write-Host ("  HTTP {0}" -f $codeAnon)
if ($codeAnon -ne 401) { throw "Esperado 401 sem token, veio $codeAnon" }

Write-Host "`n[3/9] POST /api/auth/login (qa)"
$loginQa = Invoke-Json -Method POST -Uri "$BaseUrl/api/auth/login" -Body @{
    username = $QaUser
    password = $QaPass
}
$tokenQa = $loginQa.accessToken
if (-not $tokenQa) { throw "Login qa falhou" }
Write-Host ("  roles={0}" -f ($loginQa.roles -join ","))

Write-Host "`n[4/9] GET /api/products (Bearer qa)"
$products = Invoke-Json -Method GET -Uri "$BaseUrl/api/products" -Token $tokenQa
Write-Host ("  produtos={0}" -f @($products).Count)
if (@($products).Count -lt 1) { throw "Nenhum produto retornado" }

Write-Host "`n[5/9] POST /api/orders e espera CONFIRMED"
$order = Invoke-Json -Method POST -Uri "$BaseUrl/api/orders" -Token $tokenQa -Body @{
    customerEmail       = "smoke@studyshop.local"
    forcePaymentFailure = $false
    items               = @(@{ productId = "prod-mouse"; quantity = 1 })
}
Write-Host ("  orderId={0} status={1}" -f $order.orderId, $order.status)
$confirmed = Wait-OrderStatus -OrderId $order.orderId -Token $tokenQa -Expected "CONFIRMED"

Write-Host "`n[6/9] PUT stock: qa=403, admin=200"
$codeQa = Get-StatusCode -Method PUT -Uri "$BaseUrl/api/products/prod-mouse/stock" -Token $tokenQa -Body '{"quantity":50}'
Write-Host ("  qa PUT stock -> HTTP {0}" -f $codeQa)
if ($codeQa -ne 403) { throw "Esperado 403 para USER no stock, veio $codeQa" }

$loginAdmin = Invoke-Json -Method POST -Uri "$BaseUrl/api/auth/login" -Body @{
    username = $AdminUser
    password = $AdminPass
}
$stock = Invoke-Json -Method PUT -Uri "$BaseUrl/api/products/prod-mouse/stock" -Token $loginAdmin.accessToken -Body @{ quantity = 50 }
Write-Host ("  admin PUT stock -> quantity={0}" -f $stock.quantity)

Write-Host "`n[7/9] Falha de pagamento -> CANCELLED"
$failed = Invoke-Json -Method POST -Uri "$BaseUrl/api/orders" -Token $tokenQa -Body @{
    customerEmail       = "smoke-fail@studyshop.local"
    forcePaymentFailure = $true
    items               = @(@{ productId = "prod-mouse"; quantity = 1 })
}
$failedFinal = Wait-OrderStatus -OrderId $failed.orderId -Token $tokenQa -Expected "CANCELLED"
Write-Host ("  motivo={0}" -f $failedFinal.statusReason)

Write-Host "`n[8/9] prod-raro quantidade 2 -> CANCELLED"
Invoke-Json -Method PUT -Uri "$BaseUrl/api/products/prod-raro/stock" -Token $loginAdmin.accessToken -Body @{ quantity = 1 } | Out-Null
$rare = Invoke-Json -Method POST -Uri "$BaseUrl/api/orders" -Token $tokenQa -Body @{
    customerEmail       = "smoke-rare@studyshop.local"
    forcePaymentFailure = $false
    items               = @(@{ productId = "prod-raro"; quantity = 2 })
}
$rareFinal = Wait-OrderStatus -OrderId $rare.orderId -Token $tokenQa -Expected "CANCELLED"
Write-Host ("  motivo={0}" -f $rareFinal.statusReason)

Write-Host "`n[9/9] GET notificacao do pedido confirmado"
$notes = @(Invoke-Json -Method GET -Uri "$BaseUrl/api/notifications/order/$($confirmed.orderId)" -Token $tokenQa)
Write-Host ("  notificacoes={0}" -f $notes.Count)
if ($notes.Count -lt 1) { throw "Esperada ao menos uma notificacao para $($confirmed.orderId)" }

Write-Host "`nSmoke OK." -ForegroundColor Green
