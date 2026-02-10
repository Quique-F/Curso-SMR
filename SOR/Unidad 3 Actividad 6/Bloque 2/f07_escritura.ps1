function Set-Texto ($ruta , $contenido) {
    Set-Content -Path $ruta -Value $contenido
}

Set-Texto "Test.txt" "Hola no se que poner."
