from clases.Clinica import Clinica
from clases.Paciente import Paciente
from clases.Medico import Medico
from clases.Especialidad import Especialidad
from clases.Turno import Turno
from clases.Receta import Receta
from clases.HistoriaClinica import HistoriaClinica
from excepciones.MedicoNoDisponible import MedicoNoDisponibleException
from excepciones.PacienteNoEncontrado import PacienteNoEncontradoException
from excepciones.RecetaInvalida import RecetaInvalidaException
from excepciones.TurnoOcupado import TurnoOcupadoException
from datetime import datetime


clinica = Clinica()

def agregar_paciente():
    nombre = input('Ingrese el nombre del paciente: ')
    dni = input('Ingrese el dni del paciente: ')
    nacimiento = input('Ingrese la fecha de nacimiento del paciente: ')
    paciente = Paciente(nombre,dni,nacimiento)
    clinica.agregar_paciente(paciente)
    print('Paciente agregado exitosamente')
    print(paciente)

def agregar_medico():
    nombre = input('Ingrese el nombre del medico: ')
    matricula = input('Ingrese la matricula del medico: ')
    medico = Medico(nombre,matricula)
    clinica.agregar_medico(medico)
    print('Medico agregado exitosamente')
    print(medico)

def agendar_turno():
    dni = input('Ingrese dni del paciente: ')
    matricula = input('Ingrese la matricula del medico: ')
    especialidad = input('Ingrese la especialidad del medico: ')
    fecha = input('Ingrese la fecha y hora (dd-mm-yyyy hh:mm) : ')
    fecha_object = datetime.strptime(fecha, '%d-%m-%Y %H:%M')
    clinica.agendar_turno(dni,matricula,especialidad,fecha_object)
    turno = clinica.obtener_turnos()[-1]

    print('Turno agendado exitosamente')    
    print(turno)

def agregar_especialidad():
    nombre = input('Ingrese el nombre de la especialidad: ')
    matricula = input('Ingrese la matricula del medico: ')
    medico = clinica.obtener_medico_por_matricula(matricula)
    eleccion = True
    dias = []
    while eleccion:
        dia = input('Ingrese el dia para esa especialidad, para terminar su eleccion ingrese 0: ')
        if dia =='0':
            eleccion=False
        dias.append(dia)

    especialidad = Especialidad(nombre,dias)
    medico.agregar_especialidad(especialidad)
    print('Especialidad agregada exitosamente')

def emitir_receta():
    dni = input('Ingrese el DNI del paciente: ')
    matricula = input('Ingrese la matricula del medico: ')
    eleccion = True
    medicamentos = []
    while eleccion:
        med = input('Ingrese los medicamentos para esta receta (un medicamento a la vez), para terminar su eleccion ingrese 0: ')
        if med =='0':
            eleccion=False
        medicamentos.append(med)
    clinica.emitir_receta(dni,matricula,medicamentos)
    print('Receta emitida exitosamente')

def ver_historia_clinica():
    dni = input('ingrese dni del paciente: ')
    print(clinica.obtener_historia_clinica(dni))

def ver_turnos():
    turnos = clinica.obtener_turnos()
    print('--TURNOS--')
    for i, t in enumerate(turnos):
        print(f'{i+1}- {t}')

def ver_pacientes():
    pacientes = clinica.obtener_pacientes()
    print('--PACIENTES--')
    for i, paciente in enumerate(pacientes):
        print(f'{i+1}- {paciente}')

def ver_medicos():
    medicos = clinica.obtener_medicos()
    print('--MEDICOS--')
    for i, m in enumerate(medicos):
        print(f'{i+1}- {m}')

if __name__ == '__main__':
    eligiendo = True
    print('''
    --- Menú Clínica ---
    1) Agregar paciente\n
    2) Agregar médico\n
    3) Agendar turno\n
    4) Agregar especialidad\n
    5) Emitir receta\n
    6) Ver historia clínica\n
    7) Ver todos los turnos\n
    8) Ver todos los pacientes\n
    9) Ver todos los médicos\n
    0) Salir\n
    ''')
    while eligiendo:
        menu = int(input('Elija una opcion: '))
        if menu == 0:
            eligiendo = False
        elif menu == 1:
            agregar_paciente()
        elif menu == 2:
            agregar_medico()
        elif menu == 3:
            try:
                agendar_turno()
            except MedicoNoDisponibleException:
                print('El médico no está disponible')
            except PacienteNoEncontradoException:
                print('El paciente con ese dni no fue encontrado')
        elif menu == 4:
            try:
                agregar_especialidad()
            except MedicoNoDisponibleException:
                print('No hay medico con esa matricula en el sistema')
        elif menu == 5:
            try:
                emitir_receta()
            except PacienteNoEncontradoException:
                print('El paciente con ese dni no fue encontrado')
            except MedicoNoDisponibleException:
                print('No hay medico con esa matricula en el sistema')
        elif menu == 6:
            try:
                ver_historia_clinica()
            except PacienteNoEncontradoException:
                print('Paciente no encontrado')
        elif menu == 7:
            ver_turnos()
        elif menu == 8:
            ver_pacientes()
        elif menu == 9:
            ver_medicos()
        else:
            print("Opción inválida")