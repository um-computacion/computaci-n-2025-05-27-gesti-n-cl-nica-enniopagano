class Paciente:
    def __init__(self, nombre:str, dni:str, fecha_nacimiento:str):
        self.__nombre__ = nombre
        self.__dni__ = dni
        self.__fecha_nacimiento__ = fecha_nacimiento

    def obtener_dni(self) -> str:
        return self.__dni__

    def __str__(self) -> str:
        return 'Paciente: {} - DNI: {} - Fecha de nacimiento: {}'.format(self.__nombre__, self.__dni__, self.__fecha_nacimiento__)

