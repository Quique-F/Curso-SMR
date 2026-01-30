try:
    num1 = float(input("Primer número: "))
    num2 = float(input("Segundo número: "))
    operacion = input("Operación (+, -, *, /): ")

    if operacion == '+':
            print(num1 + num2)
    elif operacion == '-':
            print(num1 - num2)
    elif operacion == '*':
            print(num1 * num2)
    elif operacion == '/':
            print(num1 / num2)


except ValueError: 
    print ("Parece que lo que escribiste no es un número válido. Intenta usar solo dígitos.")

except ZeroDivisionError:
    print ("Has intientado dividir entre cero tontito")