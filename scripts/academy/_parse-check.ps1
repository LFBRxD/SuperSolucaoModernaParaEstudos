$files = @(
    "E:\projetos\SuperSolucaoModernaParaEstudos\scripts\smoke.ps1",
    "E:\projetos\SuperSolucaoModernaParaEstudos\scripts\qa-reset.ps1",
    "E:\projetos\SuperSolucaoModernaParaEstudos\scripts\academy\validate-checkpoint.ps1",
    "E:\projetos\SuperSolucaoModernaParaEstudos\scripts\academy\validate-challenge.ps1"
)
$bad = 0
foreach ($f in $files) {
    $tokens = $null
    $errors = $null
    [void][System.Management.Automation.Language.Parser]::ParseFile($f, [ref]$tokens, [ref]$errors)
    if ($errors -and $errors.Count -gt 0) {
        Write-Host "FAIL $f"
        $errors | ForEach-Object { Write-Host $_.ToString() }
        $bad++
    } else {
        Write-Host "OK $f"
    }
}
if ($bad -gt 0) { exit 1 }
