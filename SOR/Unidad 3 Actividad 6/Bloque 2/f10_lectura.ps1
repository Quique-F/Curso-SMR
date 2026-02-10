function Get-Texto($ruta) {
    Get-Content -Path $ruta
}

Get-Texto "Test.txt"
