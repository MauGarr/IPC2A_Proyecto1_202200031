from Constructor.grupo import Grupo

class Nodo_Grupos:

    def __init__(self, dato:Grupo) -> None:
        self.dato: Grupo = dato
        self.siguiente = None