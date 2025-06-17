import unittest
from datetime import datetime
from src.clases.Clinica import Clinica
from src.clases.Paciente import Paciente
from src.clases.Medico import Medico
from src.clases.Especialidad import Especialidad
from src.excepciones.PacienteNoEncontrado import PacienteNoEncontradoException
from src.excepciones.MedicoNoDisponible import MedicoNoDisponibleException
from src.excepciones.TurnoOcupado import TurnoOcupadoException
from src.excepciones.RecetaInvalida import RecetaInvalidaException

class TestCLI(unittest.TestCase):
    def setUp(self):
        self.clinica = Clinica()
        self.paciente = Paciente("Lionel Messi", "12345678", "24-06-1987")
        self.medico = Medico("Dr. Maradona", "MED100")
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)

    def test_agregar_paciente_y_medico(self):
        self.assertIn("12345678", self.clinica._Clinica__pacientes__)
        self.assertIn("MED100", self.clinica._Clinica__medicos__)


    def test_registro_paciente_duplicado(self):
        with self.assertRaises(ValueError):
            self.clinica.agregar_paciente(self.paciente)

    def test_registro_medico_duplicado(self):
        with self.assertRaises(ValueError):
            self.clinica.agregar_medico(self.medico)


    def test_agregar_paciente_con_datos_invalidos(self):
        with self.assertRaises(ValueError):
            self.clinica.agregar_paciente(Paciente("", "", ""))


    def test_agregar_especialidad_a_medico(self):
        esp = Especialidad("Cardiología", ["Lunes", "Miércoles"])
        self.medico.agregar_especialidad(esp)
        self.assertEqual(len(self.medico.obtener_especialidades()), 1)

    def test_especialidad_duplicada(self):
        esp = Especialidad("Pediatría", ["Lunes"])
        self.medico.agregar_especialidad(esp)
        with self.assertRaises(ValueError):
            self.medico.agregar_especialidad(esp)

    def test_dias_invalidos_en_especialidad(self):
        with self.assertRaises(ValueError):
            Especialidad("Pediatria", ["Spiderman"])

    def test_agregar_especialidad_a_medico_inexistente(self):
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.obtener_medico_por_matricula("NOEXISTE")

    # 📅 Turnos
    def test_agendar_turno_exitoso(self):
        esp = Especialidad("Dermatología", ["Lunes"])
        self.medico.agregar_especialidad(esp)
        fecha = datetime.strptime("17-06-2025 10:00", "%d-%m-%Y %H:%M")  # martes
        with self.assertRaises(MedicoNoDisponibleException):  # el día no coincide
            self.clinica.agendar_turno("12345678", "MED100", "Dermatología", fecha)

    def test_turno_duplicado(self):
        esp = Especialidad("Cardiología", ["Lunes"])
        self.medico.agregar_especialidad(esp)
        fecha = datetime.strptime("16-06-2025 10:00", "%d-%m-%Y %H:%M")  # lunes
        self.clinica.agendar_turno("12345678", "MED100", "Cardiología", fecha)
        with self.assertRaises(TurnoOcupadoException):
            self.clinica.agendar_turno("12345678", "MED100", "Cardiología", fecha)

    def test_turno_con_paciente_inexistente(self):
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.agendar_turno("99999999", "MED100", "Cardiología", datetime.now())

    def test_turno_con_medico_inexistente(self):
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("12345678", "XXXX", "Cardiología", datetime.now())

    def test_turno_especialidad_invalida(self):
        fecha = datetime.strptime("17-06-2025 10:00", "%d-%m-%Y %H:%M")
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("12345678", "MED100", "Inexistente", fecha)

    # 💊 Recetas
    def test_emitir_receta_exitosa(self):
        self.clinica.emitir_receta("12345678", "MED100", ["Paracetamol"])
        historia = self.clinica.obtener_historia_clinica("12345678")
        self.assertEqual(len(historia.obtener_recetas()), 1)

    def test_emitir_receta_con_paciente_inexistente(self):
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.emitir_receta("99999999", "MED100", ["Ibuprofeno"])

    def test_emitir_receta_con_medico_inexistente(self):
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.emitir_receta("12345678", "XXXX", ["Ibuprofeno"])

    def test_emitir_receta_sin_medicamentos(self):
        with self.assertRaises(RecetaInvalidaException):
            self.clinica.emitir_receta("12345678", "MED100", [])

    # 📘 Historia Clínica
    def test_historia_clinica_turno_y_receta(self):
        esp = Especialidad("Clínica", ["Lunes"])
        self.medico.agregar_especialidad(esp)
        fecha = datetime.strptime("16-06-2025 10:00", "%d-%m-%Y %H:%M")
        self.clinica.agendar_turno("12345678", "MED100", "Clínica", fecha)
        self.clinica.emitir_receta("12345678", "MED100", ["Aspirina"])
        historia = self.clinica.obtener_historia_clinica("12345678")
        self.assertEqual(len(historia.obtener_turnos()), 1)
        self.assertEqual(len(historia.obtener_recetas()), 1)

if __name__ == '__main__':
    unittest.main()
