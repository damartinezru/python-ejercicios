#Escribir un programa que, mediante una función, calcule el resultado de restar el doble de un
#numero a su cuadrado. 

import math

def restar(numero):
    return (math.pow(numero,2) - (2 * numero))


print("El resultado del cuadrado del numero restado por el doble es : "+str(restar(int(input("Ingrese un numero : ")))))