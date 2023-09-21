#****************************************
# JOSE JULIO LOPEZ MARQUEZ 
#***************************************
# Matemática Agoritmica
# Paradigmas de progrmacion 
# ESFM IPN Septiembre 2023
#****************************************
# Mi primera función 
#****************************************
def saludo():
    #***********************************
    # Documentacón rápida de la función 
    #***********************************
    """ Esta funcón saluda """
    print ('Quiúboles , ¿cómom estas')
#******************************************
# Llamado de la función 
#******************************************
saludo()
#******************************************
# se ejecuta pero no se asigna
#********************************************
salida =saludo()

#******************************************
# Esto no funciona
#******************************************
print(salida)
#*********************************************
# Mostrar documentación 
# help(saludo)

#**********************************************
# Función con argumrnto
#*********************************************
def salu2(nombre):
    """esta función te saluda por tu nombre"""
    print("Que onda ese " , nombre , "!")
salu2("jose ")
salu2("julio")
#**********************************************
# Ahorrar trabajo del interprete 
# nombre : str la variable nombre es un str
#**********************************************
def saludos(nombre: str):
    """esta función te saluda por tu nombre estrictamente"""
    print ("Que onda ese ", nombre , "!")
saludos("jose")
a=123
print (type(a))
#******************************************
# función con muchos argumentos 
#*********************************************
def saludos_multiples(nombre1, nombre2, nombre3):
    """esta función saluda a 3 personas al mismo tiempo"""
    print("Hola ", nombre1,",",nombre2,"y", nombre3)
    
saludos_multiples("hugo", "paco", "luis")

#**************************************************
# Función con cualquier número de argumentos
#***********************************************
def muchos_saludos(*nombres):
    """Esta función saluda a todos los que quieras"""
    i=0 
    #***********************************************
    # end = es para ponerlo de corrido 
    #*******************************************
    print("hola ", end="")
    while len (nombres)>i:
        
        if (i==len(nombres)-1):
            print(nombres[i])
        i+=1    
muchos_saludos("Bosco","Angel", "David", "Tamara", "MIli", "Edwin", "lev")
def greet(firstname, lastname):
    print('Hello', firstname, lastname)
    
#***********************************************
# llamar a una función con argumentos en des oerden
#**************************************************
greet(lastname='jobs', firstname='Steve')
#**************************************************
#función con argumentos escondidos **
#*********************************************
def greet(**person):
    #*****************************************
    # Persona tiene carateristicas firstname y lastname
    #***************************************************
    print ('Hello ', person['firstname'], person["lastname"])
greet(firstname='Steve', lastname='jobs')
greet(lastname='jobs', firstname='Steve')
greet(firstname='Bili', lastname='Gates', age=55) # se pueden pasar mas argumentos de los nesesarios

#*********************************
# Funciones con valores por defecto
#***************************************
def greet(name='Guest'):
    print("Hello", name)
    
greet() # utiliza el valor dado de antemano
greet('Steve')

#****************************************
# función con resultado
#******************************
def suma(a,b):
    return a+b
#*********************************************
# Programación funcional
# se pueden usar funciones dentro de otras funciones 
total=suma(5,suma(10,20))
print(total)

#*********************************
# calculo lambda
# nombre de la función = lambda variable : función 
#************************************************

x_al_cuadrado=lambda x :x*x
al = x_al_cuadrado(5)
print(al)

#**********************************************
# Lambda de varias variables 
#************************************************
suma = lambda x1,x2,x3 : x1+x2+x3
print (suma(99,98,97))
sumas = lambda *x: x[0]+x[1]+x[2]+x[3]
print (sumas(100,200,300,400))

#**********************************
# uso de una función anónim
# el argumento de afuera entre parentesis
#******************************************
print((lambda x: x*x)(6)) #función anónima

#***************************************
# Funcion con variable global
# EVITAS EL EXCESO !!!!!!!!!!
#***************************************
name = 'Steve'
def greet():
    global name # para utilizar una variable global que viene fuera del bloque
    name='Bill'
    print('Hello', name)
    
greet()


















