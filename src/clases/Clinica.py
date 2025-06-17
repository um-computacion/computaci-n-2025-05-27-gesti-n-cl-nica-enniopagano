from clases.Paciente import Paciente
from clases.Medico import Medico
from clases.Turno import Turno
from clases.HistoriaClinica import HistoriaClinica
from clases.Receta import Receta
from typing import Dict, List
from datetime import datetime
from excepciones.MedicoNoDisponible import MedicoNoDisponibleException
from excepciones.PacienteNoEncontrado import PacienteNoEncontradoException
from excepciones.RecetaInvalida import RecetaInvalidaException
from excepciones.TurnoOcupado import TurnoOcupadoException



class Clinica:
    def __init__(self):
        self.__pacientes__: Dict[str, Paciente] = {}
        self.__medicos__: Dict[str, Medico] = {}
        self.__turnos__: List[Turno] = []
        self.__historias_clinicas__: Dict[str, HistoriaClinica] = {}

    def agregar_paciente(self, paciente: Paciente):
        dni = paciente.obtener_dni()
        if dni in self.__pacientes__:
            raise ValueError(f'El paciente con el DNI: {dni} ya está registrado')
        
        self.__pacientes__[dni] = paciente
        self.__historias_clinicas__[dni] = HistoriaClinica(paciente)

    def agregar_medico(self, medico: Medico):
        matricula = medico.obtener_matricula()
        if matricula in self.__medicos__:
            raise ValueError(f'El medico con la matricula: {matricula} ya está registrado')
        
        self.__medicos__[matricula] = medico

    def obtener_pacientes(self) -> List[Paciente]:
        return self.__pacientes__
    
    def obtener_medicos(self) -> List[Medico]:
        return self.__medicos__
    
    def obtener_medico_por_matricula(self, matricula: str) -> Medico:
        self.validar_existencia_medico(matricula)
        return self.__medicos__[matricula]
    
    def agendar_turno(self, dni: str, matricula: str, especialidad: str, fecha_hora: datetime):
        paciente = self.__pacientes__[dni]
        medico = self.__medicos__[matricula]
        dia_semana = self.obtener_dia_semana_en_espanol(fecha_hora)
        
        self.validar_especialidad_en_dia(medico, especialidad, dia_semana)
        self.validar_turno_no_duplicado(matricula, fecha_hora)
        
        nuevo_turno = Turno(paciente, medico, fecha_hora, especialidad)

        self.__turnos__.append(nuevo_turno)
        self.__historias_clinicas__[dni].agregar_turno(nuevo_turno)

    def obtener_turnos(self) -> List[Turno]:
        return self.__turnos__
    
    def emitir_receta(self, dni: str, matricula: str, medicamentos: List[str]):
        self.validar_existencia_paciente(dni)
        self.validar_existencia_medico(matricula)
        
        if not medicamentos:
            raise RecetaInvalidaException("La receta debe contener al menos un medicamento")
        
        paciente = self.__pacientes__[dni]
        medico = self.__medicos__[matricula]
        
        nueva_receta = Receta(paciente, medicamentos, medico)
        
        self.__historias_clinicas__[dni].agregar_receta(nueva_receta)

    def obtener_historia_clinica(self, dni: str) -> HistoriaClinica:
        return self.__historias_clinicas__[dni]
    
    def validar_existencia_paciente(self, dni: str):
        if dni not in self.__pacientes__:
            raise PacienteNoEncontradoException(f'Paciente con el DNI: {dni} no está registrado')
        
    def validar_existencia_medico(self, matricula: str):
        if matricula not in self.__medicos__:
            raise MedicoNoDisponibleException(f'Medico con la matricula: {matricula} no está registrado')
        
    def validar_turno_no_duplicado(self, matricula: str, fecha_hora: datetime):
        for turno in self.__turnos__:
            medico_matricula = turno.obtener_medico().obtener_matricula()
            fecha_turno = turno.obtener_fecha_hora()
            nombre_medico = turno.__medico__.__nombre__
            if medico_matricula == matricula and fecha_turno == fecha_hora:
                raise TurnoOcupadoException(f"El médico {nombre_medico} ya tiene un turno para el {fecha_hora.strftime('%d-%m-%Y %H:%M')}")
        
    def obtener_dia_semana_en_espanol(self, fecha_hora: datetime) -> str:
        dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
        return dias[fecha_hora.weekday()]
    
    def validar_especialidad_en_dia(self, medico: Medico, especialidad_solicitada: str, dia_semana: str):
        especialidad_disponible = str((medico.obtener_especialidad_para_dia(dia_semana)))
        if especialidad_disponible.lower() != especialidad_solicitada.lower():
            raise MedicoNoDisponibleException(f'El medico no atiende {especialidad_solicitada} los dias {dia_semana}')