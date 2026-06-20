# 📊 Generador de Informes ANS

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

#### Conceptos consultados

- PROG → Pedidos Programados
- PPRG → Pedidos Pendientes por Programar

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

Estos archivos son la entrada principal del proceso automatizado desarrollado en Python.

### ¿Por qué se extrae por zonas?

Fénix genera la información de forma independiente para cada subzona operativa.

Por esta razón el desarrollo posteriormente consolida todos los archivos en una única fuente de información para facilitar el análisis y la construcción del dashboard.

---

## ⚙️ Proceso del desarrollo

Después de descargar los CSV, todos los archivos se guardan en una carpeta de trabajo.

Luego se ejecuta el módulo Generar Informe ANS y se encarga de:

1. Leer los archivos CSV.
2. Unificar la información de todas las zonas.
3. Limpiar y normalizar los datos.
4. Convertir fechas.
5. Aplicar reglas contractuales del cliente.
6. Calcular días ANS.
7. Clasificar cada pedido por estado.
8. Generar el archivo final para análisis.

---
El proceso genera un archivo consolidado que contiene tanto la información original proveniente de Fénix como nuevas columnas calculadas por el sistema.

Estas columnas permiten realizar el seguimiento contractual de los pedidos y constituyen la base para la construcción del Dashboard Control ANS.

Entre las principales columnas generadas se encuentran:

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

Esta información facilita el análisis operativo, la identificación de cada uno de los pedidos y la toma de decisiones por parte de programadores, ingenieros.

## 🧮 Cálculo de Días Contractuales

Una vez consolidada la información, el sistema aplica las reglas contractuales definidas para cada actividad operativa.

Estas reglas se encuentran parametrizadas dentro del desarrollo y permiten determinar los días pactados para el cumplimiento de cada pedido.

### Configuración de actividades

Cada actividad posee una cantidad de días permitidos según:

- Actividad ejecutada.
- Tipo de dirección.
- Urbana.
- Rural.

Ejemplos:

| Actividad | Descripción | Urbano | Rural |
|------------|------------|---------|---------|
| ACREV | Puntos Conexión | 4 | 4 |
| ALEGN | Legalización | 7 | 10 |
| ALEGA | Legalización | 7 | 10 |
| ALECA | Legalización | 7 | 10 |
| ACAMN | Reforma | 7 | 10 |
| AMRTR | Movimiento Red | 9 | 14 |
| REEQU | Prepago | 11 | 11 |
| INPRE | Instalación | 11 | 11 |
| DIPRE | Desinstalar | 8 | 11 |
| ARTER | Replanteo | 5 | 8 |
| AEJDO | Ejecución | 7 | 12 |
| VITEC | Movilidad Eléctrica | 2 | 2 |

---

### Selección automática de días pactados

El sistema identifica:

- Actividad del pedido.
- Tipo de dirección (Urbana o Rural).

Posteriormente asigna automáticamente la cantidad de días pactados correspondiente.

Ejemplo:

Actividad: ALEGA

Dirección: Urbana

Días Pactados: 7

---

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

## 🧠 Estados ANS generados

### ✅ A TIEMPO

El pedido todavía está dentro del tiempo contractual permitido.

### 🟡 ALERTA

El pedido está próximo a vencer.

### 🟠 ALERTA 0 DÍAS

El pedido vence el mismo día y debe ser priorizado.

### 🔴 VENCIDO

El pedido superó el tiempo contractual permitido.

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

