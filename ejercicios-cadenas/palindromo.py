# Ejercicio Cadenas
# Decir si una frase es o no un palíndromo, es decir, si se lee igual de derecha a a izquierda
# que de izquierda a derecha.


def verificacion(palabra):
    igual, aux = 0, 0
    for ind in reversed(range(0, len(palabra))):
        if palabra[ind].lower() == palabra[aux].lower():
            igual += 1
            aux += 1
    if len(palabra) == igual:
        return "La palabra es un palindromo"
    else:
        return "La palabra no es un palindromo"
    
print(str(verificacion(input("Ingrese una palabra :"))))
