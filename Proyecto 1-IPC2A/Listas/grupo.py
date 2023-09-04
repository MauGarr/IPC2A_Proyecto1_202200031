from Listas.datos import Datos_List
from Estructuras_Listas.nodoDatos import Nodo_Datos
from Estructuras_Listas.nodoGrupo import Nodo_Grupos
from Constructor.grupo import Grupo
from Constructor.dato import DatoSenal
from Constructor.respuestas import Respuesta
import copy


class Grupo_List:

    def __init__(self) -> None:
        self.cabeza: Nodo_Grupos = None

    def add_Grupo_List(self, grupo: Grupo) -> None:

        nuevo_Dato: Nodo_Grupos = Nodo_Grupos(grupo)  # Se crea un nodo, este no esta acoplado a la lista aun

        if self.cabeza is None:  # Si la lista no tiene ningun nodo, se asigna este como primero
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

        while actual is not None:  # Recorre los grupos

            if lista_Datos.cabeza:

                actual_D: Nodo_Datos = actual.dato.d.cabeza  # Nodo Cabeza de los datos
                copia_Lista: Nodo_Datos = copy.deepcopy(actual.dato.d.cabeza)
                copia_Lista_Total = copy.deepcopy(lista_Datos)
                posicion_a = lista_Datos.cabeza.dato.a
                posicion_t = lista_Datos.cabeza.dato.t

                while actual_D:  # Recorre la lista de datos contenida en los grupos

                    dato: DatoSenal = actual_D.dato
                    a = actual.dato.size
                    v = dato.v
                    resultados = lista_Datos.buscar_Dato(a, v, posicion_t, posicion_a)
                    posicion_t = resultados.t
                    posicion_a = resultados.a
                    encontrado = resultados.e
                    final = resultados.f
                    valor = resultados.v
                    actual_D.dato.v += valor

                    if final is True:

                        copia_Lista = copy.deepcopy(actual.dato.d.cabeza)
                        copia_Lista_Total = copy.deepcopy(lista_Datos)
                        actual.dato.t += f",{posicion_t-1}"

                    if encontrado is False:

                        actual.dato.d.cabeza = copy.deepcopy(copia_Lista)
                        lista_Datos = copy.deepcopy(copia_Lista_Total)
                        actual_D = actual.dato.d.cabeza

                    else:

                        actual_D = actual_D.siguiente

                        if lista_Datos.cabeza is not None and actual_D is None:
                            actual_D = actual.dato.d.cabeza

                        elif posicion_t == 0 and posicion_a == 0:
                            break

                if lista_Datos:

                    lista_Nueva_Datos, size = lista_Datos.grupo_Cabeza()
                    no_G = actual.dato.noG+1
                    tiempo = f"{lista_Nueva_Datos.cabeza.dato.t}"
                    grupo_Nuevo:Grupo = Grupo(no_G, tiempo, lista_Nueva_Datos, size)
                    self.add_Grupo_List(grupo_Nuevo)

                else:
                    break

                actual = actual.siguiente

            else:
                break