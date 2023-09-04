from Constructor.senales import Senales

class NodoSenal:
    
    # Se crea el nodo Senal, tiene como parametro el objeto de senal
    # para guardarlo en la lista enlazada simple, se crea tambien un
    # puntero que apunta al siguiente Nodo, al ser creado por primera
    # vez se le asignara el siguiente como None 
    
    def __init__(self, senal:Senales) -> None:
        
        self.senal:Senales = senal
        self.siguiente:NodoSenal = None