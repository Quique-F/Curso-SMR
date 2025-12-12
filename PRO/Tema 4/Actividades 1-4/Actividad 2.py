
frase = input("Introduce una frase: ")

# Separar las palabras usando split()
palabras = frase.split()

# Mostrar cada palabra en una línea
for palabra in palabras:
    print(palabra)

# Mostrar el número de palabras
print(f"\nNúmero de palabras: {len(palabras)}")
