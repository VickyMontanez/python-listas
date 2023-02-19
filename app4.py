""" 4. Una empresa tiene 500 almacenes. Cada almacén debe
reportar el nombre y 5 registros c/u, contiene el tipo de articulo
y el número de unidades vendidas de ese artículo.

Haga un programa en Python para determinar cuál fue el
almacén que mas vendió, cual fue el articulo más vendido de
ese almacén y cual el más vendido en general. """

almacen=[]
posicionMayor= 0
mayorValor= 0

n= int(input("Ingrese la cantidad de almacenes que tendrá la empresa: "))

for i in range(n):
    nombre = input("Nombre del almacen: ")
    articulos = []
    totalVendido= 0

    for a in range(5):
        tipo= input("Tipo de articulo: ")
        cantidad = int(input("Cantidad vendida: "))
        articulos.append(tipo)
        articulos.append(cantidad)
        totalVendido += cantidad
    print("Total del almacen: "+ nombre,totalVendido)
    almacen.append([nombre, articulos, totalVendido])

    for i in range(len(almacen)):
        for j in range(len(almacen[i])):
            print(almacen[i][j], end=" ")
        print()

    for k in range(len(almacen)):
        if(k==0):
            posicionMayor = 0
            mayorValor = int(almacen[k][2])
        else:
            if(int(almacen[k][2])> mayorValor):
                posicionMayor = j
                mayorValor = int(almacen[k][2])
print("El amlacen que más vendió fue "+ almacen[posicionMayor][0], "con " + str(mayorValor)+ " articulos")