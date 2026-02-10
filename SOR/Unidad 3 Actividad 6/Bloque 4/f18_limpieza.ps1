function Remove-Basura($ruta, $ext) {
    Get-ChildItem $ruta -Filter "*.$ext" | Remove-Item
}

# Remove-Basura "." "tmp"