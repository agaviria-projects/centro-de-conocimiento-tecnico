# Generador de Informes ANS - ATC CHEC

----

## 1. Entrada a la reunión

El **Generador de Informes ANS - ATC CHEC** es una herramienta orientada al seguimiento operativo de los acuerdos de nivel de servicio asociados a las conexiones gestionadas por ATC CHEC.

Su función principal es transformar el archivo exportado desde el sistema **GIT** en un informe organizado, validado y preparado para el análisis operativo.

## Durante la presentación de la herramienta se recomienda iniciar con la siguiente explicación:

> El sistema toma la información exportada desde GIT, aplica automáticamente las reglas contractuales y operativas definidas por la organización, calcula el estado de cada solicitud y genera un informe consolidado para facilitar la priorización y el seguimiento de los casos.

La herramienta fue diseñada para que las reglas del negocio puedan administrarse desde archivos de configuración en Excel, evitando depender de modificaciones al software para ajustes funcionales frecuentes.

----

## La herramienta permite:

- Procesar el archivo exportado desde el sistema GIT.
- Calcular automáticamente las fechas límite de atención.
- Determinar los días transcurridos y los días restantes.
- Clasificar cada solicitud según su estado ANS.
- Aplicar reglas especiales de prioridad.
- Generar un archivo consolidado para el seguimiento operativo.
- Actualizar el dashboard de análisis.
- Disminuir el trabajo manual y el riesgo de errores.

----

## 3. Explicación de cada carpeta Principales

## 3.1 Carpeta entrada

La carpeta **entrada** es el punto de inicio del proceso.

En esta ubicación se deben guardar los archivos exportados desde el sistema GIT que correspondan al corte que se desea procesar.

Ejemplo:

```text
entrada/
├── R1.xlsx
└── R2.xlsx


```
## Recomendaciones

El sistema no requiere un nombre específico para los archivos, siempre que:

- Tengan formato Excel compatible.
- Conserven las columnas requeridas.
- Evitar guardar archivos adicionales que puedan generar confusión.
- No se encuentren abiertos durante la ejecución.
- No estén dañados o protegidos con contraseña.
- Verificar que el archivo no se encuentre abierto antes de iniciar el proceso.
- Confirmar que el archivo contenga la información completa.

### Responsabilidad del usuario

El usuario debe asegurarse de que el archivo depositado corresponda a la información oficial exportada desde GIT.

----

## 3.2 Carpeta salida

La carpeta **salida** almacena los archivos generados por la herramienta.

El resultado principal es:

```text
Informe_ANS_ELITE.xlsx
```

Este archivo contiene los registros procesados y los cálculos necesarios para el análisis.

### Información esperada

El informe incluye desde la extracción osea Origen de los datos:

- Id_Orden.
- Fecha_Orden.
- Dirección.
- Propietario.
- Zona.
- Código Municipio.
- Desc. Municipio.
- Observaciones.

Columnas desde el desarrollo:
- Región Origen.
- Tipo.
- Fecha limite ANS.
- Días transcurridos.
- Días restantes.
- Estado del ANS.

### Recomendaciones

- No editar el archivo mientras se esté generando.
- Evitar reemplazarlo manualmente.
- Conservar copias de los informes históricos cuando el proceso lo requiera.
----

## 3.3 Carpeta `dashboard`

La carpeta **dashboard** contiene el archivo utilizado para la consulta y el análisis visual de la información procesada por la herramienta.

El archivo principal es:

```text
INFORME_ANS.xlsb
```
Este archivo permite visualizar de forma rápida el estado general de los pedidos y facilita la priorización de la gestión operativa.

El dashboard presenta los siguientes indicadores:

## KPIS

Total de pedidos.
Pedidos vencidos.
Pedidos en alerta.
Pedidos a tiempo.
Pedidos con atención inmediata.
Pedidos asociados a HV.
Pedidos en factibilidad.

Estos indicadores permiten conocer rápidamente cómo se encuentra distribuida la operación.

## Filtros disponibles

El usuario puede consultar la información mediante filtros como:

- Región.
- Zona.
- Estado.
- Municipio.

Los filtros permiten analizar únicamente los pedidos que cumplen con los criterios seleccionados.

## Gráficos de análisis

El dashboard incluye gráficos que permiten identificar:

- Cantidad de pedidos por estado.
- Distribución porcentual de los pedidos.

Esto facilita la interpretación de la información sin necesidad de revisar toda la base de datos.

## Detalle de pedidos

En la parte inferior se presenta el detalle de los pedidos incluidos en el análisis.

La tabla permite consultar información como:

- ID Orden.
- Fecha Orden.
- Dirección.
- Desc. Municipio.
- Zona.
- Días pactados.
- Fecha límite ANS.
- Días restantes.
- Estado.

Los estados se identifican visualmente mediante colores para facilitar su lectura.

## Uso operativo

El dashboard permite:

- Identificar pedidos vencidos.
- Revisar pedidos próximos al vencimiento.
- Filtrar información por región, zona o municipio.
- Consultar el detalle de cada pedido.
- Priorizar la gestión diaria.
- Facilitar la toma de decisiones.
----

## 3.4 Carpeta config

La carpeta **config** contiene los archivos de parametrización funcional.

El archivo principal es:

```text
DIAS_CONTRACTUALES.xlsx
```

Este archivo administra las reglas que utiliza el sistema para realizar los cálculos.

### Importancia

La configuración permite realizar ajustes funcionales sin modificar el software(los scripts).

Desde este archivo se pueden administrar:

- Municipios.
- Días contractuales.
- Parámetros generales.
- Festivos adicionales.
- Reglas especiales de prioridad.

Importante: Antes de realizar cualquier cambio, se debe crear una copia de respaldo del archivo.

El archivo DIAS_CONTRACTUALES.xlsx contiene las reglas que utiliza la herramienta para calcular y clasificar los pedidos.

Su principal ventaja es que muchos cambios pueden realizarse directamente en Excel, sin modificar los scripts del sistema.

El archivo contiene cuatro hojas principales:

| Hoja | Función |
|---|---|
| `REGLAS_DE_NEGOCIO` | Define los días contractuales según el Municipio y cantidad de Dias. |
| `PARAMETROS` | Contiene los valores generales utilizados por la herramienta. |
| `FESTIVOS_ADICIONALES` | Permite registrar fechas que no deben contarse como días hábiles. |
| `REGLAS_PRIORIDAD` | Identifica los pedidos que requieren atención especial. |

## Hoja REGLAS_DE_NEGOCIO

Esta hoja define cuántos días hábiles tiene cada pedido para ser atendido.

La asignación depende de datos como:

- Municipio.
- Dias 

El usuario autorizado puede:

- Agregar municipios.
- Cambiar días contractuales.

Cuando el sistema encuentra un pedido con esas características, asigna automáticamente los días contractuales correspondientes.

##  Hoja `PARAMETROS`

La hoja **PARAMETROS** contiene las configuraciones generales que controlan cómo se realiza el cálculo del ANS.

Esta hoja es especialmente importante porque define:

- Cuándo un pedido pasa a estado **ALERTA**.
- Si se excluyen los sábados.
- Si se excluyen los domingos.
- Si se excluyen los festivos oficiales de Colombia.
- Si se excluyen los festivos adicionales registrados por el usuario.

----

### Parámetros configurados

| Parámetro | Valor | Función |
|---|---:|---|
| `DIAS_INICIO_ALERTA` | `2` | El pedido pasa a estado ALERTA cuando le quedan 2 días o menos para vencer. |
| `EXCLUIR_SABADOS` | `SI` | Los sábados no se cuentan dentro del cálculo del ANS. |
| `EXCLUIR_DOMINGOS` | `SI` | Los domingos no se cuentan dentro del cálculo del ANS. |
| `EXCLUIR_FESTIVOS_COLOMBIA` | `SI` | Los festivos oficiales de Colombia no se cuentan como días hábiles. |
| `EXCLUIR_FESTIVOS_ADICIONALES` | `SI` | Tampoco se cuentan las fechas registradas en la hoja `FESTIVOS_ADICIONALES`. |

----

### Cómo se interpreta `DIAS_INICIO_ALERTA`

El valor configurado actualmente es:

```text
2

Esto significa:

- Si al pedido le quedan más de 2 días, se clasifica como A TIEMPO.
- Si le quedan 2 días o menos, se clasifica como ALERTA.
- Si supera la fecha límite y los días restantes son negativos, se clasifica como VENCIDO.

```

## Importancia de esta hoja

Esta configuración permite cambiar el comportamiento del cálculo sin modificar el software.

Por ejemplo, si la operación decide que la alerta debe comenzar cuando falten 3 días, solo se cambia:

DIAS_INICIO_ALERTA = 3

## Recomendaciones
- Modificar únicamente la columna VALOR.
- No cambiar los nombres de la columna PARAMETRO.
- Utilizar solamente los valores permitidos, como SI, NO o números.
- Crear una copia de respaldo antes de realizar cambios.
- Verificar el resultado con algunos pedidos de prueba después de modificar un parámetro.

----

## Hoja `FESTIVOS_ADICIONALES`

La hoja **FESTIVOS_ADICIONALES** permite registrar fechas especiales que no deben contarse dentro del cálculo del ANS.

Esta hoja es útil cuando existe un día no laborable que no está incluido en el calendario normal de festivos de Colombia.

----

### Columnas de la hoja

| Columna | Función |
|---|---|
| `FECHA` | Día que no debe contarse como hábil. |
| `DESCRIPCION` | Motivo por el cual la fecha se excluye del cálculo. |
| `ACTIVO` | Indica si la fecha debe aplicarse: `SI` o `NO`. |

----

### Ejemplo

| FECHA | DESCRIPCION | ACTIVO |
|---|---|---|
| 24/12/2026 | Jornada institucional no laborable | SI |
| 31/12/2026 | Cierre operativo autorizado | SI |

----

### Cómo funciona

Cuando una fecha está registrada con el valor:

```text
ACTIVO = SI
```

## Hoja `REGLAS_PRIORIDAD`

La hoja **REGLAS_PRIORIDAD** permite identificar solicitudes que deben recibir un tratamiento especial dentro del cálculo ANS.

Actualmente la hoja contiene reglas como:

| PALABRA_CLAVE | TIPO | DIAS |
|---|---|---:|
| Servicio temporal urbano/Servicio temporal urbano | INMEDIATO | 0 |
| Solicitud de conexión/Habilitación de Vivienda integral urbano | HV | 15 |
| Factibilidad del servicio/Cuenta nueva | FACTIBILIDAD | 4 |

----

### ¿Cómo funciona?

El sistema busca el texto definido en la columna `PALABRA_CLAVE`.

Cuando encuentra una coincidencia, asigna:

- El tipo definido en la columna `TIPO`.
- Los días establecidos en la columna `DIAS`.

Por ejemplo:

- Si encuentra **Servicio temporal urbano**, lo clasifica como `INMEDIATO` y asigna `0` días.
- Si encuentra **Solicitud de conexión** o **Habilitación de Vivienda integral urbano**, lo clasifica como `HV` y asigna `15` días.
- Si encuentra **Factibilidad del servicio** o **Cuenta nueva**, lo clasifica como `FACTIBILIDAD` y asigna `4` días.

----

### Cómo agregar una nueva regla

Para crear una nueva regla:

1. Ir a la primera fila vacía de la tabla.
2. Escribir la palabra o frase que debe identificar el sistema.
3. Definir el tipo de prioridad.
4. Registrar la cantidad de días.
5. Guardar el archivo.

### Ejemplo

| PALABRA_CLAVE | TIPO | DIAS |
|---|---|---:|
| Conexión especial | PRIORITARIO | 2 |

A partir de ese momento, los registros que contengan la expresión **Conexión especial** podrán clasificarse como `PRIORITARIO` con `2` días.

----

### Cómo agregar varias palabras para una misma regla

Cuando varias expresiones deben producir el mismo resultado, pueden escribirse en la misma celda separadas por `/`.

### Ejemplo

```text
Conexión especial/Servicio especial/Atención especial
```

## Cómo modificar una regla

Para cambiar una regla existente:

- Ubicar la fila correspondiente.
- Modificar únicamente la palabra clave, el tipo o los días.
- Guardar el archivo.
- Ejecutar una prueba para validar el resultado.

Por ejemplo, si HV cambia de 15 a 12 días, se modifica únicamente la columna DIAS.

## Cómo eliminar una regla

Existen dos formas:

- Opción 1. Eliminar la fila completa

Se puede eliminar toda la fila de la regla cuando ya no debe utilizarse.

- Opción 2. Borrar el contenido

También se puede limpiar el contenido de las tres columnas de esa fila.

La opción más ordenada es eliminar la fila completa dentro de la tabla y verificar que no queden filas vacías intermedias.

## Riesgo de reglas duplicadas

Si dos reglas contienen palabras similares, un mismo pedido podría coincidir con más de una condición.

Por esta razón, antes de agregar una nueva regla se debe revisar que no exista otra que produzca el mismo resultado.

---

## 4. El Módulo ` Generación mapas`

El Módulo generación **mapas** contiene los archivos relacionados con la visualización geográfica de los pedidos.

Actualmente, el módulo para generar el mapa ya funciona. Sin embargo, la ubicación de los puntos depende de la calidad de las direcciones que vienen en el archivo exportado desde GIT.

Si una dirección está incompleta, abreviada o escrita de forma incorrecta, el sistema puede:

- Ubicar el pedido en un punto equivocado.
- No encontrar la dirección.
- Mostrar una ubicación aproximada.
- Dejar el pedido sin marcar en el mapa.

----

### Situación actual

La funcionalidad del mapa está disponible, pero todavía se debe mejorar la calidad de las direcciones del archivo fuente.

Por esta razón, el mapa debe considerarse actualmente como una herramienta de apoyo y no como la fuente definitiva para confirmar la ubicación exacta de un pedido.

----

### Para obtener mejores resultados

Las direcciones deberían incluir, cuando sea posible:

- Tipo de vía.
- Número de la vía.
- Número de la vivienda o predio.
- Barrio, vereda o sector.
- Municipio.
- Departamento.

### Ejemplo

```text
Dirección incompleta:
CL 23 # 6

Dirección más completa:
CL 23 # 6-15, Barrio Centro, Manizales, Caldas
```
## CONCLUSIÓN 

La herramienta facilita el procesamiento, la organización y la visualización de la información.

Sin embargo, no reemplaza el análisis de la persona responsable del proceso.

Los archivos generados, el dashboard y el mapa sirven como apoyo para:

- Identificar pedidos vencidos o en alerta.
- Filtrar la información.
- Detectar casos prioritarios.
- Revisar posibles inconsistencias.
- Facilitar la toma de decisiones.

La interpretación final de los resultados debe realizarla el usuario encargado, teniendo en cuenta el contexto operativo y la información disponible.

> **Importante:** La herramienta automatiza tareas y reduce el tiempo de análisis, pero la validación, la revisión y la decisión final continúan dependiendo del criterio humano.

---

## 5. Funcionamiento del cálculo ANS

El cálculo ANS determina la fecha máxima de atención y el estado actual de cada solicitud.

### Información mínima requerida

El archivo fuente debe contener los campos necesarios para identificar y calcular cada registro.

Entre los campos principales se encuentran:

- Pedido o identificador de la solicitud.
- Dirección.
- Municipio.
- Actividad.
- Producto.
- Fecha de inicio del ANS.
- Información necesaria para identificar la regla contractual.

### Etapas del cálculo

1. Se identifica la solicitud.
2. Se valida la fecha de inicio del ANS.
3. Se busca la regla contractual aplicable.
4. Se asignan los días contractuales.
5. Se consultan fines de semana y festivos.
6. Se calcula la fecha límite.
7. Se calculan los días transcurridos.
8. Se calculan los días restantes.
9. Se determina el estado del ANS.
10. Se aplican reglas especiales de prioridad.

### Días hábiles

El sistema no cuenta como días hábiles:

- Sábados.
- Domingos.
- Festivos oficiales aplicables.
- Festivos adicionales registrados en la configuración.

### Fecha de inicio

La fecha de inicio corresponde al momento desde el cual comienza a contabilizarse el ANS, de acuerdo con la información exportada desde GIT y las reglas operativas definidas.

### Fecha límite

La fecha límite representa el último día permitido para atender la solicitud dentro del acuerdo de nivel de servicio.

### Días transcurridos

Corresponden a los días hábiles contabilizados desde el inicio del ANS hasta la fecha de corte del informe.

### Días restantes

Corresponden a la diferencia entre la fecha de corte y la fecha límite, expresada en días hábiles.

### Resultado del cálculo

Cada solicitud queda clasificada con información suficiente para responder:

- ¿Cuánto tiempo contractual tenía?
- ¿Cuánto tiempo ha transcurrido?
- ¿Cuánto tiempo queda disponible?
- ¿La solicitud está vencida?
- ¿Requiere atención inmediata?
- ¿Tiene una prioridad especial?

----

