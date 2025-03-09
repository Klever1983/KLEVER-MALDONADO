import random

# Definir dimensiones
ciudades = ["Quito", "Guayaquil", "Manta"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 4  # Número de semanas a registrar

# Crear la matriz 3D para almacenar temperaturas
matriz_temperaturas = [[[{"day": dia, "temp": random.randint(10, 35)} for dia in dias] for _ in range(semanas)] for _ in ciudades]

# Calcular y mostrar promedios por ciudad y semana
for i, ciudad in enumerate(ciudades):
    print(f"\nTemperaturas en la ciudad de {ciudad}:")
    for semana in range(semanas):
        suma = sum(dia['temp'] for dia in matriz_temperaturas[i][semana])
        promedio_semana = suma / len(dias)
        print(f"  Semana {semana + 1}: Promedio = {promedio_semana:.2f}°C")