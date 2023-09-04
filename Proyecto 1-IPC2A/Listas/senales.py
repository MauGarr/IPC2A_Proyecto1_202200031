import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
from graphviz import Digraph

from Listas.grupo import Grupo_List
from Estructuras_Listas.nodoDatos import Nodo_Datos
from Estructuras_Listas.nodoSenales import NodoSenal
from Estructuras_Listas.nodoGrupo import Nodo_Grupos
from Listas.datos import Datos_List
from Constructor.senales import Senales
from Constructor.dato import DatoSenal
from Constructor.grupo import Grupo

class SenalesList:
    
    def __init__(self) -> None:
        self.cabeza:NodoSenal = None
    
    def cargarXML(self) -> None: #ESTA FUNCION EXTRAE LOS ARCHIVOS DEL XML Y LOS ALMACENA EN LA LISTA SIMPLE
        
        # Usa la ruta relativa si y solo si se encuentra el archivo XML dentro de la misma carpeta donde 
        # se encuentra el proyecto, de lo contrario usar la ruta completa
        # (ruta completa ej: C:\Users\user\Documentos\PythonProyect\SenalOfAudio\ArchivosXML\senales.xml)
        # (ruta relativa) ej: archivosXML\senales.xml
        
        path_XML:str = input("\nIngresa la ruta donde se encuentra el archivo (.xml)\n"
                             "Ruta: ")
        print()
        try:
            # Intentar parsear el XML desde el archivo
            tree = ET.parse(path_XML)
            root = tree.getroot()

            # Obtener los datos de la etiqueta 'senal'
            for senal in root.findall('senal'):
                
                nombre = senal.get('nombre') # Obtengo el nombre de la senal
                t = int(senal.get('t')) # Obtengo el tiempo de la senal
                A = int(senal.get('A')) # Obtengo la amplitud de la senal        
                lista_datos:Datos_List = Datos_List()
                # Obtener los datos de la etiqueta 'dato' dentro de 'senal'
                for dato in senal.findall('dato'):
                    
                    t_dato = int(dato.get('t')) # Obtengo el tiempo del dato
                    A_dato = int(dato.get('A')) # Obtengo la amplitud del dato
                    valor = int(dato.text)
                    dato_Nuevo:DatoSenal = DatoSenal(t_dato, A_dato, valor)
                    lista_datos.add_Dato_List(dato_Nuevo)

                senal_Agregada:Senales = Senales(nombre,t,A,lista_datos,None) # Se crea el objeto Senal
                self.add_Senal_List(senal_Agregada)
            print("-" *30)
            print("¡Archivo cargado exitosamente!")
            print("-" *30)

        except FileNotFoundError:
            print("Archivo no encontrado. Por favor, ingresa la ruta correcta.")
        except ET.ParseError:
            print("Error al analizar el archivo XML. Verifica que el formato sea correcto.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")

    def add_Senal_List(self, senal:Senales) -> None:
        
        nueva_Senal:NodoSenal = NodoSenal(senal) # Se crea un nodo, este no esta acoplado a la lista aun
        
        if self.cabeza is None: # Si la lista no tiene ningun nodo, se asigna este como primero
            self.cabeza = nueva_Senal
        
        else:
            actual: NodoSenal = self.cabeza # Se hace una copia de la lista de nodos por cualquier error
            
            # El while sirve para recorrer la lista de nodos hasta llegar al ultimo
            # nodo que apunte hacia un null, ahi haremos la insercion del nuevo nodo
            while actual.siguiente is not None: 
                
                actual = actual.siguiente
            # El actual.siguiente apunta hacia null
            # por lo que se le asigna el nodo nueva_senal
            actual.siguiente = nueva_Senal 

    # def listar_Senales(self) -> None:
    #
    #     actual:NodoSenal = self.cabeza # Se asigna al actual el nodo cabeza para recorrer la lista
    #     lista_Datos:Datos_List = Datos_List()
    #
    #     while actual is not None:
    #         senal:Senales = actual.senal # Se recupera el objeto senal contenida en el nodo
    #         print(f"\n{senal.nombre}\n")
    #         lista_Datos = senal.nodoC
    #         lista_Datos.listar_Datos()
    #         print()
    #
    #         actual = actual.siguiente

    def convertir_Binario(self, nodo_Cabeza:NodoSenal) -> None:

        actual:NodoSenal = nodo_Cabeza #Se obtiene el nodo inicial para recorrer la lista
        lista_datos_Binarios:Datos_List = Datos_List()
        print("\n Lista de Senales Binarias\n")

        while actual is not None:

            senal:Senales = actual.senal
            lista_datos_Binarios = senal.nodoC
            lista_datos_Binarios.datos_Binarios()
            actual = actual.siguiente

    def agrupar_Senales(self, nodo_Cabeza:NodoSenal) -> None:

        print("\n Lista de Senales Agrupadas\n")
        actual: NodoSenal = nodo_Cabeza  # Se obtiene el nodo inicial para recorrer la lista

        while actual is not None:

            senal: Senales = actual.senal
            nombre = senal.nombre
            amplitud = senal.a
            tiempo = senal.t

            # CREARME A MI LA PRIMERA LISTA DE GRUPOS, LA CUAL POSEE TODOS LOS DATOS DEL TIEMPO = 1
            lista_Datos: Datos_List = senal.nodoC
            lista, size = lista_Datos.grupo_Cabeza()
            grupo_Cabeza: Grupo = Grupo(1, "1", lista, size)
            lista_grupos:Grupo_List = Grupo_List()
            lista_grupos.add_Grupo_List(grupo_Cabeza)
            # ----------------------------------------------------------------------------
            lista_grupos.modificar_Grup(lista_Datos)

            senalNueva = Senales(nombre, tiempo, amplitud, None, lista_grupos)
            self.add_Senal_List(senalNueva)
            actual = actual.siguiente

    def lista_Senales_Grupos(self) -> None:

        actual: NodoSenal = self.cabeza  # Se asigna al actual el nodo cabeza para recorrer la lista

        while actual is not None:
            senal: Senales = actual.senal  # Se recupera el objeto senal contenida en el nodo
            print(f"\n Senal: {senal.nombre} A: {senal.a}\n")
            lista_Grupos:Grupo_List = senal.g
            lista_Grupos.listar_Grupo()

            print()

            actual = actual.siguiente

    def archivo_Salida(self) -> None:

        try:
            root = ET.Element("SenalesReducidas") # SE CREO LA ETIQUETA SENALES REDUCIDAS
            actual:NodoSenal = self.cabeza

            while actual:

                senal_Datos:Senales = actual.senal
                nombre = senal_Datos.nombre
                amplitud = senal_Datos.a

                #SE CREA LA ETIQUETA SENAL POR CADA SENAL QUE CONTENGA
                senal = ET.SubElement(root, "senal", nombre=f"{nombre}", A=f"{amplitud}")

                actual_g: Nodo_Grupos = actual.senal.g.cabeza

                while actual_g:

                    grupos: Grupo = actual_g.dato
                    no_Grupo = grupos.noG
                    tiempos = grupos.t

                    # SE CREA LA ETIQUETA GRUPO
                    new_Grup = ET.SubElement(senal, "grupo", g=f"{no_Grupo}")

                    # SE CREA LA ETIQUETA CON LOS TIEMPOS
                    etiqueta_Tiempo = ET.SubElement(new_Grup,  "tiempos")
                    etiqueta_Tiempo.text = str(tiempos)

                    # ETIQUETA <datosGrupo>
                    datosGrupo = ET.SubElement(new_Grup, "datosGrupo")
                    actual_datos: Nodo_Datos = actual_g.dato.d.cabeza

                    while actual_datos:

                        dato = actual_datos.dato
                        a_dato = dato.a
                        v_dato = dato.v
                        new_dato = ET.SubElement(datosGrupo,"dato", A=f"{a_dato}")
                        new_dato.text = str(v_dato)

                        actual_datos = actual_datos.siguiente

                    actual_g = actual_g.siguiente

                actual = actual.siguiente

            xml_str = ET.tostring(root, encoding="utf-8")
            dom = minidom.parseString(xml_str)
            path = input("\nIngresa una ruta especifica para guardar el archivo (.xml): ")

            with open(f"{path}", "w") as archivo:
                archivo.write(dom.toprettyxml(indent="   "))
            print("\n")
            print("-" * 42)
            print("¡Se generó el archivo (.xml) exitosamente!")
            print("-" * 42)

        except Exception as e:
            print(f"Surgó un error al generar archivo XML\n{e}")

    def generar_Grafica(self):

        try:
            actual = self.cabeza
            print("-" * 40)
            print("¡Ingresa la senal que deseas graficar!")  
            print("\nSenales disponibles:")

            while actual:
                print(f"\t{actual.senal.nombre}")
                actual = actual.siguiente

            respuesta = input("Ingresa el nombre: ")

            actual = self.cabeza

            while actual:
                senal:Senales = actual.senal

                if senal.nombre == respuesta:

                    graph = Digraph(comment=f"Onda_Reducida_{senal.nombre}")
                    graph.node("C", f"{senal.nombre}\nReducida")
                    graph.node("A", f"A={senal.a}")
                    graph.edge('C', 'A') # PRIMEROS PUNTEROS
                    actual_g = actual.senal.g.cabeza # Se obtiene el nodo cabeza de la lista de grupos
                    nombre_Ant = ""

                    while actual_g:
                        grupo:Grupo = actual_g.dato
                        no_G = grupo.noG
                        tiempos_G = grupo.t
                        nombre_Nodo = f"grupo={no_G}"
                        label = f"{nombre_Nodo}\n(t = {tiempos_G})"
                        graph.node(nombre_Nodo, label)

                        if no_G == 1:
                            graph.edge('C', nombre_Nodo)
                            nombre_Ant = nombre_Nodo

                        else:

                            graph.edge(nombre_Ant, nombre_Nodo)
                            nombre_Ant = nombre_Nodo

                        actual_g = actual_g.siguiente

                    actual_g = actual.senal.g.cabeza
                    nombre_D_Ant = ""
                    amplitud = 1

                    while actual_g:

                        grupo: Grupo = actual_g.dato
                        no_G = grupo.noG
                        actual_d: Nodo_Datos = grupo.d.cabeza

                        while actual_d:
                            dato_C:DatoSenal = actual_d.dato

                            if dato_C.a == amplitud:
                                nombre_Nodo_Dato = f"F{no_G}C{amplitud}"
                                label = f"{dato_C.v}"
                                graph.node(nombre_Nodo_Dato, label)

                                if no_G == 1:
                                    graph.edge('C', nombre_Nodo_Dato)
                                    nombre_D_Ant = nombre_Nodo_Dato
                                    break

                                else:
                                    graph.edge(nombre_D_Ant, nombre_Nodo_Dato)
                                    nombre_D_Ant = nombre_Nodo_Dato
                                    break

                            else:
                                actual_d = actual_d.siguiente

                        actual_g = actual_g.siguiente

                        if actual_g is None:

                            if amplitud == grupo.size:
                                break

                            else:
                                actual_g = actual.senal.g.cabeza
                                amplitud += 1

                    graph.render(f"SenalReducida_{senal.nombre}", format="jpeg", cleanup=True)
                    print("-" * 50)
                    print("¡Se ha generado y guardado gráfica exitosamente!")
                    print("-" * 50)

                    break

                else:
                    actual = actual.siguiente

        except Exception as e:
            
            print(f"Error al generar o guardar la gráfica: {e}")