class ClimaSemanal:
    def __init__(self):
        self.__temperaturas = []

    def ingresar_temperaturas(self):
        for i in range(7):
            temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
            self.__temperaturas.append(temp)

    def calcular_promedio(self):
        return sum(self.__temperaturas) / len(self.__temperaturas)

def main():
    clima = ClimaSemanal()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()
    print(f"El promedio semanal es: {promedio:.2f}°C")

main()
