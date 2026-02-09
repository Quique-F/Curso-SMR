$archivos = "test.ps1", "data.csv"
foreach ($a in $archivos) {
    $a.Split(".")
}