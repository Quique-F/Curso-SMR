

param(
    [Parameter(Mandatory=$true)]
    [string]$Archivo,

    [string]$Modo = "Lectura"
)

Write-Host "Accediendo al archivo: $Archivo"
Write-Host "Modo de acceso: $Modo"
