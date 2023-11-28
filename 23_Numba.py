#++++++++++++++++++++++++++++++++++++++++++++++
# José julio lopez marquez 
#+++++++++++++++++++++++++++++++++++++++++++++++
# Paradigmas de progrmación 
# Matemática Algoritmica
# ESFM IPN Nov_2023
#+++++++++++++++++++++++++++++++++++++

#+++++++++++++++++++++++++++++++++++++
# Importar numba, numpy y time
#+++++++++++++++++++++++++++++++++++++++

from numba import jit 
import numpy 
import time

#++++++++++++++++++++++++++++++++++++++
# Loop cualquira en python puro 
#++++++++++++++++++++++++++++++++++++++

def lento(a):
    t=0.0
    # para cada renglón 
    for i in range(a.shape[0]):
        t+= numpy.tanh(a[i,i])

#++++++++++++++++++++++++++++++
# Loop sin intérprete
#++++++++++++++++++++++++++++
@jit(nopython = True)
def rapido(a):
    t=0.0
    for i in range (a.shape[0]):
        t+= numpy.tanh(a[i,i])

    return a+t 
#++++++++++++++++++++++++++++++++++++++++++++++
# Arreglo unidimensional lleno del 1 al 10000
# convirtiendo en matriz de 100X100
#+++++++++++++++++++++++++++++++++++++++++++++++
x = numpy.arange(10000).reshape(100,100)

#++++++++++++++++++++++++++++++++++++++++++++++++
# La primera llamada incluye el tiempo de copilación 
#++++++++++++++++++++++++++++++++++++++++++++++++++
start = time.time()
rapido(x)
end = time.time()
print ("Tiempo incluyendo compilación = %s " % (end-start))
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# La segunda llamada es para obtener el tiempo de ejecución
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
start= time.time()
rapido(x)
end = time.time()
print(" Tiempo de ejecución usando numba = %s" %(end-start))
#+++++++++++++++++++++++++++++++++++++++++++++++++++++
# Tiempo para la función sin optimización 
#++++++++++++++++++++++++++++++++++++++++++++++++++++++
start = time.time()
lento(x)
end = time.time()
print ("Tiempo de ejecución en python puro =%s" %(end-start))

