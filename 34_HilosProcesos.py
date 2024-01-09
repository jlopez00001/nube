#+++++++++++++++++++++++++++++++++++++++
# José julio Lopez Marquez 
#++++++++++++++++++++++++++++++++++++
# Paradigmas de progrmación 
# Matamática Algoritmica 
# ESFM IPN Diciembre 
#+++++++++++++++++++++++++++++++++++++

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Módulo de hilos, procesos, sistema, matemáticas y tiempo
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from threading import Thread
from multiprocessing import Process
import os 
import math
import time

#++++++++++++
# Función 
def calc():
    for i in range(0,4000000):
        math.sqtr(i)
        
#++++++++++++++
# Lista de hilos 
#++++++++++++++
threads = []

#++++++++++++++++++++++++++++++
# Procesadores en mi máquina
#+++++++++++++++++++++++++++++ 

cpus = os.cpu_count()
print("Núemero de procesadores: ", cpus)

#+++++++++++++++++++++++++++++++++++++
# Inscribir hilos en la lista 
#+++++++++++++++++++++++++++++++++++++
for i in range (cpus):
    print("registrando el hilo %d" %i )
    threads.append(Thread(target=calc))
start =time.time()
#+++++++++++++++++++++++++++++++++++++++++++
# Iniciar los hilos (son seriales) 
#++++++++++++++++++++++++++++++++++++++++++
for thread in threads :
    thread.start()
    
#++++++++++++++++++++++++++++++++++++++
# Esperar a que terminen los hilos
#+++++++++++++++++++++++++++++++++
for thread in threads:
    thread.join()

end = time.time()
#++++++++++++++++++++++++++++++++
# Restar los tiempos 
#+++++++++++++++++++++++++++++++
print(" Se tardó: ", end-start) 

#++++++++++++++++++++++++++++
# lista de procesos
#+++++++++++++++++++++++++++++
procesos = [] 
for i in range (cpus):
    print(" registrando el proceso %d" % i)
    procesos.append(Process(target = calc))
    
start = time.time()

#+++++++++++++++++++++++++++++++++++++++
# Iniciar procesos
#+++++++++++++++++++++++++++++++++++++++
for proceso in procesos:
    proceso.start()
    
#+++++++++++++++++++++++++++++++
# Terminar procesos
#+++++++++++++++++++++++++++++++
for proceso in procesos:
    proceso.join()

end =time.time()
print("setardó: ", end-start )            
            