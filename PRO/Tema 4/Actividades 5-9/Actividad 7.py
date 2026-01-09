alumnos = []

while True:
    nombre = input("Nombre del alumno (o '-' para terminar): ")

    if nombre == "-":
        break

    edad = int(input("Edad del alumno: "))
    alumnos.append((nombre, edad))

print("\n=== Alumnos mayores de edad ===")
mayores = [(n, e) for n, e in alumnos if e >= 18]

if mayores:
    for n, e in mayores:
        print(f"{n} - {e} años")
else:
    print("No hay alumnos mayores de edad.")

print("\n=== Los dos alumnos más mayores ===")
if len(alumnos) >= 2:
    alumnos_ordenados = sorted(alumnos, key=lambda x: x[1], reverse=True)
    for n, e in alumnos_ordenados[:2]:
        print(f"{n} - {e} años")
elif len(alumnos) == 1:
    print(f"Solo hay un alumno: {alumnos[0][0]} - {alumnos[0][1]} años")
else:
    print("No se introdujeron alumnos.")

