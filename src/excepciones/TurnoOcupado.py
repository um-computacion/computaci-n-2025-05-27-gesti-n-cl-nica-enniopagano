class TurnoOcupadoException(Exception):
    def __init__(self, mensaje='Este turno ya está ocupado'):
        super().__init__(mensaje)