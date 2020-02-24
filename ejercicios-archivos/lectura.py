# Escribir un programa que lea y muestre en pantalla el archivo generado en el ejercicio
# anterior


def leerArchivo():
    f = open("D:/Escritorio/ejercicios-modelos2/ejercicios-20/ejercicios-archivos/file.txt",
             'r', encoding="utf-8")
    return f.read()



print(leerArchivo())
