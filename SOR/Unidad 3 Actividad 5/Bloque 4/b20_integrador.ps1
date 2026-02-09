# 1. Parámetros (recibe una lista de nombres)
param($lista = @("user_admin", "archivo.txt", "invitado_web"))

Write-Host "--- INICIO DEL RESUMEN ---"

# 2. Variable de contador (Acumulador)
$total = 0

# 3. Primer bucle: foreach para recorrer la lista
foreach ($item in $lista) {
    
    # 4. Condicional y Switch con Wildcard (comodines)
    switch -Wildcard ($item) {
        "*admin*" { Write-Host "$item es un Administrador" }
        "*.txt"   { Write-Host "$item es un Archivo de texto" }
        "*_web"   { Write-Host "$item es un Usuario Web" }
    }

    $total++ # Contamos cuántos elementos procesamos
}

# 5. Segundo bucle: for simple para mostrar una barra de progreso
for ($i = 1; $i -le 3; $i++) { 
    Write-Host "Finalizando etapa $i..." 
}

# 6. Resumen final
Write-Host "Tarea completada. Total de elementos: $total"
