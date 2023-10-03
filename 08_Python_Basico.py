#******************************************
 #josé JUlio Lopez marquez 
#*********************************************
# Paradigmas de progrmación 
# Matemática Algoritmica 
# ESFM IPN SEP 2023
#*******************************************

#**************************************++
# progrmación orientada a objetos 

#*********************************************+
# Una clase para un objeto vacio
# NO está tan vacio , necesita 
# La ppalabra pass =pasar 
#**********************************************
#****************************************
class ObjetoVacio:
    pass
# ********************************
# Nada es un objeto vacio 
#**********************************
nada =ObjetoVacio()
print(type(nada))

#***********************************************
# La clase llanta
#**********************************************+
class Llanta:
    #*********************************************+
    # Variable cuenta es de toda la clase 
    #***********************************************
    cuenta =0
    #***********************************
    # Función constructora de identidad
    # _int_ es una función reservada 
    # comienza con uno mismo : self
    # pero puede ser otro nombre (mi)
    # parametros de entrada = default
    #****************************************************+
    def _int_(mi,radio=50,ancho=30,presión =1.5):
        # Variable de la estructura completa llanta 
        Llanta.cuenta +=1
        # Variables exclusivas de cada objeto
        mi.radio = radio 
        mi.ancho = ancho
        mi.presión = presión

#**********************************************************
# Objetos (instanciados )
#*********************************************************
llanta1 = Llanta (50,30,1.5)
llanta2 = Llanta (presión=1.2)
llanta3 = Llanta ()
llanta4 = Llanta (40,30,1.6)

#********************************************************
# Objeto que contiene otros objetos 
#********************************************************
class Coche:
    def _int_(mi,ll1,ll2,ll3,ll4):
        mi.llanta1 = ll1
        mi.llanta2 = ll2
        mi.llanta3 = ll3 
        mi.llanta4 = ll4

        
micoche = Coche (llanta1,llanta2,llanta3,llanta4)

print ("Total de llantas : ", Llanta.cuenta) #Variable global de la clase 
print ("Presión de la llanta 4 =", llanta4.presión) # presión de la llanta 4
print ("Radio de la llanta 4 =" , llanta4.radio)
print ("Radio de la llanra 3 = " , llanta3.radio)
print("Presión de la llanta 1 de mi coche =", micoche.llanta1.presión)

#*******************************************************+
# Encapsulamiento
#*****************************************************

#*******************************************************
# Uso de la función de python property para poner y obtener atributos
#*******************************************************************
class Estudiantes :
    def _int_ (mi): 
        mi._nombre =  ''

    def ponerme_nombre (mi,nombre):
        print ('se llamo a ponerme_nombre ')
        mi._nombre = nombre

    def obtener_nombre(mi):
        print('sellamo a obtener nombre ')
        return mi._nombre
    nombre = property(obtener_nombre, poner_nombre)


#**********************************************************+
# Crear objeto estudiante sin nombre 
#*******************************************************
estudiante = Estudiante ()

#****************************************************
# ponerle nombre usando la propiedad nombre y el metodo ponerme_nombre
# ( sintener que llamar explicitamente a la función )
#*******************************************************

estudiante.nombre = "Diego"
#****************************************************************
# Obtener el nombre con el metdo obtener_nombre
# _nombre es una variable encapsulada ( no visible desde fuera )
# ( sin tener que llamar explicitamente a la función obtener_nombre)
#******************************************************************
print (estudiante.nombre)

# Esto no funciona 
# print (estudiante._nombre)

#**************************************************************
# Herencia de clases
#*********************************************************
class Cuadrilatero:
    def _int_(mi, a,b,c,d):
        mi.lado1=a
        mi.lado2=b
        mi.lado3=c
        mi.lado4=d


    def perimetro(mi):
        p=mi.lado1 +  mi.lado2 + mi.lado3 + mi.lado4
        print ("perimetro=", p)
        return p


#***************************************************************+
# Su hijo rectangulo 
# Rectangulo es hijo de cuadrilatero 
# Rectangulo (Cuadrilatero)
#*****************************************************
class Rectangulo (cuadrilatero):
    def _int_ (self ,a,b):
        #************************************
        # Constructor de su madre 
        #*******************************************
        super()._init_(a,b,a,b)
        
#*********************************************
# Su nieto Cuadrado 
# Hijo de Rectangulo
#********************************************
class Cuadrado (Rectangulo):
    def _init_(self,a)
    super()._init_(a,a)

def area (self):
    area = self.lado1**2
    return area
  #def perimetro (self):
  #   p= 4.0*self.lado1
  #   print("perimetro =",p)
  #   return p

#******************************************
#   Crear un cuadrado 
#***************************************
cuadrado1 = Cuadrado(5)

#********************************************
# Llamar al metodo perimetro de su abuelo cuadrilatero
#*************************************************
perimetro1= cuadrado1.perimetro()

#**********************************************
# Llamar a su propio metodo de area 
#*******************************************
area1= cuadrado1.area()
print ("perimetro =", perimetro1)
print ("Área =", area1)

#***********************************************+
# Sobre escribir un metodo de su madre o abuela o tatarabuela ....
# es volver a definir una funcion ya esxistente 
#**************************************************






























































































