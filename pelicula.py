from db import DB

class Pelicula(object):
    idPelicula = None
    nombre = None
    genero = None
    estrellas = None

    def Dar_de_Alta_Pelicula(self):
        DB.run("Insert into Pelicula(idPelicula, nombre, genero, estrellas) VALUES(" + str(self.idPelicula) + ", '" + self.nombre + "','"+ self.genero +"'," + str(self.estrellas) + ");")


    @staticmethod
    def ListarPeliculas():
        cursorPeli = DB().run("Select * from Pelicula;")
        lista = []

        for item in cursorPeli:
            lista.append(item)
        return lista

    @staticmethod
    def getPeli(idPeli):
        cursorPeli = DB().run("Select * from Pelicula where nombre = ('"+ idPeli +"');")
        lista = cursorPeli.fetchall()
        Peli = Pelicula()
        Peli.idPelicula = lista[0]["idPelicula"]
        Peli.nombre = lista[0]["nombre"]
        Peli.genero = lista[0]["genero"]
        Peli.estrellas = lista[0]["estrellas"]
        return Peli


