# Escribir un programa que almacene en un lista los números primos comprendidos
#  entre un rango definido por el usuario.
def almacenar(inicio, limite):
    lista  =[]
    for x in range(inicio,limite):
        if (x % 2 != 0):
            lista.append(x)
    return lista
print("Los numeros primos son :"+ str(almacenar(int(input("Ingrese el valor del limite inferior : ")), int(input("Ingrese el valor del limite maximo : ")))))