#+++++++++++++++++++++++++++++++++++++++++++++++++++++
# José julio lopez marquez 
#+++++++++++++++++++++++++++++++++++++++++++++++++++++
#   Paradigmas de programación
#   Matemática Algoritmica
#   ESFM-IPN    NOV_2023
#++++++++++++++++++++++++++++++++++++++++++++++++++++

#+++++++++++++++++++++++++++++++++++++++++++++++++++++
#   Del dierectorio aplicacion, el subdirectorio rapositorio,
#   el archivo basededatos.py : trae el objeto Basededatos
#+++++++++++++++++++++++++++++++++++++++++++++++++++++

from aplicacion.repositorio.basededatos import BaseDeDatos

#+++++++++++++++++++++++++++++++++++++++++++++++++++++
#   Del directorio aplicacion, el subdirectorio repositorio,
#   el archivo s3.py : trae el objeto S3
#+++++++++++++++++++++++++++++++++++++++++++++++++++++

from aplicacion.repositorio.s3 import S3

#+++++++++++++++++++++++++++++++++++++++++++++++++++++
#   Del directorio aplicacion, el sobdirectorio repositorio,
#   el archivo sistemadearchivos.py : trae el objeto SistemaDeArchivos
#+++++++++++++++++++++++++++++++++++++++++++++++++++++

from aplicacion.repositorio.sistemadearchivos import SistemaDeArchivos

#+++++++++++++++++++++++++++++++++++++++++++++++++++++
#   Del directorio aplicacion, el  subdirectorio repositorio
#   el archivo usuario.py : trae el objeto Usuario
#+++++++++++++++++++++++++++++++++++++++++++++++++++++

from aplicacion.modelos.usuario import Usuario

#+++++++++++++++++++++++++++++++++++++++++++++++++++++
#   Del directorio aplicacion, el subdirectorio negocios,
#   el archivo manejodeinscripciones.py : trae el objeto ManejoDeInscripciones
#+++++++++++++++++++++++++++++++++++++++++++++++++++++

from aplicacion.negocios.manejodeinscripciones import ManejoDeInscripciones

#+++++++++++++++++++++++++++++++++++++++++++++++++++++
#   Crear el objeto Usuario
#+++++++++++++++++++++++++++++++++++++++++++++++++++++
usuario = Usuario("Roberto","Jimenez", 18)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++
#   Clear el objeto s3
#+++++++++++++++++++++++++++++++++++++++++++++++++++++

repositorioS3 = S3("321321321","sdf324223","MiCubeta")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++
#   Interface inscribir usuario del objeto ManejoDeInscripciones
#+++++++++++++++++++++++++++++++++++++++++++++++++++++
ManejoDeInscripciones.inscribirUsuario(usuario,repositorioS3)
print("\n")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++
#   Crear el objeto sistema de archivos
#+++++++++++++++++++++++++++++++++++++++++++++++++++++

repositorioSistemaDeArchivos = SistemaDeArchivos("/home/users")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++
#   Interface inscribirUsuario del objeto ManejoDeInscripciones
#+++++++++++++++++++++++++++++++++++++++++++++++++++++

ManejoDeInscripciones.inscribirUsuario(usuario,repositorioSistemaDeArchivos)
print("\n")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++
#   Crear el objeto basededatos
#+++++++++++++++++++++++++++++++++++++++++++++++++++++
repositorioBaseDeDatos = BaseDeDatos("localhost","admin","admin123")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++
#   interface inscribirUsuario del objeto ManejoDeInscripciones
#+++++++++++++++++++++++++++++++++++++++++++++++++++++

ManejoDeInscripciones.inscribirUsuario(usuario,repositorioBaseDeDatos)
print("\n")

