def ordenar_llista(llista):
    n = len(llista)
    for i in range(n):
        index_minim = i  
        for j in range(i + 1, n):
            if llista[j] < llista[index_minim]:
                index_minim = j
        llista[i], llista[index_minim] = llista[index_minim], llista[i]
    return llista