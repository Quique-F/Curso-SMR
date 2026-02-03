

# Solicitamos el dato al usuario

$texto = Read-Host "Introduce un texto"

switch -Regex ($texto) {
    "^[0-9]+$"      { "Solo contiene números" }
    "^[a-zA-Z]+$"   { "Solo contiene letras" }
    "[0-9]"         { if ($texto -match "[a-zA-Z]") { "Es una mezcla" } }
    Default         { "Otro tipo de dato o vacío" }
}