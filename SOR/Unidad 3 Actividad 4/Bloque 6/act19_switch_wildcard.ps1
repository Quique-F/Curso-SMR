
$archivo = ("archivo1.txt")

switch -Wildcard -CaseSensitive ($archivo) {
    "*.txt" { 
        Write-Host "Se ha detectado un archivo de TEXTO plano (.txt)" -ForegroundColor Cyan 
    }
    "*.log" { 
        Write-Host "Se ha detectado un archivo de REGISTRO en minúsculas (.log)" -ForegroundColor Yellow 
    }
    "*.LOG" { 
        Write-Host "¡ALERTA! Se ha detectado un archivo de LOG en MAYÚSCULAS (.LOG)" -ForegroundColor Red 
    }
    Default { 
        Write-Host "El formato del archivo '$archivo' no es .txt ni .log (o no coincide exactamente)." 
    }
}