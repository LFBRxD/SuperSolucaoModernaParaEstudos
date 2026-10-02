# Sobe a stack Docker Compose do StudyShop (lab QA).
# Uso: .\scripts\up.ps1
$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $PSScriptRoot
$InfraDir = Join-Path $RepoRoot "infra"

Write-Host "==> StudyShop up (docker compose)" -ForegroundColor Cyan
Set-Location $InfraDir
docker compose up -d --build

Write-Host ""
Write-Host "Servicos (portas a partir de 11000):" -ForegroundColor Green
Write-Host "  Web:          http://localhost:11000"
Write-Host "  API Gateway:  http://localhost:11001"
Write-Host "  Swagger:      http://localhost:11001/swagger-ui.html"
Write-Host "  Health:       http://localhost:11001/api/health"
Write-Host "  Orders HTTP:  http://localhost:11002"
Write-Host "  Orders gRPC:  localhost:11003"
Write-Host "  Inventory:    http://localhost:11004  gRPC:11005"
Write-Host "  Payments:     http://localhost:11006"
Write-Host "  Notifications:http://localhost:11007"
Write-Host "  MongoDB:      localhost:11008"
Write-Host "  Kafka:        localhost:11009"
Write-Host "  Grafana:      http://localhost:11010  (admin/admin)"
Write-Host "  Jaeger:       http://localhost:11011"
Write-Host "  Prometheus:   http://localhost:11012"
Write-Host "  OTel gRPC/HTTP: 11013 / 11014"
Write-Host ""
Write-Host "Smoke: .\scripts\smoke.ps1"
