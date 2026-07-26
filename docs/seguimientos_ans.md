# Seguimientos de Informes ANS

## 1. Objetivo

Automatizar la generación de informes de seguimiento ANS a partir de un archivo Excel, organizando los pedidos por grupo operativo, producto, actividad y estado.

El sistema genera correos HTML profesionales y los prepara en Microsoft Outlook para su validación y envío.

---

## 2. Problema que resuelve

Antes, la elaboración del informe requería más de una hora de trabajo manual:

- Abrir y filtrar el archivo Excel.
- Identificar pedidos vencidos y en alerta.
- Separar la información por grupos.
- Calcular cantidades y porcentajes.
- Construir tablas.
- Redactar observaciones.
- Preparar los correos en Outlook.

Con la automatización, el proceso tarda aproximadamente cinco minutos.

> **Reducción estimada del tiempo operativo: 92 %.**

---

## 3. Flujo del proceso

```text
Archivo Excel FENIX
        ↓
Validación de estructura
        ↓
Lectura y filtrado de datos
        ↓
Clasificación por grupo, producto y actividad
        ↓
Cálculo de estados ANS
        ↓
Generación de KPIs y tablas
        ↓
Creación del correo HTML
        ↓
Apertura del correo en Microsoft Outlook
```

---

## 4. Estados utilizados

El sistema clasifica automáticamente cada pedido en uno de los siguientes estados:

| Estado | Descripción |
|---|---|
| A TIEMPO | Pedido dentro del plazo ANS. |
| ALERTA | Pedido próximo a vencer. |
| ALERTA 0 DÍAS | Pedido que debe gestionarse durante la jornada. |
| VENCIDO | Pedido que superó la fecha límite del ANS. |

---

## 5. Estructura del correo

Cada correo conserva la siguiente estructura:

1. Encabezado.
2. Información general.
3. KPIs ejecutivos.
4. Instrucciones de gestión.
5. Producto.
6. Actividad.
7. Resumen por estados.
8. Detalle de pedidos.
9. Observaciones.
10. Firma.

Los KPIs muestran de forma inmediata la cantidad de pedidos:

- Vencidos.
- En alerta 0 días.
- En alerta.
- A tiempo.

---

## 6. Componentes principales

```text
modules/informe_ans/
│
├── config/
│   ├── columnas.py
│   ├── correos.py
│   ├── grupos.py
│   └── parametros.py
│
├── entrada/
│
├── salida/
│   ├── correos/
│   ├── excel/
│   └── html/
│
├── src/
│   ├── agrupador.py
│   ├── comparador.py
│   ├── generador_correo.py
│   ├── generador_html.py
│   ├── historial.py
│   ├── lector_excel.py
│   ├── outlook.py
│   └── validador.py
│
├── templates/
│   ├── correo_ans.html
│   ├── footer.html
│   └── firma.html
│
├── controller.py
├── models.py
└── runner.py
```

---

## 7. Responsabilidad de cada componente

### `validador.py`

Verifica que el archivo exista y que contenga las columnas requeridas.

### `lector_excel.py`

Lee el archivo FENIX y aplica los filtros definidos.

### `agrupador.py`

Organiza los registros por grupo operativo, producto y actividad.

### `generador_html.py`

Construye los KPIs, el resumen por estados y la tabla de detalle.

### `correo_ans.html`

Define la estructura visual principal del correo.

### `footer.html`

Genera las observaciones, instrucciones finales y firma.

### `outlook.py`

Crea el correo en Microsoft Outlook con el asunto, destinatarios y contenido HTML.

### `runner.py`

Coordina la ejecución completa del proceso.

---

## 8. Beneficios

- Reduce significativamente el tiempo de elaboración.
- Disminuye errores manuales.
- Estandariza todos los correos.
- Prioriza automáticamente vencidos y alertas.
- Facilita la validación operativa.
- Permite generar varios informes en una sola ejecución.
- Se encuentra integrado al Launcher ELITE.
- Deja los correos preparados en Outlook antes del envío.

---

## 9. Integración con Launcher ELITE

El módulo está integrado dentro del Launcher ELITE para que el usuario no tenga que utilizar la terminal.

El flujo para el usuario es:

```text
Abrir Launcher ELITE
        ↓
Seleccionar Generador Informe ANS
        ↓
Cargar o validar el archivo
        ↓
Ejecutar el proceso
        ↓
Revisar los correos generados en Outlook
```

---

## 10. Cómo explicarlo en 30 segundos

> El Seguimiento de Informes ANS es una automatización desarrollada en Python que toma el archivo FENIX, valida su estructura, filtra la información, clasifica los pedidos por grupo, producto, actividad y estado ANS, genera indicadores y tablas, y finalmente crea los correos en Outlook listos para revisar y enviar. Un proceso que antes tardaba más de una hora ahora se realiza aproximadamente en cinco minutos.

---

## 11. Preguntas frecuentes

### ¿El sistema envía los correos automáticamente?

Actualmente los correos se generan y se abren en Outlook para revisión antes del envío.

### ¿Se modifican los datos del archivo original?

No. El archivo original se utiliza como fuente de información y no se altera.

### ¿Qué sucede si falta una columna?

El validador detiene el proceso e informa cuáles columnas hacen falta.

### ¿Cómo se calculan los estados?

Se utilizan las fechas límite, los días restantes y las reglas ANS definidas para el proceso.

### ¿Se pueden agregar nuevos grupos?

Sí. Los grupos, productos y actividades se administran desde los archivos de configuración.

### ¿Por qué se genera HTML?

Porque permite construir un correo profesional, con KPIs, colores, tablas y compatibilidad con Microsoft Outlook.

---
# DataSuite — Módulo Seguimiento ANS

## 1. Descripción general

**DataSuite** es la plataforma de automatización donde se encuentran integrados diferentes desarrollos operativos.

Dentro de esta plataforma, el módulo **Seguimiento ANS** permite generar, revisar y enviar correos de seguimiento a partir del archivo FENIX.

El objetivo principal es reducir el trabajo manual y estandarizar la preparación de los informes ANS.

---

## 2. Encabezado principal de DataSuite

En la parte superior se presenta la identidad de la aplicación:

- **DataSuite**
- **Plataforma de Automatización**
- **Enterprise Automation Suite**
- **Versión 1.0**

Este encabezado identifica la solución y la versión actualmente utilizada.

---

## 3. Menú lateral de módulos

El menú ubicado en el lado izquierdo permite navegar entre los diferentes desarrollos integrados en DataSuite.

Para este proceso se selecciona:

```text
Seguimiento ANS
```

Cuando el módulo está activo:

- El nombre aparece resaltado.
- Se muestra una barra vertical de color.
- El contenido central cambia a la interfaz de Seguimiento ANS.

---

## 4. Encabezado del módulo

Al ingresar al módulo se presenta:

```text
Seguimiento ANS
Generación, revisión y envío controlado de correos de seguimiento ANS.
```

Este encabezado indica la función principal del desarrollo.

---

## 5. Archivo de entrada

La sección **Archivo de entrada** muestra la ruta del archivo utilizado por el proceso.

Ejemplo:

```text
modules/informe_ans/entrada/FENIX_ANS.xlsx
```

El sistema utiliza este archivo como fuente de información.

### Funciones de esta sección

- Mostrar la ruta del archivo FENIX.
- Confirmar cuál archivo será procesado.
- Evitar que el usuario seleccione un archivo incorrecto.
- Mantener una estructura controlada dentro del proyecto.

El archivo debe estar ubicado en:

```text
modules/informe_ans/entrada/
```

---

## 6. Estado del módulo

El panel **Estado del módulo** valida que los elementos necesarios estén disponibles antes de ejecutar el proceso.

Se verifican los siguientes componentes:

| Componente | Función |
|---|---|
| Archivo FENIX | Confirma que el archivo de entrada existe. |
| Plantilla principal | Verifica la plantilla general del correo. |
| Plantilla footer | Verifica el bloque de observaciones y firma. |
| Carpeta de salida | Confirma que existe la ruta donde se guardan los resultados. |
| Motor Seguimiento ANS | Valida que el módulo pueda ejecutar el proceso. |

Cuando todos los elementos están disponibles, el sistema se encuentra listo para operar.

---

## 7. Sección de proceso

La sección **Proceso** contiene los controles utilizados para ejecutar el módulo.

### 7.1. Modo de ejecución

El sistema dispone de dos modos:

#### Modo revisión

```text
Modo revisión
```

Características:

- Genera los correos.
- Los abre en Microsoft Outlook.
- Permite revisar destinatarios, asunto y contenido.
- No realiza el envío automático.

Este modo es recomendado para pruebas, validaciones y controles previos.

#### Envío automático

```text
Envío automático
```

Características:

- Genera los correos.
- Utiliza la configuración definida para cada grupo.
- Realiza el envío sin requerir revisión manual.

Este modo debe utilizarse cuando las reglas, destinatarios y plantillas hayan sido validados.

---

### 7.2. Procesar únicamente el primer correo

Este control permite limitar la ejecución a un solo correo.

Su finalidad es:

- Probar el proceso.
- Validar el diseño HTML.
- Revisar el contenido en Outlook.
- Evitar generar todos los correos durante una prueba.

Cuando está desactivado, el sistema procesa todos los grupos configurados.

---

### 7.3. Botón Generar correos

El botón:

```text
Generar correos
```

inicia el proceso completo.

Al presionarlo, el sistema:

1. Valida el archivo FENIX.
2. Lee la información.
3. Filtra la subzona configurada.
4. Agrupa los pedidos.
5. Calcula los estados ANS.
6. Genera los KPIs.
7. Construye las tablas.
8. Genera los archivos HTML.
9. Prepara o envía los correos según el modo seleccionado.

---

## 8. Consola de resultados

La consola muestra el resultado de la ejecución.

Ejemplo:

```text
Correos generados : 4
Total grupos      : 4
Total pedidos     : 598
Tiempo ejecución  : 9.22 segundos
Ruta de salida    : modules/informe_ans/salida/html
```

### Información presentada

| Resultado | Descripción |
|---|---|
| Correos generados | Cantidad de correos creados. |
| Total grupos | Número de grupos procesados. |
| Total pedidos | Cantidad total de registros incluidos. |
| Tiempo de ejecución | Duración total del proceso. |
| Ruta de salida | Ubicación de los archivos HTML generados. |

La consola permite comprobar rápidamente si la ejecución terminó correctamente.

---

## 9. Estado general del sistema

En la parte inferior izquierda se muestra:

```text
Sistema listo
```

Este mensaje indica que DataSuite está disponible y preparado para ejecutar módulos.

En la parte inferior derecha aparece la identificación institucional de la solución.

---

## 10. Flujo operativo dentro de DataSuite

```text
Abrir DataSuite
        ↓
Seleccionar Seguimiento ANS
        ↓
Verificar archivo de entrada
        ↓
Confirmar estado del módulo
        ↓
Seleccionar modo de ejecución
        ↓
Activar o desactivar prueba de un solo correo
        ↓
Presionar Generar correos
        ↓
Revisar resultados en la consola
        ↓
Validar correos en Outlook o confirmar envío
```

---

## 11. Beneficios de la integración en DataSuite

- Evita ejecutar comandos desde la terminal.
- Centraliza el proceso en una sola aplicación.
- Reduce errores de operación.
- Permite seleccionar el modo de ejecución.
- Facilita las pruebas controladas.
- Presenta validaciones antes de procesar.
- Muestra resultados en tiempo real.
- Permite integrar el desarrollo con otros módulos empresariales.
- Reduce un proceso de más de una hora a pocos minutos.

---

## 12. Explicación breve

> El módulo Seguimiento ANS se encuentra integrado en DataSuite para centralizar la generación de los correos de seguimiento. Desde la interfaz se valida el archivo FENIX, se selecciona el modo de ejecución, se inicia el proceso y se visualizan los resultados. El sistema procesa los pedidos, genera los indicadores y construye los correos en Outlook, reduciendo significativamente el tiempo operativo.

---

## 13. Resumen de las partes de la pantalla

| Sección | Propósito |
|---|---|
| Encabezado DataSuite | Identifica la plataforma y su versión. |
| Menú lateral | Permite ingresar al módulo Seguimiento ANS. |
| Encabezado del módulo | Describe la función del desarrollo. |
| Archivo de entrada | Muestra el archivo FENIX que será procesado. |
| Estado del módulo | Valida archivos, plantillas, carpetas y motor. |
| Modo de ejecución | Define revisión o envío automático. |
| Procesar primer correo | Permite realizar una prueba controlada. |
| Generar correos | Inicia la automatización. |
| Consola | Presenta resultados, tiempos y ruta de salida. |
| Estado del sistema | Confirma que DataSuite está disponible. |


----

## 12. Próximas mejoras

- Comparación entre primer y segundo corte.
- Identificación de pedidos que continúan sin gestión.
- Histórico de ejecuciones.
- Envío automático controlado.
- Alertas por reincidencia.
- Registro de fecha y hora de los cambios.
