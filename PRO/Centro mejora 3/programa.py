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
        while True:
            nombre = input(Fore.CYAN + "Nombre: ").strip()
            if nombre.replace(" ", "").isalpha() and len(nombre) > 1:
                break
            print(Fore.RED + "Error: El nombre debe contener solo letras ❌")

        while True:
            apellidos = input(Fore.CYAN + "Apellidos: ").strip()
            if apellidos.replace(" ", "").isalpha() and len(apellidos) > 1:
                break
            print(Fore.RED + "Error: Los apellidos deben contener solo letras ❌")

        while True:
            try:
                edad = int(input(Fore.CYAN + "Edad: "))
                if 0 < edad <= 120: break
                else: print(Fore.RED + "Edad fuera de rango (1-120) ❌")
            except ValueError:
                print(Fore.RED + "Error: Introduce un número entero ❌")

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
    """Muestra un mensaje de confirmación de que los datos se han procesado."""
    if not alumnos:
        print(Fore.RED + "No hay datos para mostrar.")
    else:
        print(Fore.GREEN + f"\n✅ Se han procesado {len(alumnos)} alumnos correctamente.")

def imprimir_tabla(alumno):
    """Función auxiliar para mostrar la tabla de un alumno."""
    tramo = "Menor de edad" if alumno["edad"] < 18 else "Adulto"
    estado = "PROMOCIONA ✅" if alumno["promociona"] else "NO PROMOCIONA ❌"
    
    print(Fore.YELLOW + "\n" + "="*50)
    print(Fore.YELLOW + f"FICHA DETALLADA: {alumno['nombre'].upper()} {alumno['apellidos'].upper()}")
    print(Fore.YELLOW + "="*50)
    print(Fore.WHITE + f"{'CONCEPTO':<20} | {'VALOR'}")
    print("-" * 50)
    print(f"{'Edad':<20} | {alumno['edad']} ({tramo})")
    print(f"{'Nota Media':<20} | {alumno['media']:.2f}")
    print(f"{'Asistencia':<20} | {alumno['asistencia']}%")
    print(f"{'Resultado':<20} | {estado}")
    print("-" * 50 + "\n")

def mostrar_alumnos():
    """Módulo que lista alumnos y permite elegir uno para ver su tabla."""
    if not alumnos: return

    while True:
        print(Fore.GREEN + "\n--- SELECCIONE UN ALUMNO PARA VER DETALLES ---")
        for i, alumno in enumerate(alumnos, 1):
            print(Fore.WHITE + f"{i}. {alumno['nombre']} {alumno['apellidos']}")
        
        print(Fore.RED + "0. Finalizar consulta")
        
        try:
            opcion = int(input(Fore.YELLOW + "\nIntroduce el número del alumno: "))
            
            if opcion == 0:
                print(Fore.CYAN + "Saliendo del buscador...")
                break
            
            if 1 <= opcion <= len(alumnos):
                imprimir_tabla(alumnos[opcion - 1])
                input(Fore.CYAN + "Presiona ENTER para volver a la lista...")
            else:
                print(Fore.RED + "Número fuera de rango.")
        except ValueError:
            print(Fore.RED + "Error: Introduce un número válido.")