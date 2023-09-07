from Constructor.senales import Senales

class NodoSenal:
    
    def __init__(self, senal:Senales) -> None:          # Se crea el nodo Senal, tiene como parametro el objeto de senal
                                                        # para guardarlo en la lista enlazada simple, se crea tambien un
        self.senal:Senales = senal                      # puntero que apunta al siguiente Nodo, al ser creado por primera
        self.siguiente:NodoSenal = None                 # vez se le asignara el siguiente como None 