from pelicula import Pelicula
from cine import Cine
from sala import Sala
from horario import Horario
from butaca import Butaca

P = Pelicula()
P.idPelicula = 'NULL'
P.nombre = 'Avengers Infinity War'
P.genero = 'Accion'
P.estrellas = 5
P.Dar_de_Alta_Pelicula()

C = Cine()
C.idCine = 'NULL'
C.nombre = 'GetarCine Belgrano'
C.Dar_de_Alta_Cine()

S = Sala()
S.idSala = 'NULL'
S.Dar_de_Alta_Sala()

H = Horario()
H.idHorario = 'NULL'
H.fecha_hora = "Jueves 4 de Octubre 15:00"
H.Sala_idSala = 1
H.Pelicula_idPelicula = 1
H.Cine_idCine = 1
H.Dar_de_Alta_Horario()


H = Horario()
H.idHorario = 'NULL'
H.fecha_hora = "Miercoles 11 de Octubre 12:00"
H.Sala_idSala = 1
H.Pelicula_idPelicula = 1
H.Cine_idCine = 1
H.Dar_de_Alta_Horario()


H = Horario()
H.idHorario = 'NULL'
H.fecha_hora = "Martes 10 de Octubre 20:00"
H.Sala_idSala = 1
H.Pelicula_idPelicula = 1
H.Cine_idCine = 1
H.Dar_de_Alta_Horario()


C = Cine()
C.idCine = 'NULL'
C.nombre = 'GetarCine Moreno'
C.Dar_de_Alta_Cine()

S = Sala()
S.idSala = 'NULL'
S.Dar_de_Alta_Sala()

H = Horario()
H.idHorario = 'NULL'
H.fecha_hora = "Viernes 5 de Octubre 18:00"
H.Sala_idSala = 2
H.Pelicula_idPelicula = 1
H.Cine_idCine = 2
H.Dar_de_Alta_Horario()

B = Butaca()
B.idButaca = 'NULL'
B.id_sala = 1
B.precio_butaca = 150
B.Dar_de_Alta_Butaca()

B = Butaca()
B.idButaca = 'NULL'
B.id_sala = 1
B.precio_butaca = 150
B.Dar_de_Alta_Butaca()

B = Butaca()
B.idButaca = 'NULL'
B.id_sala = 1
B.precio_butaca = 150
B.Dar_de_Alta_Butaca()

B = Butaca()
B.idButaca = 'NULL'
B.id_sala = 2
B.precio_butaca = 150
B.Dar_de_Alta_Butaca()

B = Butaca()
B.idButaca = 'NULL'
B.id_sala = 2
B.precio_butaca = 150
B.Dar_de_Alta_Butaca()

B = Butaca()
B.idButaca = 'NULL'
B.id_sala = 2
B.precio_butaca = 150
B.Dar_de_Alta_Butaca()

P = Pelicula()
P.idPelicula = 'NULL'
P.nombre = 'Invictus'
P.genero = 'Drama'
P.estrellas = 5
P.Dar_de_Alta_Pelicula()

P = Pelicula()
P.idPelicula = 'NULL'
P.nombre = 'Viernes 13'
P.genero = 'Terror'
P.estrellas = 4
P.Dar_de_Alta_Pelicula()

P = Pelicula()
P.idPelicula = 'NULL'
P.nombre = 'Coco'
P.genero = 'Animada'
P.estrellas = 3
P.Dar_de_Alta_Pelicula()

"""
    C = Cine.InfoCine()
    lista_horarios = Cine.GetHorariosCine()
"""
"""
@app.route('/cines',methods = ['GET'])
def Cines():
    nombrePeli = request.args.get('nombrePeli')
    P = Pelicula.InfoPeli(nombrePeli)
    lista_cines = Cine.ListarCines()
    return render_template('cines.html', lista_cines=lista_cines,P=P)
"""