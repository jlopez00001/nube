#++++++++++++++++++++++++++++++++++++++++++++++++++++
# JOSE JULIO LOPEZ MARQUEZ 
# Paradigmas de Programación 
# Matemática Algortimica
# ESFM IPN Octubre 2023
#++++++++++++++++++++++++++++++++++++++++++++++++++++

#+++++++++++++++++++++++++++++++++++++++++++++++++++
# Clase computadora 
#++++++++++++++++++++++++++++++++++++++++++++++++++++
class Computadora:
    marca: str = None 
    capacidad: int =0
    ram: int =0

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++
    #  Constructor 
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++
    def _init_ (self,marca:str, capacidad:int , ram:int):
        print(f"accediendo al constrictor de la pc : {marca} con almacenaminento de {self.capacidad}GB Y memoria de {self.ram}GB")
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # Destructor 
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        def _del_(self):
            print(f"Se elimino la computadora : {self.marca}")


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# clase persona 
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class persona: 
    nombres : str = None 
    apellidos : str = None 
    edad : int =0
    direccion : str  =None 
    computadora : Computadora = None 

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Contructor de persona 
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def _init_ (self , nombres : str, apellidos : str, edad:int , direccion: str ,marca:str , capacidad:int,ram:int ):
        self.nombres = nombres 
        self.apellidos = apellidos 
        self.edad = edad
        self.direccion = direccion 
        self.Computadara = Computadora (marca, capacidad, ram)
        print (f, "---Accedimos al constructor de la persona : {nombres} {apellidos} ")




   def imprimirInfo(self) -> None :
       print (f"---Mi nombre es {self.nombres} {self.apellidos}, tengo { self.edad} años de edad , vivo en {self.direccion} ")
       self.Computadora.imprimirInfoPC()


       #+++++++++++++++++++++++++++++++++++++++++++
       # Destructor 
       #+++++++++++++++++++++++++++++++++++++
       def _del_(self):
           print (f"----Eliminamos a la persona... {self.nombres} {self.apellidos}")


#++++++++++++++++++++++++++++++++++++++++++++
# Funcion 1 es el programa
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def funcion1():
    persona =  Persona ("Carlos", "perez", 40, "xochimilco", "Lenovo", 700,8)
    print("\n")
    persona.imprimirInfo()
    print ("\n")
    persona2 = Persona ("Magdalena", "Carrillo", 35, "jalapa", "IBM", 200,4)
    print("\n")
    persona2.imprimirInfo()
    print ("\n")
#+++++++++++++++++++++++++++++++++++++++++++++++++
# Llamar a funcion1
#+++++++++++++++++++++++++++++++++++++++++++
funcion1() 























