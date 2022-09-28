# EJERCICIO 5:
# Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto debera pagar finalmente por su compra.

precio = float(input("Precio: "))
descuento = precio * 0.15 # Asi sacas un porcentaje

precio_final= precio - descuento
print(f"El precio final a pagar es de ${precio_final:.2f}")