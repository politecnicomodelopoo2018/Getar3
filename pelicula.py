from db import DB

class Pelicula(object):
    idPelicula = None
    nombre = None
    genero = None
    estrellas = None

    def Dar_de_Alta_Pelicula(self):
        DB.run("Insert into Pelicula(idPelicula, nombre, genero, estrellas) VALUES(NULL,'" + self.nombre + "','"+ self.genero +"','" + str(self.estrellas) + "');")


    @staticmethod
    def ListarPeliculas():
        cursorPeli = DB().run("Select * from Pelicula")
        Peli = Pelicula()
        listaPeliculas = []
        for item in cursorPeli:
            Peli.idPelicula = item["idPelicula"]
            Peli.nombre = item["nombre"]
            Peli.genero = item["genero"]
            Peli.estrellas = item["estrellas"]
            listaPeliculas.append(Peli)
        return listaPeliculas




