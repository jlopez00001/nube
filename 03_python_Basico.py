#*********************************************************************
#José Julio LÓpez marquez
#********************************************************
# Matemática Algorítmica
# Paradigmas de progrmación 
# ESFM IPN septiembre 2023
#**************************************************************

#*****************************************************
# Conjunto en python
#********************************************************
even_nums = {2,4,6,8,10} #subconjunto de numeros pares 
print (even_nums)       



# EL bool    no es pártte del conjunto 
emp = { 1, 'steve' , 10.5, True} # conjunto de diferentes objetos
print (emp)
nums = { 1,2,3,4,5,6,7,8,9}
print (nums)

#*************************************************************
# convertir secunecia a conjunto 
 # no lo genera en orden 
#**************************************************************
s = set ('Hola')
print (s) 
s = set ((1,2,3,4,5)) # tupla conujnto 
print (s)

#*********************************************************
# De diccionario a conjunto : conjunto de llaves 
#*******************************************************
d = {1: 'uno ', 2: 'dos'}
s = set (d)
print (s)

s.add(100)
print (s)

s.update(nums)
print (s)

s.remove(100)
print (s)

s1={1,2,3,4,5}
s2={4,5,6,7,8}

su = s1|s2  # Unión 
print (su)

si= s1&s2   # intersección 
print(si)

sr = s1-s2  # diferncia de conjuntos 
print (sr)

sp =s2-s1
print (sp)

ss= s1^s2  # difencia simetrica
print (ss)

#***************************************************************
# uso de diccionarios 
#**********************************************************+
capitales = { "USA" : "Washinton D.C", "France" : " Paris ", "India": "New Deli"}
print (capitales )

#***************************************************************************
# llave : valor
#*************************************************************************
# Diccionario vacío
d= {}

# Llave entera , valor string 
numeros = {1: "uno", 2: "dos" , 3: "tres "}

# Llave real , valor string 
decimales = { 1.5 : "uno y medio", 2.5 : "dos y medio",  3.5 : "tres y medio"}

# Llave tupla , valor string 

cosas = { ("parker ", "reynols", "Camlin") : "pluma" , ("LG" , "SAMSUNG", " REALMI"): "CELUAR"}

# Llave string ,valor int
romanos = { 'I' : 1, 'II':2, 'III': 3, 'IV' : 4, 'V':5}
print (romanos)
print (romanos ["I"])

print (capitales.get("India"))
print (capitales.get("india"))

# Reporta llave y valor 
for k in capitales:
    print("key =" + k + ", Value = " + capitales [k])

# nuevo dato para el diccionario 

capitales["Mexico"] = "CDMX"
print (capitales )

# Borrar dato del diccionario
 del capitales ["Mexico"]
 print (capitales)

# Borrar todo el diccionario 
del capitales 

# Reportar llaves 
print (romanos.keys())

#reportar valores
print (romanos.values())
              
 
# Juicio de llave (está o no está la llave en el diccionario
print ("I" in romanos)
print ( "X" in romanos )
print ("XX" not in romanos)

                             

