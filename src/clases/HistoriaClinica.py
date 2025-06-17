from Paciente import Paciente
from Turno import Turno
from Receta import Receta
from typing import List

from Medico import Medico
from Especialidad import Especialidad

class HistoriaClinica:
    def __init__(self, paciente: Paciente, turnos: List[Turno], recetas: List[Receta]):
        self.__paciente__ = paciente
        self.__turnos__ = turnos
        self.__recetas__ = recetas


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

Pedro = Paciente('Pedro Neto', '45966431', '1900-01-01')
Cardiologia = Especialidad('Cardiologia', ['lunes', 'miercoles', 'viernes'])
Miguel = Medico('Miguel Ortiz', '45678', [Cardiologia])
Receta1 = Receta(Pedro, Miguel, ['Clona', 'Fentanilo'])
Receta2 = Receta(Pedro, Miguel, ['Morfina', 'Pasto'])
Turno1 = Turno(Pedro, Miguel, '2025-06-25 13:30', 'Cardiologia')
Turno2 = Turno(Pedro, Miguel, '2025-08-25 13:30', 'Cardiologia')
HistoriaClinica1 = HistoriaClinica(Pedro, [Turno1, Turno2], [Receta1, Receta2])
# print(HistoriaClinica.obtener_recetas(HistoriaClinica1))
print(HistoriaClinica1)
# print([Turno1, Turno2])
# turnos = HistoriaClinica1.__turnos__
# print(dir(turnos[0]))
# print(dir(HistoriaClinica1))
# print(HistoriaClinica1.__turnos__[0].__medico__.__nombre__)
