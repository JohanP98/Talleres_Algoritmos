#entradas
import math
A=float(input("Escriba el primer numero"))
B=float(input("Escriba el segundo numero:"))
C=float(input("Escriba el tercer numero:"))

#caja negra
D=B**2-4*A*C
#------Formula Cuadratica--------
X1=""
X2=""
if(D==0):
    X1=X2
    X2=-B/(2*A)
    print("La respuesta a la operacion -B/2*A es:","X1 Y X2=",X2,"ya que X1=X2")
elif(D>0):
    X1=(-B+math.sqrt(D))/(2*A)
    X2=(-B-math.sqrt(D))/(2*A)
    print("Las respuestas a la ecuación AX^2+BX+C=0 son:","X1=",X1,"y X2=",X2)
elif(D<0):
    print("no tiene solución en los Reales")