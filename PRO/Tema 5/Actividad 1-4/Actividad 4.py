# PROBLEMA: Simula un cajero donde el usuario tiene 100€
# Pregunta cuánto quiere retirar y actualiza el saldo
# No puede retirar más de lo que tiene, ni cantidades negativas, ni texto
try:
    saldo = 100
    print(f"Saldo actual: {saldo}€")

    # Sin try-except:
    retiro = float(input("¿Cuánto quieres retirar? "))
    assert retiro > saldo
  
    assert retiro < 0
    
    saldo -= retiro
    print(f"Retirado: {retiro}€")
    print(f"Nuevo saldo: {saldo}€")

except ValueError :
   print ("No puedes sacar letras")

except AssertionError :
    print ("No puedes retirar dar dinero")

