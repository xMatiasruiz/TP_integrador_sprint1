def validacion_porcentaje_numerico(num: str) -> bool:
    """
    Valida si un string representa un número flotante o entero válido 
    y si se encuentra dentro del rango porcentual de 0 a 100.

    Args:
        num (str): El string que se desea evaluar como porcentaje.

    Returns:
        bool: True si el string es un número válido entre 0 y 100 (inclusive), 
            False en caso contrario.

    """

    if num == "":
        return False
    # creamos una variable para contar los puntos
    puntos = 0

    for i in range(len(num)):  # recorremos el string(numero)
        caracter = num[i]    # extraemos el caracter

        if caracter == ".":  # preguntamos si es un punto
            puntos += 1

            if puntos > 1:   # si hay ás de un punto
                return False
            
            if i == 0 or i == len(num) - 1:  # si es  al principio ni al final
                return False

        elif caracter < "0" or caracter > "9":  # si no es un número que esta en ese rango
            return False
        
    valor = float(num)  # convertimos el string a float
    if valor >= 0 and valor <= 100:  # si es mayor o igual a 0 y menor o igual a 100
        return True
    else:
        return False
     

def validacion_numerico(num: str) -> bool:
    """
    Valida si un string representa un número flotante o entero válido 
    y si es mayor o igual a 0.

    Args:
        num (str): El string que se desea evaluar.

    Returns:
        bool: True si el string es un número válido mayor o igual a 0, 
              False en caso contrario.
    """
    if num == "":
        return False
    
    puntos = 0

    # Primero nos aseguramos de que el string sea REALMENTE un número
    for i in range(len(num)):  
        caracter = num[i]    

        if caracter == ".":  
            puntos = puntos + 1
            if puntos > 1:   
                return False
            if i == 0 or i == len(num) - 1:  
                return False

        elif caracter < "0" or caracter > "9":  
            return False
        
    
    valor = float(num)  
    if valor >= 0: 
        return True
    else:
        return False


def validacion_cadena(cadena: str) -> bool:
    """
    Verifica que la cadena ingresada no esté vacía, no contenga solo espacios
    y tenga una longitud real de más de 5 caracteres.

    Args:
        cadena (str): Texto a validar (nombre de administrador o servidor).

    Returns:
        bool: True si la cadena es válida y tiene más de 5 caracteres, False de lo contrario.
    """

    if cadena == "":   # Si el dato está completamente vacío
        return False
    
    tiene_caracter_valido = False # Bandera para detectar que NO sean solo espacios

    for i in range(len(cadena)):  # Recorremos la cadena carácter por carácter
        caracter = cadena[i]
       
        if caracter != " ":   # Si encontramos AL MENOS una letra o número, ya no son solo espacios
            tiene_caracter_valido = True

    # Para ser válida, tiene que medir más de 5 caracteres Y no ser solo espacios
    if len(cadena) > 5 and tiene_caracter_valido:  
        return True
    else:
        return False

def validadcion_de_incio_de_diagnostico(inicio_de_sistema: str) -> bool:
    """
    Valida que la respuesta de inicio del diagnóstico sea correcta.

    Args:
        inicio_de_sistema (str): Respuesta ingresada por el usuario.
        Debe ser "si" o "no".

    Returns:
        bool: True si la respuesta es válida.
    """
    if inicio_de_sistema == "1" or inicio_de_sistema == "2":
        return True
