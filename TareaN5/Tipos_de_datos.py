# Programa para calcular el área de un triángulo y registrar los datos
# Autor: [Tu nombre]
# Fecha: [Fecha]
# Este programa solicita la base y altura de un triángulo, calcula el área y guarda el registro.

# Función para calcular el área
def calcular_area_triangulo(base: float, altura: float) -> float:
    return (base * altura) / 2

# Registro de datos (lista de diccionarios)
registro_areas = []

# Solicitar datos al usuario
nombre_usuario = input("Ingrese su nombre: ")
base_triangulo = float(input("Ingrese la base del triángulo (en cm): "))
altura_triangulo = float(input("Ingrese la altura del triángulo (en cm): "))

# Calcular el área
area_resultado = calcular_area_triangulo(base_triangulo, altura_triangulo)

# Guardar en el registro
registro = {
    "usuario": nombre_usuario,
    "base_cm": base_triangulo,
    "altura_cm": altura_triangulo,
    "area_cm2": area_resultado
}
registro_areas.append(registro)

# Mostrar el resultado
print(f"\nÁrea calculada: {area_resultado} cm²")
print(f"Registro guardado: {registro}")
