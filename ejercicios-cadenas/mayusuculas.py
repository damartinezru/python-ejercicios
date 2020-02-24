# Ejercicios cadenas
# Escribir un programa que cuente las mayúsculas de una cadena de caracteres.



def conteoMayusculas(cadena):
    cuenta = 0
    for x in cadena:
        if(x.isupper()) == True:
            cuenta+=1
    return cuenta

print("El numero de mayusculas en la cadena :" + str(conteoMayusculas(input("Ingresa una cadena de texto :"))))
        