from db import DB


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


