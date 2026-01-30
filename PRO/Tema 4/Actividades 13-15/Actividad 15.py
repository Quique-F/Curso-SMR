conjunto1 = {210, 200, 301, 40, 70, 32}
conjunto2 = {101, 7, 140, 30, 200, 40}

comunes = conjunto1.intersection(conjunto2)

if comunes:
    print(f"Los elementos en común son: {comunes}")
else:
    print("No hay elementos en común.")