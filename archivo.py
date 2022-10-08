import numpy

def Promedio(Notas):
    Suma=0
    for x in range(0,Cantidad_notas):
        Suma=Suma+Notas[x]

    Promedio=Suma/Cantidad_notas

    return Promedio

Notas=numpy.array([])

print("Ingrese cantidad de notas a promediar: ", end="")
Cantidad_notas=int(input())

Contador=0

while Contador < Cantidad_notas:
    print("Ingrese nota "+str(Contador + 1)+": ",end="")
    Notas=numpy.append(Notas,float(input()))
    Contador=Contador+1

Notas_ordenadas=numpy.sort(Notas)

Opcion=0

while Opcion != 4:
    print("Seleccione operación a realizar \n 1- Obtener promedio\n 2- Obtener nota más alta\n 3- Obtener nota más baja\n 4- Salir")
    Opcion=int(input())
    if Opcion == 1:
        print("El promedio es: ", Promedio(Notas), "\n\n")
    elif Opcion == 2:
        print("La nota mas alta es: ", Notas_ordenadas[Cantidad_notas-1],"\n\n")
    elif Opcion == 3:
        print("La nota más baja es: ", Notas_ordenadas[0],"\n\n")
    elif Opcion < 1 or Opcion > 4:
        print("Debe ingresar una opcion VALIDA")


    
