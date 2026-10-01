# Sobe a stack Docker Compose do StudyShop (lab QA).
# Uso: .\scripts\up.ps1
$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $PSScriptRoot
$InfraDir = Join-Path $RepoRoot "infra"

Write-Host "==> StudyShop up (docker compose)" -ForegroundColor Cyan
Set-Location $InfraDir
docker compose up -d --build

Write-Host ""
Write-Host "Servicos:" -ForegroundColor Green
Write-Host "  Web:          http://localhost:3000"
Write-Host "  API Gateway:  http://localhost:8080"
Write-Host "  Swagger:      http://localhost:8080/swagger-ui.html"
Write-Host "  Health:       http://localhost:8080/api/health"
Write-Host "  Grafana:      http://localhost:3001  (admin/admin)"
Write-Host "  Jaeger:       http://localhost:16686"
Write-Host "  Prometheus:   http://localhost:9090"
Write-Host ""
Write-Host "Smoke: .\scripts\smoke.ps1"
