def regla_sobrecarga(cpu: float, ram: float) -> bool:
    """
    regla 1 (AND): CPU y RAm al limite simultaneamente.
    """
    return cpu > 85.0 and ram > 85.0

def regla_almacenamiento(disco_libre: float, servicios_activos:int) -> bool:
    """
    Regla 2 (Rangos y multivariable): Poco disco y muchos servicios corriendo.
    """
    return disco_libre < 15.0 and servicios_activos > 10

def regla_vulnerabilidad_so(so:str, firewall:str) -> bool:
    """
    Regla 3 (Categorica y NOT): Windows Server expuesto sin proteccion
    """

    return so == "Windows Server" and not (firewall == "Activado")

def regla_trafico_sospechoso(cpu: float, trafico_red: float) -> bool:
    """
    Regla 4 (OR): Anomalias extremas entre uso de procesador y red. 
    """

    return (cpu > 90.0 and trafico_red < 10.0) or (cpu < 5.0 and trafico_red > 500.0)

def regla_servicio_inestable(servicios_activos: int, ram:float) -> bool:
    """
    Regla 5 (AND): Pocos servicios pero consumo excesivo de memoria.
    """
    return servicios_activos <= 3 and ram > 75.0

def regla_alerta_saturancion_red(trafico_red: float, firewall: str) -> bool:
    """Regla 6 (Multivariable): Trafico al limite y firewall procesando todo"""

    return trafico_red > 800.0 and firewall == "Activado"

def regla_mantenimiento_urgente(disco_libre: float, cpu: float) -> bool:
    """
    Regla 7 (OR): El servidor se queda sin aire por disco o por procesamiento.
    """

    return disco_libre < 5.0 or cpu > 95.0

def regla_optimizacion_so(so:str, servicios_activos: int) -> bool: 
    """
    Regla 8 (Categorica): Linux con excesiva cantidad de servicios simultaneos.
    """

    return so == "Linux" and servicios_activos > 25