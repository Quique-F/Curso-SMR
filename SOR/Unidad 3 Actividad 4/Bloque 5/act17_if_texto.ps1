$estado = "bloqueado"

if ($estado -eq "activo") {
    Write-Host "La cuenta está operativa." -ForegroundColor Green
}


elseif ($estado -eq "inactivo") {
    Write-Host "La cuenta está temporalmente fuera de servicio." -ForegroundColor Yellow
}


elseif ($estado -eq "bloqueado") {
    Write-Host "ALERTA: La cuenta ha sido bloqueada por seguridad." -ForegroundColor Red
}


else {
    Write-Host "Estado no reconocido."
}