# Pedir las dos palabras al usuario
una = input("Introduce la una palabra: ")
dos = input("Introduce la otra palabra: ")

# Comparar palabras
if una == dos:
    print("Son iguales")
elif una.lower() == dos.lower():
    print("Iguales (sin tener en cuenta mayúsculas/minúsculas)")
else:
    print("Diferentes")
