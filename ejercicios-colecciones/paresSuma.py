# Colecciones
# Escribir un programa que llene una lista con los veinte primeros números pares y calcule su suma.
def crearLista():
    lista = []
    n = 1
    while len(lista) < 20:
        if n % 2 == 0:
            lista.append(n)
        n += 1
    return lista

def sumarLista(lista):
    suma = 0
    for n in lista:
        suma += n
    return suma

print('La suma de los numeros pares del 1 al 20 son: ' + str(sumarLista(crearLista())))
        