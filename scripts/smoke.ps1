# Smoke test: health + cria pedido de exemplo.
# Uso: .\scripts\smoke.ps1
#      .\scripts\smoke.ps1 -BaseUrl http://localhost:10001
param(
    [string]$BaseUrl = "http://localhost:10001"
)
$ErrorActionPreference = "Stop"

function Invoke-Json {
    param(
        [string]$Method,
        [string]$Uri,
        [object]$Body = $null
    )
    if ($null -ne $Body) {
        $json = $Body | ConvertTo-Json -Depth 6 -Compress
        return Invoke-RestMethod -Method $Method -Uri $Uri -ContentType "application/json" -Body $json
    }
    return Invoke-RestMethod -Method $Method -Uri $Uri
}

Write-Host "==> Smoke StudyShop ($BaseUrl)" -ForegroundColor Cyan

Write-Host "`n[1/3] GET /api/health"
$health = Invoke-Json -Method GET -Uri "$BaseUrl/api/health"
Write-Host ("  overall={0}" -f $health.overall)
$health.services | ForEach-Object {
    Write-Host ("  - {0}: {1}" -f $_.service, $_.status)
}
if ($health.overall -ne "UP") {
    Write-Host "Health DEGRADED/DOWN — abortando create order." -ForegroundColor Yellow
    exit 1
}

Write-Host "`n[2/3] GET /api/products"
$products = Invoke-Json -Method GET -Uri "$BaseUrl/api/products"
Write-Host ("  produtos={0}" -f $products.Count)
if ($products.Count -lt 1) {
    throw "Nenhum produto retornado"
}
$sample = $products | Where-Object { $_.productId -eq "prod-mouse" } | Select-Object -First 1
if (-not $sample) { $sample = $products[0] }

Write-Host "`n[3/3] POST /api/orders (produto=$($sample.productId))"
$orderBody = @{
    customerEmail       = "smoke@studyshop.local"
    forcePaymentFailure = $false
    items               = @(
        @{ productId = $sample.productId; quantity = 1 }
    )
}
$order = Invoke-Json -Method POST -Uri "$BaseUrl/api/orders" -Body $orderBody
Write-Host ("  orderId={0} status={1} total={2}" -f $order.orderId, $order.status, $order.total)

Write-Host "`nGET /api/orders/$($order.orderId)"
$got = Invoke-Json -Method GET -Uri "$BaseUrl/api/orders/$($order.orderId)"
Write-Host ("  status={0} reason={1}" -f $got.status, $got.statusReason)

Write-Host "`nSmoke OK." -ForegroundColor Green
