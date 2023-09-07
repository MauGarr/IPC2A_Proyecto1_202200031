from Listas.senales import SenalesList
from Estructuras_Listas.nodoSenales import NodoSenal
import os

#MENÚ PRINCIPAL
def main():  

    listaSenales: SenalesList = SenalesList()  
    listaBinaria: SenalesList = SenalesList()              #--------> Instancia de lista enlazada
    listaAgrupados: SenalesList = SenalesList()
    lista = SenalesList()

    print("-"*60)
    print("                    Proyecto 1 - IPC2 A                       ")
    print("-"*60)

    opcion: int = 0

    while opcion != 7:

        try:
            opcion = int(input("# - - - - - - - - - - MENU PRINCIPAL - - - - - - - - - - #\n"
                               "1. Cargar archivo\n"
                               "2. Procesar archivo\n"
                               "3. Escribir archivo de salida\n"
                               "4. Mostrar datos del Estudiante\n"
                               "5. Generar Gráfica\n"
                               "6. Inicializar Sistema\n"
                               "7. Salir\n"
                               "Ingresa una opción: "))
            print()

            if opcion == 1:

                path_XML: str = input("\nIngresa la ruta donde se encuentra el archivo (.xml)\n"
                                      "Ruta: ")
                # Se realiza la lectura del archivo y se incorporan nodos en la lista
                listaSenales.cargarXML(path_XML) # Esta lista representa graficamente los datos originales
                lista.cargarXML(path_XML) # Los grupos se crean a partir de esta lista

                if lista.cabeza is not None:
                    print("-" *30)
                    print("¡Archivo cargado exitosamente!")
                    print("-" *30)

            elif opcion == 2:

                # La lista de datos se genera en formato binario, y luego se procede a agrupar los datos
                
                nodo_Cabeza: NodoSenal = lista.cabeza

                if lista.cabeza is None:
                    print("Para utilizar esta función, primero debes cargar un archivo (.xml) o procesarlo.")
                
                else:
                    listaBinaria.convertir_Binario()
                    listaAgrupados.agrupar_Senales(nodo_Cabeza)
                print("")

            elif opcion == 3:

                if listaAgrupados.cabeza is None:
                    print("Para utilizar esta función, primero debes cargar un archivo (.xml) o procesarlo.")

                else:
                    listaAgrupados.archivo_Salida()

            elif opcion == 4:
                print("-" * 57)
                print("Datos del Estudiante:")
                print("Edison Mauricio García Rodríguez\n"
                      "202200031\n"
                      "Introducción a la Programación y Computación 2 Sección A\n"
                      "Ingeniería en Ciencias y Sistemas\n"
                      "4to. Semestre")
                print("-" * 57)

            elif opcion == 5:

                if listaAgrupados.cabeza is None:
                    print("-" * 85)
                    print(" ¡Para utilizar esta función, primero debes cargar un archivo (.xml) o procesarlo! ")
                    print("-" * 85)
                    
                else:

                    respuesta = int(input("----- Genera una gráfica -----\n"
                                          "1. Matriz Regular\n"
                                          "2. Matriz Reducida\n"
                                          "Ingresa una opción: "))
                    if respuesta == 1:
                        listaSenales.generarGraficaOriginal()

                    elif respuesta == 2:
                        listaAgrupados.generar_Grafica()

                    else:
                        print("¡Verifica tu respuesta! La respuesta debe ser un número dentro del rango de 1 a 2.")

            elif opcion == 6:

                listaSenales = SenalesList()
                listaAgrupados = SenalesList()
                listaBinaria = SenalesList()
                lista = SenalesList()
                print("-" * 45)
                print("¡Se ha inicializado el sistema correctamente!")
                print("-" * 45)

            elif opcion == 7:
                print("-" * 30)
                print(" ¡Finalizando el programa...!")
                print("-" * 30)

            else:
                print("\n¡Opción Inválida!. Ingresa una opción correcta\n")

        except ValueError:

                print("\n¡Verifica tu respuesta! La respuesta debe ser un número dentro del rango del 1 al 7.\n")

        print()
        input("Presione ENTER para continuar...")
        os.system('cls')

main()