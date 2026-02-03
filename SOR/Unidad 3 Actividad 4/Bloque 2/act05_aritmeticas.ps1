# Simulación de recursos de disco (en GB)


$discoTotal = 500
$discoUsado = 320

#Cálculos

$discoLibre = $discoTotal - $discoUsado

$porcentaje = ($discoUsado /$discoTotal) * 100

# Resultados
Write-Host "--- ESTADO DEL DISCO ---"
Write-Host "Espacio Total: $discoTotal GB"
Write-Host "Espacio Usado: $discoUsado GB"
Write-Host "Espacio Libre: $discoLibre GB"
Write-Host "Porcentaje de Uso: $porcentaje %"

