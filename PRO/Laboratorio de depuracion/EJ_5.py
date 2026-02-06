def es_parell(n):
    if n % 2 == 0:
        return True
    else:
        return False
    

nombre = 7 
es_parell_resultat = es_parell(nombre)
print(f"El nombre {nombre} és parell ? {es_parell_resultat}")