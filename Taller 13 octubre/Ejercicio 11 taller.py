#entradas
temperatura=float(input("Escriba la temperatura en valores fahrenheit:"))

#caja negra
deporte=""
if(temperatura>85):
    deporte="Natación"
elif(70<temperatura<=85):
    deporte="Tenis"
elif(32<temperatura<=70):
    deporte="Golf"
elif(10<temperatura<=32):
    deporte="Esquí"
elif(temperatura<=10):
    deporte="Marcha"

print("El deporte apropiado para practicar a la temperatura dada es:",deporte)