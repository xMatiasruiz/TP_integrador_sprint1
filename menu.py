import calculos
import inputs
import output 
import funciones_de_validacion
from archivos import  crear_archivo_si_no_existe, registrar_diagnostico, ver_diagnosticos_realizados, buscar_diagnostico, modificar_diagnosticos, eliminar_diagnostico,cargar_diagnosticos,guardar_diagnosticos, ejecutar_diagnostico, mostrar_configuracion_actual



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
    base_datos = cargar_diagnosticos()
    bandera = True
    while bandera:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Cargar configuracion")
        print("2. Mostrar Configuracion")
        print("3. Modificar una Configuracion")
        print("4. Ejecutar Configuracion")
        print("5. Eliminar una Configuracion")
        print("6. Buscar Servidor")
        print("7. Guardar Configuracion")
        print("8. Salir")
        print("-" * 30)

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            base_datos = registrar_diagnostico(base_datos)
            print("Configuracion cargada.")
        elif opcion == "2":
            mostrar_configuracion_actual(base_datos)
        elif opcion == "3":
            base_datos = modificar_diagnosticos(base_datos)
        elif opcion == "4":
            base_datos = ejecutar_diagnostico(base_datos)
        elif opcion == "5":
            eliminar_diagnostico()
        elif opcion == "6":
            buscar_diagnostico()
        elif opcion == "7":
            guardar_diagnosticos(base_datos)
            print("Configuracion guardada!!")
        elif opcion == "8":
            print("Gracias por usar el programa. Hasta luego!")
            bandera = False
        else:
            print("Opcion invalida. Por favor, seleccione una opcion valida.")
    ##registrar registrar_diagnostico(), buscar_diagnostico(),base_datos = cargar_diagnosticos()