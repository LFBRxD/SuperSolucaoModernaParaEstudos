# Sobe a stack Docker Compose do StudyShop (lab QA).
# Uso: .\scripts\up.ps1
$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $PSScriptRoot
$InfraDir = Join-Path $RepoRoot "infra"

Write-Host "==> StudyShop up (docker compose)" -ForegroundColor Cyan
Set-Location $InfraDir
docker compose up -d --build

Write-Host ""
Write-Host "Servicos (portas a partir de 10000):" -ForegroundColor Green
Write-Host "  Web:          http://localhost:10000"
Write-Host "  API Gateway:  http://localhost:10001"
Write-Host "  Swagger:      http://localhost:10001/swagger-ui.html"
Write-Host "  Health:       http://localhost:10001/api/health"
Write-Host "  Orders HTTP:  http://localhost:10002"
Write-Host "  Orders gRPC:  localhost:10003"
Write-Host "  Inventory:    http://localhost:10004  gRPC:10005"
Write-Host "  Payments:     http://localhost:10006"
Write-Host "  Notifications:http://localhost:10007"
Write-Host "  MongoDB:      localhost:10008"
Write-Host "  Kafka:        localhost:10009"
Write-Host "  Grafana:      http://localhost:10010  (admin/admin)"
Write-Host "  Jaeger:       http://localhost:10011"
Write-Host "  Prometheus:   http://localhost:10012"
Write-Host "  OTel gRPC/HTTP: 10013 / 10014"
Write-Host ""
Write-Host "Smoke: .\scripts\smoke.ps1"
