
def menu():

    print("-------------------------------------------------------")
    print("                Proyecto 1 - IPC2 A    ")
    print("-------------------------------------------------------")

#Menú
    while True:

        print("\nMenú Principal:")
        print("1. Cargar Archivo Inicial")
        print("2. Procesar Archivo")
        print("3. Escribir Archivo Salida")
        print("4. Mostrar Datos del EStudiante")
        print("5. Generar Gráfica")
        print("6. Inicializar Sistema")
        print("7. Salir")
        opcion = input("Inrese una opción: ")

        if opcion == '1':
            """archivo_inventario = input("Ingrese el nombre del archivo (.inv): ")
            inventario.cargar_inventario_inicial(archivo_inventario)"""
            print("\n-------------------------------")
            print("Cargando datos del archivo...")
            print("-------------------------------")

        elif opcion == '2':
            """archivo_movimientos = input("Ingrese el nombre del archivo (.mov): ")
            inventario.cargar_instrucciones_movimientos(archivo_movimientos)"""
            print("\n----------------------------------")
            print("Procesando datos del archivo...")
            print("----------------------------------")
            
        elif opcion == '3':
            """archivo_informe = input("Ingrese el nombre del archivo de informe (.txt): ")
            inventario.crear_informe_inventario(archivo_informe)"""
            print("\n----------------------------------------")
            print("Datos cargados exitosamente...")
            print("----------------------------------------")

        elif opcion == '4':
            """archivo_informe = input("Ingrese el nombre del archivo de informe (.txt): ")
            inventario.crear_informe_inventario(archivo_informe)"""
            print("\n------------------------------------------------------------")
            print("Datos del Estudiante: ")
            print("Edison Mauricio García Rodríguez")
            print("202200031")
            print("Introducción a la Programación y Computación 2 sección 'A' ")
            print("Ingeniería en Ciencias y Sistemas")
            print("4to. Semestre")
            print("------------------------------------------------------------")

        elif opcion == '5':
            """archivo_informe = input("Ingrese el nombre del archivo de informe (.txt): ")
            inventario.crear_informe_inventario(archivo_informe)"""
            print("\n----------------------------------------")
            print("Generando gráfica...")
            print("----------------------------------------")

        elif opcion == '6':
            """archivo_informe = input("Ingrese el nombre del archivo de informe (.txt): ")
            inventario.crear_informe_inventario(archivo_informe)"""
            print("\n----------------------------------------")
            print("Inicializando el sistema...")
            print("----------------------------------------")
            

        elif opcion == '7':
            print("------------------------")
            print("Saliendo del programa...")
            print("------------------------")
            break

        else:
            print("\nOpción Inválida. Por favor, ingresar una opción válida.")

if __name__ == "__main__":
    menu()