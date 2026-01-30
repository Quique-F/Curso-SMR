conjunto1 = {10, 20, 30, 40, 50}
conjunto2 = {30, 40, 50, 60, 70}

# 1. Elementos idénticos en ambos (Intersección)
identicos = conjunto1.intersection(conjunto2)
print(f"Elementos idénticos: {identicos}")


# 2. Todos los elementos sin duplicados (Unión)
union = conjunto1.union(conjunto2)
print(f"Unión sin duplicados: {union}")


# 3. Actualizar conjunto1 con elementos que solo están en el 1 (Diferencia)
conjunto1.difference_update(conjunto2)
print(f"Conjunto1 actualizado (solo únicos de 1): {conjunto1}")


# Reiniciamos conjunto1 para los siguientes puntos
conjunto1 = {10, 20, 30, 40, 50}



# 4. Sacar los elementos 30 y 40 del primer conjunto

# Podemos usar remove() o discard()
conjunto1.discard(30)
conjunto1.discard(40)
print(f"Conjunto1 tras eliminar 30 y 40: {conjunto1}")



# 5. Elementos en conjunto1 o conjunto2, pero NO en ambos (Diferencia Simétrica)

# Volvemos a los valores originales para este ejemplo
conjunto1 = {10, 20, 30, 40, 50}
diferencia_simetrica = conjunto1.symmetric_difference(conjunto2)
print(f"Diferencia simétrica: {diferencia_simetrica}")