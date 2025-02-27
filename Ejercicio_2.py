# Función para ordenar una fila de la matriz utilizando Bubble Sort
def ordenar_fila_bubble(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]  # Intercambio de elementos
    return fila

# Función para mostrar la matriz de manera legible
def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

# Función principal
def main():
    # Crear una matriz 3x3 vacía
    matriz = []

    # Solicitar al usuario los valores para llenar la matriz
    print("Ingresa los valores para llenar la matriz 3x3:")
    for i in range(3):
        fila = []
        for j in range(3):
            valor = int(input(f"Valor en la posición ({i+1}, {j+1}): "))
            fila.append(valor)
        matriz.append(fila)

    # Mostrar la matriz original
    print("\nMatriz original:")
    mostrar_matriz(matriz)

    # Solicitar al usuario la fila que desea ordenar (0, 1 o 2)
    fila_a_ordenar = int(input("\n¿Quieres ordenar la fila 1, 2 o 3? (Introduce 1, 2 o 3): ")) - 1

    # Ordenar la fila seleccionada
    matriz[fila_a_ordenar] = ordenar_fila_bubble(matriz[fila_a_ordenar])

    # Mostrar la matriz con la fila ordenada
    print("\nMatriz con la fila ordenada:")
    mostrar_matriz(matriz)

# Llamar a la función principal para ejecutar el programa
main()
