#entradas

nombre=input("Escriba su nombre:")
montocompra=int(input("Escriba el monto de la compra:"))

#caja negra
descuento5=(montocompra*0.05)
descuento11=(montocompra*0.11)
descuento18=(montocompra*0.18)
descuento25=(montocompra*0.25)

montoapagar=""
if(montocompra<50000):
    print("No hay descuento")
elif(50000<montocompra<100000):
    montoapagar=(montocompra-descuento5)
    print(nombre,"el monto de la compra era de",montocompra,"COP","y ha recibido un descuento del 5% que es:",descuento5,"COP","por lo que el monto final a pagar es de:",montoapagar,"COP")
elif(100000<montocompra<700000):
    montoapagar=(montocompra-descuento11)
    print(nombre,"el monto de la compra era de",montocompra,"COP","y ha recibido un descuento del 11% que es:",descuento11,"COP","por lo que el monto final a pagar es de:",montoapagar,"COP")
elif(700000<montocompra<1500000):
    montoapagar=(montocompra-descuento18)
    print(nombre,"el monto de la compra era de",montocompra,"COP","y ha recibido un descuento del 18% que es:",descuento18,"COP","por lo que el monto final a pagar es de:",montoapagar,"COP")
elif(montocompra>1500000):
    montoapagar=(montocompra-descuento25)
    print(nombre,"el monto de la compra era de",montocompra,"COP","y ha recibido un descuento del 25% que es:",descuento25,"COP","por lo que el monto final a pagar es de:",montoapagar,"COP")