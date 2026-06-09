import calculos
import inputs
import output 

def correr_sprint2():
    """
    Funcion integradora: recolecta datos mediante inputs, llama a evaluar_sistema 
    en calculos y delega la impresion de resultados al modulo output.
    """
    print("\n" + "=" * 50)
    print("  INICIANDO DIAGNÓSTICO DE SERVIDORES  ")
    print("=" * 50)

    # 1. Recolección de datos usando módulo inputs
    nombre_sv = inputs.pedir_nombre_servidor()
    cpu = inputs.pedir_porcentaje_hardware("CPU")
    ram = inputs.pedir_porcentaje_hardware("RAM")
    disco_libre = inputs.pedir_porcentaje_hardware("Espacio Libre en Disco")
    so = inputs.pedir_sistema_operativo()
    firewall = inputs.pedir_estado_firewall()
    servicios_activos = inputs.pedir_cantidad_positiva("servicios activos")
    trafico_red = inputs.pedir_porcentaje_hardware("Tráfico de Red (MB/s)")

    # 2. Evaluación de las reglas mediante el módulo calculos
    alertas, recomendaciones = calculos.evaluar_sistema(
        cpu, ram, disco_libre, so, firewall, servicios_activos, trafico_red
    )

    # 3. Muestra resultados usando la funcion especializada de output.py
    output.mostrar_diagnostico(nombre_sv, alertas, recomendaciones)


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
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        correr_sprint2()
    elif opcion == "2":
        print("Saliendo del sistema...")
    else:
        print("Opción inválida.")