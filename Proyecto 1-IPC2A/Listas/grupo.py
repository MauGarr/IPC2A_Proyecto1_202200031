from Listas.datos import Datos_List
from Estructuras_Listas.nodoDatos import Nodo_Datos
from Estructuras_Listas.nodoGrupo import Nodo_Grupos
from Constructor.grupo import Grupo
from Constructor.dato import DatoSenal
from Constructor.respuestas import Respuesta

class Grupo_List:

    def __init__(self) -> None:
        self.cabeza: Nodo_Grupos = None

    def add_Grupo_List(self, grupo: Grupo) -> None:

        nuevo_Dato: Nodo_Grupos = Nodo_Grupos(grupo)  # Existe un nodo recién creado que aún no ha sido enlazado a la lista

        if self.cabeza is None:  # Si la lista está vacía, este se considera como el primer nodo.
            self.cabeza = nuevo_Dato

        else:
            actual: Nodo_Grupos = self.cabeza  # Se hace una copia de la lista de nodos por cualquier error

            # El while sirve para recorrer la lista de nodos hasta llegar al ultimo
            # nodo que apunte hacia un null, ahi haremos la insercion del nuevo nodo
            while actual.siguiente is not None:
                actual = actual.siguiente
            # El actual.siguiente apunta hacia null
            # por lo que se le asigna el nodo nuevo_Dato
            actual.siguiente = nuevo_Dato

    def listar_Grupo(self) -> None:

        actual: Nodo_Grupos = self.cabeza  # Se asigna al actual el nodo cabeza para recorrer la lista
        lista_Datos: Datos_List = Datos_List()

        while actual is not None:
            grupo: Grupo = actual.dato  # Se recupera el objeto senal contenida en el nodo
            print(f"\n\tg={grupo.noG} t = {grupo.t} size: {grupo.size}\n")
            lista_Datos = grupo.d
            lista_Datos.listar_Datos()
            print()

            actual = actual.siguiente

    def modificar_Grup(self, lista_Datos: Datos_List):

        actual: Nodo_Grupos = self.cabeza

        while actual:  # Recorre los grupos

            if lista_Datos.cabeza is not None:
                copia_Lista_Datos = Datos_List()
                actual_D: Nodo_Datos = actual.dato.d.cabeza  # Nodo Cabeza de los datos
                posicion_a = lista_Datos.cabeza.dato.a
                posicion_t = lista_Datos.cabeza.dato.t

                while actual_D:  # Recorre la lista de datos contenida en los grupos

                    dato: DatoSenal = actual_D.dato
                    a = actual.dato.size
                    v = dato.v
                    lista_Datos.ordenar_lista()
                    resultados = lista_Datos.buscar_Dato(a, v, posicion_t, posicion_a)
                    copia_Nodo = resultados.d

                    if copia_Nodo:
                        copia_Lista_Datos.add_Dato_List(copia_Nodo)
                        del copia_Nodo

                    posicion_t = resultados.t
                    posicion_a = resultados.a

                    encontrado = resultados.e
                    final = resultados.f
                    valor = resultados.v
                    actual_D.dato.v += valor

                    if final is True:
                        copia_Lista_Datos.cabeza = None
                        actual.dato.t += f",{resultados.j_T}"

                    if encontrado is False:
                        actual_D = actual.dato.d.cabeza
                        actual_Lista_Datos:Nodo_Datos = copia_Lista_Datos.cabeza

                        while actual_Lista_Datos:

                            dato_Recuperado = actual_Lista_Datos.dato
                            actual_D.dato.v -= actual_Lista_Datos.dato.v
                            lista_Datos.instertar_Posicion(dato_Recuperado,dato_Recuperado.t,dato_Recuperado.a)
                            actual_Lista_Datos = actual_Lista_Datos.siguiente
                            actual_D = actual_D.siguiente

                        copia_Lista_Datos.cabeza = None
                        actual_D = actual.dato.d.cabeza

                    else:
                        actual_D = actual_D.siguiente

                        if lista_Datos.cabeza is not None and actual_D is None:
                            actual_D = actual.dato.d.cabeza

                        elif posicion_t == 0 and posicion_a == 0:
                            break

                if lista_Datos.cabeza is None:
                    break

                else:
                    lista_Nueva_Datos, size = lista_Datos.grupo_Cabeza()
                    no_G = actual.dato.noG + 1
                    tiempo = f"{lista_Nueva_Datos.cabeza.dato.t}"
                    grupo_Nuevo: Grupo = Grupo(no_G, tiempo, lista_Nueva_Datos, size)
                    self.add_Grupo_List(grupo_Nuevo)

                actual = actual.siguiente

            else:
                break

    def loop(self):

        actual = self.cabeza

        while actual:
            yield actual.dato
            actual = actual.siguiente

    def __iter__(self):
        return iter(self.loop())