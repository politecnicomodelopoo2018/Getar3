from cine import Cine
from pelicula import Pelicula

ci = Cine()

p = Pelicula()
p.idPelicula = 'NULL'
p.nombrePelicula = 'Avengers'
p.genero = 'Accion'
p.estrellas = 5



ci.Agregar_pelicula(p)

p1 = Pelicula()
p1.idPelicula = 'NULL'
p1.nombrePelicula = 'Proyecto X'
p1.genero = 'Comedia'
p1.estrellas = 4



ci.Agregar_pelicula(p1)

p2 = Pelicula()
p2.idPelicula = 'NULL'
p2.nombrePelicula = 'Daredevil'
p2.genero = 'Accion'
p2.estrellas = 1



ci.Agregar_pelicula(p2)

p3 = Pelicula()
p3.idPelicula = 'NULL'
p3.nombrePelicula = 'Invictus'
p3.genero = 'drama'
p3.estrellas = 4



ci.Agregar_pelicula(p3)

for item in ci.lista_peliculas:
    print(item.nombrePelicula)
    print("")