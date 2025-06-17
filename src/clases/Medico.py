from clases.Especialidad import Especialidad
from typing import List, Optional

class Medico:
    def __init__(self, nombre:str, matricula:str):
        self.__nombre__ = nombre
        self.__matricula__ = matricula
        self.__especialidades__: List[Especialidad] = []
    
    def agregar_especialidad(self, especialidad: Especialidad) -> None:
        self.__especialidades__.append(especialidad)

    def obtener_matricula(self) -> str:
        return self.__matricula__
    
    def obtener_especialidad_para_dia(self, dia: str) -> Optional[str]:
        for especialidad in self.__especialidades__:
            if dia.lower() in especialidad.__dias__:
                return especialidad.__tipo__
        return None
    
    def __str__(self):
        return 'Medico: {} - Matricula: {} - Especialidades: {}'.format(self.__nombre__, self.__matricula__, ', '.join([especialidad.obtener_especialidad() for especialidad in self.__especialidades__ ]))
    
