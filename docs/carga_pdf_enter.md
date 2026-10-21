# Cargue de evidencias PDF a ENTER

**Centro de Conocimiento Técnico — Elite Ingenieros S.A.S.**  
**Actualización:** 21 de octubre de 2026  
**Alcance:** recepción de evidencias, preparación de archivos, cargue mediante el bot desarrollado por TI y revisión de resultados. Incluye el procedimiento manual anterior como referencia.

## 1. Objetivo

Documentar cómo se reciben y cargan las evidencias PDF a ENTER, cómo se identifican los documentos de cada pedido y qué resultados deben revisarse al finalizar. Esta guía sirve como material de consulta y apoyo para capacitación y reuniones.

## 2. Origen de las evidencias

Los técnicos reportan diariamente las evidencias desde el celular mediante un enlace a un formulario. Los PDF enviados quedan almacenados en Google Drive de la cuenta de Gmail utilizada para recibirlos.

Cada día, el responsable descarga los PDF correspondientes al día anterior y los guarda en una carpeta de trabajo.

| Canal de recepción | Evidencias reportadas | Preparación para el cargue |
| --- | --- | --- |
| Formulario mediante enlace | HV, prepagos, legalizaciones, insumos de puntos de conexión y todo tipo de descartes | Descargar los PDF del día anterior desde Drive y guardarlos en una carpeta. |
| Correo electrónico | Movimientos de redes | Guardar los PDF recibidos en la carpeta correspondiente para su posterior cargue. |

El reporte del técnico en el formulario o por correo es la recepción de la evidencia. El cargue a ENTER se realiza después mediante el procedimiento descrito en esta guía.

## 3. Conceptos para interpretar el proceso

| Concepto | Significado |
| --- | --- |
| Pedido | Número al cual se asocian las evidencias. |
| Archivo PDF | Documento individual que se carga. Un pedido puede tener uno o varios PDF. |
| Tipo de proceso | Actividad del contrato a la cual corresponden las evidencias seleccionadas. |
| Lote | Grupo de hasta 20 archivos PDF organizado para el cargue. |
| Log | Registro de la ejecución que permite revisar los archivos procesados y las novedades. |

**No debe confundirse la cantidad de archivos con la cantidad de pedidos únicos.** Por ejemplo, 60 PDF forman tres lotes de 20 archivos, pero pueden corresponder a menos de 60 pedidos si algunos tienen varios documentos.

## 4. Nomenclatura de los archivos

La estructura utilizada para identificar cada PDF es:

```text
EPM-FNX-NUMERO_PEDIDO-201-(CONSECUTIVO).pdf
```

Ejemplo ilustrativo:

```text
EPM-FNX-12345678-201-(1).pdf
```

| Parte del nombre | Descripción |
| --- | --- |
| EPM-FNX | Prefijo utilizado en la nomenclatura del proceso. |
| NUMERO_PEDIDO | Número del pedido al que pertenece el documento. |
| 201 | Código indicado para «Acta de visita». |
| (CONSECUTIVO) | Diferencia los archivos de un mismo pedido: (1), (2), (3), etc. |
| .pdf | Extensión del archivo. |

### Varios documentos para un mismo pedido

En puntos de conexión es frecuente recibir varios PDF del mismo pedido. El ejemplo explicado para este proceso es:

| Documento | Ejemplo de nombre |
| --- | --- |
| Plano | EPM-FNX-12345678-201-(1).pdf |
| Fotografías | EPM-FNX-12345678-201-(2).pdf |
| Acta de visita | EPM-FNX-12345678-201-(3).pdf |

El consecutivo permite diferenciar los archivos; no significa que sean pedidos distintos. Tampoco permite concluir que un documento sea un duplicado que deba eliminarse.

**Precisión sobre el ejemplo:** esta distribución de (1), (2) y (3) corresponde al caso explicado por el responsable. No se establece aquí como una regla universal para todos los pedidos. Aunque se informó que 201 significa «Acta de visita», también se describió su uso en los nombres de planos y fotografías del mismo pedido. La clasificación documental de esos soportes debe confirmarse con TI o con el responsable de ENTER antes de definir códigos diferentes.

## 5. Procedimiento actual: bot desarrollado por TI

### Paso 1. Preparar la carpeta de evidencias

1. Descargar desde Drive los PDF reportados el día anterior.
2. Guardar los documentos en una carpeta de trabajo.
3. Para movimientos de redes, guardar los PDF recibidos por correo en su carpeta correspondiente.
4. Identificar la actividad a la cual corresponden los archivos que se van a cargar.

Como control operativo, revisar que los archivos seleccionados correspondan al tipo de proceso elegido. Si existen actividades diferentes, preparar sus cargues por separado para evitar asociar soportes a una actividad equivocada.

### Paso 2. Abrir el bot

Ingresar a la herramienta desarrollada por TI. La primera captura muestra la pantalla **Configurar carga** de la aplicación **Automatización Enter**.

### Paso 3. Revisar el operador

En **Nombre del operador** aparece el usuario responsable de subir las evidencias a ENTER. Revisar que corresponda a la persona que realiza el cargue, ya que este dato queda asociado al registro de ejecución.

### Paso 4. Seleccionar la carpeta

1. En **Carpeta de pedidos**, pulsar **Examinar**.
2. Buscar la carpeta que contiene los PDF que se quieren subir.
3. Seleccionar la carpeta y comprobar que sea la correcta.

### Paso 5. Seleccionar el tipo de proceso

En **Tipo de proceso**, seleccionar la actividad del contrato a la que corresponden los PDF.

El ejemplo informado es **Conexión del servicio de energía eléctrica**, utilizado para:

- HV.
- Legalizaciones.
- Prepagos.

La actividad de los demás soportes debe seleccionarse según corresponda en el aplicativo. Esta guía no asigna actividades que no hayan sido confirmadas.

### Paso 6. Revisar los demás campos de configuración

En la primera captura también se observan:

- **Navegador**, con Chrome seleccionado.
- **Fecha inicio**.
- **Fecha fin (opcional)**.
- La opción **Usar rango de fechas**.

La interfaz indica que se seleccionen las fechas correspondientes a los documentos. Antes de ejecutar, revisar estos campos conforme al procedimiento definido por TI. No se ha confirmado si las fechas filtran archivos, se registran como metadatos o cumplen otra función; por tanto, no deben describirse como fecha de subida sin validar su significado.

### Paso 7. Ejecutar el proceso

Pulsar **Ejecutar proceso**.

De acuerdo con la explicación operativa recibida, el bot realiza las siguientes tareas:

1. Identifica cuántos PDF existen en la carpeta seleccionada.
2. Renombra los archivos conforme a la nomenclatura utilizada para ENTER.
3. Comprime los PDF que pesan más de 20 MB.
4. Organiza los archivos en subcarpetas o lotes de hasta 20 PDF.
5. Ejecuta el cargue de los lotes a ENTER.
6. Genera un registro de resultados en Excel.
7. Cuando un archivo no puede cargarse por alguna novedad, muestra un mensaje y lo lleva a la carpeta **INVALIDO ENTER**, según lo informado por el responsable.

**Ejemplo:** con 60 PDF, el bot crea tres lotes de 20 archivos. La cantidad de pedidos únicos dependerá de cuántos documentos tenga cada pedido.

La compresión forma parte de la preparación del archivo. Para darlo por cargado, también debe revisarse el resultado de la ejecución.

### Paso 8. Revisar el registro de resultados

El bot genera un archivo de Excel que permite consultar la trazabilidad del cargue. La segunda captura muestra una hoja llamada **Resultados**.

| Información | Qué permite identificar |
| --- | --- |
| Operador | Persona que ejecutó el cargue. |
| Archivo | Nombre completo del PDF; incluye el número de pedido y el consecutivo. |
| Fechas del proceso | Se observan columnas de fecha de inicio y fecha de fin. |
| Fecha de ejecución | Día en que se ejecutó el proceso. |
| Hora de ejecución | Hora registrada para la ejecución. |

En la captura, el número de pedido está contenido en el nombre del archivo; no se observa una columna independiente de pedido. Algunos encabezados de fecha aparecen recortados, por lo que se debe verificar su nombre completo en el Excel original si se necesita documentar cada columna con exactitud.

El registro debe revisarse junto con el estado final del bot y las novedades. La captura del Excel por sí sola no demuestra cómo se registra cada fallo ni acredita individualmente que ENTER haya aceptado todos los archivos.

### Paso 9. Revisar novedades y cierre del cargue

Al finalizar:

1. Revisar el mensaje final de la ejecución.
2. Comparar el número de PDF de entrada con los resultados registrados.
3. Consultar los logs y sus detalles cuando exista una novedad.
4. Revisar la carpeta **INVALIDO ENTER** para identificar los archivos pendientes de resolver.
5. Verificar en ENTER los casos dudosos antes de repetir su cargue.

La cuarta captura muestra un contador de **49/49 archivos** y, al mismo tiempo, el mensaje **«La carga no se completó»**. Esto demuestra que llegar al total del contador no basta para concluir que la ejecución terminó correctamente. Deben revisarse el mensaje final y el detalle del log.

La causa exacta del error no puede establecerse con esa captura. Tampoco permite concluir por sí sola cuáles documentos quedaron cargados o pendientes.

## 6. Procedimiento anterior: cargue manual en ENTER

Antes de utilizar el bot, el responsable cargaba los PDF manualmente desde el aplicativo ENTER, al que accedía mediante una dirección de SharePoint de EPM.

No se incluye una URL completa porque no fue suministrada. Para la operación se debe utilizar el enlace corporativo autorizado.

### Secuencia de cargue manual

1. Ingresar a ENTER mediante la URL corporativa.
2. Acceder a **EPM → Carga masiva**.
3. Seleccionar **Negocio: Energía**.
4. En **Evento**, elegir la actividad correspondiente. Este campo equivale a la actividad que se selecciona en **Tipo de proceso** del bot.
5. Seleccionar la carpeta con los PDF del lote.
6. Iniciar el cargue y esperar el avance de la barra de progreso.
7. Repetir el ciclo con las demás carpetas hasta terminar.

**Ejemplo:** para 60 PDF se preparaban tres carpetas de 20 archivos y se repetía el cargue tres veces.

### Novedad reportada en el procedimiento manual

Según la experiencia operativa descrita, cuando un PDF pesaba más de 20 MB podía aparecer un resultado **OK** sin una advertencia clara de que el documento no se hubiera cargado.

En ese flujo no se contaba con un resumen suficientemente claro para distinguir cuáles PDF habían subido y cuáles no. Por ello, un mensaje OK o una barra de progreso completa no se consideraban evidencia suficiente del cargue individual.

Se trata de una novedad reportada por el responsable del proceso; no de una validación técnica realizada sobre ENTER en esta guía.

### Indicadores y logs al finalizar

El responsable también describe indicadores de cantidad procesada frente al total esperado y un log cuando se presentan novedades. Es necesario interpretar si cada contador representa archivos o pedidos.

**Ubicación de la cuarta captura:** por su contenido, corresponde a una pantalla de seguimiento de ejecución con operador, contadores y logs, acompañada de una alerta. No debe presentarse como evidencia exclusiva del procedimiento manual anterior sin confirmar de qué componente proviene. Se utiliza en esta guía para ilustrar la necesidad de revisar los errores aunque el contador llegue al total.

## 7. Comparación de los procedimientos

| Aspecto | Procedimiento manual anterior | Procedimiento actual mediante el bot |
| --- | --- | --- |
| Configuración | Se ingresa directamente a ENTER y se eligen negocio y evento. | Se configura operador, carpeta y tipo de proceso en la herramienta de TI. |
| Organización de lotes | El responsable prepara y carga las carpetas de hasta 20 PDF. | El bot organiza los PDF en lotes de hasta 20 archivos. |
| Nomenclatura | Los archivos deben estar preparados para su cargue; no se detalló aquí cómo se renombraban antes. | El bot renombra los archivos conforme al proceso informado. |
| PDF de más de 20 MB | Se reportó que podían generar un OK sin advertencia clara del problema. | El bot incluye una etapa de compresión. |
| Ejecución | Se repite manualmente el ciclo de selección y cargue por carpeta. | El bot ejecuta el cargue de los lotes seleccionados. |
| Trazabilidad | Se reportó dificultad para identificar el resultado individual de los PDF. | Se genera un Excel de resultados y existen pantallas con logs de ejecución. |
| Novedades | Requieren revisión del resultado del cargue. | Se informa un mensaje y se utiliza la carpeta INVALIDO ENTER, según el procedimiento descrito. |
| Cierre | Debe comprobarse el resultado de los documentos. | Deben revisarse el mensaje final, los resultados y las novedades. |

## 8. Controles recomendados

Estos controles complementan la operación; no se afirma que todos sean validaciones automáticas del bot.

| Momento | Control | Propósito |
| --- | --- | --- |
| Antes del cargue | Revisar operador, carpeta y tipo de proceso. | Asociar las evidencias al responsable y actividad correctos. |
| Antes del cargue | Contar los PDF e identificar pedidos con varios documentos. | Definir el total esperado sin confundir archivos con pedidos. |
| Antes del cargue | Comprobar que los PDF se puedan abrir y sean legibles. | Detectar documentos dañados o evidencias que requieran corrección. |
| Después de comprimir | Revisar legibilidad de los documentos comprimidos. | Conservar la utilidad de planos, fotografías y actas. |
| Al finalizar | Revisar mensaje final, Excel y logs. | Identificar inconsistencias aunque el contador llegue al total. |
| Ante una novedad | Revisar INVALIDO ENTER y comprobar el caso en ENTER. | Determinar qué quedó pendiente antes de repetir el cargue. |
| Antes de reintentar | Confirmar si el archivo ya se encuentra en ENTER. | Evitar repetir documentos ya cargados. |

## 9. Guion breve para explicar en la reunión

Los técnicos reportan diariamente las evidencias desde el celular mediante un formulario. Los PDF quedan en Drive y cada día descargamos los del día anterior para preparar el cargue. Los movimientos de redes se reciben por correo y también se guardan en su carpeta correspondiente.

Para subir las evidencias utilizamos el bot desarrollado por TI. Revisamos el operador, seleccionamos la carpeta y elegimos la actividad del contrato. Por ejemplo, para HV, legalizaciones y prepagos se utiliza Conexión del servicio de energía eléctrica.

Al ejecutar, el bot identifica los PDF, los renombra, comprime los que superan los 20 MB y los organiza en lotes de hasta 20 archivos para cargarlos a ENTER. Al terminar genera un Excel que permite consultar el operador, el archivo y los datos de ejecución. Las novedades se revisan en los mensajes, los logs y la carpeta INVALIDO ENTER.

Un pedido puede tener varios documentos. En puntos de conexión, por ejemplo, puede haber un PDF de plano, otro de fotografías y otro de acta. Por eso distinguimos la cantidad de archivos de la cantidad de pedidos.

Antes, el cargue se hacía manualmente en ENTER, seleccionando Energía, el evento y cada carpeta de 20 archivos. Se reportaban casos de PDF de más de 20 MB que mostraban OK sin una advertencia clara del problema. El bot incorpora preparación y trazabilidad, pero el cierre siempre requiere revisar el resultado: un contador completo no garantiza por sí solo que toda la ejecución haya terminado correctamente.

## 10. Referencias y límites de esta guía

El contenido se elaboró con la explicación del responsable y cuatro capturas suministradas:

| Captura | Contenido utilizado |
| --- | --- |
| 1 — image(8).png | Configuración del bot: operador, carpeta, navegador, tipo de proceso y fechas. |
| 2 — image(9).png | Excel de resultados con operador, nombre del archivo y datos de ejecución. |
| 3 — image(10).png | Pantalla de carga masiva de ENTER utilizada como referencia del procedimiento manual. |
| 4 — image(20261021-185622).png | Seguimiento con contador, logs y mensaje «La carga no se completó». |

No se revisó el código fuente del bot ni se ejecutó un cargue de prueba. Las funciones de renombrado, compresión, organización por lotes y traslado a INVALIDO ENTER se documentan según la explicación operativa recibida.

Para ampliar esta guía quedan por confirmar: el significado exacto de los campos de fecha, el criterio técnico de compresión, la clasificación documental de planos y fotografías bajo el código 201 y el procedimiento de reintento ante cada tipo de error.
