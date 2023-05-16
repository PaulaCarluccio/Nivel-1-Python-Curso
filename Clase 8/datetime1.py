from datetime import datetime
import time
def mostrar_el_ahora():
    ahora = datetime.now()
    tiempo = int(datetime.timestamp(ahora))
    print(tiempo)
for i in range(10):
    mostrar_el_ahora()
    time.sleep(2)