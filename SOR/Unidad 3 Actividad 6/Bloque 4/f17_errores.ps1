function Get-Revision($ruta) {
    if (Test-Path $ruta) {
        Get-ChildItem $ruta
    } else {
        Write-Error "La ruta no existe"
    }
}

Get-Revision "C:\RutaFalsa"