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
        listaPeliculas = []
        for item in cursorPeli:
            Peli = Pelicula()
            Peli.idPelicula = item["idPelicula"]
            Peli.nombre = item["nombre"]
            Peli.genero = item["genero"]
            Peli.estrellas = item["estrellas"]
            listaPeliculas.append(Peli)
        return listaPeliculas

    @staticmethod
    def InfoPeli(nombrePeli):
        cursorInfoPeli = DB.run("Select * from Pelicula where nombre = ('"+nombrePeli+"');")
        P = Pelicula()
        for item in cursorInfoPeli:
            P.idPelicula = item["idPelicula"]
            P.nombre = item["nombre"]
            P.genero = item["genero"]
            P.estrellas = item["estrellas"]
        return P