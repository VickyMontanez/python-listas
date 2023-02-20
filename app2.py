""" 2. N atletas han pasado a finales en salto triple en los juegos
olímpicos de 2022.

Diseñe un programa que pida por teclado los nombres de cada
atleta finalista y a su vez, sus marcas del salto en metros.

Informar el nombre de la atleta campeona que se quede
con la medalla de oro y si rompió récord, reportar el pago que
será de 500 millones. El récord esta en 15,50 metros. """

def atletas():
    finalistas = []
    marca = []
    f = int(input("Cuantos atletlas finalistas desea agregar?: "))
    for i in range(f):
        nombre = input("Digite el nombre del atleta: ")
        finalistas.append(nombre)
        saltos= float(input("Digite la marca del finalista (en metros): "))
        marca.append(saltos)
    return finalistas, marca

def listarFinalistas(finalistas):
    print("La marca del salto de cada finalista es: ")
    for i in range(len(finalistas)):
        print(finalistas[i], marca[i])
        print()

def campeon(marca,finalistas):
    print("El atleta campeón es: ")
    finalistas.sort()
    pos=max([int(i) for i in marca])
    x=marca.index(pos)
    print(f'{finalistas[x]} con {marca[x]} metros recorridos ')
    print("GANADORA DE LA MEDALLA DE ORO")
    if pos > 15.50:
        print("ROMPIÓ EL RECORD! RECIBE 500 MILLONES!")

option = -1
while option != 0:
    print("---------------OLIMPICOS 2022-------------------")
    print("-------------SALTO TRIPLE----------------")
    print("OPCIONES A CONSULTAR: ")
    print("1. AGREGAR ATLETAS FINALISTAS")
    print("2. MOSTRAR INFORME DE CADA FINALISTA")
    print("3. MOSTRAR ATLETA CAMPEÓN")
    option=int(input("Digite su opción: "))

    if option==1:
        finalistas, marca = atletas()
    elif(option == 2):
        listarFinalistas(finalistas)
    elif(option == 3):
        campeon(marca,finalistas)