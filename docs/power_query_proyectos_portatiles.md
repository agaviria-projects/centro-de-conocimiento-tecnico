# Power Query: proyectos portátiles y entrega a otros usuarios

**Centro de Conocimiento Técnico · Versión 1.0 · 19/10/2026**

## Qué aprenderás

Construir y revisar un informe para que sus consultas encuentren los archivos en otra carpeta o PC sin editar rutas de usuario. El procedimiento documenta primero el caso real validado del maestro de coordenadas y después propone un estándar para proyectos nuevos.

La implementación del informe utiliza Excel y Power Query M, sin requerir Python ni macros. Python/Streamlit se utiliza aquí únicamente para mostrar esta documentación en el centro de conocimiento.

## Índice

1. Conceptos y límites de la solución.
2. Caso real: MAESTRO_COORDENADAS.xlsx.
3. Actualización diaria y entrega al usuario.
4. Diagnóstico de problemas comunes.
5. Estándar de desarrollo para nuevos informes.
6. Consultas M completas de la plantilla.
7. Pruebas de aceptación y criterio de cierre.

## 1. Conceptos y límites

### Problema actual

Un paso como este depende de una ubicación del desarrollador:

```powerquery
= Folder.Files("C:\Users\USUARIO_DESARROLLADOR\Desktop\mapa_ejecutados\config_fenix_Ans")
```

En el PC del destinatario cambian el usuario, la carpeta o la unidad. Además, una consulta auxiliar puede conservar una ruta fija aunque se haya corregido la principal.

### Resultado esperado

El informe obtiene su ubicación actual, construye la carpeta de entrada y actualiza desde ella. El usuario conserva la estructura del proyecto y utiliza Datos → Actualizar todo.

### Qué hace cada componente

| Componente | Responsabilidad |
|---|---|
| Fórmula CELDA en Excel | Obtiene la ubicación del libro guardado |
| Rango con nombre RutaLibro | Permite que M lea esa celda sin depender de la hoja visible |
| Consulta RutaFenix o RutaProyecto | Construye la ruta requerida |
| Consulta principal y auxiliares | Leen y transforman las entradas |
| Controles | Permiten comprobar que la actualización terminó con el resultado esperado |

Excel.CurrentWorkbook lee tablas, rangos con nombre y matrices dinámicas del libro; no obtiene automáticamente su directorio ni devuelve hojas completas.

La ruta final sigue siendo absoluta, pero se CALCULA a partir de la ubicación del libro. Que aparezca C:\Users\... en el resultado es normal; el problema es dejar esa ubicación ESCRITA FIJA dentro de las consultas.

### Reglas que no se deben asumir

- No eliminar duplicados por defecto.
- No decidir automáticamente si los cortes diarios se acumulan o reemplazan: depende del informe.
- No corregir ni inventar coordenadas.
- No suponer que una columna existe porque apareció en el primer archivo.
- No interpretar una actualización sin errores como una validación completa de totales.

Esta guía se aplica a Excel de escritorio para Windows y rutas locales o sincronizadas accesibles. No garantiza funcionamiento sin pruebas en cualquier PC.

## 2. Caso real: MAESTRO_COORDENADAS.xlsx

### Paso 1. Conservar la estructura existente

| Ruta relativa a mapa_ejecutados | Contenido |
|---|---|
| config_fenix_Ans/ | Exportaciones Fénix por fecha |
| fenix_unificado/MAESTRO_COORDENADAS.xlsx | Maestro que combina coordenadas |
| entrada/EJECUTADAS.xlsb | Libro operativo y macros |
| output/ | Mapas generados |

Mover la carpeta mapa_ejecutados completa. No mover solamente el maestro. No aplicar al caso actual la estructura distinta propuesta para proyectos nuevos en el capítulo 5.

### Paso 2. Crear la hoja CONFIGURACION

1. Abrir MAESTRO_COORDENADAS.xlsx desde su ubicación operativa y guardarlo.
2. Crear la hoja CONFIGURACION.
3. En B2 pegar esta fórmula, que usa punto y coma como separador:

```excel
=IZQUIERDA(CELDA("nombrearchivo";$A$1);HALLAR("[";CELDA("nombrearchivo";$A$1))-1)
```

**Por qué funciona:** CELDA devuelve ruta, archivo y hoja. HALLAR localiza el corchete anterior al nombre del archivo. IZQUIERDA conserva solamente la carpeta.

Resultado ilustrativo:

```text
C:\Users\USUARIO\Desktop\mapa_ejecutados\fenix_unificado\
```

Si el libro no está guardado, la fórmula puede no obtener una ruta y HALLAR fallará. Guardar y recalcular. Si devuelve https://, detener esta variante y revisar acceso local/SharePoint; no reemplazar partes de la URL sin comprobar su correspondencia real.

### Paso 3. Definir RutaLibro

1. Seleccionar CONFIGURACION!B2.
2. Fórmulas → Administrador de nombres → Nuevo.
3. Nombre: RutaLibro. Ámbito: Libro.
4. Se refiere a: =CONFIGURACION!$B$2.
5. Aceptar y comprobar la referencia.

También puede escribirse RutaLibro en el cuadro de nombres situado a la izquierda de la barra de fórmulas y pulsar Enter. Confirmar que apunta a una sola celda.

Ocultar CONFIGURACION después de validar no afecta a la fórmula ni al rango. No eliminarla ni borrar B2.

### Paso 4. Crear RutaFenix

Datos → Obtener datos → Desde otras fuentes → Consulta en blanco. En el editor: Inicio → Editor avanzado. Pegar la consulta completa y nombrarla RutaFenix:

```powerquery
let
    CeldaRuta = Excel.CurrentWorkbook(){[Name="RutaLibro"]}[Content],
    RutaLibro = Text.From(CeldaRuta{0}[Column1]),
    CarpetaMaestro = Text.TrimEnd(RutaLibro, {"\"}),
    CarpetaProyecto = Text.Combine(
        List.RemoveLastN(Text.Split(CarpetaMaestro, "\"), 1),
        "\"
    ),
    CarpetaFenix = CarpetaProyecto & "\config_fenix_Ans"
in
    CarpetaFenix
```

La consulta lee B2, quita la barra final, sube un nivel desde fenix_unificado y entra a config_fenix_Ans. Si cambia la posición del maestro respecto a esa carpeta, hay que adaptar la construcción.

### Paso 5. Cambiar la consulta principal

En el editor, seleccionar config_fenix_Ans → Pasos aplicados → Origen. Cambiar SOLO la expresión de la barra de fórmulas por:

```powerquery
= Folder.Files(RutaFenix)
```

Presionar Enter. Comprobar que se listan las exportaciones esperadas. No reemplazar los pasos de expansión, selección de columnas o tipos que ya funcionan. Seleccionar el último paso y revisar datos y errores.

Folder.Files incluye archivos de subcarpetas: no guardar respaldos de Fénix dentro de config_fenix_Ans sin una regla explícita para excluirlos.

### Paso 6. Cambiar Archivo de ejemplo

Seleccionar Archivo de ejemplo → Origen. Si tiene el mismo Folder.Files con la ruta fija, sustituirlo por:

```powerquery
= Folder.Files(RutaFenix)
```

Conservar Navegación y comprobar que siga devolviendo el binario esperado. El asistente utiliza este archivo para definir cómo transformar cada entrada. Revisar también que Navegación no contenga una ruta antigua o un nombre de archivo que no se entregará.

No cambiar la función Transformar archivo por una tabla: la función recibe un binario. Si el código difiere de este patrón, revisar su Editor avanzado antes de reemplazarlo.

### Paso 7. Dejar RutaFenix como conexión

1. Cerrar y cargar.
2. En Excel: Datos → Consultas y conexiones.
3. Clic derecho sobre RutaFenix → Cargar en… → Crear únicamente la conexión.
4. Si advierte que quitará la tabla cargada, confirmar que la seleccionada sea RutaFenix. El aviso corresponde a la tabla de una fila con la ruta, no al maestro consolidado.
5. Verificar que diga Solo conexión. Puede eliminarse la pestaña RutaFenix si quedó vacía; conservar la consulta y CONFIGURACION.
6. config_fenix_Ans conserva su carga como tabla. COORDENADAS_MANUALES conserva sus datos independientes.

### Paso 8. Probar desde otra ubicación

1. Guardar y cerrar el original.
2. Copiar TODA la carpeta mapa_ejecutados a Descargas.
3. Abrir el maestro de la copia, no el del Escritorio.
4. Pulsar Ctrl + Alt + F9 y revisar CONFIGURACION!B2.
5. La ruta debe apuntar a Downloads o Descargas según el nombre real del directorio.
6. Datos → Actualizar todo. Esperar y revisar el estado de las consultas.
7. Comparar lista de archivos, cantidad de filas y controles con el original. Guardar.

**Prueba observada en este desarrollo:** la ruta cambió de Desktop a Downloads y se cargaron 25.121 filas con las mismas entradas. Es una referencia del conjunto probado el 19/10/2026; no es un total fijo que deba mantenerse cuando se agreguen nuevas exportaciones. Esto valida el traslado de carpeta en ese PC; falta probar el PC del destinatario para comprobar sus permisos y configuración.

## 3. Actualización diaria y entrega

### Qué significa Ctrl + Alt + F9

Recalcula fórmulas de Excel. No muestra necesariamente cambios ni un aviso, y NO actualiza Power Query. Si la ruta ya era correcta, el contenido puede verse igual.

Se recomienda forzarlo al cambiar de PC o ubicación y guardar después. En la misma carpeta normalmente no hace falta repetirlo en cada apertura. Lo importante es que B2 corresponda a la ubicación actual ANTES de actualizar. Si el atajo no responde, B2 → F2 → Enter vuelve a evaluar la fórmula; verificar el resultado.

### Primera apertura en destino

1. Recibir la carpeta completa y extraerla si llegó comprimida.
2. Abrir MAESTRO_COORDENADAS desde fenix_unificado.
3. Recalcular, comprobar ruta y ejecutar Datos → Actualizar todo.
4. Esperar, revisar errores y controles y guardar.
5. Abrir EJECUTADAS.xlsb desde entrada para continuar con sus botones.

### Rutina del maestro

Guardar los nuevos archivos Fénix en config_fenix_Ans → abrir maestro → Actualizar todo → esperar → validar → guardar.

No mantener dos copias como si estuvieran sincronizadas: Escritorio y Descargas son independientes. Elegir una versión operativa y usar las otras solo para pruebas/respaldo.

### Power Query y macro de coordenadas son procesos diferentes

| Proceso | Qué hace |
|---|---|
| Power Query del maestro | Vuelve a leer y combinar los archivos incluidos. Toma las coordenadas existentes en Fénix; no las geocodifica |
| Macro de EJECUTADAS | En la versión validada, conserva parejas válidas existentes e intenta completar las pendientes, tanto nuevas como antiguas |
| Generar mapa | Crea una nueva copia HTML de la base exportada desde Excel |

No confundir actualizar la tabla del maestro con sobrescribir coordenadas del consolidado. Las capturas operativas no equivalen a una auditoría completa de cada versión de la macro.

## 4. Diagnóstico de problemas comunes

| Síntoma | Causa probable / comprobación | Acción |
|---|---|---|
| No cambia nada al recalcular | La ruta ya es correcta | Revisar B2; después actualizar datos |
| No existe RutaLibro | Nombre ausente, ámbito de hoja o referencia equivocada | Administrador de nombres, ámbito Libro y una celda |
| Error al buscar Column1 | RutaLibro no apunta al rango previsto | Comprobar que sea solamente B2 |
| No encuentra la carpeta | Se movió solo el Excel o cambió una subcarpeta | Comprobar ruta calculada y estructura |
| Funciona principal pero falla al combinar | Auxiliar o Navegación conserva dependencia | Revisar Archivo de ejemplo y Transformar archivo de ejemplo |
| Ya no existe una columna | Cambió esquema/encabezados de origen | Localizar el primer paso que falla y comparar archivos |
| Fallan fechas o decimales en otro PC | Conversión dependiente de configuración regional | Confirmar formato real y usar conversión con configuración regional explícita |
| Filas o totales aumentan inesperadamente | Archivos extra, subcarpetas, cortes repetidos o cruce de uno a varios | Comparar inventario y filas antes/después del cruce |
| Hay tabla con datos pero la actualización falló | Son resultados anteriores | No presentarlos como actuales; revisar estado y error |
| Formula.Firewall o permisos | Combinación de orígenes/configuración de privacidad o acceso | Revisar mensaje y políticas; no desactivar privacidad global como receta |

Antes de corregir: capturar texto completo del error, consulta y primer paso que falla; confirmar si B2 y RutaFenix son correctos. No reemplazar todo el proyecto por un síntoma aislado.

## 5. Estándar para proyectos nuevos

El siguiente capítulo propone otra estructura, con INFORME.xlsx en la raíz. Utilizarla para NUEVOS informes. El proyecto de coordenadas anterior conserva fenix_unificado y RutaFenix.

#### 1. Delimitar qué problema resuelve

Problema actual: una ruta escrita en un paso Origen puede apuntar al usuario del desarrollador. También pueden fallar consultas auxiliares, nombres de hoja/tabla, tipos, columnas, permisos o la interpretación de fechas.
Resultado esperado: entregar una carpeta que funcione desde otra ubicación de Windows, con el mismo proceso de actualización y controles visibles para el usuario.
Reglas de negocio: definir claves, significado de fechas, tipos de columna y tratamiento de duplicados antes de transformar. No inventar exclusiones ni eliminar duplicados por defecto.
Restricciones: Excel de escritorio Windows con Power Query y acceso a los archivos. La carpeta debe estar extraída si se entrega por ZIP. La plantilla no es una solución para Excel web ni para programar actualizaciones con el libro cerrado.
Archivos: obtener ejemplos representativos y nombres reales de tablas, hojas y columnas. Confirmar si se acumulan cortes diarios o si un archivo reemplaza al anterior.
Pruebas: ruta, lista de archivos, esquema, filas, totales y casos conocidos, además de una prueba en otra ubicación y otra cuenta/PC.

#### 2. Adoptar una estructura estable para proyectos NUEVOS

| Ubicación | Uso |
|---|---|
| PROYECTO/INFORME.xlsx | Libro que contiene las consultas; se mantiene en la raíz |
| PROYECTO/01_ENTRADA/ | Solo archivos autorizados para actualizar |
| PROYECTO/02_SALIDA/ | Exportaciones si el proceso las genera por otro medio |
| PROYECTO/03_DOCUMENTACION/ | Instrucciones y reglas |

El nombre PROYECTO puede cambiar. El nombre 01_ENTRADA es un acuerdo de esta plantilla. No colocar el libro del informe ni sus salidas en 01_ENTRADA. La plantilla no exporta archivos a 02_SALIDA: Power Query carga resultados en Excel y no es, por sí mismo, un generador arbitrario de archivos.

Mantener archivos archivados fuera de la entrada. El ejemplo usa Folder.Contents para leer solo el primer nivel. Folder.Files también lee subcarpetas; si se necesita recursión, incorporarla deliberadamente y comprobar su inventario.

#### 3. Preparar el libro

1. Crear INFORME.xlsx dentro de la raíz y guardarlo.
2. Crear hojas INICIO, CONFIGURACION y, cuando corresponda, RESULTADO y CONTROL.
3. En CONFIGURACION!A2 escribir Carpeta del libro.
4. En B2 pegar:

```excel
=IZQUIERDA(CELDA("nombrearchivo";$A$1);HALLAR("[";CELDA("nombrearchivo";$A$1))-1)
```

5. Seleccionar B2. Fórmulas → Administrador de nombres → Nuevo. Nombre RutaLibro, ámbito Libro, referencia =CONFIGURACION!$B$2. También puede usarse el cuadro de nombres y comprobar el ámbito después.
6. Recalcular y comprobar que B2 devuelve la carpeta que contiene INFORME.xlsx. No escribir la ruta manualmente encima de la fórmula.
7. CONFIGURACION se puede ocultar después de validar; ocultarla no impide leer el rango con nombre.

Esta técnica combina una fórmula que obtiene la ubicación con M que lee la celda. M no dispone aquí de una detección automática del directorio del libro mediante Excel.CurrentWorkbook: esa función devuelve tablas/rangos, no la ruta del archivo. Un parámetro con C:\Users\... escrito a mano sigue dependiendo de esa ubicación.

#### 4. Crear las consultas base

Datos → Obtener datos → Desde otras fuentes → Consulta en blanco. Inicio → Editor avanzado. Pegar cada archivo completo sin bloques Markdown. Asignar estos nombres exactos, en orden:

| Archivo | Nombre de consulta | Carga |
|---|---|---|
| 01_RutaProyecto.pq | RutaProyecto | Solo conexión |
| 02_RutaEntrada.pq | RutaEntrada | Solo conexión |
| 03_ArchivosEntrada.pq | ArchivosEntrada | Solo conexión |
| 05_ControlArchivos.pq | ControlArchivos | Hoja CONTROL, opcional |

RutaProyecto exige que el libro esté en la raíz del proyecto. No devuelve el directorio padre: no sirve sin adaptar si se mueve únicamente el Excel a una subcarpeta.

ArchivosEntrada es un inventario con Content binario; todavía no combina las filas de los Excel. Filtra .xlsx, temporales de Excel, ocultos y carpetas. Revisar este criterio según el proyecto; no asumir que todos los Excel de la carpeta son válidos. Añadir un prefijo o filtro específico solo si existe una regla definida.

#### 5. Combinar archivos conservando una sola lista de entradas

1. En Power Query, clic derecho sobre ArchivosEntrada → Referencia. Renombrar la consulta nueva DatosConsolidados.
2. Seleccionar Content y pulsar Combinar archivos. Elegir la tabla/hoja real de los archivos.
3. Mantener los archivos con errores visibles durante la validación. No activar omisión de errores como sustituto de investigar un archivo faltante.
4. Revisar las consultas que genera el asistente: Archivo de ejemplo, Transformar archivo de ejemplo, Transformar archivo y parámetro.
5. La principal debe partir de ArchivosEntrada. La auxiliar Archivo de ejemplo también debe usar esa misma lista filtrada. Si hace falta adaptarla, el archivo 04_ArchivoEjemplo_Alternativa.pq devuelve ArchivosEntrada{0}[Content]; conservar el nombre de consulta que espera el parámetro.
6. No reemplazar a ciegas la función Transformar archivo: espera un binario y su contrato debe conservarse.
7. Conservar el nombre del archivo de origen como columna para rastrear diferencias.

No entregar una transformación universal de hojas, encabezados o fechas sin conocer su estructura. Una ruta portátil no repara una columna renombrada.

#### 6. Revisar TODOS los pasos, no solamente Origen

En cada consulta relevante abrir Inicio → Editor avanzado. Buscar:
- C:\Users\, Desktop, Downloads, OneDrive y nombres de usuario.
- Folder.Files, Folder.Contents, File.Contents y enlaces web.
- Folder Path en filtros y pasos Navegación con archivo/ruta explícitos.
- Nombre de un archivo de ejemplo fijo que podría desaparecer.
- Nombres de hojas/tablas, encabezados promovidos, columnas quitadas, reordenadas/expandidas y Tipo cambiado.
- Referencias a consultas o rangos con nombre que no se incluyeron en el libro.

Comprobar dependencias en Vista → Dependencias de consultas cuando esté disponible. No sustituir textos masivamente sin revisar el tipo devuelto en cada paso.

#### 7. Construir controles del informe

En cada proyecto registrar qué archivos se esperan, cuántos se leyeron y qué filas/totales deberían producir. ControlArchivos solo acredita la lista seleccionada: no demuestra que todas sus filas se transformaron correctamente.

Revisar esquema, errores de conversión, fechas ambiguas y valores nulos. Si PEDIDO es identificador, evaluar texto para conservar ceros iniciales; no cambiar un proyecto existente sin revisar sus cruces.

En un cruce con otra tabla, comparar filas y totales antes/después. Una clave repetida en la tabla de búsqueda puede multiplicar filas. Repeticiones entre cortes diarios pueden ser legítimas; su tratamiento depende de la regla de negocio, no de esta plantilla.

El panel de calidad puede analizar solo las primeras 1.000 filas. Para validar todo, seleccionar perfil de columnas basado en el conjunto completo o crear controles explícitos.

El último resultado cargado puede seguir visible después de un fallo. La existencia de una tabla con datos no prueba que la actualización actual terminó bien. Confirmar el estado de actualización, errores y controles después de esperar su finalización.

#### 8. Preparar la guía del usuario

Preparar una guía breve en INICIO usando la rutina del capítulo 3: para qué sirve, dónde se guardan las entradas, cómo actualizar, cómo saber que terminó bien y a quién reportar un error. Solo una copia debe ser la versión operativa.

Una fórmula AHORA no certifica una actualización exitosa de Power Query. Si se muestra fecha de actualización, explicar cómo se obtiene y asociarla al resultado de la consulta cargada, no solo al reloj de Excel.

#### 9. Probar portabilidad antes de entregar

1. Guardar y cerrar el libro de desarrollo.
2. Copiar toda la carpeta a otra ubicación. Abrir únicamente la copia de prueba.
3. Recalcular con Ctrl + Alt + F9 y revisar CONFIGURACION!B2. El atajo no abre avisos ni actualiza Power Query. Si el teclado no lo ejecuta, editar B2 con F2 y Enter y comprobar el resultado.
4. Antes de actualizar, confirmar que la ruta corresponde a la COPIA. No usar una prueba que termina leyendo el origen anterior.
5. Datos → Actualizar todo. Esperar y comprobar estado, archivos, errores, filas y totales. Guardar.
6. Para una prueba más fuerte, usar entradas de prueba identificables en la copia y verificar que ControlArchivos las muestra; conservar el original fuera del alcance de la copia.
7. Probar con otro usuario/PC destinatario. La prueba de mover carpeta en el mismo PC no valida sus permisos, credenciales, versión ni configuración regional.
8. Si Excel pide niveles de privacidad o permisos, registrar el mensaje y configurar los orígenes según las políticas de la organización. No usar desactivar privacidad global como receta estándar.

#### 10. Entrega y mantenimiento

Entregar la carpeta completa o un ZIP para extraer. Documentar versión de Excel, versión del informe, estructura exigida, tipo de archivos y pruebas aprobadas. En otro PC o tras mover la carpeta, recalcular, confirmar ruta y luego actualizar. En la misma ubicación no suele requerirse forzar recálculo cada vez.

Actualizar rutas no implica actualización incremental: una combinación habitual vuelve a leer sus entradas. Para históricos y cortes definir retención y duplicados explícitamente. La plantilla no garantiza funcionamiento en cualquier PC: reduce dependencias y exige una prueba de aceptación real.


## 6. Consultas M completas para proyectos nuevos

Los nombres .pq citados en el capítulo 5 identifican los bloques siguientes; no necesitas archivos adicionales. Crear una consulta en blanco por bloque, asignar el nombre indicado y pegar SOLO su contenido en el Editor avanzado. Los comentarios son parte válida de M.

### RutaProyecto

```powerquery
let
    Lectura = try Excel.CurrentWorkbook(){[Name="RutaLibro"]}[Content],
    TablaRuta = if Lectura[HasError] then
        error "Falta el nombre RutaLibro. Defínelo sobre CONFIGURACION!B2 con ámbito Libro."
        else Lectura[Value],
    Valor = if Table.RowCount(TablaRuta) <> 1 or Table.ColumnCount(TablaRuta) <> 1 then
        error "RutaLibro debe referirse a una sola celda."
        else Record.FieldValues(TablaRuta{0}){0},
    Texto = if Valor = null then "" else Text.Trim(Text.From(Valor)),
    Ruta = if Texto = "" then
        error "La ruta está vacía. Guarda el libro y recalcula antes de actualizar."
        else if Text.StartsWith(Text.Lower(Texto), "http") then
        error "La fórmula devolvió una URL. Esta plantilla requiere una ruta local de Windows."
        else if not (Text.StartsWith(Texto, "\\") or
            (Text.Length(Texto) >= 3 and Text.Middle(Texto, 1, 2) = ":\")) then
        error "Ruta no válida para esta plantilla local de Windows."
        else Text.TrimEnd(Texto, {"\"})
in
    Ruta
```

### RutaEntrada

```powerquery
let
    Ruta = RutaProyecto & "\01_ENTRADA"
in
    Ruta
```

### ArchivosEntrada

```powerquery
let
    // No recorre subcarpetas: evita incorporar archivos archivados por accidente.
    Lectura = try Folder.Contents(RutaEntrada),
    Origen = if Lectura[HasError] then
        error Error.Record("CarpetaEntrada", "No se pudo abrir la carpeta de entrada. Revisa ruta y permisos.", [Ruta = RutaEntrada, Causa = Lectura[Error]])
        else Lectura[Value],
    // Este ejemplo admite SOLO .xlsx. Ajustar si el proyecto usa CSV, XLSB, etc.
    ArchivosValidos = Table.SelectRows(Origen, each
        [Extension] <> null and Text.Lower([Extension]) = ".xlsx"
        and not Text.StartsWith([Name], "~$")
        and [Attributes]?[Hidden]? <> true
        and [Attributes]?[Directory]? <> true),
    Ordenados = Table.Sort(ArchivosValidos, {{"Name", Order.Ascending}}),
    Resultado = if Table.IsEmpty(Ordenados) then
        error "No hay archivos .xlsx válidos en 01_ENTRADA. Revisa los archivos y los filtros."
        else Ordenados
in
    Resultado
```

### Archivo de ejemplo (adaptación opcional)

```powerquery
// Solo si se adapta la consulta auxiliar creada por Combinar archivos.
// Nombre de la consulta existente: Archivo de ejemplo.
// Devuelve el primer binario de la MISMA lista filtrada que usa la principal.
let
    Origen = ArchivosEntrada,
    Binario = Origen{0}[Content]
in
    Binario
```

### ControlArchivos

```powerquery
// Consulta de control: lista los archivos efectivamente seleccionados.
// No contabiliza filas internas de los Excel ni certifica que se transformen bien.
let
    Origen = ArchivosEntrada,
    Resultado = Table.SelectColumns(Origen, {"Name", "Extension", "Folder Path", "Date modified"})
in
    Resultado
```

## 7. Pruebas de aceptación y criterio de cierre

| Prueba | Resultado esperado |
|---|---|
| Recalcular en ubicación original | B2 coincide con la carpeta del libro abierto |
| Actualizar en original | Lista de archivos, esquema, filas y totales conciliados |
| Mover carpeta completa | La copia lee sus propios archivos, sin rutas del origen anterior |
| Actualizar en otro PC/usuario | Accesos y consultas funcionan con controles equivalentes |
| Incorporar archivo nuevo válido | Aparece en inventario y sus filas se transforman según reglas |
| Archivo con columna obligatoria ausente | Error identificable, sin omitir datos silenciosamente |
| Carpeta vacía o ausente | Error o comportamiento documentado que el usuario puede identificar |
| Repetición de pedidos/cortes | Tratamiento según regla aprobada, sin deduplicación inventada |
| Cruces | No multiplican filas/totales sin justificación |
| Entrega | Carpeta completa, versión identificada y hoja INICIO con instrucciones |

Registrar fecha, carpeta, versión de Excel, entradas utilizadas, resultado esperado, obtenido y estado de cada prueba. El cambio de ruta se cierra cuando además de actualizar se confirma el origen efectivo de los datos. La entrega operativa se acepta después de la prueba en el PC destinatario.

### Qué se validó al preparar esta documentación

Se verificó la sintaxis Python del app.py, la conservación del código previo y la existencia del Markdown esperado. Se revisaron la estructura de los ejemplos M y las rutas de ejemplo. No se ejecutó Excel ni el motor de Power Query en este entorno. La prueba de traslado documentada corresponde a las capturas compartidas por el usuario.

## Fuentes oficiales y alcance

- [Excel.CurrentWorkbook](https://learn.microsoft.com/es-es/powerquery-m/excel-currentworkbook): lectura de tablas y rangos con nombre.
- [Folder.Files](https://learn.microsoft.com/es-es/powerquery-m/folder-files): incluye subcarpetas y requiere ruta absoluta.
- [Folder.Contents](https://learn.microsoft.com/es-es/powerquery-m/folder-contents): inventario del nivel de carpeta.
- [Combinación de archivos](https://learn.microsoft.com/es-es/power-query/combine-files-overview): esquema, archivo de ejemplo y auxiliares.
- [Privacidad en Power Query](https://learn.microsoft.com/es-es/power-query/privacy-levels): tratamiento de orígenes.

La estructura de carpetas y los controles propuestos son convenciones de trabajo de esta guía; no requisitos universales impuestos por Microsoft.
