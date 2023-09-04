from Constructor.dato import DatoSenal

class Nodo_Datos:
    
    def __init__(self, dato:DatoSenal) -> None:
        self.dato = dato
        self.siguiente:Nodo_Datos = None