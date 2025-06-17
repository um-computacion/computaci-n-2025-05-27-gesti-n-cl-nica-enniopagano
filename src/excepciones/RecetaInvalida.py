class RecetaInvalidaException(Exception):
    def __init__(self, mensaje='Esta receta no es válida'):
        super().__init__(mensaje)