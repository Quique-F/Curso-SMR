
$num1 = 150

$num2 = 200


Write-Host "Comparando $num1 y $num2..."

# 1. ¿Iguales? (-eq)
if ($num1 -eq $num2) { Write-Host "Los números son iguales." } else { Write-Host "Los números son diferentes." }

# 2. ¿Mayor que? (-gt)
if ($num1 -gt $num2) { Write-Host "$num1 es mayor que $num2." }

# 3. ¿Dentro de rango? (Entre 1 y 50)
if ($num1 -ge 1 -and $num1 -le 50) {
    Write-Host "El número $num1 está dentro del rango permitido (1-50)."
}

