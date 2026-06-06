def validar_texto(cadena: str) -> bool:
    """

    Valida que el texto ingresado tenga mas de 5 caracteres reales.

    Args:
        cadena (str): El texto que ingreso el usuario.

    Returns:
        bool: True si cumple con las condiciones, False si no.
    """

    # Si el largo total es menor o igual a 5 ya no sirve
    if len(cadena) <= 5:
        return False
    
    # Contamos cuantas letras reales hay (que no sean espacios)
    caracteres_reales = 0
    for caracter in cadena:
        if caracter != " ":
            caracteres_reales += 1

    # Si despues de recorrer todo el texto no encontramos letras, esta mal
    if caracteres_reales == 0:
        return False
    
    # Si paso todos los filtros entonces es valido
    return True

def validar_porcentaje(valor: float) -> bool:
    """

    Valida que un porcentaje este en el rango correcto (0.0 a 100.0)
    
    Args:
        valor (float): El numero que representa el porcentaje (CPU o RAM).

    Returns:
        bool: True si esta entre 0.0 y 100.0 inclusive, False si no.
    """
    if 0.0 <= valor <= 100.0:
        return True
    return False

def validar_cantidad_positiva(valor: int) -> bool:
    """ 
    
    Valida que una cantidad entera sea mayor o igual a cero.

    Args:
        valor (int): La cantidad a evaluar (usuarios o procesos)

    Returns:
        bool: True si es mayor o igual a cero, False si es negativo.
    """

    if valor >= 0:
        return True
    return False


