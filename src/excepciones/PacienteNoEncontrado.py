class PacienteNoEncontradoException(Exception):
    def __init__(self, mensaje='Paciente no encontrado en el sistema'):
        super().__init__(mensaje)