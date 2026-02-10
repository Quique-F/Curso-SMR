param($miRuta, $miExt)

function Get-Filtro($r, $e) {
    Get-ChildItem $r -Filter "*.$e"
}

Get-Filtro $miRuta $miExt