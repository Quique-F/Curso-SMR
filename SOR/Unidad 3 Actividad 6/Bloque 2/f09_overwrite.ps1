function Update-Texto ($ruta , $contenido ) {
    Set-Content -Path $ruta -Value $contenido
}
Update-Texto "Test_2.txt" "Aguanta borrando"