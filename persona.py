from db import DB

class Persona(object):
    dni = None
    nombre = None
    apellido = None


    def Dar_de_Alta_Persona(self):
        DB.run("Insert into Cliente(dni,nombre,apellido) VALUES("'NULL'", '" + self.nombre + "', '" + self.apellido + "');")

    @staticmethod
    def ObtenerDatosPersona(nombrePersona,apellidoPersona):
        cursorPersona = DB.run("Select * from Cliente where nombre = "+nombrePersona+" and apellido = "+apellidoPersona+";")
        P = Persona()
        for item in cursorPersona:
            P.dni = item['dni']
            P.nombre = item['nombre']
            P.apellido = item['apellido']
        return P