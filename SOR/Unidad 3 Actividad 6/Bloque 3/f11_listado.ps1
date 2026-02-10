function Get-Lista($ruta) {
    Get-ChildItem -Path $ruta
}

Get-Lista "."