
param(
    [string]$Nombre,
    [int]$Edad,
    [string]$Rol
)


Write-Host "Ficha de Usuario:" -Separator "-"
Write-Host "El usuario $Nombre tiene $Edad años y desempeña el rol de $Rol."

