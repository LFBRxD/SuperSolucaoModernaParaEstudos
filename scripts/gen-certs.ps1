# Gera CA + certificados PEM (PKCS#8) para mTLS do lab.
# Uso: .\scripts\gen-certs.ps1
$ErrorActionPreference = "Stop"

$opensslCandidates = @(
    "openssl",
    "C:\Program Files\Git\usr\bin\openssl.exe",
    "C:\Program Files\OpenSSL-Win64\bin\openssl.exe"
)
$openssl = $opensslCandidates | Where-Object {
    if ($_ -eq "openssl") {
        return [bool](Get-Command openssl -ErrorAction SilentlyContinue)
    }
    return Test-Path $_
} | Select-Object -First 1

if (-not $openssl) {
    throw "openssl nao encontrado (instale Git for Windows ou OpenSSL)"
}

$root = Split-Path -Parent $PSScriptRoot
$certs = Join-Path $root "infra\certs"
New-Item -ItemType Directory -Force -Path $certs | Out-Null
Set-Location $certs

& $openssl genrsa -out ca.key 4096
& $openssl req -x509 -new -nodes -key ca.key -sha256 -days 3650 -out ca.crt -subj "/CN=StudyShop Lab CA"

foreach ($name in @("gateway", "orders", "inventory")) {
    & $openssl genrsa -out "$name.key.tmp" 2048
    & $openssl req -new -key "$name.key.tmp" -out "$name.csr" -subj "/CN=$name-service"
    $ext = "subjectAltName=DNS:$name-service,DNS:localhost,IP:127.0.0.1`nextendedKeyUsage=serverAuth,clientAuth`n"
    [System.IO.File]::WriteAllText((Join-Path $certs "$name.ext"), $ext)
    & $openssl x509 -req -in "$name.csr" -CA ca.crt -CAkey ca.key -CAcreateserial `
        -out "$name.crt" -days 825 -sha256 -extfile "$name.ext"
    & $openssl pkcs8 -topk8 -nocrypt -in "$name.key.tmp" -out "$name.key"
    Remove-Item "$name.key.tmp", "$name.csr", "$name.ext" -ErrorAction SilentlyContinue
}

Remove-Item "ca.srl" -ErrorAction SilentlyContinue
Write-Host "Certificados em $certs" -ForegroundColor Green
Get-ChildItem | Format-Table Name, Length
