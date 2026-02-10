function write-Mensaje($texto = "Hola mundo") {
    Write-Host "Mensaje: $texto"
}

# Llamada simple
Mostrar-Mensaje
# Llamada con parámetro
Mostrar-Mensaje -texto "Skibidi"