import enum
import random

def generar_aleatorio() -> int:
    return random.randint(1,100)

print("Ingrese la cantidad esperada a ser generada")
ganancias=input()
ganancias=int(ganancias)

probRef=40 #probabilidad de refresco
probLlevar=60 #probabilidad para llevar

preciosComidas=[20,25,30,25,22,20,15,15] #Precios de las comidas
rangoComidas=[[1,15],[16,25],[26,35],[36,45],[46,65],[66,95],[96,97.35],[97.6,100]] #Rango de probabilidades de que se venda una comida
preciosRefrescos=[7,10,10,6,10,6,10] #Precios de las bebidas
rangoBebidas=[[1,10],[11,20],[21,30],[31,40],[41,60],[61,75],[76,100]] #Rango de probabilidades de que se venda una bebida
probLlevar=[[1,5],[6,20],[21,50],[51,80],[81,100]]
comidas=["Sencilla","Beef","Brutal","Pochola","La cerda","Filadelfia","Panini de carne","Panini de queso"]
bebidas=["Coca Cola personal","Coca Cola 1L","Sprite 1L","Guaraná personal","Guaraná 1L","Pesi personal","Pepsi 1L"]

generado=0
clientes=0
num_pedido=0
while generado<ganancias:
    clientes+=1
    num=generar_aleatorio()
    if num <= 60: #el pedido es para llevar
        num_pedido+=1
        pedidos=list()
        print("-------------------------------")
        print("Pedido para llevar: ")
        #Si el pedido es para llevar la probabilidad que de que lleve mas de 1 es mayor pero tambien es muy poco probable que lleve alguna bebida
        num=generar_aleatorio()
        idCantidad=0
        for pos,x in enumerate(probLlevar): #Aqui se determina cuantos pedidos se llevarán
            if num>=x[0] and num<=x[1]:
                idCantidad=pos
        if idCantidad==5:#Si sale la opcion de mas de 4 pedidos se generá un numero aleatorio entre 5 y 10 que es lo maximo que se suele pedir para llevar
            idCantidad=random.randint(5,10)
        print(f"Se han pedido {idCantidad} platos: ")
        for x in range(idCantidad):#esta parte de codigo se repite segun la cantidad de comidas en el mismo pedido
            num=generar_aleatorio()
            idPedido=0
            for pos, x in enumerate(rangoComidas):
                if num >= x[0] and num <= x[1]: #Esto determina que comida se pidió para llevar
                    idPedido=pos
                    pass
            generado+=preciosComidas[idPedido]
            pedidos.append(idPedido)
        #pass
        pedidos.sort()
        cantidades=list()
        for x in range(8):
            cantidad=pedidos.count(x)
            cantidades.append(cantidad)
        for pos,x in enumerate(cantidades):
            if x>=1:
                print(f"{x} - {comidas[pos]}")
        print("-------------------------------")
        print("\n")
    else: #El pedido es para comer aqui
        num_pedido+=1
        print("-------------------------------")
        print("Pedido para la mesa: ")
        num=generar_aleatorio()
        idPedido=0
        for pos, x in enumerate(rangoComidas):
            if num >= x[0] and num <= x[1]: #Esto determina que comida se pidió
                idPedido=pos
                pass
        generado+=preciosComidas[idPedido]
        print(f"1 - {comidas[idPedido]}")

        num=generar_aleatorio()
        if num <= 90: #Esto quiere decir que se si el numero generado es menor que 90 significa que se pidio un refresco
            num=generar_aleatorio()
            idPedido=0
            for pos, x in enumerate(rangoBebidas):
                if num >= x[0] and num <= x[1]: #Esto determina que bebida se pidió
                    idPedido=pos
                    pass
            generado+=preciosRefrescos[idPedido]
            print(f"1 - {bebidas[idPedido]}")
        pass
        print("-------------------------------")
        print("\n")

    
    #print(f"se ha generado: {ganancias}")


print(f"ha habido {clientes} clientes")

