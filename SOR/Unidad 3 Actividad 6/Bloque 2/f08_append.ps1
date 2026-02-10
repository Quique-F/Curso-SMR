function Add-Texto ($ruta , $contenido ) {
    Add-Content -Path $ruta -Value $contenido
}
Add-Texto "Test_2.txt" "Más cosas ns"