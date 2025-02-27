# Definir una matriz 3x3 con valores numéricos
matriz = [
    [5, 3, 8],
    [1, 7, 2],
    [9, 6, 4]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)  # Retorna la posición (fila, columna)
    return None  # Si no se encuentra el valor

# Solicitar al usuario que ingrese el valor a buscar
valor_buscado = int(input("Ingresa el valor que deseas buscar en la matriz: "))

# Llamar a la función para buscar el valor
resultado = buscar_valor(matriz, valor_buscado)

# Mostrar los resultados
if resultado:
    print(f"El valor {valor_buscado} se encontró en la posición {resultado}.")
else:
    print(f"El valor {valor_buscado} no se encontró en la matriz.")
