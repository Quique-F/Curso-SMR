function New-CarpetaSegura($nombre) {
    if (-Not (Test-Path $nombre)) {
        New-Item -Path $nombre -ItemType Directory
    }
}
New-CarpetaSegura "MiCarpeta"