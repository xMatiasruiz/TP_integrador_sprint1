# Sistema de Diagnóstico de Servidores

## 🏫 Datos del Proyecto
### Integrantes
- Matias Ruiz Diaz
- Ithiel Ruiz
- Santiago Poustis
- Gianluca Di Giacomo

### Tecnologías utilizadas
* **Lenguaje:** Python 3.13
* **IDE:** Visual Studio Code
* **Control de versiones:** Git + GitHub

---

## 🚀 Descripción del Código
Es una aplicación de consola diseñada bajo un enfoque de **arquitectura modular** que analiza de forma automatizada el estado de salud, rendimiento y seguridad de un servidor a partir de las métricas solicitadas al usuario.

### Objetivos
- Evaluar el rendimiento del hardware y software del servidor en tiempo real.
- Detectar vulnerabilidades críticas de seguridad.
- Consolidar alertas y recomendaciones técnicas utilizando listas e índices algorítmicos (sin métodos avanzados de listas).
- Entregar al administrador un reporte técnico limpio y estructurado.

---

## 🛠️ Arquitectura Modular (Sprint 2)
El código se reestructuró por completo en módulos con responsabilidades independientes para cumplir con las buenas prácticas de desarrollo:

* **`main.py`:** Punto de entrada. Inicializa la aplicación invocando al menú principal.
* **`menu.py`:** Controla el flujo de navegación de la interfaz de usuario en consola.
* **`inputs.py`:** Centraliza la captura de datos por teclado.
* **`validaciones.py`:** Contiene las funciones de control encargadas de verificar rangos, tipos de datos y textos mínimos.
* **`reglas.py`:** Lógica pura del negocio. Aloja las 8 funciones condicionales de evaluación.
* **`calculos.py`:** Procesa las métricas llamando a las reglas y guardando los resultados en listas paralelas ordenadas por índice.
* **`output.py`:** Módulo especializado en recorrer las listas mediante bucles `while` y dar formato visual al reporte final.

---

## 🧠 Listado de Reglas Implementadas
El sistema evalúa de manera algorítmica un mínimo de 8 reglas lógicas combinadas (cumpliendo con operadores `AND`, `OR`, `NOT`, rangos numéricos y combinaciones de 3 o más variables):

1. **Sobrecarga de Hardware (`AND`):** Alerta si el uso de CPU y RAM superan simultáneamente el 85.0%.
2. **Almacenamiento Crítico (`AND`):** Alerta si el espacio libre en disco es menor al 15.0% y hay más de 10 servicios activos.
3. **Vulnerabilidad de S.O. (`AND`):** Alerta si el sistema es "Windows Server" y el Firewall está "Desactivado".
4. **Tráfico Sospechoso (`AND`):** Alerta si la CPU está por debajo del 20.0% pero el tráfico de red supera los 500.0 MB/s (posible anomalía/ataque).
5. **Servicio Inestable (`AND`):** Detecta fuga de memoria si hay menos de 3 servicios activos pero consumen más del 80.0% de RAM.
6. **Saturación de Red (3+ Variables / `AND`):** Alerta si el tráfico supera los 800.0 MB/s, el firewall está "Activado" y el sistema mitiga la carga.
7. **Mantenimiento Urgente (`OR` / Rango Numérico):** Determina colapso inminente si el disco libre cae por debajo del 5.0% **O** la CPU supera el 95.0%.
8. **Optimización de S.O. (`AND`):** Alerta si el entorno es "Linux" y maneja una sobrecarga de más de 25 servicios activos.

---

## 💻 Flujo de Ejecución del Programa
1. **`main.py`** arranca y cede el control a **`menu.py`**.
2. El usuario selecciona la opción `1` para iniciar el diagnóstico.
3. **`inputs.py`** pide los datos secuencialmente y se apoya en **`validaciones.py`** para asegurar que los porcentajes estén entre 0 y 100, y las cadenas sean válidas.
4. Los datos validados se envían a **`calculos.py`**, el cual interactúa con **`reglas.py`** para procesar la lógica de las listas.
5. Las listas de alertas y recomendaciones resultantes son capturadas por **`output.py`** para imprimirlas en la terminal de forma amigable.

---

## 📋 Ejemplo de Ejecución en Consola

### Datos ingresados de prueba:
- **Nombre del servidor:** sv-produccion-utn
- **CPU:** 90.0
- **RAM:** 92.0
- **Espacio Libre en Disco:** 50.0
- **Sistema Operativo:** Windows Server
- **Firewall:** Desactivado
- **Servicios activos:** 5
- **Tráfico de Red (MB/s):** 120.0

### Resultado del Reporte Técnico generado:
```text
============================================================
DIAGNOSTICO DEL SERVIDOR: sv-produccion-utn
============================================================
Estado General: Alerta crtica / Revision
------------------------------------------------------------
Problemas detectados:
- Uso critico de recursos principales (CPU/RAM).
  💡 Recomendación: Reiniciar servicios pesados o escalar hardware.
- Servidor Windows expuesto sin Firewall activo
  💡 Recomendación: Habilitar el firewall del sistema de inmediato

============================================================