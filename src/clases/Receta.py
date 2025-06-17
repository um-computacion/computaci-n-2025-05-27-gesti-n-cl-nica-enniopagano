from typing import List
from datetime import datetime
from Paciente import Paciente
from Medico import Medico
from Especialidad import Especialidad

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

Pedro = Paciente('Pedro Neto', '45966431', '1900-01-01')
Cardiologia = Especialidad('Cardiologia', ['lunes', 'miercoles', 'viernes'])
Miguel = Medico('Miguel Ortiz', '45678', [Cardiologia])
Receta1 = Receta(Pedro, Miguel, ['Clona', 'Fentanilo'])
# print(Receta1)