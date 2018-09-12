from db import DB
from pelicula import Pelicula

class Cine(object):
    idCine = None
    nombre = None
    lista_peliculas = []

    def Dar_de_Alta_Cine(self):
        DB.run("Insert into Cine(idCine,nombre) VALUES(" + str(self.idCine) + ", '" + self.nombre + "');")

    def Agregar_pelicula(self,p):
        self.lista_peliculas.append(p)

    @staticmethod
    def getUsuario():
        d = DB().run("Select * from Pelicula;")
        lista = d.fetchall()
        unaPeli = Pelicula()
        unaPeli.id = lista[0]["idUsuario"]
        unaPeli.nombrePelicula = lista[0]["nombrePelicula"]
        unaPeli.contraseña = lista[0]["genero"]
        unaPeli.estrellas = lista[0]["estrellas"]


