""" 1. Campus requiere administrar algunos datos de sus Campers
como por ejemplo, la creación, eliminación o búsqueda de los
developers, entre otros, por tal razón, ha solicitado el diseño de
un programa que cuente con el siguiente menú como panel de
control: """

""" Funciones """

def crearSputnik():
    grupoSputnik = []
    n = int(input("Cuantos campers quiere ingresar a grupo Sputnik?: "))
    for camper in range(n):
        nombre = input("Digite el nombre del camper: ")
        grupoSputnik.append(nombre)
    return grupoSputnik

def listarGrupoSputnik(grupoSputnik):
    print("Los campers son: ")
    for camper in range(len(grupoSputnik)):
        print("Camper:",(camper+1),grupoSputnik[camper], end=" ")
        print()

def agregarSputnik(grupoSputnik):
    nombreNuevo = input("Digite el nombre del nuevo camper: ")
    grupoSputnik.append(nombreNuevo)
    print("Se ha agregado exitosamente.")

def eliminarArtemis(grupoArtemis):
    camperEli= input("Digite el nombre del camper que quieres eliminar: ")
    for i in range(len(grupoArtemis)):
        if camperEli == grupoArtemis[i]:
            del grupoArtemis[i]
            print("Se borró el usuario ",camperEli)

def ordenarArtemis(grupoArtemis):
    grupoArtemis.sort()
    print(grupoArtemis)
    
def buscarArtemis(grupoArtemis):
    camperBusca= input("Digite el nombre del camper que quieres encontrar: ")
    for i in range(len(grupoArtemis)):
        if camperBusca == grupoArtemis[i]:
            print("El camper",camperBusca,"se encuentra en la lista")

def crearArtemis():
    grupoArtemis = []
    n = int(input("Cuantos campers quiere ingresar a grupo Artemis?: "))
    for camper in range(n):
        nombre = input("Digite el nombre del camper: ")
        grupoArtemis.append(nombre)
    return grupoArtemis

def listarGrupoArtemis(grupoArtemis):
    print("Los campers son: ")
    for camper in range(len(grupoArtemis)):
        print("Camper:",(camper+1),grupoArtemis[camper], end=" ")
        print()

def agregarArtemis(grupoArtemis):
    nombreNuevo = input("Digite el nombre del nuevo camper: ")
    grupoArtemis.append(nombreNuevo)
    print("Se ha agregado exitosamente.")

def eliminarArtemis(grupoArtemis):
    camperEli= input("Digite el nombre del camper que quieres eliminar: ")
    for i in range(len(grupoArtemis)):
        if camperEli == grupoArtemis[i]:
            del grupoArtemis[i]
            print("Se borró el usuario ",camperEli)

def ordenarArtemis(grupoArtemis):
    grupoArtemis.sort()
    print(grupoArtemis)
    
def buscarArtemis(grupoArtemis):
    camperBusca= input("Digite el nombre del camper que quieres encontrar: ")
    for i in range(len(grupoArtemis)):
        if camperBusca == grupoArtemis[i]:
            print("El camper",camperBusca,"se encuentra en la lista")
    
    
""" Funciones """

option = -1
while option != 0:
    print("-----------------------MENU--------------------")
    print("1.  CREAR GRUPO ARTEMIS:")
    print("1.1 LISTA CAMPERS DE ARTEMIS")
    print("1.2 AGREGAR CAMPERS A ARTEMIS")
    print("1.3 ELIMINAR CAMPERS A ARTEMIS")
    print("1.4 ORDENAR ALFABETICAMENTE EN LISTA DE ARTEMIS")
    print("1.5 BUSCAR CAMPER EN LISTA DE ARTEMIS")
    print("2.  CREAR GRUPO SPUTNIK:")
    print("2.1 LISTA CAMPERS DE SPUTNIK")
    print("2.2 AGREGAR CAMPERS A SPUTNIK")
    print("2.3 ELIMINAR CAMPERS A SPUTNIK")
    print("2.4 ORDENAR ALFABETICAMENTE EN LISTA DE SPUTNIK")
    print("2.5 BUSCAR CAMPER EN LISTA DE SPUTNIK")
    option=float(input("Digite opción: "))

    if option==1:
        grupoArtemis = crearArtemis()
    elif(option == 1.1):
        listarGrupoArtemis(grupoArtemis)
    elif(option == 1.2):
        agregarArtemis(grupoArtemis)
    elif(option == 1.3):
        eliminarArtemis(grupoArtemis)
    elif(option == 1.4):
        ordenarArtemis(grupoArtemis)
    elif(option == 1.5):
        buscarArtemis(grupoArtemis)
    elif(option == 2):
        grupoSputnik = crearSputnik()
    elif(option == 2.1):
        listarGrupoArtemis(grupoArtemis)
        
