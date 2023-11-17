#++++++++++++++++++++++++++++++++++++++++++++++++++++++
# JOSE JULIO LOPEZ MARQUEZ 
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#   Paradigmas de programación
#   Matemática Algoritmica
#   ESFM-IPN    NOV_2023
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#++++++++++++++++++++++++++++++++++++++++++++++++++
# la clase ClienteBancario está en el subdirectorio
# aplicación/banco/
#++++++++++++++++++++++++++++++++++++++++++++++++++
from aplicacion.banco.cliente_bancario import ClienteBancario

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# try: intenta (correr las indtrucciones )
# except : atrapar el error en una variable e
# e se puede convertir  en string
#++++++++++++++++++++++++++++++++++++++++++++++++++++

#++++++++++++++++++++++++++++++++++++++++++++++++++++
# Error por sacar más dinero del que tiene
#+++++++++++++++++++++++++++++++++++++++++++++++++
try:
      cliente = ClienteBancario("Jaime Andrade", "Hernández sánchez",28, 0.0)
      cliente.guardarDinero(300)
      print(cliente.imprimirInfo())
      cliente.retirarDinero(400)
      print(cliente.imprimirInfo())

      
#++++++++++++++++++++++++++++++++++++++++++++++++
# Excepcion es el objeto más general del error
#+++++++++++++++++++++++++++++++++++++++++++
except Excepion as e:
      print("Error:" + str(e))
            
#++++++++++++++++++++++++++++++
# Error por usar un atributo privado
#+++++++++++++++++++++++++++++++++++
            
try:
            print (cliente._nombres)
            
except Exception as ex:
            print ("Errro : " + str (ex))



            
#+++++++++++++++++++++++++++++++++
# Forma correcta
#+++++++++++++++++++++++++++++++
print (cliente.nombres)            










      
