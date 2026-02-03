$archivoCompleto = "memoria _final.pdf"


# Buscamos la posición del punto

$posicionPunto = $archivoCompleto.LastIndexOf(".")

# Lo extraemos

$SinExtension = $archivoCompleto.Substring(0,$posicionPunto)
$extension = $archivoCompleto.Substring($posicionPunto)

# Mostrar resultados
Write-Host "Nombre del archivo: $archivoCompleto"
Write-Host "Nombre base: $SinExtension"
Write-Host "Extensión:   $extension"

