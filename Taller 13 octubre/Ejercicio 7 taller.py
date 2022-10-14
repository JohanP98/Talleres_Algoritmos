#entradas

distanciarecorrida=int(input("Escriba la distancia recorrida con el automovil alquilado:"))

#caja negra
adicional=(distanciarecorrida-300)*30000
adicional2=(distanciarecorrida-1000)*9000
dineroacancelar=""
if(distanciarecorrida<300):
    dineroacancelar=50000
elif(distanciarecorrida>300):
    if(distanciarecorrida<1000):
        dineroacancelar=70000+adicional
    elif(distanciarecorrida>1000):
        dineroacancelar=150000+adicional2

print("lo que debe pagar el cliente segun la distancia recorrida es:",dineroacancelar,"COP")