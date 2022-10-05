#entradas
import math


lado1=float(input("ingrese lado uno:"))
lado2=float(input("ingrese lado dos:"))
lado3=float(input("ingrese lado tres:"))
#caja negra
s=(lado1+lado2+lado3)/2
area=math.sqrt(s*(s-lado1)*(s-lado2)*(s-lado3))
#salidas
print("El area es: "+str(area))