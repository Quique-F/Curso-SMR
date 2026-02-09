$texto = "PowerShell es genial y potente"
foreach ($p in $texto.Split(" ")) {
    if ($p.Length -gt 5) { $p }
}