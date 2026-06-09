import calculos
import inputs

def correr_sprint2():
    """
    Funcion integradora: recolecta datos mediante inputs, llama a evaluar_sistema 
    en calculos y muestra los resultados formateados en pantalla.
    """
    print("\n" + "=" * 50)
    print("  INICIANDO DIAGNÓSTICO DE SERVIDORES  ")
    print("=" * 50)

    # 1. Recolección de datos usando tu módulo inputs
    nombre_sv = inputs.pedir_nombre_servidor()
    cpu = inputs.pedir_porcentaje_hardware("CPU")
    ram = inputs.pedir_porcentaje_hardware("RAM")
    disco_libre = inputs.pedir_porcentaje_hardware("Espacio Libre en Disco")
    so = inputs.pedir_sistema_operativo()
    firewall = inputs.pedir_estado_firewall()
    servicios_activos = inputs.pedir_cantidad_positiva("servicios activos")
    trafico_red = inputs.pedir_porcentaje_hardware("Tráfico de Red (MB/s)")

    print("\n" + "-" * 50)
    print(f"Procesando diagnóstico para el servidor: {nombre_sv}")
    print("-" * 50)

    # 2. Evaluación de las reglas mediante el módulo calculos
    alertas, recomendaciones = calculos.evaluar_sistema(
        cpu, ram, disco_libre, so, firewall, servicios_activos, trafico_red
    )

    # 3. Mostrar resultados en pantalla recorriendo las listas con len()
    print("\n⚠️  ALERTAS DETECTADAS:")
    hubo_alertas = False
    
    for i in range(len(alertas)):
        if alertas[i] != "":
            print(f"- {alertas[i]}")
            print(f"  💡 Recomendación: {recomendaciones[i]}")
            hubo_alertas = True

    if not hubo_alertas:
        print("✅ El servidor se encuentra en un estado estable y seguro. No se detectaron anomalías.")

    print("\n" + "=" * 50)


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