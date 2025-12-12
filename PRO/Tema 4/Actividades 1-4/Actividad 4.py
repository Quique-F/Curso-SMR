
while True:
    print("\n=== Validación de datos ===")

    nombre = input("Nombre y apellidos (3 palabras, inicial mayúscula): ")
    edad = input("Edad (número): ")
    telefono = input("Teléfono (9 dígitos): ")
    nick = input("Nickname (alfanumérico): ")

    errores = []

    # Validación del nombre: 3 palabras y cada una empieza por mayúscula
    partes = nombre.split()
    if len(partes) != 3 or not all(p[0].isupper() and p[1:].islower() for p in partes):
        errores.append("Nombre y Apellidos")

    # Validar edad: solo números
    if not edad.isdigit():
        errores.append("Edad")

    # Validar teléfono: 9 dígitos
    if not (telefono.isdigit() and len(telefono) == 9):
        errores.append("Teléfono")

    # Validar nickname: solo letras y números
    if not nick.isalnum():
        errores.append("Nickname")

    # Resultado final
    if not errores:
        print("\n✔ Todos los datos son válidos.")
    else:
        print("\n❌ Datos incorrectos:")
        for e in errores:
            print(" -", e)

    # Preguntar si se repite
    if input("\n¿Validar otros datos? (s/n): ").lower() != 's':
        print("Fin del programa.")
        break
