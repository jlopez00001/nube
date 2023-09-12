#**********************************************
# José Julio López Márquez
#**********************************************
#Matemática Algorítmica
#ESFM
#Septiembre de 2023
#********************************************

#**************************************************
# Input permite obtener datos del usuario en prompter
#**************************************************
nombre = input ("Dame tu nombre")
print ("Hola como estás", nombre)

#****************************************************
#Los enteros son de precisión ilimitada
#******************************************************
y= 50000000000000000000000000000000
print (y)

#******************************************************
# Sepueden delimitar números con guion bajo pero no con coma
#************************************************************
y= 5_000_000
print (y)

#***********************************************************
# La función int() cambia strings y floats a enteros
#*********************************************************

numero = int ( input (" Dame tu edad : "))
type (numero)
#************************************************************
# La notacón cinetifica de flotantes utiliza e o E
#*********************************************************
# 1.2 x 10 ^{-9}
#*******************************************************
y = 1.2e-09
print (y)

#*********************************************************************
# La funnción float () convierte strings y enteros a flotantes
#******************************************************************
y= float ("14.3")
print (y)

#*********************************************************************
# Los complejos se escriben con la raiz de menos uno
# j siempre con un  numero como prefijo 
# no acepta la j suelta
#*********************************************************************
z= 1+1j

# suma +
# resta -
# multiplicación *
# divición /
# modulo %
# exponente **
# // función piso 
# Funciones para transformar números int() float() complex()
# Operaciones abs() round() pow()
print (round (3.14159,1))

#************************************************************************
# strings de varias líneas
#***********************************************************************
parrafo = """ En el bosque de la china
la chinita se perdio"""
print(parrafo)

#*************************************************
# La funcion len() obtiene el tamaño del string 
#******************************************************
n = len (parrafo)
print(n)

#*****************************************************************************
# Las letras en un string ocupan lugares como en un arreglo
# (tambien de atras para adelante comenzando en -1 el ultimo)
#********************************************************************
palabra = "hola"
print (palabra[0])
print (palabra[-1])


