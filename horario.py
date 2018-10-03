from db import DB

class Horario(object):
    idHorario = None
    fecha_hora = None
    Sala_idSala = None
    Pelicula_idPelicula = None
    Cine_idCine = None

    def Dar_de_Alta_Horario(self):
        DB.run("Insert into Horarios(idHorarios,fecha_hora,Sala_idSala,Pelicula_idPelicula,Cine_idCine) VALUES(" + str(self.idHorario) + ",'"+ (self.fecha_hora) +"'," + str(self.Sala_idSala) + ","+ str(self.Pelicula_idPelicula) +", " + str(self.Cine_idCine) + ");")

