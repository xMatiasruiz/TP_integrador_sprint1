def mostrar_diagnostico(nombre: str, alertas: list, recomendaciones: list) -> None:
    """
    Módulo Output: Renderiza en pantalla el reporte técnico final del servidor
    recién evaluado, incorporando de forma obligatoria f-strings, tabulaciones
    y la justificación técnica de cada diagnóstico según las reglas del negocio.
    """
    print("\n" + "=" * 60)
    print(f"       📊 REPORTE TÉCNICO GENERADO: {nombre}")
    print("=" * 60)
    
    print("  ⚠️  ALERTAS CRÍTICAS DETECTADAS:")
    hay_alertas = False
    
    for i in range(len(alertas)):
        alerta = alertas[i]
        if alerta != "":
            hay_alertas = True
            print(f"\t❌ {alerta}")
            
            if i == 0:
                print("\t   ↳ Justificación: Ambos recursos principales superan el umbral crítico del 85%.")
            elif i == 1:
                print("\t   ↳ Justificación: Espacio en disco menor al 15% con alta concurrencia de servicios.")
            elif i == 2:
                print("\t   ↳ Justificación: Sistema Windows Server expuesto públicamente sin directivas de Firewall.")
            elif i == 3:
                print("\t   ↳ Justificación: Anomalía de red. Tráfico entrante/saliente elevado con CPU en reposo.")
            elif i == 4:
                print("\t   ↳ Justificación: Fuga de memoria (Memory Leak) potencial detectada por consumo asimétrico.")
            elif i == 5:
                print("\t   ↳ Justificación: Mitigación de carga activa sobre Firewall con tráfico extremo.")
            elif i == 6:
                print("\t   ↳ Justificación: Colapso inminente de infraestructura por almacenamiento o CPU al límite.")
            elif i == 7:
                print("\t   ↳ Justificación: Sobrecarga de hilos y procesos activos en entorno de kernel Linux.")
    
    if not hay_alertas:
        print("\t✅ El sistema no presenta anomalías. Operando bajo parámetros normales.")
        
    print("-" * 60)
    
    print("  💡 ACCIONES RECOMENDADAS DE INMEDIATO:")
    hay_recom = False
    
    for recom in recomendaciones:
        if recom != "":
            print(f"\t🛠️  {recom}")
            hay_recom = True
            
    if not hay_recom:
        print("\t🔹 No se requieren tareas de mantenimiento ni escalabilidad preventivas.")
        
    print("=" * 60 + "\n")