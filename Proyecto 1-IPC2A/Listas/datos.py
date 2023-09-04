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

        while actual is not None:

            if actual.dato.t == t_grupo:
                dato_Senal = DatoSenal(t_grupo, actual.dato.a, actual.dato.v)
                lista_Datos.add_Dato_List(dato_Senal)
                self.eliminar_Datos(t_grupo, actual.dato.a)
                actual = self.cabeza
                size += 1

            else:
                break

        return lista_Datos, size

    def eliminar_Datos(self, tiempo, amplitud) -> None:

        if self.cabeza.dato.t == tiempo and self.cabeza.dato.a == amplitud:
            self.cabeza = self.cabeza.siguiente
            return

        actual = self.cabeza
        anterior = None

        while actual:

            if actual.dato.t == tiempo and actual.dato.a == amplitud:
                break

            anterior = actual
            actual = actual.siguiente

        if actual is None:
            print("No se encontró un nodo con los datos especificados.")
            return

            # Actualizar los punteros para eliminar el nodo en medio
        anterior.siguiente = actual.siguiente

    def buscar_Dato(self, amplitud_Dato_Grupo, valor, posicion_t, posicion_a):

        actual: Nodo_Datos = self.cabeza
        resultado = Respuesta(0, 0, False, False, 0)

        while actual:

            if actual.dato.t == posicion_t and actual.dato.a == posicion_a:
                break

            actual = actual.siguiente

        while actual is not None:
            dato: DatoSenal = actual.dato

            if dato.a == posicion_a:

                if dato.v != 0 and valor != 0:

                    if amplitud_Dato_Grupo == dato.a:
                        resultado.t = dato.t + 1
                        resultado.a = 1
                        resultado.e = True
                        resultado.f = True
                        resultado.v = dato.v
                        self.eliminar_Datos(dato.t, dato.a)
                        return resultado
                    else:
                        resultado.t = dato.t
                        resultado.a = dato.a + 1
                        resultado.e = True
                        resultado.f = False
                        resultado.v = dato.v
                        self.eliminar_Datos(dato.t, dato.a)
                        return resultado

                elif dato.v == 0 and valor == 0:

                    if amplitud_Dato_Grupo == dato.a:
                        resultado.t = dato.t + 1
                        resultado.a = 1
                        resultado.e = True
                        resultado.f = True
                        resultado.v = 0
                        self.eliminar_Datos(dato.t, dato.a)
                        return resultado
                    else:
                        resultado.t = dato.t
                        resultado.a = dato.a + 1
                        resultado.e = True
                        resultado.f = False
                        resultado.v = dato.v
                        self.eliminar_Datos(dato.t, dato.a)
                        return resultado

                else:

                    resultado.t = dato.t + 1
                    resultado.a = 1
                    resultado.e = False
                    resultado.f = False
                    resultado.v = 0
                    return resultado

            actual = actual.siguiente

        resultado.t = 0
        resultado.a = 0
        resultado.e = True
        resultado.f = False
        resultado.v = 0
        return resultado