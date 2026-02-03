import time
from colorama import init, Fore

init(autoreset=True)

# ======================================================
# LISTA GLOBAL DE ALUMNOS
# ======================================================
alumnos = []

# ======================================================
# MENÚ
# ======================================================
def menu1():
    centro = "CIPFP Luís Suñer Sanchis"
    print(Fore.CYAN + "-- Control de Promoción del CIPFP Luís Suñer Sanchis --")
    time.sleep(1)
    print(Fore.YELLOW + "+-----------------------------------------------------+")
    print(Fore.YELLOW + "|----------------Entrando en el sistema --------------|")
    print(Fore.YELLOW + "|----------------------- Cargando... -----------------|")
    print(Fore.YELLOW + "+-----------------------------------------------------+")
    time.sleep(2)
    print(Fore.CYAN + "+--------------- Hola, BIENVENIDO/A ------------------+")
    print(Fore.CYAN + f"|====== Registro de alumnado en {centro} ======|")
    print(Fore.YELLOW + "+-----------------------------------------------------+")

# ======================================================
# GUARDAR ALUMNO
# ======================================================
def guardar_alumno(nombre, apellidos, edad, media, asistencia):
    promociona = media >= 5 and asistencia >= 85
    alumnos.append({
        "nombre": nombre,
        "apellidos": apellidos,
        "edad": edad,
        "media": media,
        "asistencia": asistencia,
        "promociona": promociona
    })
    # No imprimimos nada aquí para evitar duplicados

# ======================================================
# MOSTRAR LISTA + INFORME FINAL (solo una vez)
# ======================================================
def mostrar_lista_y_informe():
    print()  # espacio arriba

    # Lista final
    print(Fore.YELLOW + "📋 LISTA FINAL DE ALUMNOS")
    print(Fore.YELLOW + "-" * 40)

    for i, alumno in enumerate(alumnos, 1):
        estado = "Sí" if alumno["promociona"] else "No"
        print(Fore.CYAN + f"{i}. {alumno['nombre']} {alumno['apellidos']} | Edad: {alumno['edad']} | Promociona: {estado}")

    print(Fore.GREEN + "\nPrograma finalizado ✔️")
    print(Fore.YELLOW + "-" * 40)  # separador antes del informe

    # Informe final
    print(Fore.YELLOW + "+=====================================================+")
    print(Fore.YELLOW + "|================= INFORME FINAL =====================|")
    print(Fore.YELLOW + "+=====================================================+")

    for alumno in alumnos:
        tramo = "menor de edad" if alumno["edad"] <= 18 else "adulto"
        estado = "Sí ✅" if alumno["promociona"] else "No ❌"

        print(Fore.CYAN + "-" * 40)  # separador entre alumnos
        print(Fore.CYAN + f"Alumno/a: {alumno['nombre']} {alumno['apellidos']}")
        print(Fore.CYAN + f"Edad: {alumno['edad']} ({tramo})")
        print(Fore.CYAN + f"Media: {alumno['media']:.2f}")
        print(Fore.CYAN + f"Asistencia: {alumno['asistencia']}%")
        print(Fore.CYAN + f"¿Promociona?: {estado}")

# ======================================================
# Alias para compatibilidad con main.py
# ======================================================
parrafo = mostrar_lista_y_informe
mostrar_alumnos = mostrar_lista_y_informe  # main.py sigue funcionando

# ======================================================
# PEDIR DATOS DEL ALUMNO
# ======================================================
def informacion1():
    while True:
        # Nombre
        while True:
            nombre = input(Fore.CYAN + "Nombre: ").strip()
            if nombre.replace(" ", "").isalpha():
                break
            print(Fore.RED + "Nombre no válido ❌")

        # Apellidos
        while True:
            apellidos = input(Fore.CYAN + "Apellidos: ").strip()
            if apellidos.replace(" ", "").isalpha():
                break
            print(Fore.RED + "Apellidos no válidos ❌")

        # Edad
        while True:
            try:
                edad = int(input(Fore.CYAN + "Edad: "))
                assert 0 < edad <= 120
                break
            except:
                print(Fore.RED + "Edad incorrecta ❌")

        # Pedir notas
        def pedir_nota(texto):
            while True:
                try:
                    nota = float(input(Fore.CYAN + texto))
                    assert 0 <= nota <= 10
                    return nota
                except:
                    print(Fore.RED + "Nota incorrecta ❌")

        n1 = pedir_nota("Nota 1: ")
        n2 = pedir_nota("Nota 2: ")
        n3 = pedir_nota("Nota 3: ")

        # Asistencia
        while True:
            try:
                asistencia = int(input(Fore.CYAN + "Asistencia (%): "))
                assert 0 <= asistencia <= 100
                break
            except:
                print(Fore.RED + "Asistencia incorrecta ❌")

        media = (n1 + n2 + n3) / 3
        guardar_alumno(nombre, apellidos, edad, media, asistencia)

        # Preguntar si quiere añadir otro alumno
        otra = input(Fore.CYAN + "\n¿Quieres añadir otro alumno? (s/n): ").lower()
        if otra != "s":
            parrafo()  # imprime lista + informe al final solo una vez
            break
