import time
from colorama import init, Fore

init(autoreset=True)

alumnos = []

def menu1():
    centro = "CIPFP Luís Suñer Sanchis"
    print(Fore.CYAN + "=====================================================")
    print(Fore.CYAN + f"-- Control de Promoción: {centro} --")
    print(Fore.CYAN + "=====================================================")
    time.sleep(1)
    print(Fore.YELLOW + "Cargando base de datos...")
    time.sleep(1)

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

def informacion1():
    while True:
        # Validación de Nombre
        while True:
            nombre = input(Fore.CYAN + "Nombre: ").strip()
            if nombre.replace(" ", "").isalpha() and len(nombre) > 1:
                break
            print(Fore.RED + "Error: El nombre debe contener solo letras ❌")

        # Validación de Apellidos
        while True:
            apellidos = input(Fore.CYAN + "Apellidos: ").strip()
            if apellidos.replace(" ", "").isalpha() and len(apellidos) > 1:
                break
            print(Fore.RED + "Error: Los apellidos deben contener solo letras ❌")

        # Validación de Edad
        while True:
            try:
                edad = int(input(Fore.CYAN + "Edad: "))
                if 0 < edad <= 120: break
                else: print(Fore.RED + "Edad fuera de rango (1-120) ❌")
            except ValueError:
                print(Fore.RED + "Error: Introduce un número entero ❌")

        # Función interna para validar notas 0-10
        def pedir_nota(texto):
            while True:
                try:
                    nota = float(input(Fore.CYAN + texto))
                    if 0 <= nota <= 10: return nota
                    print(Fore.RED + "La nota debe estar entre 0 y 10 ❌")
                except ValueError:
                    print(Fore.RED + "Error: Introduce un número válido ❌")

        n1 = pedir_nota("Nota 1: ")
        n2 = pedir_nota("Nota 2: ")
        n3 = pedir_nota("Nota 3: ")

        # Validación de Asistencia
        while True:
            try:
                asistencia = int(input(Fore.CYAN + "Asistencia (%): "))
                if 0 <= asistencia <= 100: break
                print(Fore.RED + "La asistencia debe ser entre 0 y 100 ❌")
            except ValueError:
                print(Fore.RED + "Error: Introduce un número entero ❌")

        media = (n1 + n2 + n3) / 3
        guardar_alumno(nombre, apellidos, edad, media, asistencia)

        otra = input(Fore.YELLOW + "\n¿Deseas registrar otro alumno? (s/n): ").lower()
        if otra != "s":
            break

def parrafo():
    """Muestra la lista de nombres y el informe detallado."""
    if not alumnos:
        print(Fore.RED + "No hay datos para mostrar.")
        return

    print(Fore.YELLOW + "\n" + "="*55)
    print(Fore.YELLOW + "           INFORME DE PROMOCIÓN FINAL")
    print(Fore.YELLOW + "="*55)

    for alumno in alumnos:
        tramo = "Menor de edad" if alumno["edad"] < 18 else "Adulto"
        estado = "PROMOCIONA ✅" if alumno["promociona"] else "NO PROMOCIONA ❌"
        
        print(Fore.CYAN + f"ALUMNO/A: {alumno['nombre'].upper()} {alumno['apellidos'].upper()}")
        print(f"Situación: {tramo} | Media: {alumno['media']:.2f} | Asistencia: {alumno['asistencia']}%")
        print(f"Resultado: {estado}")
        print("-" * 55)

def mostrar_alumnos():
    """Módulo de búsqueda personalizada."""
    if not alumnos: return

    print(Fore.GREEN + "\nSISTEMA DE BÚSQUEDA DE ALUMNADO")
    while True:
        buscar = input(Fore.YELLOW + "¿Quieres buscar a una persona específica? (s/n): ").lower()
        if buscar != 's':
            print(Fore.CYAN + "Cerrando sistema de gestión. ¡Buen día!")
            break
        
        criterio = input(Fore.WHITE + "Escribe el nombre o apellido a localizar: ").strip().lower()
        encontrados = [a for a in alumnos if criterio in a['nombre'].lower() or criterio in a['apellidos'].lower()]
        
        if encontrados:
            print(Fore.GREEN + f"\nSe han encontrado {len(encontrados)} coincidencia(s):")
            for a in encontrados:
                res = "SÍ" if a['promociona'] else "NO"
                print(Fore.WHITE + f"-> {a['nombre']} {a['apellidos']} | Media: {a['media']:.2f} | Promociona: {res}")
        else:
            print(Fore.RED + f"No hay registros que coincidan con '{criterio}'.")