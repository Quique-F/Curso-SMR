function Get-ArchivosExt($ruta, $ext) {
    Get-ChildItem -Path $ruta -Filter "*.$ext"
}

Get-ArchivosExt "." "txt"
