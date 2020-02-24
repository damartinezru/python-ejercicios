# Modifique el ejercicio anterior para que el conteo se haga hacia atrás desde el tiempo leído
# hasta cero

from datetime import datetime, timedelta
import time

def lecturaNumero(nombre):
    return int(input('Ingrese un numero para ' + nombre + ': '))

def contadorReversa(d=0, h=0, m=0, s=0):
    contador = timedelta(days=d, hours=h, minutes=m, seconds=s)
    while contador:
        time.sleep(1)
        contador -= timedelta(seconds=1)
        print("Tiempo que falta: {}".format(contador))


contadorReversa(lecturaNumero('dias'),lecturaNumero('horas'),lecturaNumero('minutos'),lecturaNumero('segundos'))
