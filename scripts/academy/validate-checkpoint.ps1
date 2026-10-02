# Valida checkpoints do projeto espelho (estrutura e README, nao estilo).
# $env:ACADEMY_PROJECT_DIR = caminho do studyshop-do-zero
param(
    [Parameter(Mandatory = $true)]
    [string]$Checkpoint
)
$ErrorActionPreference = "Stop"
$dir = $env:ACADEMY_PROJECT_DIR
if (-not $dir -or -not (Test-Path $dir)) {
    Write-Error "Defina ACADEMY_PROJECT_DIR para a pasta do espelho."
    exit 1
}

function Has-Text([string]$pattern) {
    $files = Get-ChildItem -Path $dir -Recurse -File -ErrorAction SilentlyContinue |
        Where-Object { $_.Extension -match '^\.(md|java|yml|yaml|xml|proto)$' }
    foreach ($f in $files) {
        if (Select-String -Path $f.FullName -Pattern $pattern -SimpleMatch -Quiet) { return $true }
    }
    return $false
}

$checks = @{
    bootstrap = {
        (Test-Path (Join-Path $dir "pom.xml")) -and (Test-Path (Join-Path $dir "src\main\java"))
    }
    "catalog-api" = { (Has-Text "11101") -or (Has-Text "/api/products") }
    "orders-mongo" = {
        $ymlHit = Get-ChildItem -Path $dir -Recurse -File -Filter "application*.yml" -ErrorAction SilentlyContinue |
            Select-String -Pattern "11008" -SimpleMatch -Quiet
        (Has-Text "11108") -and -not $ymlHit
    }
    "grpc-gateway" = { (Get-ChildItem -Path $dir -Recurse -Filter *.proto -ErrorAction SilentlyContinue | Select-Object -First 1) -ne $null }
    "kafka-events" = { (Has-Text "eventType") -or (Has-Text ".events") }
    saga = { Has-Text "CONFIRMED" }
    "scheduled-jobs" = { (Has-Text "quartz") -and (Has-Text "@Scheduled") }
    "web-auth" = { (Has-Text "401") -or (Has-Text "SecurityFilterChain") }
    observability = { (Has-Text "otel") -or (Has-Text "log") }
    "automation-ci" = { Has-Text "mvn test" }
    platform = {
        (Get-ChildItem -Path $dir -Recurse -Filter Dockerfile -ErrorAction SilentlyContinue | Select-Object -First 1) -ne $null -or
        (Get-ChildItem -Path $dir -Recurse -Filter "compose*.yml" -ErrorAction SilentlyContinue | Select-Object -First 1) -ne $null -or
        (Has-Text "Dockerfile")
    }
}

$names = @($checks.Keys)
if ($Checkpoint -ne "all") {
    if (-not $checks.ContainsKey($Checkpoint)) { throw "Checkpoint desconhecido: $Checkpoint" }
    $names = @($Checkpoint)
}

$failed = 0
foreach ($name in ($names | Sort-Object)) {
    $ok = & $checks[$name]
    if ($ok) {
        Write-Host "OK  $name"
    } else {
        Write-Host "FALHOU  $name"
        $failed++
    }
}
if ($failed -gt 0) { exit 1 }
Write-Host "Checkpoints verdes: $($names.Count)"
