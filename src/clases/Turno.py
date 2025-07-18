from datetime import datetime
from clases.Medico import Medico
from clases.Paciente import Paciente
from clases.Especialidad import Especialidad

class Turno:
    def __init__(self, paciente: Paciente, medico: Medico, fecha_hora: datetime, especialidad: str):
        self.__paciente__ = paciente
        self.__medico__ = medico
        self.__fecha_hora__ = fecha_hora
        self.__especialidad__ = especialidad

    def obtener_medico(self) -> Medico:
        return self.__medico__
    
    def obtener_fecha_hora(self) -> datetime:
        return self.__fecha_hora__
    
    def __str__(self) -> str:
        return 'Paciente: {} - Medico: {} - Especialidad: {} - Fecha/Hora: {}'.format(self.__paciente__.__nombre__, self.__medico__.__nombre__, self.__especialidad__, self.__fecha_hora__)

    def __repr__(self):
        return self.__str__()

