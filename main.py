from inputs import pedir_nombre_servidor, pedir_porcentaje_hardware, pedir_cantidad_positiva

from calculos import evaluar_sistema
from output import mostrar_diagnostico

def main():
    print("=== SISTEMA DE DIAGNOSTICO DE SERVIDORES Vol.2 ===")
    print("Por favor, ingrese los datos requeridos para la evaluacion.\n")

    nombre_sv = pedir_nombre_servidor()

    cpu = pedir_porcentaje_hardware("CPU")
    ram =pedir_porcentaje_hardware("RAM")
    disco_libre =pedir_porcentaje_hardware("Espacio libre en disco")

    servicios_activos = pedir_cantidad_positiva("servicios activos")
    trafico_red = pedir_cantidad_positiva("trafico de red(en Mbps)")

    so = "Linux"
    firewall = "Desactivado"

    print("\n[INFO] Procesando datos del servidor y evaluando reglas...")

    alertas, recomendaciones = evaluar_sistema(
        cpu, ram, disco_libre, so, firewall, servicios_activos, trafico_red
    )

    mostrar_diagnostico(nombre_sv, alertas, recomendaciones)

main()