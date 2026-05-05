# ---- FUNCIONES ---- 

def analizar_seguridad(fire_estado):
    """
    Evalúa si el firewall está activo o no.
    Recibe: fire_estado (str)
    Devuelve: un mensaje de falla o un string vacío.
    """
    if not fire_estado == "ACTIVO":
        return "Critico: El firewall no esta activo. Riesgo de intrusion.\n"
    return ""

def analizar_recursos_criticos(cpu, ram):
    """
    Evalúa si el uso del hardware es excesivo (Regla con AND).
    Recibe: cpu (float), ram (float).
    Devuelve: un mensaje de alerta (str) o un string vacío.
    """
    if cpu > 85 and ram > 80: 
        return "ALERTA: SOBRECARGA CRITICA DE HARDWARE (CPU/RAM).\n"
    return ""

# ---- PROGRAMA PRINCIPAL ---- 

print ("="*50)
print("Sistema de diagnostico de servidor - UTN AVELLANEDA")
print("="*50)

# 1. Ingreso de datos (10 variables obligatorias)
sv_nombre = input("Nombre del servidor: ")
admn = input("Administrador responsable: ")
## NUMERICOS
CPU_uso = float(input("Uso de CPU (%): "))
RAM_uso = float(input("Uso de RAM (%): "))
disco_libre = float(input("Espacio libre en disco (GB):"))
usuarios_cantidad = int(input("Cantidad de usuarios conectados: "))
procesos_cantidad = int(input("Cantidad de procesos activos: "))
## ESTADOS
SO_tipo = input("Sistema Operativo (Linux/ Windows Server): ").strip().upper()
fire_estado = input("Estado del Firewall (Activo / Desactivado): ").strip().upper()
sv_tipo = input("Tipo de servidor(Web / Base de datos / Archivos): ").strip().upper()

carga_recursos_total = (CPU_uso + RAM_uso) / 2 

procesos_por_usuario = procesos_cantidad / usuarios_cantidad if usuarios_cantidad > 0 else procesos_cantidad

problemas= ""
recomendaciones = ""

msg_sec = analizar_seguridad(fire_estado)
if msg_sec:
    problemas += msg_sec
    recomendaciones += "Activar el firewall desde la consola de red\n"

msg_res = analizar_recursos_criticos(CPU_uso, RAM_uso)
if msg_res:
    problemas += msg_res
    recomendaciones += "Finalizar procesos de alta prioridad o reiniciar el nodo\n"

if 40 <= CPU_uso <= 70:
    pass

if sv_tipo == "WEB" and usuarios_cantidad > 100 and CPU_uso > 75:
    problemas += "RIESGO: saturacion por trafico web\n"
    recomendaciones += "Implementar balanceador de carga o escalar CPU\n"

if disco_libre < 10 or procesos_cantidad > 300:
    problemas += "ADVERTENCIA: poco espacio en disco o exceso de procesos activos\n"
    recomendaciones += "Realizar limpieza de logs y depuracion de procesos\n"

if sv_tipo == "BASE DE DATOS" and RAM_uso > 90:
    problemas += "ALERTA: memoria insuficiente para la base de datos.\n"
    recomendaciones += "Optimizar indices y consultas SQL\n"

if carga_recursos_total > 80 and disco_libre < 20:
    problemas += "Estado: rendimiento general degradado (Carga alta + Disco bajo)\n"
    recomendaciones += "Ampliar almacenamiento\n"

if procesos_por_usuario > 50 and CPU_uso > 60: 
    problemas += "Anomalia: Demasiados procesos por cada usuario conectado\n"
    recomendaciones += "Buscar posible malware\n"

estado_final = "Sistema Estable" if not problemas else "ALERTA"

print("\n" + "·"*50)
print(f"REPORTE TÉCNICO PARA: {sv_nombre}")
print(f"RESPONSABLE:        {admn}")
print(f"ESTADO GENERAL:     {estado_final}")
print("·"*50)

if problemas:
    print(f"Problemas detectados:\n{problemas}")
    print(f"Recomendaciones tecnicas:\n{recomendaciones}")
else:
    print("No se detectaron problemas :)")

print("="*50)