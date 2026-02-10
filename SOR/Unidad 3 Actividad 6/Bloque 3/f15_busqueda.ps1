function Search-Contenido($ruta, $texto) {
    Select-String -Path "$ruta\*.txt" -Pattern $texto
}

Search-Contenido "." "borrando"