from db import DB

class Persona(object):
    dni = None
    nombre = None
    apellido = None


    def Dar_de_Alta_Persona(self):
        cur = DB.run("Insert into Cliente(dni,nombre,apellido) VALUES("'NULL'", '" + self.nombre + "', '" + self.apellido + "');")
        self.dni = cur.lastrowid

    @staticmethod
    def ObtenerDatosPersona(dni):
        cursorPersona = DB.run("Select * from Cliente where dni = " + str(dni)+";")
        dict = cursorPersona.fetchone()
        P = Persona()
        P.dni = dict['dni']
        P.nombre = dict['nombre']
        P.apellido = dict['apellido']
        return P