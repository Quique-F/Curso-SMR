function New-Archivo($ruta, $nombre) {
    New-Item -Path (Join-Path $ruta $nombre) -ItemType File -Force
}

New-Archivo "." "test.txt"
