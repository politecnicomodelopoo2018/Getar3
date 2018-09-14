from cine import Cine
from pelicula import Pelicula
"""
ci = Cine()

p = Pelicula()
p.idPelicula = 'NULL'
p.nombrePelicula = 'Avengers'
p.genero = 'Accion'
p.estrellas = 5
p.Dar_de_Alta_Pelicula()


p1 = Pelicula()
p1.idPelicula = 'NULL'
p1.nombrePelicula = 'Proyecto X'
p1.genero = 'Comedia'
p1.estrellas = 4
p1.Dar_de_Alta_Pelicula()


p2 = Pelicula()
p2.idPelicula = 'NULL'
p2.nombrePelicula = 'Daredevil'
p2.genero = 'Accion'
p2.estrellas = 1
p2.Dar_de_Alta_Pelicula()

p3 = Pelicula()
p3.idPelicula = 'NULL'
p3.nombrePelicula = 'Invictus'
p3.genero = 'drama'
p3.estrellas = 4
p3.Dar_de_Alta_Pelicula()
"""

Pelicula.getPeli(2)

"""
@staticmethod
def getPeli(idPelicula):
    cursorPeli = DB().run("Select * from Pelicula where idPelicula = " + str(idPelicula) + ";")
    lista = cursorPeli.fetchall()
    Peli= Pelicula()
    Peli.idPelicula = lista[0]["idPelicula"]
    Peli.nombre = lista[0]["nombre"]
    Peli.genero = lista[0]["genero"]
    Peli.estrellas = lista[0]["estrellas"]
    return Peli
"""