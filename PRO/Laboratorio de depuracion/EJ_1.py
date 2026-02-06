def sumar_elements(llista):
    suma = 0
    for element in llista :
        suma += element
    return suma

llista = [1,2,3,4,5]
resultat = sumar_elements(llista)
print(f"La suma dels elements és: {resultat}")