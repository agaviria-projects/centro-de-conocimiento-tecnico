# DataSuite — Módulo Seguimiento ANS

## 1. Descripción general

**Seguimiento ANS** es un módulo desarrollado en Python e integrado en **DataSuite** para automatizar la generación, revisión y envío controlado de correos de seguimiento de Acuerdos de Nivel de Servicio —ANS—.

El módulo utiliza como fuente el archivo **FENIX_ANS.xlsx**, valida su estructura, filtra la información operativa, clasifica los pedidos y genera correos HTML profesionales compatibles con Microsoft Outlook.

Su propósito es transformar un procedimiento manual, repetitivo y propenso a errores en un flujo estandarizado, trazable y ejecutable desde una interfaz gráfica.

---

## 2. Objetivo del desarrollo

Automatizar el procesamiento del archivo FENIX para:

- Validar que la fuente de información sea correcta.
- Filtrar los registros correspondientes a la operación configurada.
- Organizar los pedidos por grupo, producto y actividad.
- Clasificar los registros según su estado ANS.
- Calcular indicadores ejecutivos.
- Construir tablas de resumen y detalle.
- Generar correos HTML con una presentación uniforme.
- Permitir la revisión previa o el envío automático desde Outlook.
- Mostrar los resultados de la ejecución dentro de DataSuite.

---

## 3. Problema que resuelve

Antes de implementar la automatización, la elaboración del seguimiento requería realizar manualmente actividades como:

1. Abrir el archivo Excel.
2. Aplicar filtros operativos.
3. Separar la información por grupos.
4. Identificar pedidos vencidos y próximos a vencer.
5. Calcular cantidades y porcentajes.
6. Construir tablas.
7. Redactar observaciones.
8. Preparar cada correo en Outlook.
9. Revisar destinatarios, asunto y contenido.
10. Repetir el mismo procedimiento para cada grupo operativo.

Este proceso podía tardar más de una hora.

Con **Seguimiento ANS**, el motor de procesamiento puede completar la generación en segundos y el ciclo operativo completo, incluida la revisión, puede realizarse en pocos minutos.

> **Resultado esperado:** reducción considerable del tiempo operativo, mayor uniformidad y menor riesgo de errores manuales.

---

## 4. Alcance funcional

El módulo cubre las siguientes etapas:

```text
Archivo FENIX
      ↓
Validación de existencia y estructura
      ↓
Lectura del archivo Excel
      ↓
Filtrado de la información
      ↓
Agrupación por grupo, producto y actividad
      ↓
Clasificación por estado ANS
      ↓
Cálculo de KPIs
      ↓
Construcción de tablas
      ↓
Generación del correo HTML
      ↓
Revisión o envío mediante Outlook
      ↓
Presentación de resultados en DataSuite
```

El archivo original se utiliza únicamente como fuente de información y no es modificado por el proceso.

---

## 5. Fuente de información

El módulo procesa el archivo:

```text
modules/informe_ans/entrada/FENIX_ANS.xlsx
```

La ubicación controlada del archivo permite:

- Evitar que se procese una fuente incorrecta.
- Mantener una estructura estándar del proyecto.
- Facilitar las validaciones automáticas.
- Simplificar el uso para el usuario final.
- Conservar la trazabilidad del proceso.

---

## 6. Columnas requeridas

Para ejecutar correctamente el proceso, el archivo debe contener las columnas definidas por el módulo.

Entre las columnas utilizadas se encuentran:

```text
PEDIDO
FECHA_INICIO_ANS
DIRECCION
MUNICIPIO
TIPO_DIRECCION
CONCEPTO
ACTIVIDAD
PRODUCTO
DIAS_PACTADOS
FECHA_LIMITE_ANS
DIAS_RESTANTES
ESTADO
SUBZONA
```

Si falta una columna obligatoria, el proceso debe detenerse e informar la inconsistencia antes de generar los correos.

---

## 7. Clasificación de los estados ANS

Cada pedido se organiza de acuerdo con su condición operativa.

| Estado | Interpretación |
|---|---|
| **A TIEMPO** | El pedido continúa dentro del plazo establecido. |
| **ALERTA** | El pedido se aproxima a su fecha límite. |
| **ALERTA 0 DÍAS** | El pedido debe gestionarse durante la jornada actual. |
| **VENCIDO** | El pedido superó el plazo definido en el ANS. |

Estos estados se utilizan en:

- Tarjetas de indicadores.
- Resumen por estados.
- Detalle de pedidos.
- Observaciones automáticas.
- Priorización de la gestión operativa.

---

## 8. Reglas de agrupación

El sistema organiza los registros por grupos operativos, productos y actividades previamente configurados.

La configuración evita que las reglas queden dispersas dentro del código y permite administrar de forma centralizada:

- Grupos.
- Productos.
- Actividades.
- Destinatarios.
- Asuntos de correo.
- Reglas de presentación.

Ejemplo conceptual:

```text
Grupo operativo
    └── Producto
          └── Actividad
                └── Pedidos clasificados por estado
```

Cada grupo configurado produce un correo independiente o un correo consolidado, según las reglas definidas.

---

## 9. Arquitectura del módulo

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
│   └── FENIX_ANS.xlsx
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

Esta estructura separa la configuración, la lógica de negocio, las plantillas, las entradas y las salidas.

---

## 10. Responsabilidad de los componentes

### 10.1. `config/parametros.py`

Centraliza las rutas y parámetros generales del módulo.

Ejemplos:

- Ruta base.
- Archivo de entrada.
- Carpetas de salida.
- Subzona que debe procesarse.
- Opciones generales de ejecución.

---

### 10.2. `config/columnas.py`

Define las columnas obligatorias y los nombres utilizados durante el procesamiento.

Su función es impedir que la lógica dependa de nombres escritos repetidamente en diferentes archivos.

---

### 10.3. `config/grupos.py`

Contiene las reglas para clasificar la información por:

- Grupo operativo.
- Producto.
- Actividad.

Permite modificar la matriz de procesamiento sin alterar el flujo principal.

---

### 10.4. `config/correos.py`

Administra la configuración relacionada con:

- Destinatarios.
- Copias.
- Asuntos.
- Reglas particulares de envío.

---

### 10.5. `src/validador.py`

Comprueba que:

- El archivo FENIX exista.
- La extensión sea correcta.
- La hoja requerida esté disponible.
- Las columnas obligatorias estén presentes.
- Los componentes necesarios para ejecutar el módulo estén disponibles.

Si una validación falla, el proceso se detiene antes de generar resultados incorrectos.

---

### 10.6. `src/lector_excel.py`

Lee el archivo Excel y prepara los datos para el procesamiento.

Entre sus responsabilidades se encuentran:

- Cargar la hoja configurada.
- Normalizar valores.
- Aplicar filtros.
- Conservar únicamente los registros correspondientes a la operación requerida.
- Entregar un conjunto de datos limpio al agrupador.

---

### 10.7. `src/agrupador.py`

Organiza los registros de acuerdo con las reglas de negocio.

Sus funciones principales son:

- Separar la información por grupo.
- Identificar productos.
- Identificar actividades.
- Consolidar registros relacionados.
- Preparar la información que será utilizada en cada correo.

---

### 10.8. `src/generador_html.py`

Construye la representación visual del informe.

Genera:

- Información general.
- KPIs ejecutivos.
- Resumen por estados.
- Tabla de detalle.
- Bloques de producto y actividad.
- Observaciones.
- Contenido compatible con Outlook.

---

### 10.9. `src/generador_correo.py`

Organiza los elementos necesarios para cada mensaje:

- Destinatarios.
- Asunto.
- Contenido HTML.
- Grupo procesado.
- Datos utilizados.
- Opciones de revisión o envío.

---

### 10.10. `src/outlook.py`

Gestiona la integración con Microsoft Outlook.

Según el modo seleccionado, puede:

- Crear el correo.
- Cargar destinatarios.
- Asignar el asunto.
- Insertar el contenido HTML.
- Abrir el mensaje para revisión.
- Enviar el correo automáticamente.

---

### 10.11. `src/comparador.py`

Está destinado a comparar diferentes cortes de información.

Puede utilizarse para identificar:

- Pedidos que continúan pendientes.
- Pedidos que cambiaron de estado.
- Registros nuevos.
- Registros gestionados entre dos ejecuciones.

---

### 10.12. `src/historial.py`

Administra la conservación de información histórica para futuras comparaciones y trazabilidad.

---

### 10.13. `templates/correo_ans.html`

Define la estructura visual principal del correo.

Contiene la distribución de:

- Encabezado.
- Bloques informativos.
- Indicadores.
- Tablas.
- Secciones de gestión.

---

### 10.14. `templates/footer.html`

Define el bloque final del correo, incluyendo:

- Observaciones.
- Recomendaciones.
- Mensajes de prioridad.
- Información de cierre.

---

### 10.15. `templates/firma.html`

Contiene la firma institucional utilizada en los correos.

---

### 10.16. `models.py`

Define las estructuras de datos utilizadas para transferir información entre los componentes.

Su propósito es mantener contratos claros entre:

- Lectura.
- Agrupación.
- Generación.
- Envío.
- Resultado de la ejecución.

---

### 10.17. `controller.py`

Conecta la interfaz de DataSuite con el motor de Seguimiento ANS.

Recibe las opciones seleccionadas por el usuario y ejecuta el flujo correspondiente.

---

### 10.18. `runner.py`

Es el coordinador principal del proceso.

Ejecuta de forma ordenada:

1. Validación.
2. Lectura.
3. Filtrado.
4. Agrupación.
5. Construcción de informes.
6. Generación HTML.
7. Apertura o envío de correos.
8. Consolidación de resultados.

---

## 11. Estructura del correo generado

Cada correo conserva un orden uniforme:

1. Encabezado.
2. Saludo inicial.
3. Información general.
4. KPIs ejecutivos.
5. Instrucciones de gestión.
6. Producto.
7. Actividad.
8. Resumen por estados.
9. Detalle de pedidos.
10. Observaciones.
11. Firma.

Esta estructura permite que la información sea comprendida rápidamente tanto a nivel ejecutivo como operativo.

---

## 12. Indicadores del correo

Los KPIs muestran la cantidad de pedidos clasificados como:

- Vencidos.
- Alerta 0 días.
- Alerta.
- A tiempo.

La finalidad de estas tarjetas es ofrecer una lectura inmediata del estado general del grupo antes de revisar el detalle.

---

## 13. Priorización operativa

El correo debe facilitar la atención en el siguiente orden:

```text
1. VENCIDOS
2. ALERTA 0 DÍAS
3. ALERTA
4. A TIEMPO
```

Esta priorización ayuda a dirigir la gestión hacia los registros con mayor riesgo de incumplimiento.

---

# Interfaz del módulo en DataSuite

## 14. Encabezado de DataSuite

En la parte superior se presenta la identidad de la plataforma:

```text
DataSuite
Plataforma de Automatización
Enterprise Automation Suite | Versión 1.0
```

Este encabezado permite identificar la aplicación y la versión utilizada.

---

## 15. Menú lateral

El menú lateral centraliza el acceso a los desarrollos integrados.

Para ingresar al proceso se selecciona:

```text
Seguimiento ANS
```

Cuando el módulo se encuentra activo:

- El nombre aparece resaltado.
- Se muestra una barra vertical de selección.
- El área central cambia a la interfaz del módulo.

---

## 16. Encabezado del módulo

La interfaz presenta el título:

```text
Seguimiento ANS
```

Y la descripción:

```text
Generación, revisión y envío controlado de correos de seguimiento ANS.
```

Este bloque resume la función principal del desarrollo.

---

## 17. Sección Archivo de entrada

Muestra la ruta exacta del archivo que será procesado.

Ejemplo:

```text
C:\...\modules\informe_ans\entrada\FENIX_ANS.xlsx
```

### Finalidad

- Confirmar la fuente de datos.
- Evitar selecciones incorrectas.
- Facilitar el diagnóstico de rutas.
- Mantener el archivo dentro de una ubicación controlada.

---

## 18. Panel Estado del módulo

Antes de ejecutar, el sistema valida los componentes esenciales.

| Componente | Validación |
|---|---|
| Archivo FENIX | Confirma que la fuente de entrada exista. |
| Plantilla principal | Verifica el diseño general del correo. |
| Plantilla footer | Comprueba el bloque final del mensaje. |
| Carpeta de salida | Confirma dónde se almacenarán los resultados. |
| Motor Seguimiento ANS | Verifica que el proceso pueda ejecutarse. |

Cuando todos los elementos se encuentran disponibles, el módulo está listo para operar.

---

## 19. Sección Proceso

La sección **Proceso** contiene las opciones que controlan la ejecución.

### 19.1. Modo revisión

En este modo el sistema:

- Genera los correos.
- Los abre en Microsoft Outlook.
- Permite revisar destinatarios.
- Permite validar el asunto.
- Permite inspeccionar el contenido.
- No realiza el envío automático.

Es el modo recomendado durante pruebas y validaciones.

---

### 19.2. Envío automático

En este modo el sistema:

- Genera los correos.
- Carga los destinatarios configurados.
- Construye el asunto y el contenido.
- Envía los mensajes sin revisión manual.

Debe utilizarse únicamente cuando las reglas, plantillas y destinatarios ya hayan sido validados.

---

### 19.3. Procesar únicamente el primer correo

Esta opción permite ejecutar una prueba controlada.

Cuando está activada:

- Solo se procesa el primer grupo.
- Se genera un único correo.
- Se puede revisar el diseño.
- Se evita abrir o enviar todos los mensajes.

Cuando está desactivada, se procesan todos los grupos configurados.

---

### 19.4. Botón Generar correos

El botón inicia el flujo completo.

Al presionarlo, el sistema:

1. Valida la fuente.
2. Lee el archivo.
3. Aplica los filtros.
4. Agrupa los pedidos.
5. Clasifica los estados.
6. Calcula los indicadores.
7. Construye las tablas.
8. Genera los HTML.
9. Prepara o envía los correos.
10. Presenta el resultado en la consola.

---

## 20. Consola de resultados

La consola permite verificar rápidamente el resultado de la ejecución.

Ejemplo:

```text
Correos generados : 4
Total grupos      : 4
Total pedidos     : 598
Tiempo ejecución  : 9.22 segundos
Ruta de salida    : modules/informe_ans/salida/html
```

| Resultado | Significado |
|---|---|
| Correos generados | Cantidad de mensajes creados. |
| Total grupos | Número de grupos procesados. |
| Total pedidos | Registros incluidos en los informes. |
| Tiempo de ejecución | Duración del motor de procesamiento. |
| Ruta de salida | Ubicación de los archivos HTML generados. |

> Los valores mostrados dependen del contenido del archivo utilizado en cada ejecución.

---

## 21. Estado general de DataSuite

En la barra inferior se presenta el mensaje:

```text
Sistema listo
```

Este estado indica que la plataforma se encuentra disponible para ejecutar sus módulos.

---

## 22. Flujo de uso desde la interfaz

```text
Abrir DataSuite
        ↓
Seleccionar Seguimiento ANS
        ↓
Verificar el archivo de entrada
        ↓
Confirmar el estado del módulo
        ↓
Seleccionar el modo de ejecución
        ↓
Definir si se procesará un solo correo
        ↓
Presionar Generar correos
        ↓
Revisar la consola
        ↓
Validar los mensajes en Outlook
        ↓
Enviar o confirmar el envío automático
```

---

## 23. Archivos de salida

El módulo puede generar resultados en las siguientes carpetas:

```text
modules/informe_ans/salida/html/
modules/informe_ans/salida/excel/
modules/informe_ans/salida/correos/
```

### `salida/html`

Almacena las versiones HTML de los informes.

### `salida/excel`

Puede utilizarse para guardar archivos de respaldo o información procesada.

### `salida/correos`

Puede conservar elementos relacionados con la preparación de los mensajes.

---

## 24. Controles de seguridad y calidad

El desarrollo incorpora controles para reducir errores operativos:

- Validación de existencia del archivo.
- Validación de columnas obligatorias.
- Rutas centralizadas.
- Reglas de grupos separadas del motor.
- Plantillas HTML independientes.
- Modo revisión.
- Prueba con un solo correo.
- Consola de resultados.
- Conservación del archivo original.
- Separación entre entrada y salida.

---

## 25. Beneficios del desarrollo

### Beneficios operativos

- Reduce el tiempo de elaboración.
- Evita repetir filtros manuales.
- Genera varios informes en una sola ejecución.
- Facilita la priorización de pedidos.
- Centraliza el flujo dentro de DataSuite.

### Beneficios de calidad

- Estandariza los correos.
- Disminuye errores de transcripción.
- Mantiene una estructura visual uniforme.
- Valida la información antes de procesarla.
- Permite revisar antes de enviar.

### Beneficios técnicos

- Arquitectura modular.
- Separación de responsabilidades.
- Configuración centralizada.
- Plantillas reutilizables.
- Facilidad para agregar nuevos grupos.
- Base preparada para históricos y comparaciones.

---

## 26. Diferencia entre tiempo técnico y tiempo operativo

Es importante diferenciar dos mediciones:

### Tiempo técnico

Es el tiempo utilizado por el motor para:

- Leer el archivo.
- Filtrar los datos.
- Agrupar los registros.
- Generar los HTML.
- Preparar los correos.

Este tiempo puede ser de pocos segundos, como se observa en la consola.

### Tiempo operativo

Incluye además:

- Ubicar o actualizar el archivo.
- Abrir DataSuite.
- Ejecutar el módulo.
- Revisar los correos.
- Confirmar la información.
- Realizar el envío.

Por esta razón, puede afirmarse que el ciclo completo tarda pocos minutos, aunque el motor se ejecute en segundos.

---

## 27. Limitaciones actuales

El funcionamiento depende de:

- Que el archivo FENIX se encuentre en la ruta configurada.
- Que las columnas mantengan los nombres esperados.
- Que las reglas de grupos estén actualizadas.
- Que Outlook esté instalado y configurado.
- Que los destinatarios hayan sido validados.
- Que las plantillas HTML sean compatibles con Outlook.

---

## 28. Próximas mejoras

- Comparación entre primer y segundo corte.
- Comparación entre cortes posteriores.
- Identificación de pedidos sin gestión.
- Registro histórico de ejecuciones.
- Alertas por reincidencia.
- Registro de cambios de estado.
- Conservación de fecha y hora de cada corte.
- Movimiento automático de archivos procesados.
- Reporte de diferencias entre ejecuciones.
- Mayor trazabilidad del envío automático.

---

## 29. Cómo explicarlo en 30 segundos

> Seguimiento ANS es un módulo integrado en DataSuite que toma el archivo FENIX, valida su estructura, filtra la información y organiza los pedidos por grupo, producto, actividad y estado. Después calcula indicadores, construye tablas y genera correos HTML profesionales en Outlook. El proceso que antes requería más de una hora de trabajo manual ahora puede ejecutarse en pocos minutos, con mayor control y menor riesgo de errores.

---

## 30. Explicación técnica breve

> El desarrollo utiliza una arquitectura modular en Python. La configuración administra rutas, columnas, grupos y correos; el motor valida y lee el Excel; el agrupador aplica las reglas de negocio; el generador HTML construye los indicadores y tablas; y el componente de Outlook crea o envía los mensajes. DataSuite actúa como interfaz para ejecutar el proceso sin utilizar la terminal.

---

## 31. Configuración de destinatarios y envío de correos

La configuración de correos del módulo se administra principalmente desde el archivo:

```text
modules/informe_ans/config/correos.py
```

Este archivo permite controlar:

- Los destinatarios utilizados durante las pruebas.
- Los destinatarios reales de producción.
- Las personas que recibirán copia.
- Las copias ocultas.
- La prioridad de los mensajes.
- La compatibilidad con configuraciones anteriores.

Es importante diferenciar dos controles independientes:

> **`MODO_PRUEBA` controla quién recibe el correo.**

> **DataSuite controla si Outlook abre el correo o lo envía automáticamente.**

---

### 31.1. Configuración general recomendada

```python
# ==========================================================
# MODO DE DESTINATARIOS
# ==========================================================

# True:
# Usa DESTINATARIOS_PRUEBA y COPIA_PRUEBA.
#
# False:
# Usa DESTINATARIOS y COPIAS según cada grupo.
#
# IMPORTANTE:
# Esta variable no determina si Outlook abre o envía.
# Esa acción se controla desde la interfaz de DataSuite.

MODO_PRUEBA = True


# ==========================================================
# DESTINATARIOS DE PRUEBA
# ==========================================================

DESTINATARIOS_PRUEBA = [
    "d.leon@eliteingenieros.com.co",
]


COPIA_PRUEBA = [
    "h.gaviria@eliteingenieros.com.co",
]


# ==========================================================
# DESTINATARIOS DE PRODUCCIÓN
# ==========================================================

DESTINATARIOS = {

    "PUNTOS DE CONEXIÓN": [
        "l.perez@eliteingenieros.com.co",
        "a.villegas@eliteingenieros.com.co",
    ],

    "PREPAGO_HV_ARTER": [
        "l.perez@eliteingenieros.com.co",
        "a.villegas@eliteingenieros.com.co",
    ],

    "MOVIMIENTO DE REDES": [
        "l.perez@eliteingenieros.com.co",
        "a.villegas@eliteingenieros.com.co",
    ],

    "PARTICULARES": [
        "l.perez@eliteingenieros.com.co",
        "a.villegas@eliteingenieros.com.co",
    ],

}


# ==========================================================
# COPIAS DE PRODUCCIÓN
# ==========================================================

COPIAS = {

    "PUNTOS DE CONEXIÓN": [
        "c.oliveros@eliteingenieros.com.co",
        "j.barbosa@eliteingenieros.com.co",
    ],

    "PREPAGO_HV_ARTER": [
        "c.oliveros@eliteingenieros.com.co",
        "j.barbosa@eliteingenieros.com.co",
    ],

    "MOVIMIENTO DE REDES": [
        "c.oliveros@eliteingenieros.com.co",
        "j.barbosa@eliteingenieros.com.co",
    ],

    "PARTICULARES": [
        "c.oliveros@eliteingenieros.com.co",
        "j.barbosa@eliteingenieros.com.co",
    ],

}


# ==========================================================
# COPIA OCULTA
# ==========================================================

COPIA_OCULTA = [
]


# ==========================================================
# PRIORIDAD DEL CORREO
# ==========================================================

# 0 = Baja
# 1 = Normal
# 2 = Alta

IMPORTANCIA = 2


# ==========================================================
# CONFIGURACIÓN LEGADA
# ==========================================================

# Estas variables se conservan por compatibilidad con
# versiones anteriores del módulo.
#
# Actualmente, DataSuite controla si el mensaje se abre
# para revisión o se envía automáticamente.

MOSTRAR_CORREO = True

ENVIAR_AUTOMATICAMENTE = False
```

---

### 31.2. Función de `MODO_PRUEBA`

La variable:

```python
MODO_PRUEBA
```

determina cuáles destinatarios serán utilizados por el sistema.

No controla la apertura ni el envío del mensaje.

---

#### `MODO_PRUEBA = True`

Cuando se configura:

```python
MODO_PRUEBA = True
```

el sistema utiliza únicamente:

```python
DESTINATARIOS_PRUEBA
COPIA_PRUEBA
```

Ejemplo:

```python
DESTINATARIOS_PRUEBA = [
    "d.leon@eliteingenieros.com.co",
]

COPIA_PRUEBA = [
    "h.gaviria@eliteingenieros.com.co",
]
```

Con esta configuración, todos los informes se dirigirán a los destinatarios de prueba, sin importar el grupo procesado.

Esto aplica para:

- Puntos de Conexión.
- Prepago HV Arter.
- Movimiento de Redes.
- Particulares.

El contenido del correo continúa correspondiendo al grupo operativo, pero los destinatarios serán reemplazados por las direcciones de prueba.

Este modo permite:

- Validar el diseño HTML.
- Revisar el asunto.
- Confirmar los indicadores.
- Verificar las tablas.
- Revisar las observaciones.
- Evitar envíos accidentales a producción.

---

#### `MODO_PRUEBA = False`

Cuando se configura:

```python
MODO_PRUEBA = False
```

el sistema utiliza:

```python
DESTINATARIOS
COPIAS
```

En este modo, cada informe utiliza los destinatarios configurados para su grupo operativo.

Ejemplo:

```python
DESTINATARIOS = {

    "PUNTOS DE CONEXIÓN": [
        "responsable_puntos@empresa.com",
    ],

    "PARTICULARES": [
        "responsable_particulares@empresa.com",
    ],

}
```

Esto significa que:

- Puntos de Conexión utiliza sus destinatarios.
- Prepago HV Arter utiliza sus destinatarios.
- Movimiento de Redes utiliza sus destinatarios.
- Particulares utiliza sus destinatarios.

Este es el modo correspondiente a producción.

---

### 31.3. Modo de ejecución seleccionado en DataSuite

La interfaz de DataSuite controla la acción que realizará Microsoft Outlook.

Las opciones disponibles son:

```text
Modo revisión
Envío automático
```

Esta selección funciona de manera independiente de `MODO_PRUEBA`.

---

### 31.4. Modo revisión

Cuando se selecciona en DataSuite:

```text
Modo revisión
```

Outlook ejecuta conceptualmente:

```python
mail.Display()
```

El sistema realiza las siguientes acciones:

1. Genera el correo.
2. Asigna los destinatarios.
3. Asigna las copias.
4. Construye el asunto.
5. Inserta el contenido HTML.
6. Abre el mensaje en Microsoft Outlook.
7. No realiza el envío.

El usuario puede revisar:

- Destinatarios.
- Copias.
- Asunto.
- Indicadores.
- Resumen por estados.
- Detalle de pedidos.
- Observaciones.
- Firma.

Después de validar la información, el usuario puede presionar manualmente el botón **Enviar** de Outlook.

> Este es el modo recomendado para pruebas y primeras ejecuciones.

---

### 31.5. Envío automático

Cuando se selecciona en DataSuite:

```text
Envío automático
```

Outlook ejecuta conceptualmente:

```python
mail.Send()
```

El sistema:

1. Genera el correo.
2. Asigna los destinatarios.
3. Asigna las copias.
4. Construye el asunto.
5. Inserta el contenido HTML.
6. Envía inmediatamente el mensaje.

En este modo, el correo no se abre para revisión manual.

> El envío automático debe utilizarse únicamente cuando los destinatarios, las reglas y las plantillas hayan sido completamente validados.

---

### 31.6. Combinaciones posibles

| `MODO_PRUEBA` | Opción en DataSuite | Destinatarios utilizados | Acción de Outlook |
|---|---|---|---|
| `True` | Modo revisión | Destinatarios de prueba | Abre el correo y no lo envía. |
| `True` | Envío automático | Destinatarios de prueba | Envía automáticamente. |
| `False` | Modo revisión | Destinatarios reales | Abre los correos y no los envía. |
| `False` | Envío automático | Destinatarios reales | Envía automáticamente. |

---

### 31.7. Prueba más segura

Configuración en `correos.py`:

```python
MODO_PRUEBA = True
```

Selección en DataSuite:

```text
Modo revisión
```

Resultado:

- Se utilizan los destinatarios de prueba.
- Outlook abre el correo.
- El mensaje no se envía.
- Se puede revisar toda la información.
- No existe riesgo de afectar a los destinatarios reales.

> Esta es la configuración recomendada para la primera prueba.

---

### 31.8. Prueba real de envío

Configuración en `correos.py`:

```python
MODO_PRUEBA = True
```

Selección en DataSuite:

```text
Envío automático
```

Resultado:

- Se utilizan los destinatarios de prueba.
- El correo se envía automáticamente.
- Se valida el funcionamiento completo del proceso.
- Los destinatarios reales no reciben ningún mensaje.

Esta prueba debe realizarse después de validar previamente el diseño en modo revisión.

---

### 31.9. Producción con revisión

Configuración en `correos.py`:

```python
MODO_PRUEBA = False
```

Selección en DataSuite:

```text
Modo revisión
```

Resultado:

- Cada grupo utiliza sus destinatarios reales.
- Outlook abre los correos generados.
- Los mensajes no se envían automáticamente.
- El usuario puede revisar cada correo antes de enviarlo.

Esta modalidad ofrece un control adicional antes del envío definitivo.

---

### 31.10. Producción automática

Configuración en `correos.py`:

```python
MODO_PRUEBA = False
```

Selección en DataSuite:

```text
Envío automático
```

Resultado:

- Cada grupo utiliza sus destinatarios reales.
- Se generan todos los correos configurados.
- Outlook envía inmediatamente los mensajes.
- No existe revisión manual previa.

> Esta configuración solo debe habilitarse después de completar las pruebas funcionales y validar los destinatarios.

---

### 31.11. Destinatarios principales

Los destinatarios principales corresponden al campo **Para** del correo.

En Outlook se asignan conceptualmente mediante:

```python
mail.To
```

Ejemplo:

```python
DESTINATARIOS = {

    "PUNTOS DE CONEXIÓN": [
        "responsable1@empresa.com",
        "responsable2@empresa.com",
    ],

}
```

Todas las direcciones incluidas en la lista recibirán directamente el mensaje.

---

### 31.12. Copias de correo

Las copias corresponden al campo **CC**.

En Outlook se asignan conceptualmente mediante:

```python
mail.CC
```

Ejemplo:

```python
COPIAS = {

    "PUNTOS DE CONEXIÓN": [
        "supervisor1@empresa.com",
        "supervisor2@empresa.com",
    ],

}
```

Las personas incluidas en copia pueden visualizar:

- El contenido del correo.
- Los destinatarios principales.
- Las demás personas copiadas.

---

### 31.13. Copia oculta

La variable:

```python
COPIA_OCULTA
```

corresponde al campo **CCO** o **BCC** de Outlook.

Ejemplo:

```python
COPIA_OCULTA = [
    "auditoria@empresa.com",
]
```

En Outlook se asigna conceptualmente mediante:

```python
mail.BCC
```

Las personas incluidas recibirán el mensaje, pero los demás destinatarios no podrán ver sus direcciones.

Si no se requiere copia oculta, la lista debe permanecer vacía:

```python
COPIA_OCULTA = [
]
```

---

### 31.14. Prioridad del correo

La variable:

```python
IMPORTANCIA = 2
```

define la prioridad asignada al mensaje.

| Valor | Prioridad |
|---:|---|
| `0` | Baja |
| `1` | Normal |
| `2` | Alta |

Para los correos de Seguimiento ANS se utiliza:

```python
IMPORTANCIA = 2
```

Esto permite que el mensaje aparezca marcado como de alta importancia en Outlook.

---

### 31.15. Variables de configuración legada

Las variables:

```python
MOSTRAR_CORREO = True
ENVIAR_AUTOMATICAMENTE = False
```

pertenecen a una versión anterior del funcionamiento del módulo.

Antes de integrar la selección en DataSuite, estas variables controlaban si el correo debía abrirse o enviarse.

Actualmente pueden conservarse por compatibilidad, pero la acción principal se controla desde la interfaz.

La lógica actual es:

```text
correos.py
      ↓
Controla los destinatarios

DataSuite
      ↓
Controla si Outlook abre o envía
```

---

### 31.16. Regla crítica para los nombres de los grupos

Las claves de los diccionarios deben coincidir exactamente con los nombres generados por el módulo.

Por ejemplo, estas claves son diferentes:

```python
"MOVIMIENTO DE REDES"
```

```python
"MOVIMIENTO_DE_REDES"
```

La primera utiliza espacios.

La segunda utiliza guiones bajos.

Si el motor genera:

```python
"MOVIMIENTO DE REDES"
```

pero `correos.py` contiene:

```python
"MOVIMIENTO_DE_REDES"
```

el sistema puede no encontrar los destinatarios correspondientes.

Debe mantenerse el mismo nombre en:

- `grupos.py`
- `correos.py`
- `agrupador.py`
- `generador_correo.py`
- `runner.py`

El estándar documentado es:

```python
"PUNTOS DE CONEXIÓN"
"PREPAGO_HV_ARTER"
"MOVIMIENTO DE REDES"
"PARTICULARES"
```

> Antes de modificar una clave, debe verificarse cómo la genera actualmente el motor.

---

### 31.17. Cómo agregar un destinatario

Para agregar una nueva dirección principal:

```python
"PUNTOS DE CONEXIÓN": [
    "responsable1@empresa.com",
    "responsable2@empresa.com",
    "nuevo_responsable@empresa.com",
],
```

Cada dirección debe:

- Estar escrita entre comillas.
- Terminar con una coma.
- Encontrarse dentro de la lista correspondiente.

---

### 31.18. Cómo agregar una copia

Para agregar una nueva persona en copia:

```python
"PUNTOS DE CONEXIÓN": [
    "supervisor1@empresa.com",
    "supervisor2@empresa.com",
    "nueva_copia@empresa.com",
],
```

---

### 31.19. Cómo retirar un destinatario

Para retirar una dirección, se elimina la línea correspondiente.

Antes:

```python
"PUNTOS DE CONEXIÓN": [
    "responsable1@empresa.com",
    "responsable2@empresa.com",
],
```

Después:

```python
"PUNTOS DE CONEXIÓN": [
    "responsable1@empresa.com",
],
```

Debe conservarse correctamente la estructura de la lista.

---

### 31.20. Grupo sin destinatarios

Una lista vacía se representa así:

```python
"PUNTOS DE CONEXIÓN": [
],
```

Sin embargo, no es recomendable ejecutar producción con un grupo sin destinatarios.

El sistema debería validar esta condición antes de abrir o enviar el correo.

---

### 31.21. Buenas prácticas

- Realizar primero las pruebas con `MODO_PRUEBA = True`.
- Seleccionar inicialmente **Modo revisión**.
- Verificar que cada correo corresponda al grupo correcto.
- Confirmar destinatarios y copias.
- Revisar que no existan direcciones duplicadas.
- Mantener los nombres de los grupos exactamente iguales.
- No habilitar producción automática sin pruebas previas.
- Mantener la copia oculta vacía cuando no sea necesaria.
- No dejar destinatarios temporales en la configuración de producción.
- Documentar cualquier cambio realizado en las listas.
- Realizar una prueba de recepción antes de activar el envío automático.

---

### 31.22. Secuencia recomendada para pasar a producción

```text
1. Configurar MODO_PRUEBA = True
        ↓
2. Seleccionar Modo revisión en DataSuite
        ↓
3. Validar diseño, contenido y destinatarios
        ↓
4. Mantener MODO_PRUEBA = True
        ↓
5. Seleccionar Envío automático
        ↓
6. Confirmar la recepción del correo de prueba
        ↓
7. Configurar MODO_PRUEBA = False
        ↓
8. Seleccionar Modo revisión
        ↓
9. Validar los destinatarios reales
        ↓
10. Habilitar Envío automático cuando corresponda
```

Esta secuencia reduce el riesgo de errores y permite validar progresivamente el funcionamiento.

---

### 31.23. Resumen de la configuración

| Elemento | Responsabilidad |
|---|---|
| `MODO_PRUEBA` | Determina si se utilizan destinatarios de prueba o de producción. |
| `DESTINATARIOS_PRUEBA` | Contiene los destinatarios principales utilizados durante las pruebas. |
| `COPIA_PRUEBA` | Contiene las copias utilizadas durante las pruebas. |
| `DESTINATARIOS` | Contiene los destinatarios reales organizados por grupo. |
| `COPIAS` | Contiene las copias reales organizadas por grupo. |
| `COPIA_OCULTA` | Define destinatarios que reciben el correo sin ser visibles para los demás. |
| `IMPORTANCIA` | Define la prioridad del mensaje en Outlook. |
| Modo revisión | Abre el correo y permite verificarlo antes de enviarlo. |
| Envío automático | Envía el correo inmediatamente desde Outlook. |

---

### 31.24. Idea clave

> `MODO_PRUEBA` controla a quién se dirige el correo.

> DataSuite controla si Outlook abre el mensaje o lo envía automáticamente.

La configuración más segura es:

```python
MODO_PRUEBA = True
```

Y en DataSuite:

```text
Modo revisión
```

De esta forma, el correo se abre con los destinatarios de prueba y no se envía hasta que el usuario lo confirme.