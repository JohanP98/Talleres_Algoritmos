#entradas
import math

chelinesaustriacos=float(input("Escriba la cantidad de chelines austriacos que quiere convertir a pesetas:"))
dracmasgriegos=float(input("Escriba la cantidad de dracmas griegos que quiere convertir a francos franceses:"))
pesetas=float(input("Escriba la cantidad de pesetas que quiere convertir a dolares y liras italianas:"))

#cajanegra
converapes=(chelinesaustriacos*956.871)/100
dracapese=(dracmasgriegos*88.607)/100
converafranc=(dracapese/20.110)
converadolar=(pesetas/122.499)
converaliras=(pesetas*100)/9.289

#salidas
print("La cantidad dada de chelines austriacos convertida a pesetas es de:",converapes,"pesetas")
print("La cantidad dada de dacmas griegos convertida a franco franceses es de:",converafranc,"franco franceses")
print("La cantidad dada de pesetas convertida a dolares estadounidenses es de:",converadolar,"dolares EE.UU")
print("La cantidad dada de pesetas convertida a liras italianas es de:",converaliras,"liras italianas")