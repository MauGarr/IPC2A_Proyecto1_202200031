from Listas.senales import SenalesList
from Estructuras_Listas.nodoSenales import NodoSenal
import copy
import os

#MENÚ PRINCIPAL
def main():  

    listaSenales: SenalesList = SenalesList()  # Instancia de la lista enlazada
    listaBinaria: SenalesList = SenalesList()  # Instancia de la lista enlazada
    listaAgrupados: SenalesList = SenalesList()

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

                if listaSenales is None:
                    listaSenales = SenalesList()

                listaSenales.cargarXML()  # Se lee el archivo y se agregan nodos a la lista

            elif opcion == 2:

                """
                Se generan la lista de datos en binario
                Se agrupan los datos
                """
                if listaBinaria is None and listaAgrupados is None:
                    listaBinaria = SenalesList()
                    listaAgrupados = SenalesList()

                nodo_Cabeza:NodoSenal = copy.deepcopy(listaSenales.cabeza) #Uso de copy para hacer una copia del objeto y
                nodo_Copia:NodoSenal = copy.deepcopy(listaSenales.cabeza) #asi generar una instancia diferente para cada caso

                listaBinaria.convertir_Binario(nodo_Cabeza)
                listaAgrupados.agrupar_Senales(nodo_Copia)

            elif opcion == 3:
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
                listaAgrupados.generar_Grafica()

            elif opcion == 6:

                listaSenales = None
                listaAgrupados = None
                listaBinaria = None
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

                print("\¡Verifica tu respuesta! La respuesta debe ser un número dentro del rango del 1 al 7.\n")

        print()
        input("Presione ENTER para continuar...")
        os.system('cls')

main()