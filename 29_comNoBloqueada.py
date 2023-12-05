#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# JOSÉ JULIO LOPEZ MARQUEZ
#++++++++++++++++++++++++++++++++++++++++++++++++
# Paradigmas de programción 
# Matemática Algoritmica
# ESFM IPN Dic_2023
#++++++++++++++++++++++++++++++++++++++++++

#++++++++++++++++++++++++++++++++++++++++++++++++
# Uso de MPI optimizado para cálculos numéricos
#+++++++++++++++++++++++++++++++++++++++++++++++++
from mpi4py import MPI
import numpy as np 

class Mensaje:
    def __init__(self,rank):

        #+++++++++++++++++++++++++++++++++
        # lista común 
        #+++++++++++++++++++++++++++++++++++
        self.x = [i for i in range(rank*10)]
        self.p = "vengo del proceso " +str(rank)

#+++++++++++++++++++++++++++
# Programa principal
#+++++++++++++++++++++++++++++++++
if __name__ == "__main__":
    comm= MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()

    s= Mensaje(rank)
    src = rank-1 if rank!=0 else size-1
    dst = rank+1 if rank!=size-1 else 0

    #++++++++++++++++++++++++++++++++++++
    # Envio no bloqueante 
    #++++++++++++++++++++++++++++++++++++
    comm.isend(s, dest =dst)

    #+++++++++++++++++++++++++++++++++++++++
    # Recibir no bloqueante con espera
    # req: request (petición)
    #+++++++++++++++++++++++++++++++++++++++++
    req = comm.irecv(source=src)
    a = req.wait()
    print ("soy el proceso ", rank, ", el resultado es " , len (a.x), a.p)

    #+++++++++++++++++++++++++++++++++++++
    # Arreglo de numpy para enviar 
    #++++++++++++++++++++++++++++++++++
    m = s.xx

    #+++++++++++++++++++++++++++++++++++++++++
    # Isend Irecv son para comunicación 
    # no bloqueante de arreglos de numpy
    #+++++++++++++++++++++++++++++++++++++
    comm.Isend(m, dest,dst)

    #++++++++++++++++++++++++++++++++
    # Arreglo vaacío para recibir 
    # con dimensión 10 y tipo de datos 
    # float64 (doble presición)
    #++++++++++++++++++++++++++++++++++
    aa = np.zeros(10,dtype=np.float64)
    req = comm.Irecv(aa, source=src)
    req.wait()
    print ("Soy el proceso", rank," , el resultado es ", aa)
    
