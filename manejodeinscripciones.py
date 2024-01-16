#+++++++++++++++++++++++++++++++++++++++++++++++++++++
# JOSÉ JULIO LOPEZ MARQUEZ 
#+++++++++++++++++++++++++++++++++++++++++++++++++++++
#   Paradigmas de programación
#   Matemática Algoritmica
#   ESFM-IPN    Noviembre 2023
#+++++++++++++++++++++++++++++++++++++++++++++++++++++

from aplicacion.modelos.usuario import Usuario
from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios

#+++++++++++++++++++++++++++++++++++++++++++++++++++++
#   Clase ManejoDeInscripciones
#   NO TIENE VARIABLES!!!
#+++++++++++++++++++++++++++++++++++++++++++++++++++++

class ManejoDeInscripciones:
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++
    #   Decorador staticmethod
    #   el objeto sólo tiene la función iscribirUsuario
    #   ENVUELVE LA FUNCION SIN LLAMAR VARIABLES LOCALES
    #   el objeto ManejoDeInscripciones es la interface intercambiable


    @staticmethod
    def inscribirUsuario(usuario: Usuario, repositorioDeUsuarios: RepositorioDeUsuarios) -> None:
        print("------> Guardando usuario ... \n")
        repositorioDeUsuarios.abrir()
        repositorioDeUsuarios.guardar(usuario)
        repositorioDeUsuarios.cerrar()

