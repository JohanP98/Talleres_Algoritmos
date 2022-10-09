#entradas
import math

Hombres=int(input("Escriba el numero de hombres que hay en el grupo de estudiantes:"))
Mujeres=int(input("Escriba el numero de mujeres que hay en el grupo de estudiantes:"))

#caja negra
totalpersonas=(Hombres+Mujeres)
porcentajehombres=(Hombres*100)/totalpersonas
porcentajemujeres=(Mujeres*100)/totalpersonas

#salidas
print("El porcentaje de hombres del grupo de estudiantes es:",porcentajehombres,"%")
print("El porcentaje de mujeres del grupo de estudiantes es:",porcentajemujeres,"%")