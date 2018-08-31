from db import DB

class Cliente(object):
    dni = None
    nombre = None
    apellido = None

    def Dar_de_Alta_Cliente(self):
        DB.run("Insert into Cliente(dni,nombre,apellido) VALUES("'NULL'", '" + self.nombre + "', '" + self.apellido + "');")

