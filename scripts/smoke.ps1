# Smoke autenticado (JWT local).
# Uso: .\scripts\smoke.ps1
#      .\scripts\smoke.ps1 -BaseUrl http://localhost:11001
param(
    [string]$BaseUrl = "http://localhost:11001",
    [string]$QaUser = "qa",
    [string]$QaPass = "qa123",
    [string]$AdminUser = "admin",
    [string]$AdminPass = "admin123"
)
$ErrorActionPreference = "Stop"

function Invoke-Json {
    param(
        [string]$Method,
        [string]$Uri,
        [object]$Body = $null,
        [string]$Token = $null,
        [switch]$SkipHttpErrorCheck
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
    if ($SkipHttpErrorCheck) {
        try {
            return Invoke-RestMethod @params
        } catch {
            $resp = $_.Exception.Response
            if ($null -eq $resp) { throw }
            return [pscustomobject]@{
                StatusCode = [int]$resp.StatusCode
                Error      = $_
            }
        }
    }
    return Invoke-RestMethod @params
}

Write-Host "==> Smoke StudyShop ($BaseUrl)" -ForegroundColor Cyan

Write-Host "`n[1/5] GET /api/health (publico)"
$health = Invoke-Json -Method GET -Uri "$BaseUrl/api/health"
Write-Host ("  overall={0}" -f $health.overall)
if ($health.overall -ne "UP") {
    Write-Host "Health DEGRADED/DOWN - abortando." -ForegroundColor Yellow
    exit 1
}

Write-Host "`n[2/5] POST /api/auth/login (qa)"
$loginQa = Invoke-Json -Method POST -Uri "$BaseUrl/api/auth/login" -Body @{
    username = $QaUser
    password = $QaPass
}
$tokenQa = $loginQa.accessToken
if (-not $tokenQa) { throw "Login qa falhou" }
Write-Host ("  roles={0}" -f ($loginQa.roles -join ","))

Write-Host "`n[3/5] GET /api/products (Bearer qa)"
$products = Invoke-Json -Method GET -Uri "$BaseUrl/api/products" -Token $tokenQa
Write-Host ("  produtos={0}" -f $products.Count)
if ($products.Count -lt 1) { throw "Nenhum produto retornado" }
$sample = $products | Where-Object { $_.productId -eq "prod-mouse" } | Select-Object -First 1
if (-not $sample) { $sample = $products[0] }

Write-Host "`n[4/5] POST /api/orders (Bearer qa)"
$order = Invoke-Json -Method POST -Uri "$BaseUrl/api/orders" -Token $tokenQa -Body @{
    customerEmail       = "smoke@studyshop.local"
    forcePaymentFailure = $false
    items               = @(
        @{ productId = $sample.productId; quantity = 1 }
    )
}
Write-Host ("  orderId={0} status={1}" -f $order.orderId, $order.status)

Write-Host "`n[5/5] PUT stock: qa=403, admin=200"
try {
    Invoke-RestMethod -Method PUT -Uri "$BaseUrl/api/products/$($sample.productId)/stock" `
        -Headers @{ Authorization = "Bearer $tokenQa" } `
        -ContentType "application/json" `
        -Body '{"quantity":50}' | Out-Null
    throw "Esperado 403 para USER no stock"
} catch {
    $code = [int]$_.Exception.Response.StatusCode
    Write-Host ("  qa PUT stock -> HTTP {0}" -f $code)
    if ($code -ne 403) { throw "Esperado 403 para USER no stock, veio $code" }
}

$loginAdmin = Invoke-Json -Method POST -Uri "$BaseUrl/api/auth/login" -Body @{
    username = $AdminUser
    password = $AdminPass
}
$stock = Invoke-Json -Method PUT -Uri "$BaseUrl/api/products/$($sample.productId)/stock" `
    -Token $loginAdmin.accessToken `
    -Body @{ quantity = 50 }
Write-Host ("  admin PUT stock -> quantity={0}" -f $stock.quantity)

Write-Host "`nSmoke OK." -ForegroundColor Green
