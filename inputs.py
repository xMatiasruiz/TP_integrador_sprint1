import validaciones

def pedir_nombre_servidor() -> str:
    """
    Solicita y valida el nombre del servidor hasta que sea correcto.
    
    Returns:
        str: El nombre del servidor validado.
    """
    nombre_servidor_valido = False
    nombre_servidor = ""

    while not nombre_servidor_valido:
        nombre_servidor = input("Ingrese el nombre del servidor (minimo 6 caracteres): ")

        if validaciones.validar_texto(nombre_servidor):
            nombre_servidor_valido = True
        else:
            print("❌ERROR❌: El nombre debe tener mas de 5 caracteres reales. Reintente.")
        
    return nombre_servidor

def pedir_porcentaje_hardware(componente: str) -> float:
    """
    Solicita y valida el porcentaje de uso de un componente de hardware.

    Args:
        componente (str): El nombre del componente a pedir (ej: "CPU" o "RAM").

    Returns:
        float: El porcentaje validado entre 0.0 y 100.0.
    """
    porcentaje_valido = False
    porcentaje_ingresado = 0.0

    while not porcentaje_valido:
        ingreso_usuario = input(f"Ingrese el porcentaje de uso de {componente}: ")
        porcentaje_ingresado = float(ingreso_usuario)

        if validaciones.validar_porcentaje(porcentaje_ingresado):
            porcentaje_valido = True
        else:
            print(f"❌ERROR❌: El porcentaje de {componente} debe estar entre 0 y 100. Reintente.")

    return porcentaje_ingresado

def pedir_cantidad_positiva(tipo_cantidad: str) -> int:
    """
    Solicita y valida una cantidad entera mayor o igual a cero.

    Args:
        tipo_cantidad (str): El nombre de la cantidad a pedir (ej: "servicios activos").

    Returns:
        int: La cantidad entera validada.
    """
    cantidad_valida = False
    cantidad_ingresada = 0

    while not cantidad_valida:
        ingreso_usuario = input(f"Ingrese la cantidad de {tipo_cantidad}: ")
        cantidad_ingresada = int(ingreso_usuario)

        if validaciones.validar_cantidad_positiva(cantidad_ingresada):
            cantidad_valida = True
        else:
            print(f"❌ERROR❌: La cantidad de {tipo_cantidad} no puede ser negativa. Reintente.")

    return cantidad_ingresada

def pedir_sistema_operativo() -> str:
    """
    Solicita y valida el tipo de sistema operativo instalado.

    Returns:
        str: El nombre del sistema operativo validado ("Linux" o "Windows Server").
    """
    so_valido = False
    so_ingresado = ""
    while not so_valido:
        so_ingresado = input("Sistema Operativo (escribir exactamente Linux / Windows Server): ")
        if so_ingresado == "Linux" or so_ingresado == "Windows Server":
            so_valido = True
        else:
            print("❌ERROR❌: Debe escribir exactamente Linux o Windows Server (respetando mayusculas). Reintente.")
    return so_ingresado

def pedir_estado_firewall() -> str:
    """
    Solicita y valida el estado del firewall.

    Returns:
        str: El estado del firewall ("Activado" o "Desactivado").
    """
    fw_valido = False
    fw_ingresado = ""
    while not fw_valido:
        fw_ingresado = input("Estado del Firewall (escribir exactamente Activado / Desactivado): ")
        if fw_ingresado == "Activado" or fw_ingresado == "Desactivado":
            fw_valido = True
        else:
            print("❌ERROR❌: Debe escribir exactamente Activado o Desactivado. Reintente.")
    return fw_ingresado