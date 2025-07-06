# Clase base: Empleado
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre                # atributo público
        self.__salario = salario            # atributo privado (encapsulación)

    # Método para mostrar información general del empleado
    def mostrar_info(self):
        print(f"Empleado: {self.nombre}, Salario: ${self.__salario}")

    # Getter del salario (encapsulación)
    def get_salario(self):
        return self.__salario

    # Setter del salario (encapsulación)
    def set_salario(self, nuevo_salario):
        if nuevo_salario > 0:
            self.__salario = nuevo_salario
        else:
            print("Error: El salario debe ser positivo.")

# Clase derivada: Gerente (hereda de Empleado)
class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)       # Llamada al constructor de la clase base
        self.departamento = departamento

    # Sobrescritura de método (polimorfismo)
    def mostrar_info(self):
        print(f"Gerente: {self.nombre}, Departamento: {self.departamento}, Salario: ${self.get_salario()}")

# Clase derivada: Desarrollador (hereda de Empleado)
class Desarrollador(Empleado):
    def __init__(self, nombre, salario, lenguaje):
        super().__init__(nombre, salario)
        self.lenguaje = lenguaje

    # Otro ejemplo de polimorfismo
    def mostrar_info(self):
        print(f"Desarrollador: {self.nombre}, Lenguaje: {self.lenguaje}, Salario: ${self.get_salario()}")

# Ejecución del programa: creación de instancias y uso de métodos
if __name__ == "__main__":
    # Crear objetos de las diferentes clases
    emp1 = Empleado("Carlos", 1000)
    gerente1 = Gerente("Ana", 2000, "Ventas")
    dev1 = Desarrollador("Luis", 1800, "Python")

    # Mostrar información de cada uno (polimorfismo en acción)
    emp1.mostrar_info()
    gerente1.mostrar_info()
    dev1.mostrar_info()

    # Uso de métodos encapsulados
    print("\nAumento de salario a Carlos...")
    emp1.set_salario(1200)
    emp1.mostrar_info()
