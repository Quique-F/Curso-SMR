try:
    num1 = input("Escribe el primer número: ")
    num2 = input("Escribe el segundo número: ")
    resultado = int(num1) / int(num2)
    print(f"Resultado: {resultado}")

except ValueError: 
    print ("Parece que lo que escribiste no es un número válido. Intenta usar solo dígitos.")

except ZeroDivisionError:
    print ("Has intientado dividir entre cero tontito")

