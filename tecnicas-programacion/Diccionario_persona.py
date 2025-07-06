# Pedir información al usuario para llenar el diccionario
informacion_personal = {
    "nombre": input("Ingrese su nombre: "),
    "edad": int(input("Ingrese su edad: ")),  # Convertimos la entrada a entero
    "ciudad": input("Ingrese su ciudad: "),
    "profesion": input("Ingrese su profesión: ")
}

# Modificar el valor de la clave "ciudad"
nueva_ciudad = input("Ingrese una nueva ciudad para actualizar su información: ")
informacion_personal["ciudad"] = nueva_ciudad

# Agregar un número de teléfono si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = input("Ingrese su número de teléfono: ")

# Eliminar la clave "edad"
del informacion_personal["edad"]

# Imprimir el diccionario final después de las modificaciones
print("\nDiccionario final actualizado:")
print(informacion_personal)
