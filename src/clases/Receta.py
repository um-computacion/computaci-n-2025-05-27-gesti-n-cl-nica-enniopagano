from typing import List
from datetime import datetime
from clases.Paciente import Paciente
from clases.Medico import Medico
from clases.Especialidad import Especialidad

class Receta:
    def __init__(self, paciente: Paciente, medico: Medico, medicamentos: List[str]):
        self.__paciente__ = paciente
        self.__medico__ = medico
        self.__medicamentos__ = medicamentos
        self.__fecha_hora__ = datetime.now()

    def __str__(self):
        return 'Paciente: {} - Medico: {} - Medicamentos: {} - Fecha/Hora: {}'.format(self.__paciente__.__nombre__, self.__medico__.__nombre__, ', '.join(self.__medicamentos__), self.__fecha_hora__.strftime('%d-%m-%Y %H:%M'))
    
    def __repr__(self):
        return self.__str__()

