def regla_sobrecarga(cpu: float, ram: float) -> bool:
    """
    Evalua si los recursos principales (CPU y RAM) estan sobrecargados en simultaneo.

    Args:
        cpu (float): Porcentaje de uso de la CPU.
        ram (float): Porcentaje de uso de la memoria RAM.

    Returns:
        bool: True si ambos superan el 85.0%, False en caso contrario.
    """
    return cpu > 85.0 and ram > 85.0


def regla_almacenamiento(disco_libre: float, servicios_activos: int) -> bool:
    """
    Evalua si el espacio en disco es critico considerando la cantidad de servicios.

    Args:
        disco_libre (float): Porcentaje de espacio libre en el disco.
        servicios_activos (int): Cantidad de servicios corriendo en el servidor.

    Returns:
        bool: True si el disco es menor al 15.0% y hay mas de 10 servicios.
    """
    return disco_libre < 15.0 and servicios_activos > 10


def regla_vulnerabilidad_so(so: str, firewall: str) -> bool:
    """
    Chequea si el servidor corre Windows Server y tiene el firewall caido.

    Args:
        so (str): Nombre del sistema operativo ("Linux" o "Windows Server").
        firewall (str): Estado del firewall ("Activado" o "Desactivado").

    Returns:
        bool: True si el SO es Windows Server y el firewall esta Desactivado.
    """
    return so == "Windows Server" and firewall == "Desactivado"


def regla_trafico_sospechoso(cpu: float, trafico_red: float) -> bool:
    """
    Detecta una anomalia entre el bajo uso de CPU y el alto trafico de red.

    Args:
        cpu (float): Porcentaje de uso de la CPU.
        trafico_red (float): Trafico de red en MB/s.

    Returns:
        bool: True si la CPU es menor al 20.0% y el trafico supera los 500.0 MB/s.
    """
    return cpu < 20.0 and trafico_red > 500.0


def regla_servicio_inestable(servicios_activos: int, ram: float) -> bool:
    """
    Detecta una posible fuga de memoria (pocos procesos consumiendo mucha RAM).

    Args:
        servicios_activos (int): Cantidad de servicios corriendo.
        ram (float): Porcentaje de uso de la memoria RAM.

    Returns:
        bool: True si hay menos de 3 servicios y la RAM supera el 80.0%.
    """
    return servicios_activos < 3 and ram > 80.0


def regla_alerta_saturacion_red(trafico_red: float, firewall: str) -> bool:
    """
    Evalua si la red esta saturada a pesar de tener el firewall activo.

    Args:
        trafico_red (float): Trafico de red en MB/s.
        firewall (str): Estado del firewall ("Activado" o "Desactivado").

    Returns:
        bool: True si el trafico supera los 800.0 MB/s y el firewall esta Activado.
    """
    return trafico_red > 800.0 and firewall == "Activado"


def regla_mantenimiento_urgente(disco_libre: float, cpu: float) -> bool:
    """
    Determina si la maquina requiere mantenimiento por colapso inminente.

    Args:
        disco_libre (float): Porcentaje de espacio libre en el disco.
        cpu (float): Porcentaje de uso de la CPU.

    Returns:
        bool: True si el disco libre es menor al 5.0% o la CPU supera el 95.0%.
    """
    return disco_libre < 5.0 or cpu > 95.0


def regla_optimizacion_so(so: str, servicios_activos: int) -> bool:
    """
    Evalua si un entorno Linux esta sobrecargado de procesos activos.

    Args:
        so (str): Nombre del sistema operativo ("Linux" o "Windows Server").
        servicios_activos (int): Cantidad de servicios corriendo.

    Returns:
        bool: True si el SO es Linux y maneja mas de 25 servicios.
    """
    return so == "Linux" and servicios_activos > 25