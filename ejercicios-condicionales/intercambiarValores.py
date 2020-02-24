# Condicionales
# Escribir un programa que lea dos números desde el teclado y si el primero es mayor que el segundo
# intercambie sus valores.

def intercambio(numeroUno, numeroDos):
    if (numeroUno > numeroDos):
        valorAnteriorUno = numeroUno
        valorAnteriorDos = numeroDos
        numeroDos = valorAnteriorUno
        numeroUno = valorAnteriorDos
        return "El valor uno ahora es :" + str(numeroUno) + " El valor dos ahora es: " + str(numeroDos)
    else :
        return "El valor uno es menor que el dos"

print(str(intercambio(int(input("Ingrese el valor uno :")), int(input("Ingrese el valor dos :")))))
    
        