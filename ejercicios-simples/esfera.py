# Simple
# Un programa que calcule el volumen de una esfera de radio = r, volumen de la esfera = 4/3 * PI * radio3

import math

def volumenEsfera(radio):
    return (4/3) * math.pi * (math.pow(radio, 3))

print('El valor del volumen de la esfera es: ' + 
    str(volumenEsfera(float(input('Ingresa el valor del radio de la esfera:')))))
