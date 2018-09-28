from pelicula import Pelicula
from cine import Cine

p = Pelicula()
p.nombre= 'Avengers'
p.genero = 'Accion'
p.estrellas = 5
p.Dar_de_Alta_Pelicula()


p = Pelicula()
p.nombre = 'Proyecto X'
p.genero = 'Comedia'
p.estrellas = 4
p.Dar_de_Alta_Pelicula()


p = Pelicula()
p.nombre = 'Daredevil'
p.genero = 'Accion'
p.estrellas = 1
p.Dar_de_Alta_Pelicula()

p = Pelicula()
p.nombre = 'Invictus'
p.genero = 'drama'
p.estrellas = 4
p.Dar_de_Alta_Pelicula()



C = Cine()
C.nombre = 'GetarCine Belgrano'
C.Dar_de_Alta_Cine()

C = Cine()
C.nombre = 'GetarCine Moreno'
C.Dar_de_Alta_Cine()

C = Cine()
C.nombre = 'GetarCine Salta'
C.Dar_de_Alta_Cine()

C = Cine()
C.nombre = 'GetarCine Cordoba'
C.Dar_de_Alta_Cine()