import reglas

def evaluar_sistema(cpu: float, ram: float, disco_libre: float, so: str, firewall:str, servicios_activos: int, trafico_red: float):
    """
        Evalua todas las reglas e integra las alertas y recomendaciones utilizando listas de forma puramente algoritmica
    """

    alertas = ["","","","","","","",""]
    recomendaciones = ["","","","","","","",""]

    if reglas.regla_sobrecarga(cpu, ram):
        alertas[0] = "Uso critico de recursos principales (CPU/RAM)."
        recomendaciones[0] = "Reiniciar servicios pesados o escalar hardware."
    
    if reglas.regla_almacenamiento(disco_libre, servicios_activos):
        alertas[1] = "Poco espacio en disco con alta carga de servicios"
        recomendaciones[1] = "Liberar almacenamiento temporal y logs"
    
    if reglas.regla_vulnerabilidad_so(so, firewall):
        alertas[2] = "Servidor Windows expuesto sin Firewall activo"
        recomendaciones[2] = "Habilitar el firewall del sistema de inmediato"
    
    if reglas.regla_trafico_sospechoso(cpu, trafico_red):
        alertas[3] = "Desconexion entre trafico de red y uso de CPU"
        recomendaciones[3] = "Auditar conexiones entrantes por posible ataque o cuelgue"
    
    if reglas.regla_servicio_inestable(servicios_activos,ram):
        alertas[4] = "Fuga de memoria detectada(pocos servicios, mucha RAM)"
        recomendaciones[4] = "Identificar y reiniciar el servicio inestable."
    
    if reglas.regla_alerta_saturacion_red(trafico_red, firewall):
        alertas[5] = "Saturación de red con Firewall mitigando tráfico."
        recomendaciones[5] = "Implementar balanceador de carga o filtro IP externo."
        
    if reglas.regla_mantenimiento_urgente(disco_libre, cpu):
        alertas[6] = "Colapso inminente de la máquina (Límite de Disco o CPU)."
        recomendaciones[6] = "Aplicar protocolo de mantenimiento de emergencia."
        
    if reglas.regla_optimizacion_so(so, servicios_activos):
        alertas[7] = "Entorno Linux con sobrecarga de procesos activos."
        recomendaciones[7] = "Optimizar hilos de ejecución o distribuir tareas."
    

    return alertas, recomendaciones
