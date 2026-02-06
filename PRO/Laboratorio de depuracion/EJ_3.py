try:  
    def trobar_maxim(llista):
            maxim = llista[0]
            for element in llista:
                if element > maxim:
                    maxim = element
            return maxim

    llista = []
    valor_maxim = trobar_maxim(llista)
    print(f"El valor mâxim és: {valor_maxim}")
    
except IndexError :
    print ("La lista esta vacia")