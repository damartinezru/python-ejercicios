# Simple
# Programa que calcule la hipotenusa de un triángulo rectángulo

import math


def hipotenusa(catetoOpuesto, catetoAdyacente):
    return math.sqrt((math.pow(catetoOpuesto, 2)+math.pow(catetoAdyacente, 2)))


print('La hipotenusa del triangulo es: ' + 
    str(hipotenusa(float(input('Valor del cateto adyacente:')),
    float(input('Valor del cateto opuesto:')))))
