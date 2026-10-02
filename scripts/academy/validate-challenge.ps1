# Desafios: webhook, quartz e dlq olham o espelho.
# mtls olha o oraculo (este repositorio).
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet("webhook", "quartz", "dlq", "mtls")]
    [string]$Name
)
$ErrorActionPreference = "Stop"
$repo = Split-Path (Split-Path $PSScriptRoot -Parent) -Parent
if ($Name -eq "mtls") {
    $need = @(
        "infra\docker-compose.mtls.yml",
        "docs\tutoriais\03-mtls-grpc.md",
        "infra\certs\ca.crt",
        "apps\api-gateway\src\main\resources\application-mtls.yml"
    )
    $missing = @($need | Where-Object { -not (Test-Path (Join-Path $repo $_)) })
    if ($missing.Count -gt 0) {
        Write-Host "FALHOU mtls. Ausente:"
        $missing | ForEach-Object { Write-Host "  $_" }
        exit 1
    }
    Write-Host "OK  mtls (arquivos do oraculo)"
    exit 0
}
$dir = $env:ACADEMY_PROJECT_DIR
if (-not $dir -or -not (Test-Path $dir)) {
    Write-Error "Defina ACADEMY_PROJECT_DIR."
    exit 1
}
function Has([string]$pattern) {
    $files = Get-ChildItem -Path $dir -Recurse -File -ErrorAction SilentlyContinue |
        Where-Object { $_.Extension -match '^\.(md|java|yml|yaml|xml)$' }
    foreach ($f in $files) {
        if (Select-String -Path $f.FullName -Pattern $pattern -SimpleMatch -Quiet) { return $true }
    }
    return $false
}
$ok = switch ($Name) {
    webhook { (Has "X-Signature") -and (Has "11180") }
    quartz { (Has "quartz") -and (Has "@Scheduled") }
    dlq { (Has "dlq") -or (Has "dead_letter") }
}
if ($ok) { Write-Host "OK  $Name"; exit 0 }
Write-Host "FALHOU $Name"
exit 1
