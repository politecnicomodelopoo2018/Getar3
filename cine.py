from db import DB
from horario import Horario

class Cine(object):
    idCine = None
    nombre = None

    def Dar_de_Alta_Cine(self):
        DB.run("Insert into Cine(idCine, nombre) VALUES(NULL,'" + self.nombre + "');")

    @staticmethod
    def ListarCines():
        cursorCine = DB().run("Select * from Cine")
        listaCines = []
        for item in cursorCine:
            Ci = Cine()
            Ci.idCine = item["idCine"]
            Ci.nombre = item["nombre"]
            listaCines.append(Ci)
        return listaCines

    @staticmethod
    def InfoCine(nombreCine):
        cursorInfoCine = DB.run("Select * from Cine where nombre = '" + nombreCine + "';")
        C = Cine()
        for item in cursorInfoCine:
            C.idCine = item["idCine"]
            C.nombre = item["nombre"]
        return C

    @staticmethod
    def GetHorariosCine(idCine):
        cursorHorariosCine = DB.run("Select * from Horarios join Cine on Horarios.Cine_idCine = Cine.idCine where Cine.nombre = '"+ nombreCine +"';")
        listaHorarios = []
        for item in cursorHorariosCine:
            H = Horario()
            H.idHorario = item['idHorarios']
            H.fecha_hora = item['fecha_hora']
            H.Sala_idSala = item['Sala_idSala']
            H.Pelicula_idPelicula = item['Pelicula_idPelicula']
            H.Cine_idCine = item['Cine_idCine']
            listaHorarios.append(H)
        return listaHorarios

