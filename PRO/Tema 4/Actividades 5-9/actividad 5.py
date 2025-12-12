import random

# Crear lista con 5 valores aleatorios entre 1 y 10
lista = [random.randint(1, 10) for _ in range(5)]

print("Lista generada:", lista)

# Mostrar unidades, decenas y miles de cada número
for numero in lista:
    unidades = numero % 10
    decenas = (numero // 10) % 10
    miles = (numero // 1000) % 10

    print(f"\nNúmero: {numero}")
    print(f"  Unidades: {unidades}")
    print(f"  Decenas : {decenas}")
    print(f"  Miles   : {miles}")
