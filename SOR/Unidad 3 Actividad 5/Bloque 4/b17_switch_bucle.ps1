do {
    $op = Read-Host "A o B?"
} while ($op -notin "A","B")
"Elegiste $op"
