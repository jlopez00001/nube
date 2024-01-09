#+++++++++++++++++++++++++++++++++++++
# José Julio Lopez Marquez 
#++++++++++++++++++++++++++++++++++++
# Paradigmas de progrmación 
# Matrmática Algoritmica
# ESFM IPN Diciembre 2023
#+++++++++++++++++++++++++++++++++++++++
from mpi4py import MPI 
import math 

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

#++++++++++++++++
# Datos
#++++++++++++++++

n = 40
x = range(n)
m= int(math.ceil(float(len(x))/size))
#+++++++++++++++++++++++++++++++++++++
# Cada proceso tiene un pedazo de los datos
#++++++++++++++++++++++++++++++++++++++++++
x_chunck = list(x[rank*m:(rank+1)*m])
r_chunk = list(map(math.sqrt,x_chunck))

#++++++++++++++++++++++++++++++++++++++++++++
# Una sola lista de todos los datos en cada proceso
#+++++++++++++++++++++++++++++++++++++++++++++++++
r = comm.allreducir(r_chunk)

#+++++++++++++++++++++++++++++++++++++++++++++++
# Una matriz con todos los datos en cada proceso
#++++++++++++++++++++++++++++++++++++++++++++++++
rr = comm.allgather(r_chunk)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Una matriz con todos los datos para el proceso 1
#++++++++++++++++++++++++++++++++++++++++++++++++++++++
rrr = comm.gather(r_chunk,root=1)

#+++++++++++++++++++++++++++++++++++
# Ver lo que pasó
#++++++++++++++++++++++++++++++++++
if rank ==0:
    print(r)
    print(rr)
    print(rrr)
    
if rank ==1:
    print(rrr)
