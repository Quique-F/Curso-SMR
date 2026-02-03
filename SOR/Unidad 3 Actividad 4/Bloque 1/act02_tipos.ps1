
#Actividad 2 – Tipos de datos y comprobación


# Declaración de tipos

$entero = 10
$decimal = 15.5
$cadena = "Hola PowerShell"
$booleano = $false



# Mostrar valores y tipos

Write-Host "Valor: $entero - Tipo: $($entero.GetType().Name)"
Write-Host "Valor: $decimal - Tipo: $($decimal.GetType().Name)"
Write-Host "Valor: $cadena - Tipo: $($cadena.GetType().Name)"
Write-Host "Valor: $booleano - Tipo: $($booleano.GetType().Name)"



# Modificación de tipo (Casting dinámico)

Write-Host "`n--- Cambiando tipo de variable ---"
$entero = "Ahora soy un texto"
Write-Host "Nuevo valor: $entero - Nuevo tipo: $($entero.GetType().Name)"