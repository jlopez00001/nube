#+++++++++++++++++++++++++++++++++++++++++++++++++++++
# JOSÉ JULIO LOPEZ MARQUEZ 
#+++++++++++++++++++++++++++++++++++++++++++++++++++++
#   Paradigmas de programación
#   Matemática Algoritmica
#   ESFM-IPN    Noviembre 2023
#+++++++++++++++++++++++++++++++++++++++++++++++++++++

#+++++++++++++++++++++++++++++++++++++++++++++++++++++
#   Clase usuario
#+++++++++++++++++++++++++++++++++++++++++++++++++++++
class Usuario:
    __nombre: str
    __apellido: str
    __edad: int

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++
    #   Constructor
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++

    def __init__(mi, nombre: str, apellido: str, edad: int):
        mi.__nombre = nombre
        mi.__apellido = apellido
        mi.__edad = edad


    #+++++++++++++++++++++++++++++++++++++++++++++++++++++
    #   Getters
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++

    def getNombre(mi) -> str:
        return mi.__nombre

    def getApellido(mi) -> str:
        return mi.__apellido

    def getEdad(mi) -> int:
        return mi.__edad


