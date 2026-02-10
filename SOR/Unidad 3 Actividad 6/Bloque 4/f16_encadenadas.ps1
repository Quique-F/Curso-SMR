function New-Todo($dir, $file, $txt) {
    New-Item -Path $dir -ItemType Directory -Force
    Set-Content -Path (Join-Path $dir $file) -Value $txt
}

New-Todo "Backup" "log.txt" "Inicio de copia"