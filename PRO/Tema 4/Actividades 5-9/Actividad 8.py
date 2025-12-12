nombres = []
horas = []

while True:
    
    nombre = input("Nombre del trabajador (o '-' para terminar): ")
    
    if nombre == "-":
        break
    
    nombres.append(nombre)

    print(f"Introduce las horas extra semanales de {nombre}: ")
    horas_semana = []

    for i in range(4):
        h = float(input(f"  Semana {i+1}: "))

        horas_semana.append(h)

    horas.append(tuple(horas_semana))




# Calcular el total extra (fuera del while)

total_extras = []



for i in range(len(nombres)):

    total_horas = sum(horas[i])

    total_dinero = total_horas * 16.25

    total_extras.append(total_dinero)




# Mostrar resultados

print("\n=== RESULTADO FINAL ===")
for i in range(len(nombres)):
    print(f"{nombres[i]} -> {total_extras[i]:.2f} € generados en horas extra")
