try:   
    # PROBLEMA: Pide al usuario un índice y muestra el elemento en esa posición
    amigos = ["Ana", "Luis", "Carlos", "María"]

    # Sin try-except:
    indice = int(input(f"Elige un índice (0-{len(amigos)-1}): "))
    print(f"Tu amigo es: {amigos[indice]}")

except IndexError:
    print ("Tiene que ser un numero de la lista")

except ValueError:
    print ("Tiene que ser un numero")

    