#entradas
sueldo=int(input("Escriba su sueldo actual:"))

#caja negra
porcentaje15=(sueldo*0.15)
porcentaje12=(sueldo*0.12)

nuevosueldo=""
if(sueldo<900000):
    nuevosueldo=(sueldo+porcentaje15)

elif(sueldo>=900000):
    nuevosueldo=(sueldo+porcentaje12)

print("Su nuevo saldo sera de:",nuevosueldo,"COP")
