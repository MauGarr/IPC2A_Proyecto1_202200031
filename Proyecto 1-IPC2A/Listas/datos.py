from Estructuras_Listas.nodoDatos import Nodo_Datos
from Constructor.dato import DatoSenal
from Constructor.respuestas import Respuesta

class Datos_List:

    def __init__(self) -> None:
        self.cabeza: Nodo_Datos = None

    def add_Dato_List(self, dato: DatoSenal) -> None:

        nuevo_Dato: Nodo_Datos = Nodo_Datos(dato)

        if self.cabeza is None:
            self.cabeza = nuevo_Dato
        else:
            actual: Nodo_Datos = self.cabeza

            while actual.siguiente is not None:
                actual = actual.siguiente

            actual.siguiente = nuevo_Dato

    def listar_Datos(self) -> None:

        actual: Nodo_Datos = self.cabeza

        while actual is not None:
            dato: DatoSenal = actual.dato
            print(f"\ttiempo:{dato.t} amplitud:{dato.a} valor:{dato.v}")
            actual = actual.siguiente

    def datos_Binarios(self) -> None:

        actual: Nodo_Datos = self.cabeza

        while actual is not None:
            dato: DatoSenal = actual.dato

            if dato.v != 0:
                dato.v = 1

            actual = actual.siguiente

    def grupo_Cabeza(self):

        actual: Nodo_Datos = self.cabeza
        t_grupo = actual.dato.t
        lista_Datos = Datos_List()
        size = 0

        while actual:

            if actual.dato.t == t_grupo:
                dato_Senal = DatoSenal(t_grupo, actual.dato.a, actual.dato.v)
                lista_Datos.add_Dato_List(dato_Senal)
                self.eliminar_Datos(t_grupo, actual.dato.a)
                actual = self.cabeza
                size += 1

            else:
                actual = actual.siguiente

        return lista_Datos, size

    def eliminar_Datos(self, tiempo, amplitud) -> None:

        actual: Nodo_Datos = self.cabeza
        anterior: Nodo_Datos = None
        encontrado = False

        while actual and not encontrado:

            if actual.dato.t == tiempo and actual.dato.a == amplitud:
                encontrado = True

            else:
                anterior = actual
                actual = actual.siguiente

        if actual is None:
            print("No existe un nodo que contenga los datos que se han especificado.")
            return

        if anterior is None:
            self.cabeza = actual.siguiente
        else: 
            anterior.siguiente = actual.siguiente

    def buscar_Dato(self, amplitud_Dato_Grupo, valor, posicion_t, posicion_a):

        actual: Nodo_Datos = self.cabeza
        resultado = Respuesta(0, 0, False, False, 0)

        while actual:

            if actual.dato.t == posicion_t and actual.dato.a == posicion_a:
                break

            actual = actual.siguiente

        while actual:
            dato: DatoSenal = actual.dato

            if dato.a == posicion_a:

                if dato.v != 0 and valor != 0:

                    if amplitud_Dato_Grupo == dato.a:

                        resultado.t = dato.t + 1
                        resultado.a = 1
                        existe = self.existe(resultado.t, resultado.a)

                        if existe is False:

                            if actual.siguiente is not None:
                                resultado.t = actual.siguiente.dato.t
                                resultado.a = actual.siguiente.dato.a

                            else:
                                resultado.a = 0

                        resultado.e = True
                        resultado.f = True
                        resultado.v = dato.v
                        resultado.d = dato
                        resultado.j_T = dato.t # Añade el valor de T para completar la operación de agregado!!!
                        self.eliminar_Datos(dato.t, dato.a)
                        return resultado

                    else:
                        resultado.t = dato.t
                        resultado.a = dato.a + 1
                        existe = self.existe(resultado.t, resultado.a)

                        if existe is False:

                            if actual.siguiente is not None:
                                resultado.t = actual.siguiente.dato.t
                                resultado.a = actual.siguiente.dato.a

                            else:
                                resultado.t = 0
                                resultado.a = 0

                        resultado.e = True
                        resultado.f = False
                        resultado.v = dato.v
                        resultado.d = dato
                        self.eliminar_Datos(dato.t, dato.a)
                        return resultado

                elif dato.v == 0 and valor == 0:

                    if amplitud_Dato_Grupo == dato.a:
                        resultado.t = dato.t + 1
                        resultado.a = 1
                        existe = self.existe(resultado.t, resultado.a)

                        if existe is False:

                            if actual.siguiente is not None:
                                resultado.t = actual.siguiente.dato.t
                                resultado.a = actual.siguiente.dato.a

                            else:
                                resultado.a = 0

                        resultado.e = True
                        resultado.f = True
                        resultado.v = 0
                        resultado.d = dato
                        resultado.j_T = dato.t
                        self.eliminar_Datos(dato.t, dato.a)
                        return resultado
                    
                    else:
                        resultado.t = dato.t
                        resultado.a = dato.a + 1
                        existe = self.existe(resultado.t, resultado.a)

                        if existe is False:

                            if actual.siguiente is not None:
                                resultado.t = actual.siguiente.dato.t
                                resultado.a = actual.siguiente.dato.a

                            else:
                                resultado.t = 0
                                resultado.a = 0

                        resultado.e = True
                        resultado.f = False
                        resultado.v = dato.v
                        resultado.d = dato
                        self.eliminar_Datos(dato.t, dato.a)
                        return resultado

                else:

                    while actual:

                        if actual.siguiente is not None:
                            dato_siguiente = actual.siguiente.dato

                            if dato_siguiente.a == 1:
                                resultado.t = dato_siguiente.t
                                resultado.a = dato_siguiente.a
                                resultado.e = False
                                resultado.f = False
                                resultado.v = 0
                                resultado.d = None
                                return resultado

                        else:
                            break

                        actual = actual.siguiente

                    resultado.t = 0
                    resultado.a = 0
                    resultado.e = False
                    resultado.f = False
                    resultado.v = 0
                    resultado.d = None
                    return resultado

        resultado.t = 0
        resultado.a = 0
        resultado.e = True
        resultado.f = False
        resultado.v = 0
        resultado.d = None
        return resultado

    def modificar_Dato(self, tiempo, amplitud, valor):

        actual = self.cabeza

        while actual:

            if actual.dato.t == tiempo and actual.dato.a == amplitud:
                actual.dato.v = valor

                return False

            actual = actual.siguiente

        return True

    def existe(self, tiempo, amplitud):

        actual = self.cabeza

        while actual:

            if actual.dato.t == tiempo and actual.dato.a == amplitud:
                return True

            actual = actual.siguiente
        return False

    def instertar_Posicion(self, dato:DatoSenal, tiempo_destino, amplitud_destino):
        nuevo_Dato: Nodo_Datos = Nodo_Datos(dato)

        if self.cabeza is None:
            self.cabeza = nuevo_Dato
            return

        # Caso especial: si la posición de destino es antes de la cabeza
        if tiempo_destino < self.cabeza.dato.t or (
                tiempo_destino == self.cabeza.dato.t and amplitud_destino < self.cabeza.dato.a):
            nuevo_Dato.siguiente = self.cabeza
            self.cabeza = nuevo_Dato
            return

        actual: Nodo_Datos = self.cabeza
        anterior: Nodo_Datos = None

        while actual:
            if actual.dato.t > tiempo_destino or (actual.dato.t == tiempo_destino and actual.dato.a > amplitud_destino):
                break
            anterior = actual
            actual = actual.siguiente

        if anterior:
            nuevo_Dato.siguiente = actual
            anterior.siguiente = nuevo_Dato
        else:
            nuevo_Dato.siguiente = self.cabeza
            self.cabeza = nuevo_Dato

    def ordenar_lista(self):
        if self.cabeza is None:
            return

        cambio = True
        while cambio:
            cambio = False
            actual = self.cabeza
            while actual.siguiente is not None:
                if actual.dato.t > actual.siguiente.dato.t or (
                        actual.dato.t == actual.siguiente.dato.t and actual.dato.a > actual.siguiente.dato.a):
                    actual.dato, actual.siguiente.dato = actual.siguiente.dato, actual.dato
                    cambio = True
                actual = actual.siguiente