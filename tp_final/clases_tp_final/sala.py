from tp_final.clases_tp_final.db import DB
from tp_final.clases_tp_final.butaca import Butaca

class Sala(object):
    idSala = None

    def Dar_de_Alta_Sala(self):
        DB.run("Insert into Sala(idSala) Values (" + str(self.idSala) + ")")

    @staticmethod
    def Listar_Butacas(idSala):
        cursorButaca = DB().run("Select * from Butaca where Butaca.Sala_idSala = " + str(idSala) + "")
        listaButacas = []
        for item in cursorButaca:
            B = Butaca()
            B.idButaca = item["idButaca"]
            B.id_sala = item["Sala_idSala"]
            B.precio_butaca = item["precio_butaca"]
            listaButacas.append(B)
        return listaButacas