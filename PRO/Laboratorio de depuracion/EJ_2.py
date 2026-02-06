def comptar_vocals(frase) :
    vocals = "aeiouAEIOUáéíóúÁÉÍÓÚàèìòùÀÈÌÒÙ"
    comptador = 0
    for lletra in frase :
        if lletra in vocals:
            comptador += 1
    return comptador 

frase = "Hola, Benbinguts a la Classe De Programació!"
nombre_vocals = comptar_vocals(frase)
print(f"Hi ha {nombre_vocals} vocals en la frase.")
