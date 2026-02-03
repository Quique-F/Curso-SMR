$nota = 8.5 # Ejemplo

if ($nota -lt 5) {
    Write-Host "Resultado: Suspenso" -ForegroundColor Red
}
elseif ($nota -lt 7) {
    Write-Host "Resultado: Aprobado" -ForegroundColor Cyan
}
elseif ($nota -lt 9) {
    Write-Host "Resultado: Notable" -ForegroundColor Blue
}
else {
    Write-Host "Resultado: Sobresaliente" -ForegroundColor Magenta
}