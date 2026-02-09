$archivos = "nota.txt", "foto.jpg", "doc.txt"
foreach ($a in $archivos) {
    if ($a -like "*.txt") { "$a es TXT" } else { "$a es OTRO" }
}