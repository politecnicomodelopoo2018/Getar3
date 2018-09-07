from db import DB

class Cine(object):
    idCine = None
    nombre = None
    lista_peliculas = []

    def Dar_de_Alta_Cine(self):
        DB.run("Insert into Cine(idCine,nombre) VALUES(" + str(self.idCine) + ", '" + self.nombre + "');")

    def Agregar_pelicula(self,p):
        self.lista_peliculas.append(p)

