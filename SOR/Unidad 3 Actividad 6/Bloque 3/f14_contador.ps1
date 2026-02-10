function Get-Conteo($ruta) {
    $items = Get-ChildItem $ruta
    Write-Host "Total elementos: $($items.Count)"
}

Get-Conteo "."