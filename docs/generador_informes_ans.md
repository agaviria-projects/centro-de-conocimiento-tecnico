## 🎯 Objetivo

El Generador de Informes ANS permite consolidar, transformar y analizar la información operativa extraída desde Fénix, con el fin de controlar el cumplimiento de los tiempos contractuales definidos por el cliente.

Este desarrollo ayuda a identificar pedidos:

- A tiempo
- En alerta
- En alerta 0 días
- Vencidos

Además, proporciona herramientas de visualización y geolocalización para facilitar la toma de decisiones operativas.

---


## 📥 Fuente principal

La fuente principal del informe es Fénix.

Desde Fénix se extraen archivos CSV por cada zona operativa.


#### Rango de Fechas

- Fecha Inicial: Día anterior
- Fecha Final: Día actual

#### Estado

- PENDI

#### Conceptos consultados

- PPRG → Pedidos Pendientes por Programar
- PROG → Pedidos Programados

#### Área Operativa

- SUR-ENE

#### Subzonas

Se realiza una extracción independiente para:

- MET → Metropolitana
- OCC → Occidente
- ORI → Oriente
- NDC → Nordeste
- SOE → Suroeste

### Resultado de la extracción

Por cada zona se genera un archivo CSV.

Ejemplo:

- MET.csv
- OCC.csv
- ORI.csv
- NDC.csv
- SOE.csv

Estos archivos son la entrada principal del proceso automatizado desarrollado,posteriormente consolida todos los archivos en una única fuente de información para facilitar el análisis y la construcción del dashboard que sera el INFORME ANS.

### Estados de un pedido

- PPRG → Pedidos Pendientes por Programar(extracción)
- PROG → Pedidos Programados(extracción)
- CUMPL → Cumplido se cumple cuando los técnicos ejecutan la tarea y le envian el informe al programador de la ejecución del pedido.

---

## ⚙️ Proceso del desarrollo

Después de descargar los archivos CSV desde Fénix, todos los archivos se almacenan en una carpeta de trabajo.

Posteriormente se ejecuta el módulo **Generar Informe ANS**, el cual realiza automáticamente las siguientes tareas:

1. Leer los archivos CSV exportados desde Fénix.
2. Unificar la información de todas las zonas operativas.
3. Limpiar y normalizar los datos.
4. Aplicar las reglas contractuales definidas por el cliente.
5. Calcular los días ANS de cada pedido.
6. Clasificar cada pedido según su estado.
7. Construir automáticamente el Informe ANS, incluye el Dashboard y demás elementos de análisis.
8. Publicar el informe final en una carpeta compartida denominada **Informes Fénix**, permitiendo que programadores y demás usuarios de la operación puedan consultar la información para realizar seguimiento y control de los pedidos.
9. En el dia a dia se generan tres extracciones con el fin de mantener el informe permanentemente actualizado.

---
### 📊 Columnas calculadas y enriquecimiento de la información

El proceso genera un archivo consolidado que contiene tanto la información original proveniente de Fénix como nuevas columnas calculadas automáticamente por el sistema.

Estas columnas permiten realizar el seguimiento contractual de los pedidos y constituyen la base para la construcción del Dashboard Control ANS.

Entre las principales columnas se encuentran:

- Fecha Inicio ANS.
- Días Pactados.
- Fecha Límite ANS.
- Días Transcurridos.
- Días Restantes.
- Estado ANS.
- Tipo de Dirección.
- Actividad.
- Zona.
- Municipio.

Toda esta información permite:

- Identificar el estado actual de cada pedido.
- Priorizar la atención de pedidos próximos a vencer.
- Realizar seguimiento contractual de la operación.
- Construir indicadores y tableros de control.
- Facilitar la toma de decisiones por parte de programadores, ingenieros y demás usuarios involucrados en la operación.

Estas columnas transforman la información operativa proveniente de Fénix en información analítica orientada a la gestión y seguimiento del contrato.

## 🧠 Estados ANS generados

### ✅ A TIEMPO

El pedido todavía está dentro del tiempo contractual permitido.

### 🟡 ALERTA

El pedido está próximo a vencer.

### 🟠 ALERTA 0 DÍAS

El pedido vence el mismo día y debe ser priorizado.

### 🔴 VENCIDO

El pedido superó el tiempo contractual permitido.

## 📦 Productos contemplados dentro del contrato

El Informe ANS consolida información correspondiente a todos los diferentes productos operativos definidos dentro del contrato:(Columna O - ACTIVIDAD).

* Prepagos.
* Legalizaciones.
* Movimientos de Redes.
* Puntos de Conexión.
* Movilidad Eléctrica.


### Agrupaciones implementadas : ver archivo C:\Users\hector.gaviria\Desktop\Proyecto_Actas\CONFIG

| Actividad | Agrupado por actividad | Item |
|-----------|------------------------|----------------|
| ACVIS | AGPE | C07R-C07U |
| AORDI | DELINEANTE DE ARQUITECTURA | E05U |
| AORDI | ORDENES INTERNAS | No aplica |
| AORDI | TÉCNICOS GPS | E04R-E04U-E06R-E06U-F07R-F07U |
| AORDI | TECNÓLOGO AIE | E01U-E01R-E02R-E02U |
| AEJDO | HV | No aplica |
| ACAMN-ALECA-ALEGA-ALEGN-LEGM | LEGALIZACIÓN | No aplica |
| VITEC | MOVILIDAD ELÉCTRICA | F01R-F01U |
| AMRTR | MOVIMIENTO DE REDES | D02R-D02U-D03R-D03U-D04R-D04U |
| DIPRE-DSPRE-REEQU | PREPAGO | No aplica |
| ACREV | PUNTOS DE CONEXIÓN | D01R-D01U |

## 📖 Glosario
- **AORDI:** Actividad utilizada para la gestión de órdenes internas.
- **HV:** Habilitación de Vivienda.
- **AGPE:** Autogeneradores de Pequeña Escala.
- **ALEGA:** Legalización residencial.
- **ALEGN:** Legalización No residencial.
- **ALECA:** Reforma residencial.
- **ACAMN:** Reforma No residencial.
- **AEJDO:** Ejecución Habilitación vivienda.
- **ARTER:** Replanteo HV.
- **INPRE:** Ejecución prepago.
- **DIPRE:** Retiro prepago.
- **REEQU:** Trabajo prepago.

---

## 🧮 Cálculo de Días Contractuales

Una vez consolidada la información, el sistema aplica las reglas contractuales definidas para cada actividad operativa.

Estas reglas se encuentran parametrizadas dentro del desarrollo y permiten determinar los días pactados para el cumplimiento de cada pedido.

## ⏳ Días Pactados y Margen Operativo

Cada actividad definida dentro del contrato posee una cantidad máxima de días permitidos para su ejecución.

Estos días corresponden al tiempo contractual establecido por el cliente y pueden variar dependiendo de:

* La actividad ejecutada.
* El tipo de dirección.
* Si el pedido corresponde a zona urbana o rural.

El sistema utiliza esta información para calcular automáticamente las fechas límite ANS y determinar el estado de cada pedido.

Adicionalmente, Elite define tiempos internos de gestión con el fin de anticiparse a posibles incumplimientos contractuales.

Este margen operativo permite identificar oportunamente los pedidos que requieren atención prioritaria antes de alcanzar la fecha límite establecida por el cliente.

### Ejemplos de días pactados

| Actividad | Descripción            | Urbano | Rural |
| --------- | ---------------------- | ------ | ----- |
| ACREV     | Puntos de Conexión     | 4      | 4     |
| ALEGN     | Legalización           | 7      | 10    |
| ALEGA     | Legalización           | 7      | 10    |
| ALECA     | Legalización           | 7      | 10    |
| ACAMN     | Reforma                | 7      | 10    |
| AMRTR     | Movimiento de Red      | 9      | 14    |
| REEQU     | Prepago                | 11     | 11    |
| INPRE     | Instalación Prepago    | 11     | 11    |
| DIPRE     | Desinstalación Prepago | 8      | 11    |
| ARTER     | Replanteo              | 5      | 8     |
| AEJDO     | Ejecución              | 7      | 12    |
| VITEC     | Movilidad Eléctrica    | 2      | 2     |

> **Nota:** El sistema consulta automáticamente esta parametrización para calcular la **Fecha Límite ANS**, los **Días Restantes** y el **Estado ANS** de cada pedido.

---

## 📊 Dashboard

Con base en el archivo procesado, se construye un dashboard para facilitar el análisis.

### Indicadores Principales

El dashboard presenta indicadores en tiempo real para controlar el estado de los pedidos.

Indicadores mostrados en

- Total Pedidos
- Vencidos
- Alerta 0 Días
- Alertas
- A Tiempo

Estos indicadores permiten identificar rápidamente el estado general de la operación.

---

### Segmentadores Disponibles

El usuario puede filtrar la información mediante:

#### Subzona

- Metropolitana Sur
- Metropolitana Norte
- Occidente
- Oriente
- Suroeste

#### Tipo Dirección

- Rural
- Urbana

#### Estado

- Vencido
- Alerta
- Alerta 0 Días
- A Tiempo

#### Concepto

- PROG
- PPRG

#### Actividad

Permite filtrar por la actividad operativa asociada al pedido.

#### Municipio

Permite consultar la información para un municipio específico.

---

### Visualizaciones del Dashboard

#### Gráfico de Barras

Muestra la cantidad de pedidos por estado.

Permite identificar rápidamente:

- Cantidad de pedidos vencidos.
- Cantidad de pedidos en alerta.
- Cantidad de pedidos a tiempo.

#### Gráfico de Torta

Muestra la distribución porcentual de los pedidos por estado.

Permite visualizar el peso de cada estado dentro de la operación.

---

### Tabla de Detalle

El dashboard incorpora una tabla detallada con información como:

- Pedido
- Fecha Inicio ANS
- Dirección
- Municipio
- Actividad
- Concepto
- Días Pactados
- Fecha Límite
- Días Restantes
- Estado
- Subzona

Esta tabla permite realizar análisis detallados y seguimiento individual de cada pedido.

## 🗺️ Mapa de geolocalización

El informe incorpora un módulo de geolocalización que permite visualizar los pedidos sobre el territorio utilizando las coordenadas obtenidas desde Fénix.

Su objetivo es facilitar la gestión operativa, la priorización de pedidos y la ubicación de direcciones en campo.

Al filtrar por subzona se podra generar el mapa exclusivamente para ese filtro aplicado por subzona; generando el mapa y la cantidad de marcadores, puede presentarse que la cantidad de marcadores no sea igual al total de pedidos;  pero esto es debido que desde la extracción en Fenix hayan pedidos sin coordenadas.

### Panel de Control ANS

El mapa incorpora un panel lateral desde donde el usuario puede:

- Buscar un pedido específico.
- Mostrar todos los pedidos.
- Centrar el mapa.
- Copiar el enlace de ubicación.
- Filtrar información.

---

### Filtros Disponibles

La información puede filtrarse por:

- Estado del pedido.
- Concepto.
- Actividad.
- Zona.

Estos filtros permiten analizar sectores específicos de la operación y facilitar la programación de actividades en campo.

### Estados visuales del mapa

Los pedidos se representan mediante marcadores de colores según su estado:

🟢 A TIEMPO

🟡 ALERTA

🟠 ALERTA 0 DÍAS

🔴 VENCIDO

🟣 SIN FECHA

Esto permite identificar visualmente las prioridades operativas dentro del territorio.

---

### Búsqueda de pedidos

El usuario puede ingresar un número de pedido para localizarlo automáticamente dentro del mapa.

Al encontrar el pedido, el sistema centra la visualización sobre la ubicación correspondiente para facilitar su análisis.

---

### Información Disponible por Pedido

Al seleccionar o posicionarse sobre un pedido, el sistema muestra información relevante como:

- Número de pedido.
- Nombre del cliente.
- Dirección.
- Coordenadas.
- Teléfono o celular.
- Estado del pedido.
- Zona.
- Actividad.

---

### Compartir ubicación al técnico

Cada pedido dispone de un enlace de ubicación que puede compartirse mediante:

- WhatsApp.
- Correo electrónico.
- Otros medios de comunicación.

El técnico puede abrir el enlace desde su celular y utilizar aplicaciones de navegación para dirigirse al punto de atención.

---

### Beneficio operativo del mapa

El mapa permite:

- Priorizar pedidos vencidos o críticos.
- Identificar concentraciones de trabajo por zona.
- Optimizar desplazamientos.
- Mejorar la programación de técnicos.
- Reducir tiempos de atención.
- Facilitar la ubicación de direcciones en campo.
- Apoyar la toma de decisiones operativas.


---
# COMO REALIZA LOS CÁLCULOS DE FECHAS LIMITES ANS

### Cálculo de Fecha Límite

Una vez definidos los días pactados, el sistema calcula la fecha límite contractual.

Fórmula conceptual:

Fecha Inicio ANS + Días Pactados = Fecha Límite ANS

Esta fecha representa el último día permitido para cumplir el pedido según las condiciones contractuales.

---

### Cálculo de Seguimiento

Con base en la fecha actual, el sistema calcula:

- Días Transcurridos.
- Días Restantes.
- Estado ANS.

Estas columnas permiten determinar automáticamente si un pedido se encuentra:

- A Tiempo.
- En Alerta.
- En Alerta 0 Días.
- Vencido.

---

### Resultado Final

El archivo consolidado genera información adicional para cada pedido:

- Fecha Inicio ANS.
- Días Pactados.
- Fecha Límite ANS.
- Días Transcurridos.
- Días Restantes.
- Estado ANS.

Estas columnas son la base para la construcción de los indicadores, gráficos y mapas del Dashboard Control ANS.

---

### Resultado Final

El desarrollo genera un archivo consolidado enriquecido con información calculada automáticamente a partir de las reglas contractuales del cliente.

Además de los datos extraídos desde Fénix, el sistema incorpora indicadores de seguimiento que permiten conocer el estado real de cada pedido y alimentar el Dashboard Control ANS.

Este archivo se convierte en la fuente principal para:

- Indicadores de gestión.
- Gráficos de seguimiento.
- Tablas de análisis.
- Geolocalización de pedidos.
- Priorización operativa.
- Control de cumplimiento ANS.

## 🎤 Preguntas que me pueden hacer

### ¿De dónde salen los datos?

Los datos provienen directamente de Fénix mediante una consulta de pendientes en la operación SUR-ENE. Se extraen archivos CSV por cada zona operativa utilizando los conceptos PROG y PPRG.

### ¿Qué recibe Python como entrada?

Python recibe los archivos CSV generados desde Fénix para cada zona operativa y los consolida en una única fuente de información para análisis.

### ¿Por qué se usa Python?

Porque permite automatizar la lectura de varios archivos CSV, consolidar la información, aplicar cálculos de fechas y generar una salida lista para análisis.

### ¿Cuál es la fuente principal?

La fuente principal es Fénix.

### ¿Qué filtros se aplican en la extracción?

Se aplican los filtros PROG y PPRG para identificar pedidos programados y pendientes por programar.

### ¿Cómo se clasifican los estados?

Se clasifican según los días contractuales definidos por el cliente y la fecha límite calculada para cada pedido.

### "¿Cómo sabe el sistema que un pedido está vencido?"

Porque cada actividad tiene días contractuales parametrizados según si la dirección es urbana o rural. El sistema asigna automáticamente los días pactados, calcula la fecha límite y con base en ella determina el estado ANS."

### ¿Qué aporta el mapa?

Permite ubicar geográficamente los pedidos, buscar un pedido específico y compartir la ruta al técnico por WhatsApp.

### ¿Cuál es el mayor beneficio?

Reduce el trabajo manual y permite priorizar los pedidos críticos antes de que se venzan o cuando ya están vencidos.

