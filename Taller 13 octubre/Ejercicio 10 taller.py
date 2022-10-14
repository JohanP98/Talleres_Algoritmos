#Entradas
import math
categoria=int(input("Escriba la categoria de trabajador a la que corresponde:"))

#caja negra
#------sueldobruto---------
sueldobruto=""
if(categoria==1):
    sueldobruto=5000000
elif(categoria==2):
    sueldobruto=4300000
elif(categoria==3):
    sueldobruto=3600000
elif(categoria==4):
    sueldobruto=2000000
elif(categoria==5):
    sueldobruto=900000
#-------aumento--------
aumento=""
if(sueldobruto==5000000):
    aumento=(sueldobruto*0.10)
elif(sueldobruto==4300000):
    aumento=(sueldobruto*0.15)
elif(sueldobruto==3600000):
    aumento=(sueldobruto*0.20)
elif(sueldobruto==2000000):
    aumento=(sueldobruto*0.40)
elif(sueldobruto==900000):
    aumento=(sueldobruto*0.60)
#------sueldonuevo---------
sueldonuevo=""
if(categoria==1):
    sueldonuevo=(sueldobruto+aumento)
elif(categoria==2):
    sueldonuevo=(sueldobruto+aumento)
elif(categoria==3):
    sueldonuevo=(sueldobruto+aumento)
elif(categoria==4):
    sueldonuevo=(sueldobruto+aumento)
elif(categoria==5):
    sueldonuevo=(sueldobruto+aumento)

print("La categoria a la que pertenece es:",categoria,", por lo tanto su nuevo sueldo es:",sueldonuevo,"COP")
