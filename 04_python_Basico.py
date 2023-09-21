*********************************
# Jose julio lopez marquez 
#***********************************
# Mematemática Algoritmica
# Paradigmas de progrmación 
# ESFM IPN Septiembre
#*******************************

#*********************************
# Listas 
# las listas pueden ser de objetos diferentes
#***********************************
miprimeralista=[]
print(miprimeralista)
#********************************************
# Llenado de listas
#**************************************
miprimeralista=[1,"javier", 1.34,"Bosco", "Angel", "Abigail", True]
print(miprimeralista)

#*************************************************
# list hacer una listas
# range (i,j) : secuencia de i asta j-1
#*************************************************
nums =list (range(1,61))
for i in nums:
    print (i)

#************************************************
# Incluir nuevos elementos a una listas
#***********************************************
nums.append(61)
nums.append(62)
nums.append(61)
print(nums)

#********************************
# Quitar elementos de una listas
#**************************************
nums.remove(61)
print(nums)

#******************************************
# Quitar elmentos con indice indice i 
#*******************************************
i =61
del nums[i]
print (nums)
#*********************************************
# Borrar la listas
#*********************************************
del nums
#**********************************************
# sumar listas
#****************************************************
L1=[1,2,3]
L2=[4,5,6]
print(L1+L2)

#****************************************************
# llenado a mano
#***********************************************
potencial = []
for i in range (0,10000):
    potencial.append(float(i))
print(potencial[100])

#*****************************************************
# Generar una tupla con la listas
#****************************************************
potencial= tuple(potencial)
print (potencial[100])#**







































    









