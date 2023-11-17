#++++++++++++++++++++++++++++++++++++
# JOSÉ JULIO LOPEZ MARQUEZ 
#+++++++++++++++++++++++++++++++++++++++++
# Paradimas de programación 
# Matemática Algoritmica
# ESFM IPN nov_2023
#++++++++++++++++++++++++++++++++++++++++++++

#++++++++++++++++++++++++++
# yield transforma la función a iterador
#+++++++++++++++++++++++++++++++++++++
def migenerador():
      print("Primero")
      yield 10
      print("segundo")
      yield "20"
      print("Tercero")
      yield "hola"

      
#++++++++++++++++++++++++++++++++++++++++
#  gen es un iterador
#++++++++++++++++++++++++++++++++++++
gen = migenerador ()
val1 = next(gen)
print(val1)
val2 = next(gen)
val3= next(gen)
print(val3)
