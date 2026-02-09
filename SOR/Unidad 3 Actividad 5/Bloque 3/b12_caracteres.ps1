$cadena = "A1b2C3"
foreach ($c in $cadena.ToCharArray()) {
    if ([char]::IsDigit($c)) { "$c es número" } else { "$c es letra" }
}