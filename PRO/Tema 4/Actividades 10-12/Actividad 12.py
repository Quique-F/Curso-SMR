animales = "gato, perro, canario, pescado, conejo, hámster"



lista_animales = [animal.strip() for animal in animales.split(",")]

resultado = tuple((animal, len(animal)) for animal in lista_animales)


print(resultado)
