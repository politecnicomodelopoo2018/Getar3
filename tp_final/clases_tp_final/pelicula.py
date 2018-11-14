from tp_final.clases_tp_final.db import DB

class Pelicula(object):
    idPelicula = None
    nombre = None
    genero = None
    estrellas = None

    def Dar_de_Alta_Pelicula(self):
        DB.run("Insert into Pelicula(idPelicula, nombre, genero, estrellas) VALUES(NULL,'" + self.nombre + "','"+ self.genero +"','" + str(self.estrellas) + "');")

    @staticmethod
    def Dar_de_Baja_Pelicula(idPelicula):
        DB.run("Delete from Pelicula where idPelicula = ("+ str(idPelicula) +");")

    @staticmethod
    def Modificar_Pelicula(idPelicula,nombre,genero,estrellas):
        DB.run("UPDATE Pelicula SET nombre = '%s', genero = '%s', estrellas = '%i' WHERE idPelicula = %i;" % (
        nombre, genero, estrellas, idPelicula))

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
    def InfoPeli(idPeli):
        cursorInfoPeli = DB.run("Select * from Pelicula where idPelicula = ("+str(idPeli)+");")
        P = Pelicula()
        dict = cursorInfoPeli.fetchone()
        P.idPelicula = dict["idPelicula"]
        P.nombre = dict["nombre"]
        P.genero = dict["genero"]
        P.estrellas = dict["estrellas"]
        return P