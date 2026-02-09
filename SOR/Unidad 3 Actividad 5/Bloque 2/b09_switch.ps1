$estados = "activo", "bloqueado"
foreach ($e in $estados) {
    switch ($e) {
        "activo" { "OK" }
        "bloqueado" { "ERROR" }
    }
}