
def preguntaCiclica():
    respuesta = input("¿Desea Continuar S/N?")
    while respuesta != 'N':
        respuesta = input("¿Desea Continuar S/N?")
        if respuesta == 'N':
            pass
preguntaCiclica()
