# Sistema de diagnostico de servidor
## Datos del proyecto
### Integrantes
- Matias Ruiz Diaz
- Ithiel Ruiz
- Santiago Poustis
- Gianluca Di Giacomo

### Lenguaje utilizado
- Python 3.13.5


Listado de Reglas Implementadas - Sprint 1

8 reglas logicas utilizadas para el diagnostico del servidor

1. Seguridad(Operador NOT): Evalua si el fire_estado no es "ACTIVO". si el firewall esta desactivado, se genera una alerta critica

2. Sobrecarga de Hardware(Operador AND): si el CPU_uso es mayor a 85% y el RAM_uso es mayor a 80%, se detecta una sobrecarga critica.

3. Mantenimiento(Operador OR): Si el disco_libre es menor a 10gb o la procesos_cantidad supera los 250_ se recomienda limpieza.

4. Rango Estable(Rango Numerico): Se evalua si el CPU_uso se encuentra entre el 40% y 70% para informar un estado de trabajo normal.

5. Saturacion Web(3+ variables): Especifica para servidores tipo "WEB". Evalua si el tipo_servidor es web, los usuarios_cantidad superan los 100 y el CPU_uso es mayor a 75%.

6. Memoria en Base de Datos: Si el sv_tipo es "Base de Datos" y el RAM_uso supera el 90%, se alerta sobre posible perdida de rendimiento.

7. Rendimiento Degradado(Variable Calculada): Utiliza la variable calculada carga_recursos_total. Si es mayor a 80 y el disco es menor a 20gb, el sistema entra en estado de alerta

8. Anomalia de Procesos(Variable Calculada): Utiliza procesos_por_usuario si un usuario tiene mas de 50 procesos en promedio y la CPU esta alta, se alerta por posible malware
