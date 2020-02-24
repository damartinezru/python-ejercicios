# Ciclos
# Escribir un programa que visualice en pantalla los números pares entre 1 y 25

lista = []
def numerosPares():
    for x in range(1,25):
        if (x % 2 == 0):
            lista.append(x)
    return print(lista)

numerosPares()