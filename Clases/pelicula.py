from Clases.db import DB

class Pelicula(object):
    idPelicula = None
    nombrePelicula = None
    genero = None
    estrellas = None

    def Dar_de_Alta_Pelicula(self):
        DB.run("Insert into Pelicula(idPelicula, nombre, genero, estrellas) VALUES(" + str(self.idPelicula) + ", '" + self.nombrePelicula + "','"+ self.genero +"'," + str(self.estrellas) + ");")
