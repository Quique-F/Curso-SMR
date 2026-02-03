$empezar = ("start")

switch ($empezar) {
    "start" { Write-Host "Iniciando el servicio..." -ForegroundColor Green }
    "stop"  { Write-Host "Deteniendo el servicio..." -ForegroundColor Red }
    "restart" { Write-Host "Reiniciando el servicio..." -ForegroundColor Yellow }


    Default {Write-Host "Error: Acción no reconocida." -ForegroundColor Gray}
}