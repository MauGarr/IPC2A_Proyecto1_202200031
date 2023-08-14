
print("-------------------------------------------------------")
print("                Proyecto 1 - IPC2 A    ")
print("-------------------------------------------------------")
print("Menú Principal: ")

menuprincipal = int(input("\n 1. Cargar archivo \n 2. Procesar archivo \n 3. Escribir archivo salida \n 4. Mostrar datos del estudiante \n 5. Generar gráfica \n 6. Inicializar sistema \n 7. Salida \n Ingrese una opción: "))

while menuprincipal !=7: 

    if menuprincipal == 1:
        print("\nCargue el archivo")

    elif menuprincipal == 2:
        print("\nProcesando archivo")

    elif menuprincipal == 3:
        print("\nArchivo salida")

    elif menuprincipal == 4:
        print("\nDatos del estudiante")

    elif menuprincipal == 5:
        print("\nGenerando gráfica")

    elif menuprincipal == 6:
        print("\nInicializando el sistema")

    else:   
        print("\n¡Por favor dígita una opción correcta!")

    menuprincipal = int(input("\n 1. Cargar archivo \n 2. Procesar archivo \n 3. Escribir archivo salida \n 4. Mostrar datos del estudiante \n 5. Generar gráfica \n 6. Inicializar sistema \n 7. Salida \n Ingrese una opción: "))
    print("Has salido del sistema")