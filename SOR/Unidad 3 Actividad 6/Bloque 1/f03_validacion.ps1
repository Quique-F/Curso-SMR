function Test-NumeroPositivo($num) {
    if ($num -gt 0) { return "Válido" } else { return "Inválido" }
}
Write-Host (Test-NumeroPositivo 10)
