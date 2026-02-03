$ruta = "C:\Proyectos\Scripts\configuracion.json"

# Operaciones
$longitud = $ruta.Length
$mayusculas = $ruta.ToUpper()
$minusculas = $ruta.ToLower()

# Mostrar resultados
Write-Host "Ruta original: $ruta"
Write-Host "1. Longitud: $longitud caracteres."
Write-Host "2. Mayúsculas: $mayusculas"
Write-Host "3. Minúsculas: $minusculas"

<#
UTILIDAD:
- Longitud: Para validar que una ruta no pase el límite de caracteres.
- Mayúsculas/Minúsculas: Para evitar errores por diferencias de escritura.
#>
