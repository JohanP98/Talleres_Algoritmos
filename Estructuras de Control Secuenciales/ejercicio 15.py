#Entradas
import math

preciooriginal=int(input("Escriba el precio de venta al publico:"))
preciopagado=int(input("Escriba el precio pagado:"))

#Caja negra
porcentaje=(preciopagado*100)/preciooriginal
descuentoaplicado=(porcentaje-100)*(-1)

#Salidas
print("El porcentaje de descuento aplicado al precio original del producto fue de:",descuentoaplicado,"%")