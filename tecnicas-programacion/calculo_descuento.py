# Función para calcular el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Llamada 1: Solo monto total (usa 10% por defecto)
monto1 = 150.0
descuento1 = calcular_descuento(monto1)
total_pagar1 = monto1 - descuento1

print(f"Compra 1:")
print(f"Monto total: ${monto1}")
print(f"Descuento aplicado (10%): ${descuento1}")
print(f"Total a pagar después del descuento: ${total_pagar1}\n")

# Llamada 2: Monto total y porcentaje personalizado (por ejemplo, 20%)
monto2 = 200.0
porcentaje_personalizado = 20
descuento2 = calcular_descuento(monto2, porcentaje_personalizado)
total_pagar2 = monto2 - descuento2

print(f"Compra 2:")
print(f"Monto total: ${monto2}")
print(f"Descuento aplicado ({porcentaje_personalizado}%): ${descuento2}")
print(f"Total a pagar después del descuento: ${total_pagar2}")
