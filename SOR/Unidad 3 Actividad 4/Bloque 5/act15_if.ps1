
$usuario = "admin" # Cambia para probar


if ($usuario -eq "admin") {
    Write-Host "ACCESO TOTAL: Bienvenido, Administrador." -ForegroundColor Green
}
else {
    Write-Host "ACCESO LIMITADO: Permisos de usuario estándar." -ForegroundColor Yellow
}