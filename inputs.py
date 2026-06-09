import validaciones

def pedir_nombre_servidor() -> str:
    """
    
    Solicita y valida el nombre del servidor hasta que sea correcto.
    
    Returns:
        str: El nombre del servidor validado.
    """

    # Creamos la bandera para controlar el bucle
    nombre_servidor_valido = False
    nombre_servidor = ""

    while not nombre_servidor_valido:
        nombre_servidor = input("Ingrese el nombre del servidor (minimo 6 caracteres): ")

        # Evaluamos la variable con nuestra validacion
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
            print(f"❌ERROR❌: El porcentaje de {componente} debe estar entre 0 y 100. Reintente")

    return porcentaje_ingresado

def pedir_cantidad_positiva(tipo_cantidad: str) -> int:
    """
    
    Solicita y valida una cantidad entera mayor o igual a cero.

    Args:
        tipo_cantidad (str): El nombre de la cantidad a pedir (ej: "usuarios" o "procesos").

    Returns:
        int: La cantidad entera validada.
    """

    cantidad_valida = False
    cantidad_ingresada = 0

    while not cantidad_valida:
        ingreso_usuario = input(f"Ingrese la cantidad de {tipo_cantidad}: ")
        cantidad_ingresada = int(ingreso_usuario)

        # Mandamos el numero entero a la funcion de validaciones
        if validaciones.validar_cantidad_positiva(cantidad_ingresada):
            cantidad_valida = True

        else:
            print(f"❌ERROR❌: La cantidad de {tipo_cantidad} no puede ser negativa. Reintete.")

    return cantidad_ingresada

    