from datetime import datetime
hoy = datetime.now()
dia_a=hoy.day
mes_a=hoy.month
año_a=hoy.year
#entradas
fecha=input("Escriba su fecha de nacimiento dd/mm/yyyy:")
(dia,mes,año)=fecha.split("/")
dian=int(dia)
mesn=int(mes)
añon=int(año)
#caja negra
#-------Edad---------
edad=0
if(mes_a>mesn):
    edad=año_a-añon
elif(mes_a<mesn):
    edad=(año_a-añon)-1
elif(mes_a==mesn):
    if(dia_a>dian):
        edad=año_a-añon
    elif(dia_a<dian):
        edad=(año_a-añon)-1
    elif(dia_a==dian):
        edad=año_a-añon
print("la edad es:",edad)
#-------Signo Zodiacal----------
signo=""
if(mesn==1):
    if(dian>=1 and dian<=20):
        signo="Capricornio"
    elif(dian>=21 and dian<=31):
        signo="Acuario"
if(mesn==2):
    if(dian>=1 and dian<=19):
        signo="Acuario"
    elif(dian>=20 and dian<=28):
        signo="Piscis"
if(mesn==3):
    if(dian>=1 and dian<=20):
        signo="Piscis"
    elif(dian>=21 and dian<=31):
        signo="Aries"
if(mesn==4):
    if(dian>=1 and dian<=20):
        signo="Aries"
    elif(dian>=21 and dian<=30):
        signo="Tauro"
if(mesn==5):
    if(dian>=1 and dian<=21):
        signo="Tauro"
    elif(dian>=22 and dian<=31):
        signo="Géminis"
if(mesn==6):
    if(dian>=1 and dian<=21):
        signo="Géminis"
    elif(dian>=22 and dian<=30):
        signo="Cáncer"
if(mesn==7):
    if(dian>=1 and dian<=22):
        signo="Cáncer"
    elif(dian>=23 and dian<=31):
        signo="Leo"
if(mesn==8):
    if(dian>=1 and dian<=23):
        signo="Leo"
    elif(dian>=24 and dian<=31):
        signo="Virgo"
if(mesn==9):
    if(dian>=1 and dian<=22):
        signo="Virgo"
    elif(dian>=23 and dian<=30):
        signo="Libra"
if(mesn==10):
    if(dian>=1 and dian<=22):
        signo="Libra"
    elif(dian>=23 and dian<=31):
        signo="Escorpión"
if(mesn==11):
    if(dian>=1 and dian<=21):
        signo="Escorpión"
    elif(dian>=22 and dian<=30):
        signo="Sagitario"
if(mesn==12):
    if(dian>0 and dian<=21):
        signo="Sagitario"
    elif(dian>=22 and dian<=31):
        signo="Capricornio"
print("Su signo zodiacal es:",signo)