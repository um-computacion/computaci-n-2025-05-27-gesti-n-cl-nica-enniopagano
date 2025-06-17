class MedicoNoDisponibleException(Exception):
    def __init__(self, mensaje='Medico no está disponible'):
        super().__init__(mensaje)