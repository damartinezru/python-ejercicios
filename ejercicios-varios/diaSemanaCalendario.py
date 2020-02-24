#Escribir un programa que implemente un calendario perpetuo, es decir, que dado una fecha
#en formato mes, día y año le retorne al usuario el día de la semana que corresponde para esta
#fecha.

diasSemana = ("Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo")

import datetime



def calendario(ano, mes, dia):
    tiempo = datetime.date(ano,mes,dia)
    diaTiempo = tiempo.weekday()
    diaSemana = diasSemana[diaTiempo]
    return "Este dia de ese año fue un {}".format(diaSemana)


print(str(calendario(int(input("Ingrese el año : ")), int(input("Ingrese el mes : ")), int(input("Ingrese el dia : ")))))
    