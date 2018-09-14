from db import DB


class Cine(object):
    idCine = None
    nombre = None
    lista_peliculas = []
    lista_salas = []
    lista_horarios = []

    def Dar_de_Alta_Cine(self):
        DB.run("Insert into Cine(idCine,nombre) VALUES(" + str(self.idCine) + ", '" + self.nombre + "');")


