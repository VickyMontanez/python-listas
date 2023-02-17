""" 3. En pocos días comienza la vuelta a España y la federación
colombiana de ciclismo, como incentivo ha determinado pagar
un valor adicional. El programa pedirá por teclado el sueldo
básico por kilometro recorrido, el número de kilómetros
recorridos durante toda la vuelta, numero de kilómetros
recorridos con la camiseta de líder.
Calcular el valor a pagar total, si se sabe que si recorre en la
bici más de 1800 kilómetros con la camiseta de líder, esos
kilómetros se consideran especiales y tendrán un recargo de
25%.
El total de kilómetros por recorrer durante toda la vuelta serán
3.277 kilómetros,el ganador de la vuelta a España recibirá 700
millones de pesos. """

def vuelta():
    ciclista = []
    sueldoBasico = []
    Nkilometros = []
    f = int(input("Cuantos ciclistas desea agregar?: "))
    sueldo= float(input("Digite el sueldo básico: "))
    sueldoBasico.append(sueldo)
    for i in range(f):
        nombre = input("Digite el nombre del ciclista: ")
        ciclista.append(nombre)
        kilom= float(input("Ingrese los kilometros recorridos: "))
        Nkilometros.append(kilom)
        
    return ciclista, sueldoBasico, Nkilometros

def listarCiclistas(ciclista):
    print("Los ciclistas ingresados son: ")
    for i in range(len(ciclista)):
        print(ciclista[i], Nkilometros[i])
        print()

option = -1
while option != 0:
     
    print("-------M E N U-----")
    print("1. Agregar ciclistas")
    print("2. Informe de los ciclistas")
    print("3. Calcular el valor a pagar")
    print("4. Ganador de la vuelta España")
    option=int(input("Digite la opción que desea: "))

    if option==1:
        ciclista, sueldoBasico, Nkilometros = vuelta()
    elif(option == 2):
        listarCiclistas(ciclista)
        
