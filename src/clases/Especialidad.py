from typing import List

class Especialidad:
    def __init__(self, tipo:str, dias:List[str]):
        self.__tipo__ = tipo
        self.__dias__ = dias

    def obtener_especialidad(self) -> str:
        return self.__tipo__
    
    def verificar_dia(self, dia:str) -> bool:
        return dia.lower() in self.__dias__
    
    def __str__(self):
        return '{} (Dias: {})'.format(self.__tipo__, ', '.join(self.__dias__))



Cardiologia = Especialidad('Cardiologia', ['lunes', 'miercoles', 'viernes'])
Pediatria = Especialidad('Pediatria', ['jueves'])
# print(Cardiologia)