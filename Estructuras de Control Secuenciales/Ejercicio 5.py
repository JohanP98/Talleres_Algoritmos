#entradas
import math

NotaP1=float(input("Escriba su primera nota parcial:"))
NotaP2=float(input("Escriba su segunda nota parcial:"))
NotaP3=float(input("Escriba su tercera nota parcial:"))
Examen=float(input("Escriba la nota obtenida del examen final:"))
Trabajofinal=float(input("Escriba la nota obtenida en el trabajo final:"))

#caja negra
PromedioNotasP=(NotaP1+NotaP2+NotaP3)/3
cincuentacinco=(PromedioNotasP*0.55)
treinta=(Examen*0.30)
quince=(Trabajofinal*0.15)
Calificaciónfinal=(cincuentacinco+treinta+quince)

#salidas
print("La calificación final a obtener en la materia de commputación sera de:",Calificaciónfinal)