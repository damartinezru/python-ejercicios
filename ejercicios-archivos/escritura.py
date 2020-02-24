# Escribir un programa que escriba la lista de caracteres ASCII dentro de un archivo de texto


def escribirArchivo():
    texto = ""
    for n in range(1, 254):
        texto += " " + chr(n)
    with open("D:/Escritorio/ejercicios-modelos2/ejercicios-20/ejercicios-archivos/file.txt", 'w', encoding="utf-8") as f:
        f.write(texto)
    return texto


print(escribirArchivo())
