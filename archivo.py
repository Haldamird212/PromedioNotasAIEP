import numpy

def Promedio(Notas):
    Suma=0
    for x in range(0,3):
        Suma=Suma+Notas[x]

    Promedio=Suma/3

    return Promedio

Notas=numpy.array([])
for Contador in range(0,3):
    print("Ingrese nota "+str(Contador+1)+": ",end="")
    Notas=numpy.append(Notas,float(input()))

Notas_ordenadas=numpy.sort(Notas)

print("El promedio es: ", Promedio(Notas))
print("La nota más baja es: ", Notas_ordenadas[0])
print("La nota mas alta es: ", Notas_ordenadas[2])


    
