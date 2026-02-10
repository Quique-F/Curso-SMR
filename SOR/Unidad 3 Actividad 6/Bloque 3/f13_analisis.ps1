function Get-Analisis($ruta) {
    Get-ChildItem $ruta | Select-Object Name, @{Name="KB"; Expression={$_.Length / 1KB}}
}

Get-Analisis "."