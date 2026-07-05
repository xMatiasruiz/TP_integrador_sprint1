import calculos
import inputs
import output 
import funciones_de_validacion
from archivos import  crear_archivo_si_no_existe, registrar_diagnostico, ver_diagnosticos_realizados, buscar_diagnostico, modificar_diagnosticos, eliminar_diagnostico
def mostrar_menu():
    """
    Controla el flujo del menú principal del sistema.
    """
    print("=" * 50)
    print("            MENÚ DE MONITOREO - UTN FRA           ")
    print("=" * 50)
    print("1. Ejecutar Diagnóstico de Servidor")
    print("2. Salir")
    print("-" * 50)
    
    opcion = input("Seleccione una opción (1 para iniciar / 2 para salir): ")

    while not funciones_de_validacion.validadcion_de_incio_de_diagnostico(opcion):
        opcion = input("Opción inválida. Seleccione una opción válida (1/2): ")

    if opcion == '1':
        menu_de_archivos()
    else:
        print("Gracias por usar el programa, vuelva pronto!")
    
def menu_de_archivos():
    
    """
    Despliega el menu principal del sistema de gestion de alumnos.

    Esta funcion inicializa el entorno de archivos, mantiene el bucle de ejecucion
    del programa y gestiona la navegacion entre las distintas funcionalidades
    del sistema
    
    Returns:
        None: Esta funcion no retorna valores, su proposito es la interaccion directa.
    """
    crear_archivo_si_no_existe()
    bandera = True
    while bandera:
        print("\n--- MENU PRINCIPAL ---")
        print("1. iniciar un diagnostico")
        print("2. ver diagnosticos")
        print("3. Buscar un diagnostico")
        print("4. modificar un diagnostico")
        print("5. Eliminar un diagnostico")
        print("6. Salir")
        print("-" * 30)

        opcion = input("Seleccione una opccion: ")

        if opcion == "1":
            registrar_diagnostico()
        elif opcion == "2":
            ver_diagnosticos_realizados()
        elif opcion == "3":
            buscar_diagnostico()
        elif opcion == "4":
            modificar_diagnosticos()
        elif opcion == "5":
            eliminar_diagnostico()
        elif opcion == "6":
            print("Gracias por usar el programa. Hasta luego!")
            bandera = False
        else:
            print("Opcion invalida. Por favor, seleccione una opcion valida.")
