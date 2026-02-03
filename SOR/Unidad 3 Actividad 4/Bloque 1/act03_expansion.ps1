# Actividad 3 – Expansión de variables y comillas


$archivo = "datos_config.txt"


Write-Host 'Comillas simples: El archivo es $archivo'
Write-Host "Comillas dobles: El archivo es $archivo"


<# 
DESCRIPCIÓN:
1. Comillas simples (' '): Son literales. No procesan el símbolo '$', 
   por lo que muestran el nombre de la variable tal cual.
2. Comillas dobles (" "): Permiten la expansión. El motor de PowerShell 
   busca el símbolo '$', identifica la variable y la sustituye por su valor.
#>