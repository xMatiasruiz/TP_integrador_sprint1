import json
from calculos import evaluar_sistema
from inputs import pedir_nombre_servidor, pedir_porcentaje_hardware,pedir_cantidad_positiva,pedir_sistema_operativo, pedir_estado_firewall
from output import mostrar_diagnostico

SERVIDORES = "servers/servidores.json"  # Variable contante donde esta guardada la ruta del JSON

# Inicializacion segura (crea el archivo si no existe con un diccionario vacio)
def crear_archivo_si_no_existe() -> None:
    """
    Inicializa el archivo JSON de almacenamiento si no existe previamente.

    Crea un archivo vacío con un diccionario `{}` si el archivo no existe 
    o está completamente vacío, previniendo errores de lectura en el primer inicio.
    
    Returns:
        None
    """
    with open(
        SERVIDORES, "a"
    ) as servidores:  # habre el archivo  y se asegura de cerrarlo automaticamente
        if servidores.tell() == 0:  # el .tell nos dice donde esta el puntero
            json.dump(
                {}, servidores
            )  # el .dump agarra un objeto y lo guarda en el archivo


def cargar_diagnosticos() -> dict:
    """
    Carga todos los servidores y sus históricos registrados desde el archivo JSON.

    Returns:
        dict: Diccionario donde la llave es el nombre del servidor y el valor
              es otro diccionario con sus métricas y los resultados del diagnóstico.
    """
    with open(SERVIDORES, "r") as servidores:  # habre el archivo en modo lectura
        return json.load(servidores)  # el .load() convierte en JSON en un diccionario


def guardar_diagnosticos(servidores: dict) -> None:
    """
    Guarda y sobrescribe de forma segura el estado actual de los servidores en el JSON.

    Args:
        servidores (dict): El diccionario completo mapeado con la información actualizada.
        
    Returns:
        None
    """
    with open(SERVIDORES, "w") as archivo:
        json.dump(servidores, archivo, indent=4)  # Guarda con indentación para que sea legible humanamente

def registrar_diagnostico() -> None:
    """
    Controlador para dar de alta un nuevo servidor.
    
    Solicita los datos técnicos al administrador usando el módulo 'inputs',
    procesa las reglas algorítmicas mediante el módulo 'calculos', guarda el
    resultado en el archivo y despliega el reporte técnico final en pantalla.

    Returns:
        None
    """
    
    servidores = cargar_diagnosticos()

    nombre = pedir_nombre_servidor()
    if nombre in servidores:
        print("ESTE SERVIDOR YA TIENE UN REGISTRO")
        return
    cpu = pedir_porcentaje_hardware("CPU")  
    ram = pedir_porcentaje_hardware("RAM")
    disco = pedir_porcentaje_hardware("Espacio Libre en Disco")
    so = pedir_sistema_operativo()
    firewall = pedir_estado_firewall()
    servicios_activos = pedir_cantidad_positiva("servicios activos")
    trafico_red = pedir_porcentaje_hardware("Tráfico de Red (MB/s)")

    alertas, recomendaciones = evaluar_sistema(cpu, ram, disco, so, firewall, servicios_activos, trafico_red)
    
    #creamos un registro nuevo con el nombre de servidor como llave
    servidores[nombre] = {"cpu": cpu, "ram": ram, "disco": disco, "sistema operativo": so, "firewall": firewall, "servicios activos": servicios_activos, "trafico red": trafico_red, "alertas": alertas, "recomendaciones": recomendaciones}

    guardar_diagnosticos(servidores)
    print("servidor registrado con exito")
    mostrar_diagnostico(nombre, alertas, recomendaciones)
    input("Presione UNA TECLA para continuar...")


def ver_diagnosticos_realizados() -> None:
    """
    Recorre el historial completo de la base de datos y lo imprime de forma limpia.

    Filtra los elementos vacíos de las listas estáticas de alertas y recomendaciones
    para renderizar únicamente las incidencias reales detectadas en cada infraestructura.

    Returns:
        None
    """
    servidores = cargar_diagnosticos()
    
    
    print("\n" + "=" * 60)
    print("      📋 HISTORIAL DE DIAGNÓSTICOS REALIZADOS")
    print("\n" + "=" * 60)
    
    if not servidores:
        print("  No hay servidores registrados en la base de datos.")
    else:
        for nombre, datos in servidores.items():
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
                print("    ✅ Ninguna. El servidor opera bajo parámetros normales.")
                
            # FILTRAR Y MOSTRAR RECOMENDACIONES
            print("  💡 Acciones Recomendadas:")
            hay_recom = False
            lista_recom = datos.get("recomendaciones", [])
            
            for recom in lista_recom:
                if recom != "": 
                    print(f"    🛠️  {recom}")
                    hay_recom = True
            
            if not hay_recom:
                print("    🔹 No se requieren acciones de mantenimiento inmediatas.")
                
            print("-" * 60) # Línea divisoria entre servidores

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

def modificar_diagnosticos() -> None:
    """
    Modifica los parámetros de un registro existente y fuerza una re-evaluación.
    
    Busca la llave del servidor, solicita la carga de los nuevos parámetros de 
    hardware/entorno, recalcula las listas fijas de alertas y guarda la 
    actualización sobreescribiendo el JSON.

    Returns:
        None
    """
    servidores = cargar_diagnosticos()
    nombre = pedir_nombre_servidor()

    if nombre in servidores:
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
        servidores[nombre]["alertas"] = alertas
        servidores[nombre]["recomendaciones"] = recomendaciones

        guardar_diagnosticos(servidores)
        print("Se modificaron los datos del servidor y se volvio a realaizar el diagnostico.")
        mostrar_diagnostico(nombre, alertas, recomendaciones)
    else:
        print("a este servidor aun no se le realizo un diagnostico")
    input("Presione UNA TECLA para continuar...")


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
        print("diagnostico eliminado corecctamente.")
    else:
        print("a este servidor no se le realaizo un diagnostico.")

    input("Presione UNA TECLA para continuar...")
