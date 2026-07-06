import os
import json
from calculos import evaluar_sistema
from inputs import pedir_nombre_servidor, pedir_porcentaje_hardware,pedir_cantidad_positiva,pedir_sistema_operativo, pedir_estado_firewall
from output import mostrar_diagnostico

SERVIDORES = "TP_integrador_sprint1/servers/servidores.json"  # Variable contante donde esta guardada la ruta del JSON

def crear_archivo_si_no_existe() -> None:
    """
    Inicializa el archivo JSON de almacenamiento si no existe previamente.

    Crea un archivo vacío con un diccionario `{}` si el archivo no existe 
    o está completamente vacío, previniendo errores de lectura en el primer inicio.
    
    Returns:
        None
    """

    ## fix crear carpeta si no existe -M
    directorio = os.path.dirname(SERVIDORES)
    if directorio and not os.path.exists(directorio):
        os.makedirs(directorio)
    
    with open( SERVIDORES, "a") as servidores:  # abre el archivo y se asegura de cerrarlo automaticamente
        if servidores.tell() == 0:  # el .tell nos dice donde esta el puntero
            json.dump( {}, servidores)  # el .dump agarra un objeto y lo guarda en el archivo


def cargar_diagnosticos() -> dict:
    # Si el archivo no existe, devolvemos un diccionario vacío
    if not os.path.exists(SERVIDORES):
        return {}
    
    # Si el archivo existe pero está vacío, el json.load fallará, 
    # por eso capturamos el error para devolver un dict vacío
    try:
        with open(SERVIDORES, "r", encoding="utf-8") as f:
            datos = json.load(f)
            # Solo si lo que cargamos es realmente un diccionario, lo devolvemos
            if type(datos) == dict:
                return datos
            else:
                return {}
    except:
        return {}
    

def guardar_diagnosticos(servidores: dict) -> None:
    """
    Guarda y sobrescribe de forma segura el estado actual de los servidores en el JSON.

    Args:
        servidores (dict): El diccionario completo mapeado con la información actualizada.
        
    Returns:
        None
    """
    with open(SERVIDORES, "w") as archivo:
        json.dump(servidores, archivo, indent=4)  # Guarda con indentación para que sea legible


def registrar_diagnostico(mis_servidores:dict) -> dict:
    """
    Controlador para dar de alta un nuevo servidor.
    
    Solicita los datos técnicos al administrador usando el módulo 'inputs',
    procesa las reglas algorítmicas mediante el módulo 'calculos', guarda el
    resultado en el archivo y despliega el reporte técnico final en pantalla.

    Returns:
        dict
    """
    
    #mis_servidores = cargar_diagnosticos()

    nombre = pedir_nombre_servidor()
    if nombre in mis_servidores:
        print("ESTE SERVIDOR YA TIENE UN REGISTRO")
        return mis_servidores
    cpu = pedir_porcentaje_hardware("CPU")  
    ram = pedir_porcentaje_hardware("RAM")
    disco = pedir_porcentaje_hardware("Espacio Libre en Disco")
    so = pedir_sistema_operativo()
    firewall = pedir_estado_firewall()
    servicios_activos = pedir_cantidad_positiva("servicios activos")
    trafico_red = pedir_porcentaje_hardware("Tráfico de Red (MB/s)")

    alertas, recomendaciones = evaluar_sistema(cpu, ram, disco, so, firewall, servicios_activos, trafico_red)
    
    #creamos un registro nuevo con el nombre de servidor como llave
    mis_servidores[nombre] = {"cpu": cpu, "ram": ram, "disco": disco, "sistema operativo": so, "firewall": firewall, "servicios activos": servicios_activos, "trafico red": trafico_red, "alertas": [], "recomendaciones": []}

    print("✅ Servidor registrado en memoria con exito. Use la opcion 6 para guardar.")
    ##mostrar_diagnostico(nombre, alertas, recomendaciones)
    print("⚠️ Recuerde usar la opcion 4 para generar el reporte")
    input("Presione ENTER para continuar...")
    return mis_servidores


def ejecutar_diagnostico(mis_servidores:dict) -> dict:
    """
    Opción para Ejecutar: Busca un servidor cargado previamente,
    le aplica las reglas de evaluación y guarda los resultados.
    """
    nombre = pedir_nombre_servidor()

    if nombre not in mis_servidores:
        print("❌ Ese servidor no existe. Carguelo primero con la Opcion 1.")
        input("Presione una tecla para continuar. . .")
        return mis_servidores

    datos = mis_servidores[nombre]
    print(f"Evaluando el servidor'{nombre}' ")
    alertas, recomendaciones = evaluar_sistema(
        datos["cpu"], 
        datos["ram"], 
        datos["disco"], 
        datos["sistema operativo"], 
        datos["firewall"], 
        datos["servicios activos"], 
        datos["trafico red"]
    )

    mis_servidores[nombre]["alertas"] = alertas
    mis_servidores[nombre]["recomendaciones"] = recomendaciones

    print("✅ Diagnostico ejecutado con exito.")
    mostrar_diagnostico(nombre, alertas, recomendaciones)
    input("Presione una tecla para continuar. . . ")
    return mis_servidores


def mostrar_configuracion_actual(mis_servidores: dict) -> None:
    """
    Recorre las configuraciones activas en la memoria y las muestra.
    Muestra los datos ingresados en la Opción 1 en tiempo real.
    """
    print("\n" + "=" * 60)
    print("       📋 CONFIGURACIONES ACTUALES EN MEMORIA")
    print("=" * 60)
    
    if not mis_servidores:
        print("  No hay servidores cargados en la memoria actual.")
    else:
        for nombre, datos in mis_servidores.items():
            print(f"\n🖥️  SERVIDOR: {nombre}")
            print(f"  📊 Métricas -> CPU: {datos['cpu']}% | RAM: {datos['ram']}% | Disco Libre: {datos['disco']}%")
            print(f"  ⚙️  Entorno  -> SO: {datos['sistema operativo']} | Firewall: {datos['firewall']}")
            print(f"  🔌 Tráfico  -> {datos['trafico red']} MB/s | Servicios Activos: {datos['servicios activos']}")
            
            # FILTRAR Y MOSTRAR ALERTAS
            print("  ⚠️  Alertas Detectadas:")
            hay_alertas = False
            lista_alertas = datos.get("alertas", [])
            
            for alerta in lista_alertas:
                if alerta != "": 
                    print(f"    ❌ {alerta}")
                    hay_alertas = True
            
            if not hay_alertas:
                print("    ✅ Ninguna (Requiere ejecutar diagnóstico para procesar).")
                
            # FILTRAR Y MOSTRAR RECOMENDACIONES
            print("  💡 Acciones Recomendadas:")
            hay_recom = False
            lista_recom = datos.get("recomendaciones", [])
            
            for recom in lista_recom:
                if recom != "": 
                    print(f"    🛠️  {recom}")
                    hay_recom = True
            
            if not hay_recom:
                print("    🔹 Ninguna (Requiere ejecutar diagnóstico para procesar).")
                
            print("-" * 60) 

    print("\n" + "=" * 60)
    input("Presione ENTER para continuar...")


def buscar_diagnostico() -> None:
    """
    Busca un servidor específico por su nombre en la base de datos JSON
    y muestra su ficha técnica completa junto con el diagnóstico detallado
    respetando el diseño visual del historial.
    """
    servidores = cargar_diagnosticos()
    nombre = pedir_nombre_servidor()

    if nombre in servidores:
        datos = servidores[nombre]
        
        print("\n" + "=" * 60)
        print("       🔍 SERVIDOR ENCONTRADO EN LA BASE DE DATOS")
        print("=" * 60)
        
        # 1. FICHA TÉCNICA (Idéntica a tu formato de Historial)
        print(f"\n🖥️  SERVIDOR: {nombre}")
        print(f"  📊 Métricas -> CPU: {datos['cpu']}% | RAM: {datos['ram']}% | Disco Libre: {datos['disco']}%")
        print(f"  ⚙️  Entorno  -> SO: {datos['sistema operativo']} | Firewall: {datos['firewall']}")
        print(f"  🔌 Tráfico  -> {datos['trafico red']} MB/s | Servicios Activos: {datos['servicios activos']}")
        
        # 2. FILTRAR Y MOSTRAR ALERTAS (Igual a tu historial)
        print("  ⚠️  Alertas Detectadas:")
        hay_alertas = False
        lista_alertas = datos.get("alertas", [])
        
        for alerta in lista_alertas:
            if alerta != "": 
                print(f"    ❌ {alerta}")
                hay_alertas = True
        
        if not hay_alertas:
            print("    ✅ Ninguna. El servidor opera bajo parámetros normales.")
            
        # 3. FILTRAR Y MOSTRAR RECOMENDACIONES (Igual a tu historial)
        print("  💡 Acciones Recomendadas:")
        hay_recom = False
        lista_recom = datos.get("recomendaciones", [])
        
        for recom in lista_recom:
            if recom != "": 
                print(f"    🛠️  {recom}")
                hay_recom = True
        
        if not hay_recom:
            print("    🔹 No se requieren acciones de mantenimiento inmediatas.")
            
    else:
        print("\n❌ El servidor no se encuentra en la base de datos.")
        
    print("\n" + "=" * 60)
    input("Presione ENTER para continuar...")


def modificar_diagnosticos(servidores:dict) -> dict:
    """
    Modifica los parámetros de un registro existente y fuerza una re-evaluación.
    
    Busca la llave del servidor, solicita la carga de los nuevos parámetros de 
    hardware/entorno, recalcula las listas fijas de alertas y guarda la 
    actualización sobreescribiendo el JSON.

    Returns:
        None
    """
    
    nombre = pedir_nombre_servidor()

    if nombre in servidores:
        print(f"\n🛠️ Modificando parámetros para el servidor: {nombre}")
        servidores[nombre]["cpu"] = pedir_porcentaje_hardware("cpu")
        servidores[nombre]["ram"] = pedir_porcentaje_hardware("ram")
        servidores[nombre]["disco"] = pedir_porcentaje_hardware("disco")
        servidores[nombre]["sistema operativo"] = pedir_sistema_operativo()
        servidores[nombre]["firewall"] = pedir_estado_firewall()
        servidores[nombre]["servicios activos"] = pedir_cantidad_positiva("servicios activos")
        servidores[nombre]["trafico red"] = pedir_porcentaje_hardware("trafico red")
        alertas, recomendaciones = evaluar_sistema(
            servidores[nombre]["cpu"],
            servidores[nombre]["ram"],
            servidores[nombre]["disco"],
            servidores[nombre]["sistema operativo"],
            servidores[nombre]["firewall"],
            servidores[nombre]["servicios activos"],
            servidores[nombre]["trafico red"],
        )
        servidores[nombre]["alertas"] = []
        servidores[nombre]["recomendaciones"] = []
        
        print("\n ✅ Datos modificados en memoria con éxito.")
        print("⚠️ Recuerde usar la opción 4 para volver a ejecutar el diagnostico y la opción de Guardar para confirmar.")
        
    else:
        print("❌ Este servidor aún no está registrado en el sistema.")

    input("Presione UNA TECLA para continuar...")
    return servidores



def eliminar_diagnostico() -> None:
    """
    Remueve permanentemente el registro de un servidor de la base de datos JSON.

    Returns:
        None
    """

    servidores = cargar_diagnosticos()
    nombre = pedir_nombre_servidor()

    if nombre in servidores:
        del servidores[nombre]
        guardar_diagnosticos(servidores)
        print(" ✅ Diagnostico eliminado corecctamente.")
    else:
        print("⚠️ Este servidor no tiene un diagnostico realizado")

    input("Presione UNA TECLA para continuar...")

