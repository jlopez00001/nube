#+++++++++++++++++++++++++++++++++++++++++
# JOSÉ JULIO LOPEZ MARQUEZ 
#++++++++++++++++++++++++++++++++++++++++
# Paradigmas de progrmación 
# Matemática Algortimica
# ESFM Dic_2023
#+++++++++++++++++++++++++++++++++++++++++++++++

#++++++++++++++++++++++++++++++++++++++++++++++
# Ojo !!! PARA CORRER SE ESCRIBE:
# mpiexec -n 4 python3 27_mpibasico.py
# o estae es otra
# mpirum -n 4 python3 27_mpibasico.py
#+++++++++++++++++++++++++++++++++++++++++++++
# Para correr en 4 procesos
#+++++++++++++++++++++++++++++++++++++++++++++
from mpi4py import MPI

#++++++++++++++++++++++++++++++++++++++++++++++
# Crear un objeto comunicador 
#++++++++++++++++++++++++++++++++++++++++++++++
comunicadores = MPI.COMM_WORLD

#++++++++++++++++++++++++++++++++++++++++++++++++
# Numero total de procesos
#++++++++++++++++++++++++++++++++++++++++++++++++++
n_procesos = comunicadores.Get_size()

#++++++++++++++++++++++++++++++++++++++++++++++++
# Identificador de este proceso
#++++++++++++++++++++++++++++++++++++++++++++++++
quien_soy = comunicadores.Get_rank()
print (" Saludos desde el proceso " , str(quien_soy), "de", str(n_procesos))

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Si yo soy el cero hago esto 
#++++++++++++++++++++++++++++++++++++++++++++++++++
if quien_soy == 0:
    print("yo soy el proceso 0")

#++++++++++++++++++++++++++++++++++++++++++++++++
# Si yo soy el uno hago esto otro
#++++++++++++++++++++++++++++++++++++++++
elif quien_soy ==1 :
    print("soy el proceso 1")

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Si yo no soy ni el uno ni el cero hago esto
#++++++++++++++++++++++++++++++++++++++++++++++++++++
else :
    print ("yo no soy ninguno de los dos primeros procesos")

    
