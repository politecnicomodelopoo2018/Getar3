from sala import Sala
from horario import Horario

a = Horario.GetSala_En_Horario('Martes 10 de Octubre 20:00')
b = a.idSala
lista = Sala.Listar_Butacas(a.idSala)
