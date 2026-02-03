

# Variables de usuario

$nombre = "Quique"
$apellidos = "Ferri Martinez"
$departamento = "Ciberseguridad"



# Construcción del mensaje (Concatenación por expansión)

$mensajeFinal = "FICHA DE EMPLEADO:`n"
$mensajeFinal += "------------------`n"
$mensajeFinal += "Nombre completo: $nombre $apellidos`n"
$mensajeFinal += "Departamento:    $departamento"



# Mostrar el resultado
Write-Host $mensajeFinal -ForegroundColor Cyan