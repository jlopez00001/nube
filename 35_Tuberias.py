#+++++++++++++++++++++++++++++++++++++++
# José julio Lopez Marquez 
#++++++++++++++++++++++++++++++++++++
# Paradigmas de progrmación 
# Matamática Algoritmica 
# ESFM IPN Diciembre 
#+++++++++++++++++++++++++++++++++++++

#++++++++++++++++++++++++++++++++
# Uso de tuberías para comunicación 
#+++++++++++++++++++++++++++++++++++++++++
from multiprocessing import process, Pipe 

#+++++++++++++++++++++
# Manda vector 
#+++++++++++++++++++++
def f(extremo):
    extremo.send([0,1,2,3,4])
    extremo.close()
    
#++++++++++++++++++++++++++++++
# Recibe vector y le suma 100 a cada componente 
#++++++++++++++++++++++++++++++
def g(extremo):
    a= extremo.recv()
    for i in a:
        a[i] += 100
    print(a) 
    extremo.close()
    
 #+++++++++++++++++++++++++
 # programa principal
 #++++++++++++++++++++++++++
if __name__ == "__main__":
    
    #++++++++++++++++++++++++++
    # Tuberia con sus extremos 
    #+++++++++++++++++++++++++++
    extremo1, extremo2, =Pipe()
     
     #+++++++++++++++++++++++++++++++++++
     # instanciar procesos (target es la función)
     #   (args son los argumentos de la función ) 
    proceso1 = process(target=f, args= (extremo1, ))
    proceso2 = process(target=g, args= (extremo2, ))
     
     #++++++++++++++++++++++++++
     # Comenzar procesos
     #+++++++++++++++++++++++++
    proceso2.start()
    proceso1.start()
     #+++++++++++++++++++++++++++++++
     # Esperar a que terminen los procesos
     #+++++++++++++++++++++++++++++++++
    proceso1.join()
    proceso2.join()
          