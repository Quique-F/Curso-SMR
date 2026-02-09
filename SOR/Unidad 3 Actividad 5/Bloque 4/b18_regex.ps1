$lista = "123" , "ABC" , "1A"

foreach ($Algo in $lista) {
    switch - Regex ($Algo) {
      "^\d+$" { "$Algo es número" }
        "^[A-Z]+$" { "$Algo es letra" }
    }
        
}