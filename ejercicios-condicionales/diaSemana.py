# Condicionales
# Programa que dado un número del 1 a 7 escriba el correspondiente nombre del día de la semana

semana = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
def diaSemana(dia):
    if (dia > 7 or dia <= 0):
        return "Numero de la semana no valido"
    if(dia != 0):
        return semana[dia-1]

            
print("El dia de la semana que elegiste es " + str(diaSemana(int(input("Elige un dia de la semana :")))))