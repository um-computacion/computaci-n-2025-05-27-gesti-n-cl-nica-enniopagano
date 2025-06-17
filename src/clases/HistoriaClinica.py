from clases.Paciente import Paciente
from clases.Turno import Turno
from clases.Receta import Receta
from typing import List
from clases.Medico import Medico
from clases.Especialidad import Especialidad

class HistoriaClinica:
    def __init__(self, paciente: Paciente):
        self.__paciente__ = paciente
        self.__turnos__: List[Turno] = []
        self.__recetas__: List[Receta] = []


    def agregar_turno(self, turno: Turno):
        self.__turnos__.append(turno)

    def agregar_receta(self, receta: Receta):
        self.__recetas__.append(receta)
    
    def obtener_turnos(self) -> List[Turno]:
        return self.__turnos__

    def obtener_recetas(self) -> List[Receta]:
        return self.__recetas__

    def __str__(self) -> str:
        turnos_str = '\n'.join('--- Médico: {}, Fecha: {}, Especialidad: {}'.format(turno.__medico__.__nombre__, turno.__fecha_hora__, turno.__especialidad__)
            for turno in self.__turnos__)  if self.__turnos__ else '  (No hay turnos registrados)'
       

        recetas_str = '\n'.join('--- Médico: {}, Medicamentos: {}'.format(receta.__medico__.__nombre__, receta.__medicamentos__) 
            for receta in self.__recetas__) if self.__recetas__ else '  (No hay recetas registradas)'

        return (
            f'{self.__paciente__}\n'
            f'Turnos:\n{turnos_str}\n'
            f'Recetas:\n{recetas_str}'
        )

