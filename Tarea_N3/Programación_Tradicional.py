def pedir_temperaturas():
    temps = []
    for i in range(7):
        t = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        temps.append(t)
    return temps

def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

def main():
    temperaturas = pedir_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal es: {promedio:.2f}°C")

main()
