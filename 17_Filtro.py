#++++++++++++++++++++++++++++++++++++
# JOSÉ JULIO LOPEZ MARQUEZ 
#+++++++++++++++++++++++++++++++++++++++++
# Paradimas de programación 
# Matemática Algoritmica
# ESFM IPN nov_2023
#++++++++++++++++++++++++++++++++++++++++++++

#+++++++++++++++++++++++++++++++++++
# Uso de filtros
#+++++++++++++++++++++++++++++++

#++++++++++++++++++++++++++
# Uso de filtros
#+++++++++++++++++++++++++

#+++++++++++++++++++++++++++
# Hacer una lista de los números por arriba del promedio
#++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Módulo de estadistica
import statistics

bigdata = [ 1.3,2.7,0.8,4.1,4.3,-0.1]
promedio =statistics.mean(bigdata)
print (promedio)

#++++++++++++++++++++++++++++++++++++++++
# Hazme una lista de elementos que cumplan que la consición x>promedio
# filter (condición,datos )
#+++++++++++++++++++++++++++++++++++++++
print (list(filter(lambda x: x>promedio,bigdata)))

#+++++++++++++++++++++++++++++++++++++
# limpiar los datos
#++++++++++++++++++++++++++++++
paises = ["", "Argentina","", "Brasil","chile", "MÉXICO", "", "Colombia","","","Cuba","Venezuela"]

#+++++++++++++++++++++++++++++++++++++
# Filtra lo que no tiene nada
#+++++++++++++++++++++++++++++++++
print (list(filter(None, paises)))
