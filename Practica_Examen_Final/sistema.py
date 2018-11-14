from Practica_Examen_Final.mascota import Mascota
from Practica_Examen_Final.persona import Persona

class Sistema(object):

    def __init__(self):
        lista_animales = []
        lista_personas = []

    def Eliminar_Mascota(self,idm):
        for item in self.lista_mascotas:
            if item.idm == idm:
                self.lista_mascotas.remove(item)

    def Agregar_Persona(self,id,nombre):
        P = Persona()
        P.id = id
        P.nombre = nombre
        self.lista_personas.append(P)

    def Modificar_Persona(self,id,nuevo_nombre):
        P = Persona
        if P.id == id:
            P.nombre = nuevo_nombre
        else:
            pass

    def Eliminar_Persona(self,id):
        for item in self.lista_personas:
            if item.id == id:
                self.lista_personas.remove(item)
                for item2 in item.lista_mascotas_persona:
                    self.Eliminar_Mascota(item2.idm)
            else:
                pass