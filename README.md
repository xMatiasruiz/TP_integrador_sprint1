# Sistema de diagnostico de servidor
## Datos del proyecto
### Integrantes
- Matias Ruiz Diaz
- Ithiel Ruiz
- Santiago Poustis
- Gianluca Di Giacomo

### Tecnologias utilizadas
* **Lenguaje:** Python 3.13.5
* **IDE:** Visual Studio Code
* **Control de versiones:** Git + GitHub

## Descripcion del codigo

Es una aplicacion que analiza el estado de un servidor a partir de datos solicitados al usuario

### Objetivos

- Evaluar el rendimiento del servidor
- Detectar posibles fallos
- Generar alertas
- Entrega al usuario recomendaciones de administracion 

## Reglas
Debe implementarse: 

- Un mínimo de 8 reglas (condiciones que evalúen distintas variables).  

### Las reglas deben incluir: 

- Reglas que utilicen 3 o más variables en la condición. 

- 3 reglas con combinación AND / OR. 

- 1 regla con NOT. 

- 1 regla que evalúe rangos numéricos. 

# Listado de Reglas Implementadas - Sprint 1

8 reglas logicas utilizadas para el diagnostico del servidor

1. Seguridad(Operador NOT): Evalua si el fire_estado no es "ACTIVO". si el firewall esta desactivado, se genera una alerta critica

2. Sobrecarga de Hardware(Operador AND): si el CPU_uso es mayor a 85% y el RAM_uso es mayor a 80%, se detecta una sobrecarga critica.

3. Mantenimiento(Operador OR): Si el disco_libre es menor a 10gb o la procesos_cantidad supera los 250_ se recomienda limpieza.

4. Rango Estable(Rango Numerico): Se evalua si el CPU_uso se encuentra entre el 40% y 70% para informar un estado de trabajo normal.

5. Saturacion Web(3+ variables): Especifica para servidores tipo "WEB". Evalua si el tipo_servidor es web, los usuarios_cantidad superan los 100 y el CPU_uso es mayor a 75%.

6. Memoria en Base de Datos: Si el sv_tipo es "Base de Datos" y el RAM_uso supera el 90%, se alerta sobre posible perdida de rendimiento.

7. Rendimiento Degradado(Variable Calculada): Utiliza la variable calculada carga_recursos_total. Si es mayor a 80 y el disco es menor a 20gb, el sistema entra en estado de alerta

8. Anomalia de Procesos(Variable Calculada): Utiliza procesos_por_usuario si un usuario tiene mas de 50 procesos en promedio y la CPU esta alta, se alerta por posible malware

### Flujo del codigo

    1. Solicitar datos al usuario
    2. Calcula los valores de uso de CPU Y RAM
    3. Se evaluan las reglas condicionales
    4. Acumulacion de alertas en base a las condiciones cumplidas
    5. Determinar estado final
    6. Presentacion de Resultado y Reporte Tecnico


## **Ejemplo de ejecucion**

### Datos ingresados 
    - Nombre del servidor: sv-prueba
    - Responsable: ejemplo
    - CPU: 95
    - RAM: 92
    - Disco: 5
    - Usuarios: 2
    - Procesos: 350
    - S.O: Linux
    - Firewall: Desactivado
    - Tipo de servidor: Web

### **Resultado**

··················································
REPORTE TÉCNICO PARA: sv-critico
RESPONSABLE:        made
ESTADO GENERAL:     ALERTA ❗
··················································
Problemas detectados:
Critico: El firewall no esta activo. Riesgo de intrusion.
ALERTA: SOBRECARGA CRITICA DE HARDWARE (CPU/RAM).
❌ ADVERTENCIA: poco espacio en disco o exceso de procesos activos
❌ Estado: rendimiento general degradado (Carga alta + Disco bajo)
❌ Anomalia: Demasiados procesos por cada usuario conectado

Recomendaciones tecnicas:
💡 Activar el firewall desde la consola de red
💡 Finalizar procesos de alta prioridad o reiniciar el nodo
💡 Limpiar archivos y revisar procesos
💡 Ampliar almacenamiento
💡 Buscar posible malware