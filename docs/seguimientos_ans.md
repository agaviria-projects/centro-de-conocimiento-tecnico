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

## 31. Preguntas frecuentes

### ¿El archivo original se modifica?

No. El archivo FENIX se utiliza como fuente y no se altera.

### ¿Qué sucede si falta una columna?

El validador detiene la ejecución e informa la inconsistencia.

### ¿Se pueden revisar los correos antes de enviarlos?

Sí. Para eso se utiliza el modo revisión.

### ¿El sistema puede enviar los correos automáticamente?

Sí. El modo de envío automático utiliza los destinatarios y reglas configurados.

### ¿Se puede generar un solo correo de prueba?

Sí. Se activa la opción **Procesar únicamente el primer correo**.

### ¿Dónde se guardan los archivos HTML?

En:

```text
modules/informe_ans/salida/html/
```

### ¿Se pueden agregar nuevos grupos?

Sí. Las reglas se administran desde los archivos de configuración.

### ¿Por qué se utiliza HTML?

Porque permite construir correos con:

- Indicadores.
- Colores.
- Tablas.
- Encabezados.
- Observaciones.
- Diseño compatible con Microsoft Outlook.

### ¿Por qué el tiempo de la consola puede ser menor a cinco minutos?

Porque la consola mide principalmente la ejecución técnica. Los cinco minutos corresponden al ciclo operativo completo, incluida la revisión.

---

## 32. Resumen final

**Seguimiento ANS** convierte un procedimiento manual en un proceso automatizado, controlado y reutilizable.

La solución:

- Procesa el archivo FENIX.
- Aplica reglas operativas.
- Clasifica estados ANS.
- Genera indicadores.
- Construye correos profesionales.
- Permite revisar o enviar.
- Presenta resultados.
- Se ejecuta directamente desde DataSuite.

El desarrollo no solo reduce tiempo: también crea una base técnica para incorporar históricos, comparación entre cortes, alertas y trazabilidad.
