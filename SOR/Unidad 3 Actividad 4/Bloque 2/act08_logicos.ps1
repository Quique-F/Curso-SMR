

$edad = 19
$esAdmin = $true


# Evaluación de acceso (Mayor de 18 Y es admin)

if ($edad -ge 18 -and $esAdmin) {
    Write-Host "ACCESO CONCEDIDO: Eres mayor de edad y administrador."
}




# Permisos avanzados (O es admin O tiene una edad especial, ej. > 65)

if ($esAdmin -or $edad -gt 65) {
    Write-Host "PERMISOS AVANZADOS: Tienes privilegios especiales."
} else {
    Write-Host "PERMISOS ESTÁNDAR: No cumples los requisitos avanzados."
}