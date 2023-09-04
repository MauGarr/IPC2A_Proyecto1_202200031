from Listas.datos import Datos_List

class Senales:
    
    # nodoC indica Nodo Cabeza, esto para crear una lista dentro del objeto y asi tener
    # todos los datos separados por objeto, es decir, Cada senal tendra dentro de si su 
    # propia lista de datos.
    
    def __init__(self, nombre:str, tiempo:int, amplitud:int, nodoC, grupos) -> None:
        self.nombre:str = nombre
        self.t:int = tiempo
        self.a:int = amplitud
        self.nodoC:Datos_List = nodoC
        self.g = grupos