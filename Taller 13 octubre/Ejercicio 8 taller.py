#entradas
P=float(input("Escriba el primer valor:"))
Q=float(input("Escriba el segundo valor:"))

#caja negra
operacion=P**3+Q**4-2*P**2

if(operacion>680):
    print(P,"y",Q,"satisfacen la expresión")
else:
    print(P,"y",Q,"no satisfacen la expresión")