from db import DB

class Sala(object):
    idSala = None
    id_cine = None

    def Dar_de_Alta_Sala(self):
        DB.run("Insert into Sala(idSala,Cine_idCine) Values (" + str(self.idSala) + ", " + str(self.nombre) + ")")