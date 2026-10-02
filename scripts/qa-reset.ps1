# Apaga volumes do lab (Mongo e Grafana) e sobe de novo.
# Uso consciente: o seed de produtos volta; pedidos somem.
param([switch]$Yes)
$ErrorActionPreference = "Stop"
if (-not $Yes) {
    Write-Host "Isto apaga o volume do Mongo do oraculo. Rode de novo com -Yes se for o que voce quer."
    exit 1
}
& "$PSScriptRoot\down.ps1" -Volumes
& "$PSScriptRoot\up.ps1"
