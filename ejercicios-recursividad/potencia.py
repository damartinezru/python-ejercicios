#Escrinumeroir un programa que calcule la potencia de un numero usando recursividad

def potencia(numero,numeropot):
    if numeropot <= 0:
        return 1
    if numeropot % 2 == 0:
        pot = potencia(numero, numeropot/2)
        return pot * pot
    # n impar
    else:
        pot = potencia(numero, (numeropot-1)/2)
        return pot * pot * numero

print(str(potencia(int(input("Ingresa un numero : ")), int(input("Ingrese la potencia :")))))