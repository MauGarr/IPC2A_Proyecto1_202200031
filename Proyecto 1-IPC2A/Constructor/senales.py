from Listas.datos import Datos_List

class Senales:
    
    def __init__(self, nombre:str, tiempo:int, amplitud:int, nodoC, grupos) -> None:                # nodoC indica Nodo Cabeza, esto para crear una lista dentro del objeto y asi tener
        self.nombre:str = nombre                                                                    # todos los datos separados por objeto, es decir, Cada senal tendra dentro de si su 
        self.t:int = tiempo                                                                         # propia lista de datos.
        self.a:int = amplitud
        self.nodoC:Datos_List = nodoC
        self.g = grupos