class Persona(object):
    id = None
    nombre = None

    def __init__(self,id,nombre):
        self.id = id
        self.nombre = nombre
        self.lista_mascotas_persona = []