# Derruba a stack Docker Compose do StudyShop.
# Uso: .\scripts\down.ps1
#      .\scripts\down.ps1 -Volumes   # remove volumes (mongo/grafana)
param(
    [switch]$Volumes
)
$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $PSScriptRoot
$InfraDir = Join-Path $RepoRoot "infra"

Write-Host "==> StudyShop down" -ForegroundColor Cyan
Set-Location $InfraDir

if ($Volumes) {
    docker compose down -v
} else {
    docker compose down
}

Write-Host "Stack parada." -ForegroundColor Green
