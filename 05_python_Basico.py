#****************************************
# JOSE JULIO LOPEZ MARQUEZ 
#***************************************
# Matemática Agoritmica
# Paradigmas de progrmacion 
# ESFM IPN Septiembre 2023
#****************************************+


#*********************************
# Condicionales 

#********************************+
precio=50
#************************************
# si esto ...
#*******************************+
if precio <50
print ("El precio es menor que 50")
#**********************************************
# si no si esto otro.....
# ********************************+
elif precio >50:
    print(" El precio es mayor a 50")
#----------------------------------------
# si nada de lo anterior 
#-------------------------------------
else :
    print("Elprecio es 50")

precio = 50
cantidad =5 
total = precio * cantidad
#*********************************************
# Condicional de igualdad son ==
# --------------------------------------------
elif total ==100:
    print ("total es 100")
else:
    print ("Total menor que 100")

# *********************************************
# Contador minetras la condicion sea verdadera
#--------------------------------------
num =0
while num <5:
    num = num +1
    print ('num = ', num)
num =0
while num <5:
    num += 1              num=num+1
    print('num=', num)
    if num ==3:
        break
num =0
while num <5:
    num +=1
    if num >3:
        continue   # evitar lo que sigue 
    print ('num= ' , num)

#**************************
# Bucle sobre listas
#*****************************
nums = [10,20,30,40,50]
for i in nums :
    print(i)
#************************************
# Bucle sobre un string 
#******************************+
for char in 'hola':
    print(char)

#*************************+
# Bucle sobre un diccionario 
#****************************
# key = llave
# value = valor 
#*******************************
for k,v in numeros.items():
    print("key =", k, ", value=", v)

