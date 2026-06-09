def mostrar_diagnostico(nombre_servidor: str, alertas: list, recomendaciones: list): 
    """
    Muestra de forma estructurada y amigable el diagnostico final
    """

    print("\n" + "=" *60)
    print(f"DIAGNOSTICO DEL SERVIDOR: {nombre_servidor}")
    print("=" *60)

    tiene_problemas = False
    i = 0 
    while i < len(alertas):
        if alertas[i] !="":
            tiene_problemas = True
        i = i + 1
    
    if tiene_problemas:
        estado_general = "Alerta crtica / Revision"
    else: 
        estado_general = "Estable / Operativo"
    print(f"Estado General: {estado_general}")
    print("-"*60)

    print("Problemas detectados:")
    hay_alertas = False
    i=0
    while i < len(alertas):
        if alertas[i] != "":
            print(f"💢{alertas[i]}")
            hay_alertas = True
        i = i + 1 
    if not hay_alertas:
        print("✓ Ninguno. El servidor responde a los parámetros normales")

    print("\nRecomendaciones de accion:")
    hay_reco = False
    i = 0
    while i < len(recomendaciones):
        if recomendaciones[i] != "":
            print(f"⚡ {recomendaciones[i]}")
            hay_reco = True
        i = i + 1
    if not hay_reco:
        print("✓ No se requieren acciones correctivas inmediatas.")
    
    print("=" * 60 + "\n")
    
