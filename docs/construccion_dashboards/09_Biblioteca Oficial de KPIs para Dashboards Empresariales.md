# KPIs
## Manual Definitivo de Construcción de KPIs con Python para Dashboards Empresariales

> Framework Dashboards Streamlit con Python

Versión 1.0

---

# Introducción

Los indicadores constituyen el corazón de cualquier Dashboard Empresarial.

Un Dashboard sin KPIs es únicamente una colección de tablas y gráficos.

Los KPIs (Key Performance Indicators) transforman grandes volúmenes de datos en información clara, resumida y útil para apoyar la toma de decisiones.

Sin embargo, uno de los errores más comunes durante el desarrollo de Dashboards consiste en creer que un KPI es simplemente un número mostrado dentro de una tarjeta.

Eso es incorrecto.

El número que observa el usuario es únicamente el resultado final de un proceso mucho más amplio que comienza con una necesidad del negocio, continúa con la obtención y transformación de los datos y finaliza con una representación visual fácil de interpretar.

Por esta razón, un desarrollador de Dashboards debe comprender mucho más que la sintaxis de Pandas o Streamlit.

Debe comprender el negocio.

Debe comprender los datos.

Debe comprender la lógica matemática.

Y finalmente debe comprender cómo comunicar correctamente esa información.

Este capítulo tiene precisamente ese objetivo.

No aprenderemos únicamente funciones como:

- count()
- sum()
- mean()
- groupby()

Aprenderemos cómo pensar un KPI.

Cómo diseñarlo.

Cómo documentarlo.

Cómo validarlo.

Cómo implementarlo.

Cómo comprobarlo.

Y finalmente cómo presentarlo dentro de un Dashboard Profesional.

---

# Objetivo del capítulo

Al finalizar este manual serás capaz de:

- Comprender qué es realmente un KPI.
- Diferenciar una métrica de un indicador.
- Diseñar indicadores antes de escribir código.
- Identificar la operación matemática adecuada para cada necesidad.
- Construir KPIs completamente reutilizables.
- Validar la calidad de los datos antes del cálculo.
- Documentar correctamente la regla de negocio.
- Implementar indicadores utilizando Pandas.
- Representar indicadores mediante componentes reutilizables del Framework.
- Construir Dashboards Empresariales con indicadores profesionales.

---

# ¿Qué es un KPI?

KPI significa:

**Key Performance Indicator**

o

**Indicador Clave de Desempeño.**

Un KPI es un indicador diseñado para medir el comportamiento de un proceso mediante una regla matemática aplicada sobre datos confiables.

En otras palabras...

Un KPI resume una realidad compleja en un único valor fácilmente interpretable.

Por ejemplo.

En lugar de revisar veinte mil registros de pedidos, un Dashboard puede mostrar:

```
Pedidos Atendidos

2.548
```

Ese número resume toda la operación.

---

# Un KPI NO es un número

Este concepto es probablemente el más importante de todo el manual.

Muchas personas creen que un KPI es esto:

```
2.548
```

No.

Ese número únicamente representa el resultado.

El KPI completo incluye:

- Necesidad del negocio.
- Regla de negocio.
- Fuente de información.
- Validaciones.
- Limpieza.
- Transformación.
- Operación matemática.
- Formato.
- Visualización.

Cuando alguno de estos elementos falla, el KPI deja de ser confiable.

---

# Ejemplo

Supongamos que un gerente realiza la siguiente pregunta.

> ¿Cuántos pedidos fueron atendidos durante este mes?

Parece una pregunta sencilla.

Sin embargo, antes de escribir una sola línea de código debemos responder muchas preguntas.

¿Dónde están los datos?

¿Existe una columna llamada PEDIDO?

¿Existen pedidos repetidos?

¿Debemos contar registros o pedidos únicos?

¿Existen pedidos anulados?

¿Hay filas vacías?

¿Existen pedidos en prueba?

¿El informe incluye únicamente este mes?

Como puede observarse, responder correctamente la pregunta del negocio requiere mucho más que utilizar `count()`.

---

# Filosofía del Framework

Dentro de este Framework todos los KPIs siguen exactamente la misma arquitectura.

Un KPI nunca comienza escribiendo una tarjeta en Streamlit.

Antes de llegar a la visualización debemos comprender el negocio, construir la lógica del indicador y finalmente mostrar el resultado dentro del Dashboard.

Cada KPI se desarrolla siguiendo tres responsabilidades claramente definidas.

```text
analytics/

        │

        ▼

app.py

        │

        ▼

components/kpis.py

        │

        ▼

Dashboard
```

Esta separación permite que cualquier indicador pueda reutilizarse, mantenerse y validarse fácilmente en cualquier Dashboard.

---

# Arquitectura Oficial para Construir un KPI

Cada nuevo KPI debe construirse siguiendo siempre este proceso.

## Paso 1. Construir el indicador

La lógica del negocio se desarrolla dentro de:

```text
analytics/

└── indicadores.py
```

Aquí se realizan todos los cálculos utilizando Pandas.

Ejemplo.

```python
def calcular_ventas(df):

    return df["Venta"].sum()


def calcular_clientes(df):

    return df["Cliente"].nunique()
```

---

### Responsabilidad

- Construir indicadores.
- Aplicar reglas de negocio.
- Utilizar Pandas.
- Devolver el resultado.

**Nunca debe utilizar Streamlit.**

Osea que no existe:

- st.metric()
- st.write()
- st.dataframe()

Este módulo debe contener únicamente lógica de negocio y cálculos. No debe incluir componentes visuales de Streamlit (st.metric, st.write, st.dataframe, st.plotly_chart, etc.), ya que la presentación pertenece a la capa components/.

---

## Paso 2. Construir el componente visual

La presentación del KPI se desarrolla dentro de:

```text
components/

└── kpis.py
```

Plantilla base.

```python
import streamlit as st


def mostrar_kpi(

    titulo,

    valor,

    icono,

    delta=None,

):

    st.metric(

        label=f"{icono} {titulo}",

        value=valor,

        delta=delta

    )
```

### Responsabilidad

- Dibujar la tarjeta KPI.
- Mostrar iconos.
- Mostrar títulos.
- Mostrar colores y estilos.

**Nunca debe realizar cálculos de negocio.**

---

## Paso 3. Coordinar el Dashboard

El archivo `app.py` actúa como el orquestador del Framework.

Primero importa los cálculos.

```python
from analytics.indicadores import (

    calcular_ventas,

    calcular_clientes,

)
```

Después importa el componente visual.

```python
from components.kpis import mostrar_kpi
```

Obtiene los indicadores.

```python
ventas = calcular_ventas(df)

clientes = calcular_clientes(df)
```

Finalmente los publica en el Dashboard.

```python
col1, col2 = st.columns(2)

with col1:

    mostrar_kpi(

        titulo="Ventas",

        valor=ventas,

        icono="💰"

    )

with col2:

    mostrar_kpi(

        titulo="Clientes",

        valor=clientes,

        icono="👥"

    )
```

### Responsabilidad

- Cargar los datos.
- Invocar los cálculos.
- Enviar los resultados a los componentes.
- Construir el Dashboard.

**No debe contener reglas de negocio complejas.**

---

# Flujo Oficial del Framework

```text
Excel / Base de Datos

        │

        ▼

DataFrame

        │

        ▼

analytics/

Calcula el KPI

        │

        ▼

Resultado

ventas = 458250000

        │

        ▼

app.py

Coordina

        │

        ▼

components/kpis.py

Presenta el KPI

        │

        ▼

Dashboard
```

---

# Plantilla Oficial del Framework

| Archivo | Responsabilidad |
|----------|-----------------|
| `analytics/indicadores.py` | Calcular los indicadores y aplicar las reglas de negocio. |
| `components/kpis.py` | Diseñar y mostrar visualmente los KPIs. |
| `app.py` | Coordinar el Dashboard, invocar los cálculos y enviar los resultados a los componentes visuales. |

---

# Regla de Oro del Framework

Antes de construir un nuevo KPI recuerda siempre esta regla:

- **`analytics/` piensa y calcula.**
- **`app.py` coordina.**
- **`components/` presenta la información.**

Si respetas estas tres responsabilidades, podrás reutilizar la misma arquitectura en cualquier Dashboard desarrollado con Streamlit.

---
---

# Organización de `app.py`

El archivo `app.py` debe mantenerse limpio y organizado.

Su trabajo consiste en coordinar el Dashboard, separando claramente el cálculo de los indicadores de su presentación.

## Paso 1. Calcular los indicadores

Cuando el usuario selecciona el módulo **KPIs**, `app.py` ingresa a esta sección del Dashboard.

```python
# ==========================================================
# MÓDULO KPIs
# ==========================================================

elif opcion == "📊 KPIs":
```

A partir de este punto, el primer paso consiste en obtener todos los indicadores que se mostrarán en el Dashboard.

Para ello, `app.py` invoca las funciones definidas en la capa de análisis (`analytics/indicadores.py`).

```python
# ==========================================================
# CALCULAR INDICADORES
# ==========================================================

ventas = indicadores.calcular_ventas()

clientes = indicadores.calcular_clientes()

promedio = indicadores.calcular_tiempo_promedio()
```

En este punto `app.py` no conoce la lógica del negocio.

Simplemente solicita los resultados a `analytics/indicadores.py`.

---

## Paso 2. Mostrar los KPIs

Después utiliza los componentes visuales para construir el Dashboard.

```python
# ==========================================================
# MOSTRAR KPIs
# ==========================================================

st.subheader("Indicadores Principales")

col1, col2, col3 = st.columns(3)

with col1:

    mostrar_kpi(

        titulo="Ventas",

        valor=ventas,

        icono="💰",

        delta="+12 %"

    )

with col2:

    mostrar_kpi(

        titulo="Clientes",

        valor=clientes,

        icono="👥",

        delta="+8"

    )

with col3:

    mostrar_kpi(

        titulo="Tiempo Promedio",

        valor=promedio,

        icono="⏱",

        delta="-0.8"

    )
```

Observa que este bloque tampoco realiza cálculos.

Únicamente organiza el diseño del Dashboard y envía la información al componente visual.

---

# Flujo final del Framework

```text
analytics/
        │
        │ Calcula
        ▼
Resultados
        │
        ▼
app.py
        │ Coordina
        ▼
components/
        │ Presenta
        ▼
Dashboard
```
---

# Filosofía del Framework

Todos los componentes siguen exactamente la misma filosofía.

| Componente | Responsabilidad |
|------------|-----------------|
| `sidebar.py` | Dibujar el menú lateral. |
| `banner.py` | Dibujar el banner principal. |
| `navigation.py` | Dibujar la navegación principal. |
| `subnavigation.py` | Dibujar la navegación secundaria. |
| `filtros.py` | Mostrar los filtros. |
| `kpis.py` | Mostrar las tarjetas KPI. |
| `graficos.py` | Mostrar los gráficos. |
| `tablas.py` | Mostrar las tablas. |
| `footer.py` | Mostrar el pie de página. |

Cada componente debe tener una única responsabilidad.

Esta separación hace que el Framework sea más limpio, reutilizable y fácil de mantener.

---

# Conclusión

Antes de crear un nuevo componente recuerda siempre este proceso.

```text
1. Definir la responsabilidad.

            ↓

2. Diseñar la función.

            ↓

3. Definir los parámetros.

            ↓

4. Construir el diseño.

            ↓

5. Importarlo desde app.py.

            ↓

6. Reutilizarlo en cualquier Dashboard.
```

Este patrón de diseño se aplica a todos los componentes del Framework y garantiza una arquitectura modular, escalable y fácil de mantener.


# Ciclo de Vida de un KPI

Todo indicador construido mediante este Framework seguirá el siguiente flujo.

```
Necesidad del negocio

        │

        ▼

Fuente de información

        │

        ▼

Obtención de datos

        │

        ▼

Limpieza

        │

        ▼

Validaciones

        │

        ▼

Transformación

        │

        ▼

Regla matemática

        │

        ▼

Resultado

        │

        ▼

Formato

        │

        ▼

Visualización

        │

        ▼

Dashboard Ejecutivo
```

Es importante comprender que únicamente el último paso corresponde al Dashboard.

Todo lo anterior pertenece al proceso de construcción del indicador.

---

# El verdadero trabajo del Analista de Datos

Muchas personas piensan que el trabajo consiste en crear gráficos.

En realidad, el mayor esfuerzo se encuentra antes de llegar a la visualización.

Un buen Analista de Datos dedica la mayor parte del tiempo a:

- Comprender el proceso de negocio.
- Validar la información.
- Detectar errores.
- Definir reglas.
- Construir indicadores confiables.

Una vez terminado ese trabajo, mostrar el resultado en un Dashboard suele convertirse en la parte más sencilla del proyecto.

---

# Conclusión de esta primera parte

Antes de aprender una sola función de Pandas es indispensable comprender que un KPI no nace del código.

Nace de una necesidad del negocio.

A lo largo de este manual construiremos indicadores siguiendo exactamente esa filosofía.

Cada operación matemática será presentada no únicamente desde el punto de vista técnico, sino también desde su aplicación empresarial, permitiendo comprender cuándo utilizarla, cuándo evitarla y cómo transformarla en un indicador profesional dentro de un Dashboard Empresarial.

En la siguiente parte estudiaremos la diferencia entre **Dato**, **Métrica** e **Indicador**, tres conceptos que suelen confundirse y que constituyen la base para construir KPIs verdaderamente útiles para la toma de decisiones.

# Dato, Métrica e Indicador

---

# Introducción

Uno de los errores más comunes durante el desarrollo de Dashboards consiste en utilizar indistintamente los términos **dato**, **métrica** e **indicador**, como si todos significaran lo mismo.

Aunque en muchas organizaciones estos conceptos se utilizan de forma incorrecta, dentro del Framework Dashboards Streamlit cada uno posee un significado específico.

Comprender esta diferencia permitirá construir KPIs correctamente desde el inicio y evitará errores tanto en el análisis como en el desarrollo.

Antes de escribir una sola línea de código debemos entender exactamente qué información estamos observando y cuál es su propósito dentro del negocio.

---

# La Pirámide de la Información

Todo Dashboard profesional transforma la información siguiendo la siguiente jerarquía.

```
                 DECISIÓN

                     ▲

              INDICADOR (KPI)

                     ▲

                 MÉTRICA

                     ▲

                   DATO
```

Mientras más ascendemos dentro de la pirámide, menor es la cantidad de información, pero mayor es su valor para la toma de decisiones.

---

# ¿Qué es un Dato?

Un dato es el elemento más básico de la información.

No posee contexto.

No responde preguntas.

Simplemente representa un valor almacenado.

Ejemplos.

| Pedido | Ciudad | Valor |
|---------|---------|-------:|
|23547891|Medellín|35000|
|23547892|Bogotá|28000|
|23547893|Cali|45000|

Cada fila representa únicamente un dato.

Por sí solo, un dato no permite tomar decisiones.

---

# Características de un Dato

Un dato puede ser:

- Número.
- Texto.
- Fecha.
- Hora.
- Valor monetario.
- Coordenada.
- Código.
- Estado.
- Identificador.

Ejemplos.

```
23547891

Medellín

15/07/2026

$ 45.000

A Tiempo

TPQ282
```

Todos ellos son datos.

Todavía no representan conocimiento.

---

# ¿Qué es una Métrica?

Una métrica es el resultado de aplicar una operación matemática sobre uno o varios datos.

Las métricas responden preguntas sencillas.

Por ejemplo.

- ¿Cuántos pedidos existen?
- ¿Cuánto dinero se facturó?
- ¿Cuántos vehículos participaron?
- ¿Cuál fue el promedio?

Ejemplos.

```
Pedidos

2548
```

```
Ventas

$ 528.000.000
```

```
Vehículos

312
```

Aquí ya existe un cálculo.

Sin embargo, todavía no sabemos si ese resultado es bueno o malo.

---

# Características de una Métrica

Las métricas generalmente provienen de operaciones como:

- count()
- nunique()
- sum()
- mean()
- max()
- min()

Por ejemplo.

```
Total de Pedidos

2548
```

Es una métrica.

No necesariamente es un KPI.

---

# ¿Qué es un Indicador (KPI)?

Un indicador utiliza una o varias métricas para medir el desempeño de un proceso mediante una regla de negocio.

Aquí aparece el contexto.

Supongamos.

```
Pedidos Atendidos

2548
```

Eso continúa siendo una métrica.

Pero ahora agreguemos una meta.

```
Meta

2500 pedidos
```

Ahora podemos responder.

```
2548

>

2500
```

Resultado.

```
Cumplimiento

101.9 %
```

Ahora sí tenemos un KPI.

Porque el negocio ya puede responder una pregunta.

> ¿Estamos cumpliendo el objetivo?

---

# Diferencia entre Métrica e Indicador

Supongamos el siguiente ejemplo.

```
Ventas del mes

$ 285.000.000
```

Esto es una métrica.

Ahora comparemos contra la meta.

```
Meta

$ 250.000.000
```

Resultado.

```
Cumplimiento

114 %
```

Ahora tenemos un indicador.

La diferencia radica en que el KPI interpreta el resultado.

---

# Ejemplo Empresarial

Una empresa posee el siguiente Dashboard.

```
Pedidos

2.350
```

¿Qué significa ese número?

No lo sabemos.

Ahora agreguemos contexto.

```
Meta

2.500
```

Resultado.

```
Cumplimiento

94 %
```

Ahora sí podemos concluir.

La operación se encuentra por debajo de la meta.

Ese porcentaje constituye un verdadero KPI.

---

# Comparación

| Concepto | Ejemplo |
|-----------|----------|
| Dato | Pedido 23547891 |
| Métrica | 2.548 pedidos |
| Indicador | Cumplimiento 94 % |

---

# ¿Por qué esta diferencia es importante?

Porque muchos Dashboards muestran únicamente métricas y las llaman KPIs.

Por ejemplo.

```
Ventas

$ 320.000.000
```

Visualmente parece un KPI.

Sin embargo, todavía no sabemos.

- ¿Es bueno?
- ¿Es malo?
- ¿Es superior al mes pasado?
- ¿Cumple la meta?
- ¿Está creciendo?

Hasta responder alguna de estas preguntas continúa siendo únicamente una métrica.

---

# Regla Fundamental del Framework

Dentro de este Framework seguiremos la siguiente regla.

```
Dato

↓

Operación Matemática

↓

Métrica

↓

Regla de Negocio

↓

Indicador (KPI)

↓

Dashboard
```

Esta filosofía garantiza que todos los indicadores construidos puedan justificarse matemáticamente y verificarse manualmente.

---

# Caso Real

Supongamos el Dashboard de Control ANS.

Datos.

```
Pedido

Estado

Fecha Recepción

Fecha Límite
```

Operación.

```
count()
```

Resultado.

```
Pedidos

2458
```

Todavía es una métrica.

Ahora aplicamos la regla del negocio.

```
Pedidos Atendidos

2458

Pedidos Vencidos

45
```

Calculamos.

```
Cumplimiento

98.17 %
```

Ahora sí existe un KPI.

Ese indicador responde inmediatamente si la operación cumple o no con el nivel de servicio esperado.

---

# Error más común

Uno de los errores más frecuentes consiste en construir Dashboards repletos de métricas sin ningún tipo de interpretación.

Por ejemplo.

```
Ventas

Clientes

Pedidos

Vehículos

Horas
```

Todos muestran números.

Pero ninguno responde una pregunta de negocio.

Un Dashboard profesional debe transformar esos valores en indicadores que permitan evaluar el desempeño del proceso.

---

# Lección Aprendida

Antes de construir cualquier KPI pregúntate siempre:

> ¿Estoy mostrando únicamente una métrica o realmente estoy construyendo un indicador que ayude a tomar decisiones?

Responder correctamente esta pregunta marcará la diferencia entre un Dashboard informativo y un Dashboard verdaderamente ejecutivo.

---

# Resumen

En esta parte aprendimos que:

- Un dato representa información sin contexto.
- Una métrica representa un cálculo matemático.
- Un indicador interpreta una o varias métricas mediante reglas del negocio.
- Todo KPI nace de una necesidad empresarial y no simplemente de una operación matemática.
- Un Dashboard profesional debe mostrar indicadores, no únicamente números.

Con estos conceptos claros, en la siguiente parte aprenderemos cómo identificar correctamente una necesidad del negocio y transformarla en un KPI antes de escribir la primera línea de código.

# Cómo identificar una necesidad del negocio y convertirla en un KPI

---

# Introducción

Uno de los errores más frecuentes al desarrollar un Dashboard consiste en comenzar escribiendo código antes de comprender qué necesita realmente el negocio.

Muchos desarrolladores abren Python, crean un DataFrame y empiezan a utilizar funciones como:

```python
count()

sum()

groupby()

mean()
```

Sin embargo, todavía no saben qué desean medir.

El resultado suele ser un Dashboard lleno de números que, aunque son matemáticamente correctos, no ayudan a tomar decisiones.

Dentro de este Framework seguiremos una filosofía diferente.

Antes de escribir una sola línea de código, aprenderemos a transformar una necesidad del negocio en un KPI.

---

# El origen de todo KPI

Todo KPI nace de una pregunta.

Nunca nace del código.

Nunca nace de Pandas.

Nunca nace de Streamlit.

Siempre nace de una necesidad del negocio.

Por ejemplo.

Un gerente podría preguntar:

- ¿Cuántos clientes compraron este mes?
- ¿Cuánto dinero se vendió?
- ¿Cuál fue el producto más vendido?
- ¿Cuántos pedidos siguen pendientes?
- ¿Cuál fue el tiempo promedio de atención?
- ¿Qué porcentaje de entregas se realizó a tiempo?
- ¿Qué empleado atendió más casos?
- ¿Cuál fue el margen de utilidad?

Cada una de estas preguntas representa una posible necesidad del negocio.

Nuestro trabajo consiste en convertir esa pregunta en un indicador medible.

---

# La metodología oficial del Framework

Antes de programar cualquier KPI responderemos siempre las siguientes preguntas.

```
¿Qué desea conocer el negocio?

        ↓

¿Qué información existe?

        ↓

¿Dónde están los datos?

        ↓

¿Qué columna contiene esa información?

        ↓

¿Qué operación matemática debo utilizar?

        ↓

¿Cómo validaré el resultado?

        ↓

¿Cómo visualizaré el indicador?
```

Este proceso evita construir indicadores incorrectos.

---

# Paso 1. Comprender la necesidad

Supongamos que el Director Comercial realiza la siguiente pregunta.

> ¿Cuánto dinero vendimos durante este mes?

Todavía no debemos pensar en código.

Lo primero consiste en comprender exactamente qué significa la pregunta.

Debemos aclarar aspectos como:

- ¿Qué se considera una venta?
- ¿Existen ventas anuladas?
- ¿Se incluyen devoluciones?
- ¿Qué rango de fechas se utilizará?
- ¿La información proviene de un único sistema?
- ¿Los valores ya están consolidados?

Mientras estas preguntas no estén resueltas, todavía no existe un KPI.

---

# Paso 2. Identificar la información necesaria

Una vez comprendida la necesidad del negocio debemos identificar qué datos permiten responderla.

Ejemplo.

| Fecha | Cliente | Producto | Valor |
|---------|----------|-----------|-------:|
|01/01/2026|Empresa A|Producto X|250000|
|01/01/2026|Empresa B|Producto Y|180000|

Ahora podemos reconocer las columnas disponibles.

- Fecha
- Cliente
- Producto
- Valor

Todavía no realizamos ningún cálculo.

Simplemente identificamos la información.

---

# Paso 3. Identificar la operación matemática

Ahora debemos preguntarnos.

¿Qué operación convierte esos datos en la respuesta que necesita el negocio?

Dependiendo de la pregunta, la operación cambia completamente.

| Pregunta | Operación |
|----------|-----------|
|¿Cuántos registros existen?|Conteo|
|¿Cuánto dinero se vendió?|Suma|
|¿Cuál es el promedio?|Promedio|
|¿Cuál es el mayor valor?|Máximo|
|¿Cuál es el menor valor?|Mínimo|
|¿Cuántos clientes diferentes existen?|Conteo único|
|¿Qué categoría aparece más?|Frecuencia|

Observe que todavía no estamos hablando de Python.

Estamos pensando como analistas.

---

# Paso 4. Validar la información

Un KPI solamente será confiable si los datos también lo son.

Antes de realizar cualquier cálculo debemos revisar aspectos como:

- Valores vacíos.
- Registros duplicados.
- Fechas incorrectas.
- Valores negativos.
- Errores de digitación.
- Información incompleta.
- Datos fuera del rango esperado.

Construir un indicador sobre información incorrecta producirá decisiones incorrectas.

---

# Paso 5. Definir la regla del negocio

Este paso suele confundirse con la operación matemática.

No son lo mismo.

Por ejemplo.

La suma representa únicamente una operación matemática.

La regla del negocio define cuándo esa suma es válida.

Ejemplos de reglas.

- Solo considerar registros activos.
- Excluir anulaciones.
- Analizar únicamente el mes actual.
- Ignorar registros de prueba.
- Incluir únicamente clientes con compras confirmadas.

Estas reglas hacen parte del conocimiento del negocio, no del lenguaje de programación.

---

# Paso 6. Construir el KPI

Solo después de completar los pasos anteriores estaremos listos para construir el indicador.

Observe el flujo completo.

```
Necesidad del negocio

↓

Comprensión del proceso

↓

Identificación de datos

↓

Validación

↓

Regla del negocio

↓

Operación matemática

↓

Resultado

↓

Visualización
```

En este punto el código se convierte únicamente en una herramienta para implementar una solución que ya fue diseñada previamente.

---

# Un error muy común

Imagine que un desarrollador recibe la siguiente solicitud.

> Necesitamos mostrar el número de clientes.

Sin analizar el problema escribe inmediatamente.

```python
df["Cliente"].count()
```

¿Es correcto?

No necesariamente.

La función `count()` contará todos los registros.

Pero el negocio podría estar preguntando realmente:

> ¿Cuántos clientes diferentes compraron?

En ese caso el resultado correcto sería completamente diferente.

Este ejemplo demuestra que comprender la pregunta es más importante que conocer la sintaxis.

---

# Pensar antes de programar

Dentro de este Framework seguiremos siempre esta regla.

```
Nunca elegir la función primero.

Primero comprender la pregunta.

Después seleccionar la operación matemática.
```

Este principio evitará la mayoría de errores en la construcción de KPIs.

---

# Ejercicio Mental

Antes de abrir Python, intenta responder las siguientes preguntas únicamente utilizando lógica.

Pregunta 1.

> ¿Cuántos empleados trabajan actualmente en la empresa?

¿Qué operación utilizarías?

---

Pregunta 2.

> ¿Cuál fue el ingreso total del trimestre?

¿Qué operación matemática sería necesaria?

---

Pregunta 3.

> ¿Cuál fue el tiempo promedio de atención por solicitud?

¿Qué cálculo utilizarías?

---

Pregunta 4.

> ¿Cuál fue el producto más vendido?

¿Qué tipo de análisis requeriría esta pregunta?

---

Pregunta 5.

> ¿Cuántos clientes diferentes realizaron compras durante el año?

¿Qué diferencia existe entre contar registros y contar clientes únicos?

Responder correctamente estas preguntas demuestra que ya estás pensando como un Analista de Datos y no únicamente como un programador.

---

# Lección aprendida

Todo KPI comienza mucho antes del código.

Primero comprendemos el negocio.

Luego analizamos la información disponible.

Después definimos las reglas.

Seleccionamos la operación matemática adecuada.

Y únicamente al final implementamos la solución en Python.

Cuando se sigue esta metodología, los indicadores son mucho más confiables, reutilizables y fáciles de mantener.

---

# Resumen

En esta parte aprendimos que:

- Todo KPI nace de una necesidad del negocio.
- La pregunta del negocio determina la operación matemática.
- La operación matemática no debe elegirse antes de comprender el problema.
- Las reglas del negocio son tan importantes como el cálculo.
- El código representa la última etapa del proceso y no la primera.

En la siguiente parte comenzaremos a estudiar las operaciones matemáticas que permiten construir indicadores empresariales. Empezaremos con la función más utilizada en cualquier Dashboard: **el conteo de registros (`count()`)**, aprendiendo cuándo utilizarla, cuándo evitarla y cómo convertir un simple conteo en un KPI profesional.

# count(): Contar registros correctamente

---

# Introducción

La función **count()** es una de las operaciones más utilizadas al construir KPIs.

Su objetivo consiste en contar la cantidad de valores existentes dentro de una columna.

Aunque parece una función muy sencilla, utilizarla de forma incorrecta puede generar indicadores equivocados.

---

# ¿Qué hace count()?

Cuenta la cantidad de valores **no nulos** de una columna.

Ejemplo.

```python
df["Cliente"].count()
```

Resultado.

```
1250
```

Significa que existen **1.250 registros con información** en la columna **Cliente**.

---

# Sintaxis

```python
df["columna"].count()
```

---

# ¿Cuándo utilizar count()?

Utiliza `count()` cuando necesites conocer la cantidad de registros que contienen información.

Ejemplos.

- Número de pedidos.
- Número de facturas.
- Número de empleados.
- Número de ventas.
- Número de productos registrados.

---

# Ejemplo

Supongamos el siguiente DataFrame.

| Cliente | Ciudad |
|---------|---------|
|Ana|Bogotá|
|Luis|Cali|
|Carlos|Medellín|
|María|Pereira|

Código.

```python
total_clientes = df["Cliente"].count()

print(total_clientes)
```

Resultado.

```
4
```

---

# Aplicación en un KPI

```python
total_clientes = df["Cliente"].count()

st.metric(

    label="Clientes",

    value=total_clientes

)
```

Resultado.

```
👤

Clientes

4
```

---

# Error común

Muchas personas creen que `count()` cuenta filas.

No exactamente.

Cuenta únicamente los valores que **no están vacíos**.

Ejemplo.

| Cliente |
|---------|
|Ana|
|Luis|
||
|María|

Código.

```python
df["Cliente"].count()
```

Resultado.

```
3
```

La fila vacía no se cuenta.

---

# Buenas prácticas

✔ Utiliza `count()` cuando quieras contar valores existentes.

✔ Verifica que la columna no tenga datos vacíos.

✔ Comprueba el resultado con Excel cuando el KPI sea importante.

✔ Utiliza nombres descriptivos para las variables.

```python
total_clientes = df["Cliente"].count()
```

En lugar de.

```python
x = df["Cliente"].count()
```

---

# Resumen

La función `count()` permite contar los valores existentes de una columna.

Es una excelente opción para construir KPIs básicos como:

- Total de clientes.
- Total de ventas.
- Total de pedidos.
- Total de empleados.
- Total de productos.

Sin embargo, recuerda que **count() cuenta registros con datos**, no necesariamente registros únicos.

En la siguiente parte aprenderemos la diferencia entre **count()** y **nunique()**, una de las confusiones más comunes al construir Dashboards Empresariales.

# nunique(): Contar valores únicos

---

# Introducción

En muchos Dashboards no basta con conocer la cantidad total de registros. En numerosas ocasiones, el negocio necesita saber **cuántos elementos diferentes existen**.

Para este tipo de análisis Pandas ofrece la función **`nunique()`**, una de las herramientas más utilizadas en la construcción de KPIs.

---

# ¿Qué hace nunique()?

La función **`nunique()`** cuenta la cantidad de valores **únicos** que existen en una columna, ignorando los registros repetidos.

Es ideal cuando un mismo valor puede aparecer varias veces y solo queremos contarlo una vez.

---

# Sintaxis

```python
df["columna"].nunique()
```

---

# ¿Cuándo utilizar nunique()?

Utiliza `nunique()` cuando necesites conocer la cantidad de elementos diferentes.

Ejemplos.

- Clientes diferentes.
- Productos diferentes.
- Ciudades diferentes.
- Categorías diferentes.
- Vehículos diferentes.
- Empleados diferentes.

---

# Ejemplo

Supongamos el siguiente DataFrame.

| Cliente |
|----------|
|Ana|
|Luis|
|Ana|
|Carlos|
|Luis|
|María|

Código.

```python
clientes_unicos = df["Cliente"].nunique()

print(clientes_unicos)
```

Resultado.

```
4
```

Los clientes únicos son:

- Ana
- Luis
- Carlos
- María

Aunque existen seis registros, únicamente hay cuatro clientes diferentes.

---

# Aplicación en un KPI

```python
clientes_unicos = df["Cliente"].nunique()

st.metric(

    label="Clientes Únicos",

    value=clientes_unicos

)
```

Resultado.

```
👥

Clientes Únicos

4
```

---

# Diferencia entre count() y nunique()

Supongamos el siguiente conjunto de datos.

| Cliente |
|----------|
|Ana|
|Luis|
|Ana|
|Carlos|
|Luis|
|María|

Si utilizamos:

```python
df["Cliente"].count()
```

Resultado.

```
6
```

Porque cuenta todos los registros.

Ahora utilizamos:

```python
df["Cliente"].nunique()
```

Resultado.

```
4
```

Porque cuenta únicamente los valores diferentes.

---

# ¿Cuál debo utilizar?

Depende de la pregunta del negocio.

Pregunta:

> ¿Cuántas compras se realizaron?

Respuesta.

```python
count()
```

Pregunta.

> ¿Cuántos clientes compraron?

Respuesta.

```python
nunique()
```

Siempre analiza primero qué desea conocer el negocio.

---

# Error común

Uno de los errores más frecuentes consiste en utilizar `count()` cuando realmente se desea conocer la cantidad de elementos diferentes.

Por ejemplo.

```
Ventas realizadas

2.350
```

Esto no significa que existan 2.350 clientes.

Es posible que un mismo cliente haya realizado varias compras.

En este caso, el indicador correcto sería:

```python
df["Cliente"].nunique()
```

---

# Buenas prácticas

✔ Utiliza `nunique()` cuando quieras eliminar duplicados de forma lógica.

✔ Comprueba que la columna realmente identifica un elemento único.

✔ No confundas registros con entidades.

✔ Verifica siempre el resultado comparándolo con Excel cuando el KPI sea crítico.

---

# Ejemplo práctico

Imagina una tienda con la siguiente información.

| Factura | Cliente |
|----------|----------|
|1001|Ana|
|1002|Luis|
|1003|Ana|
|1004|Carlos|
|1005|Luis|

Indicadores posibles.

**Total de Facturas**

```python
df["Factura"].count()
```

Resultado.

```
5
```

**Total de Clientes**

```python
df["Cliente"].nunique()
```

Resultado.

```
3
```

Observa cómo dos indicadores diferentes responden preguntas distintas utilizando el mismo conjunto de datos.

---

# Resumen

La función **`nunique()`** permite contar únicamente los valores diferentes de una columna.

Es una función indispensable para construir KPIs relacionados con:

- Clientes únicos.
- Productos diferentes.
- Empleados distintos.
- Vehículos registrados.
- Categorías existentes.
- Ciudades atendidas.

Recuerda siempre esta regla:

- **`count()` → Cuenta registros.**
- **`nunique()` → Cuenta elementos diferentes.**

Elegir la función correcta dependerá de la pregunta que el negocio necesite responder.

---

# Lo que aprendimos

En esta parte comprendimos que no siempre es suficiente contar registros.

Muchas veces el verdadero valor para el negocio está en conocer la cantidad de elementos únicos.

Saber identificar cuándo utilizar `count()` y cuándo utilizar `nunique()` es uno de los primeros pasos para construir KPIs precisos y confiables.

En la siguiente parte aprenderemos la función **`sum()`**, utilizada para calcular totales y construir indicadores relacionados con cantidades, costos, ingresos y cualquier valor numérico acumulado.

# sum(): Calcular Totales

---

# Introducción

Muchos KPIs necesitan calcular un valor acumulado.

Por ejemplo:

- Total de ventas.
- Total de costos.
- Total de ingresos.
- Total de unidades.
- Total de horas.
- Total de kilómetros.

Para este tipo de indicadores utilizamos la función **sum()**.

---

# ¿Qué hace sum()?

Suma todos los valores numéricos de una columna.

---

# Sintaxis

```python
df["columna"].sum()
```

---

# ¿Cuándo utilizarla?

Cuando necesites conocer el valor total de una variable.

Ejemplos:

- Ventas.
- Costos.
- Utilidad.
- Horas trabajadas.
- Producción.
- Inventario.

---

# Ejemplo

| Venta |
|-------:|
|120|
|300|
|180|

```python
total = df["Venta"].sum()

print(total)
```

Resultado

```
600
```

---

# Aplicación en un KPI

```python
ventas_totales = df["Venta"].sum()

st.metric(

    "Ventas",

    f"${ventas_totales:,.0f}"

)
```

---

# Error común

Intentar sumar columnas que contienen texto.

---

# Buenas prácticas

✔ Verificar que la columna sea numérica.

✔ Revisar valores nulos.

✔ Validar el resultado con Excel.

---

# Resumen

Utiliza **sum()** cuando necesites conocer el total acumulado de una variable numérica.

# mean(): Calcular Promedios

---

# Introducción

Los promedios permiten conocer el comportamiento típico de un conjunto de datos.

---

# ¿Qué hace mean()?

Calcula el promedio aritmético.

---

# Sintaxis

```python
df["columna"].mean()
```

---

# ¿Cuándo utilizarla?

- Edad promedio.
- Tiempo promedio.
- Venta promedio.
- Calificación promedio.
- Consumo promedio.

---

# Ejemplo

| Tiempo |
|-------:|
|5|
|8|
|7|

```python
promedio = df["Tiempo"].mean()
```

Resultado

```
6.67
```

---

# KPI

```python
st.metric(

    "Tiempo Promedio",

    round(promedio,2)

)
```

---

# Error común

Aplicar promedios sobre columnas categóricas.

---

# Buenas prácticas

✔ Revisar valores extremos.

✔ Validar que todos los datos tengan la misma unidad.

---

# Resumen

**mean()** permite construir KPIs basados en promedios.

# min(): Valor Mínimo

---

# ¿Qué hace?

Obtiene el valor más pequeño de una columna.

---

# Sintaxis

```python
df["columna"].min()
```

---

# ¿Cuándo utilizarla?

- Precio mínimo.
- Edad mínima.
- Tiempo mínimo.
- Temperatura mínima.

---

# Ejemplo

```python
precio_minimo = df["Precio"].min()
```

---

# KPI

```python
st.metric(

    "Precio Mínimo",

    precio_minimo

)
```

---

# Buenas prácticas

Verificar que la columna sea numérica.

---

# Resumen

Utiliza **min()** cuando necesites conocer el menor valor registrado.

# max(): Valor Máximo

---

# ¿Qué hace?

Obtiene el valor más alto de una columna.

---

# Sintaxis

```python
df["columna"].max()
```

---

# Ejemplo

```python
venta_maxima = df["Venta"].max()
```

Resultado

```
520000
```

---

# KPI

```python
st.metric(

    "Venta Máxima",

    venta_maxima

)
```

---

# Buenas prácticas

Verificar valores atípicos.

---

# Resumen

**max()** identifica el mayor valor dentro de un conjunto de datos.

# median(): La Mediana

---

# Introducción

Cuando existen valores extremadamente altos o bajos, el promedio puede ser engañoso.

En estos casos es preferible utilizar la mediana.

---

# ¿Qué hace?

Obtiene el valor central de una distribución ordenada.

---

# Sintaxis

```python
df["columna"].median()
```

---

# Ejemplo

Datos

```
5

7

8

9

50
```

Promedio

```
15.8
```

Mediana

```
8
```

La mediana representa mucho mejor el comportamiento real.

---

# KPI

```python
st.metric(

    "Tiempo Mediano",

    mediana

)
```

---

# Resumen

Utiliza **median()** cuando existan valores extremos que puedan distorsionar el promedio.

# mode(): Moda

---

# Introducción

La moda representa el valor que más veces aparece.

---

# ¿Qué hace?

Identifica el dato más frecuente.

---

# Sintaxis

```python
df["columna"].mode()
```

---

# Ejemplo

| Ciudad |
|---------|
|Bogotá|
|Cali|
|Bogotá|
|Medellín|
|Bogotá|

Resultado

```
Bogotá
```

---

# ¿Cuándo utilizarla?

- Ciudad más frecuente.
- Producto más vendido.
- Categoría más utilizada.
- Medio de pago más usado.

---

# KPI

```python
ciudad = df["Ciudad"].mode()[0]

st.metric(

    "Ciudad Más Frecuente",

    ciudad

)
```

---

# Error común

Olvidar que puede existir más de una moda.

Por esta razón normalmente se utiliza:

```python
.mode()[0]
```

---

# Resumen

La función **mode()** permite conocer cuál es el valor que aparece con mayor frecuencia dentro de una columna.

# value_counts(): Contar la frecuencia de los valores

---

# Introducción

Muchas veces no basta con conocer el total de registros.

También necesitamos responder preguntas como:

- ¿Qué categoría aparece más?
- ¿Qué producto se vende con mayor frecuencia?
- ¿Cuál es el estado más común?
- ¿Qué ciudad tiene más registros?

Para este tipo de análisis utilizamos **value_counts()**.

---

# ¿Qué hace value_counts()?

Cuenta cuántas veces aparece cada valor dentro de una columna.

---

# Sintaxis

```python
df["columna"].value_counts()
```

---

# ¿Cuándo utilizarla?

- Productos más vendidos.
- Ciudad con mayor cantidad de clientes.
- Estado más frecuente.
- Categoría más utilizada.
- Tipo de documento más común.

---

# Ejemplo

| Ciudad |
|---------|
|Bogotá|
|Cali|
|Bogotá|
|Medellín|
|Bogotá|
|Cali|

Código.

```python
df["Ciudad"].value_counts()
```

Resultado.

```
Bogotá       3

Cali         2

Medellín     1
```

---

# Aplicación en un Dashboard

Permite construir:

- Rankings.
- Top 10.
- Gráficos de barras.
- Gráficos circulares.

---

# Error común

Creer que ordena alfabéticamente.

En realidad ordena por frecuencia.

---

# Buenas prácticas

✔ Ideal para construir rankings.

✔ Muy útil antes de crear gráficos.

✔ Permite detectar rápidamente comportamientos dominantes.

---

# Resumen

Utiliza **value_counts()** cuando quieras conocer qué valores aparecen con mayor frecuencia.

# groupby(): Agrupar información

---

# Introducción

La mayoría de los Dashboards necesitan responder preguntas agrupando información.

Por ejemplo.

- Ventas por ciudad.
- Clientes por región.
- Producción por planta.
- Gastos por departamento.

Para ello utilizamos **groupby()**.

---

# ¿Qué hace groupby()?

Agrupa los registros según una columna para realizar cálculos sobre cada grupo.

---

# Sintaxis

```python
df.groupby("columna")
```

Generalmente se combina con otras funciones.

```python
df.groupby("Ciudad")["Venta"].sum()
```

---

# Ejemplo

| Ciudad | Venta |
|---------|-------:|
|Bogotá|120|
|Bogotá|200|
|Cali|180|
|Cali|90|

Código.

```python
df.groupby("Ciudad")["Venta"].sum()
```

Resultado.

```
Bogotá    320

Cali      270
```

---

# ¿Cuándo utilizarla?

- Ventas por ciudad.
- Costos por departamento.
- Clientes por país.
- Pedidos por vendedor.
- Producción por planta.

---

# Aplicación en un Dashboard

Con groupby() pueden construirse:

- Gráficos de barras.
- Rankings.
- Tablas resumen.
- KPIs por categoría.

---

# Error común

Olvidar indicar qué columna será calculada.

Incorrecto.

```python
df.groupby("Ciudad")
```

Correcto.

```python
df.groupby("Ciudad")["Venta"].sum()
```

---

# Buenas prácticas

✔ Utiliza nombres descriptivos.

✔ Ordena posteriormente los resultados.

✔ Reinicia el índice cuando sea necesario.

---

# Resumen

**groupby()** permite dividir la información en grupos para analizar cada uno por separado.

# agg(): Realizar varios cálculos al mismo tiempo

---

# Introducción

En muchos casos necesitamos obtener varios indicadores de una sola vez.

Por ejemplo.

- Total.
- Promedio.
- Máximo.
- Mínimo.

En lugar de escribir varias líneas utilizamos **agg()**.

---

# ¿Qué hace agg()?

Permite aplicar varias funciones sobre una misma columna.

---

# Sintaxis

```python
df["Venta"].agg(["sum","mean","max","min"])
```

---

# Ejemplo

Código.

```python
df["Venta"].agg(

    [

        "sum",

        "mean",

        "max",

        "min"

    ]

)
```

Resultado.

```
sum

mean

max

min
```

---

# ¿Cuándo utilizarla?

Cuando un Dashboard necesita mostrar varios indicadores relacionados con la misma variable.

---

# Aplicación

Ideal para paneles ejecutivos.

Permite construir rápidamente KPIs como:

- Venta Total.
- Venta Promedio.
- Venta Máxima.
- Venta Mínima.

---

# Buenas prácticas

✔ Agrupar cálculos relacionados.

✔ Mantener nombres claros.

---

# Resumen

**agg()** simplifica el cálculo de múltiples métricas sobre la misma información.

# sort_values(): Ordenar información

---

# Introducción

Un Dashboard rara vez muestra información desordenada.

Generalmente necesitamos ordenar datos para identificar:

- Los mayores.
- Los menores.
- Los mejores.
- Los peores.

---

# ¿Qué hace sort_values()?

Ordena un DataFrame según una columna.

---

# Sintaxis

Ascendente.

```python
df.sort_values("Venta")
```

Descendente.

```python
df.sort_values(

    "Venta",

    ascending=False

)
```

---

# Ejemplo

| Producto | Venta |
|-----------|-------:|
|A|120|
|B|450|
|C|300|

Resultado descendente.

| Producto | Venta |
|-----------|-------:|
|B|450|
|C|300|
|A|120|

---

# ¿Cuándo utilizarla?

- Top 10.
- Bottom 10.
- Ranking de ventas.
- Ranking de clientes.
- Ranking de productos.

---

# Aplicación

Después de ordenar es muy común utilizar:

```python
.head(10)
```

Para obtener el Top 10.

---

# Buenas prácticas

✔ Ordenar antes de graficar.

✔ Utilizar descending cuando se busquen los mejores resultados.

---

# Resumen

**sort_values()** permite construir rankings y priorizar la información.

# pivot_table(): Construir tablas dinámicas

---

# Introducción

Una de las funciones más poderosas de Pandas es **pivot_table()**.

Permite resumir grandes volúmenes de información de forma muy similar a una Tabla Dinámica de Excel.

---

# ¿Qué hace pivot_table()?

Agrupa información y realiza cálculos automáticamente.

---

# Sintaxis

```python
pd.pivot_table(

    df,

    index="Ciudad",

    values="Venta",

    aggfunc="sum"

)
```

---

# Ejemplo

| Ciudad | Venta |
|---------|-------:|
|Bogotá|120|
|Bogotá|200|
|Cali|180|

Resultado.

| Ciudad | Venta |
|---------|-------:|
|Bogotá|320|
|Cali|180|

---

# ¿Cuándo utilizarla?

- Resúmenes ejecutivos.
- Tablas de análisis.
- Informes consolidados.
- Comparativos.

---

# Diferencia con groupby()

**groupby()**

Ideal para análisis durante el procesamiento de datos.

**pivot_table()**

Ideal para presentar información resumida.

---

# Aplicación en un Dashboard

Permite crear:

- Tablas ejecutivas.
- Resúmenes por categoría.
- Comparativos por región.
- Reportes gerenciales.

---

# Buenas prácticas

✔ Utilizar nombres claros para las filas.

✔ Elegir correctamente la función de agregación.

✔ Revisar siempre el resultado antes de visualizarlo.

---

# Resumen

**pivot_table()** es una de las herramientas más importantes para construir Dashboards Empresariales porque transforma miles de registros en información resumida y fácil de interpretar.

Dominar esta función permitirá construir reportes muy similares a las Tablas Dinámicas de Excel, pero completamente automatizados en Python.

---

## Biblioteca Oficial de KPIs para Dashboards Empresariales

# Plantilla 1 - KPI de Conteo

---

# 🎯 Pregunta del negocio

> ¿Cuántos registros existen?

---

# ¿Cuándo utilizarlo?

- Clientes
- Pedidos
- Facturas
- Productos
- Vehículos
- Empleados

---

# Operación

```python
count()
```

---

# Plantilla Python

```python
# ==========================================
# KPI
# Total de Registros
# ==========================================

total = df["Columna"].count()
```

---

# Publicación en Streamlit

```python
st.metric(

    label="Total",

    value=total

)
```

---

# Resultado

```
📦

2.548
```

---

# Personalización

Solo cambia:

```python
df["Columna"]
```

por la columna que deseas contar.

Ejemplo.

```python
df["Cliente"]
```

o

```python
df["Pedido"]
```

---

# Error común

Utilizar count() cuando realmente necesitas contar elementos únicos.

En ese caso utiliza:

```python
nunique()
```

# Plantilla 2 - KPI de Conteo Único

---

# 🎯 Pregunta

> ¿Cuántos elementos diferentes existen?

---

# ¿Cuándo utilizarlo?

- Clientes diferentes.
- Productos diferentes.
- Ciudades.
- Vehículos.
- Categorías.

---

# Operación

```python
nunique()
```

---

# Plantilla Python

```python
# ==========================================
# KPI
# Clientes Únicos
# ==========================================

clientes = df["Cliente"].nunique()
```

---

# Publicación

```python
st.metric(

    "Clientes",

    clientes

)
```

---

# Resultado

```
👥

352
```

---

# Error común

Confundir registros con elementos únicos.

# Plantilla 3 - KPI Monetario

---

# 🎯 Pregunta

> ¿Cuánto dinero se obtuvo?

---

# ¿Cuándo utilizarlo?

- Ventas.
- Costos.
- Utilidades.
- Gastos.
- Compras.

---

# Operación

```python
sum()
```

---

# Plantilla Python

```python
# ==========================================
# KPI
# Ventas Totales
# ==========================================

ventas = df["Venta"].sum()
```

---

# Publicación

```python
st.metric(

    "Ventas",

    f"${ventas:,.0f}"

)
```

---

# Resultado

```
💰

$ 528.000.000
```

---

# Personalización

Cambiar únicamente:

```python
df["Venta"]
```

por cualquier columna numérica.

# Plantilla 4 - KPI Promedio

---

# 🎯 Pregunta

> ¿Cuál es el promedio?

---

# Operación

```python
mean()
```

---

# Plantilla

```python
promedio = df["Tiempo"].mean()
```

---

# Publicación

```python
st.metric(

    "Tiempo Promedio",

    round(promedio,2)

)
```

---

# Resultado

```
⏱

5.43
```

# Plantilla 5 - KPI Máximo

---

# 🎯 Pregunta

> ¿Cuál fue el mayor valor?

---

# Plantilla

```python
maximo = df["Venta"].max()
```

---

# Publicación

```python
st.metric(

    "Venta Máxima",

    f"${maximo:,.0f}"

)
```

# Plantilla 6 - KPI Mínimo

---

# 🎯 Pregunta

> ¿Cuál fue el menor valor?

---

# Plantilla

```python
minimo = df["Venta"].min()
```

---

# Publicación

```python
st.metric(

    "Venta Mínima",

    f"${minimo:,.0f}"

)
```

# Plantilla 7 - KPI Moda

---

# 🎯 Pregunta

> ¿Cuál es el valor más frecuente?

---

# Plantilla

```python
valor = df["Ciudad"].mode()[0]
```

---

# Publicación

```python
st.metric(

    "Ciudad Más Frecuente",

    valor

)
```

# Plantilla 8 - KPI Ranking

---

# 🎯 Pregunta

> ¿Cuáles son los 10 mejores?

---

# Plantilla

```python
ranking = (

    df

    .groupby("Producto")["Venta"]

    .sum()

    .sort_values(

        ascending=False

    )

    .head(10)

)
```

---

# Visualización

Ideal para:

- Tabla.

- Barras.

- Top 10.

# Plantilla 9 - KPI Comparativo

---

# 🎯 Pregunta

> ¿Cómo comparar categorías?

---

# Plantilla

```python
comparativo = (

    df

    .groupby("Categoría")["Venta"]

    .sum()

)
```

---

# Visualización

Ideal para:

- Barras.

- Columnas.

- Tablas.

# Plantilla 10 - KPI Resumen Ejecutivo

---

# 🎯 Pregunta

> ¿Cómo resumir toda la información?

---

# Plantilla

```python
resumen = pd.pivot_table(

    df,

    index="Categoría",

    values="Venta",

    aggfunc="sum"

)
```

---

# Visualización

Ideal para:

- Tablas ejecutivas.

- Reportes.

- Dashboards.

## 📚 Biblioteca Oficial de KPIs Empresariales

# KPI 1 - Cumplimiento de Meta

---

# 🎯 Pregunta del negocio

> ¿Estamos cumpliendo el objetivo establecido?

---

# ¿Qué mide?

Mide el porcentaje de cumplimiento respecto a una meta definida.

Es uno de los KPIs más utilizados en cualquier Dashboard.

---

# Fórmula

Cumplimiento (%) = (Valor Real / Meta) × 100

---

# Plantilla Python

```python
valor_real = 850
meta = 1000

cumplimiento = (valor_real / meta) * 100
```

---

# Publicación

```python
st.metric(

    "Cumplimiento",

    f"{cumplimiento:.1f}%"

)
```

---

# Interpretación

100 % = Meta cumplida

Mayor a 100 % = Meta superada

Menor a 100 % = Meta pendiente

---

# Casos de uso

- Ventas.
- Producción.
- Cumplimiento de presupuesto.
- Objetivos comerciales.
- Proyectos.

# KPI 2 - Variación Porcentual

---

# 🎯 Pregunta

> ¿Cuánto crecimos o disminuimos frente al período anterior?

---

# Fórmula

Variación (%) =

((Actual - Anterior) / Anterior) × 100

---

# Plantilla

```python
actual = 2500

anterior = 2200

variacion = (

    (actual - anterior)

    / anterior

) * 100
```

---

# Publicación

```python
st.metric(

    "Variación",

    f"{variacion:.2f}%"

)
```

---

# Casos

- Crecimiento de ventas.

- Clientes.

- Producción.

- Facturación.

- Inventario.

# KPI 3 - Participación

---

# 🎯 Pregunta

> ¿Qué porcentaje representa cada categoría respecto al total?

---

# Fórmula

Participación =

(Categoría / Total) × 100

---

# Plantilla

```python
ventas_categoria = 250

ventas_totales = 1500

participacion = (

    ventas_categoria

    / ventas_totales

) * 100
```

---

# Publicación

```python
st.metric(

    "Participación",

    f"{participacion:.1f}%"

)
```

---

# Casos

- Participación de mercado.

- Participación por ciudad.

- Participación por vendedor.

- Participación por producto.

# KPI 4 - Ticket Promedio

---

# 🎯 Pregunta

> ¿Cuánto compra en promedio cada cliente?

---

# Fórmula

Ventas Totales

/

Número de Clientes

---

# Plantilla

```python
ventas = df["Venta"].sum()

clientes = df["Cliente"].nunique()

ticket = ventas / clientes
```

---

# Publicación

```python
st.metric(

    "Ticket Promedio",

    f"${ticket:,.0f}"

)
```

---

# Casos

- Comercio.

- Retail.

- Restaurantes.

- Tiendas.

- E-commerce.

# KPI 5 - Productividad

---

# 🎯 Pregunta

> ¿Cuánto produce cada empleado?

---

# Fórmula

Producción

/

Empleados

---

# Plantilla

```python
produccion = df["Produccion"].sum()

empleados = df["Empleado"].nunique()

productividad = (

    produccion

    / empleados

)
```

---

# Publicación

```python
st.metric(

    "Productividad",

    round(productividad,2)

)
```

# KPI 6 - Top 10

---

# 🎯 Pregunta

> ¿Quiénes son los mejores?

---

# Plantilla

```python
top10 = (

    df

    .groupby("Categoría")["Valor"]

    .sum()

    .sort_values(

        ascending=False

    )

    .head(10)

)
```

---

# Visualización

Ideal para:

- Barras.

- Rankings.

- Tablas.


# KPI 7 - Bottom 10

---

# 🎯 Pregunta

> ¿Quiénes presentan el menor desempeño?

---

# Plantilla

```python
bottom10 = (

    df

    .groupby("Categoría")["Valor"]

    .sum()

    .sort_values()

    .head(10)

)
```

# KPI 8 - Crecimiento Acumulado

---

# 🎯 Pregunta

> ¿Cómo ha evolucionado el indicador durante el tiempo?

---

# Plantilla

```python
df["Acumulado"] = (

    df["Valor"]

    .cumsum()

)
```

---

# Visualización

Ideal para:

- Líneas.

- Área.

- Tendencias.

# KPI 9 - Ranking General

---

# 🎯 Pregunta

> ¿Cómo se ordenan todos los elementos?

---

# Plantilla

```python
ranking = (

    df

    .sort_values(

        "Valor",

        ascending=False

    )

)
```

# KPI 10 - Porcentaje de Registros

---

# 🎯 Pregunta

> ¿Qué porcentaje representa cada grupo?

---

# Plantilla

```python
porcentaje = (

    df["Categoría"]

    .value_counts(

        normalize=True

    )

    * 100

)
```

---

# Resultado

```
A

35 %

B

28 %

C

15 %
```

## Catálogo de 100 KPIs Empresariales

# Cómo construir un KPI desde cero

---

# Introducción

Hasta este momento hemos aprendido funciones de Pandas y plantillas reutilizables.

Sin embargo, un Analista de Datos Senior no memoriza KPIs.

Aprende a construirlos.

Cuando un usuario solicita un nuevo Dashboard, normalmente no dice:

> Necesito un count().

Lo que realmente dice es algo como:

> Quiero saber cuántos clientes nuevos tengo.

o

> Quiero conocer cuál vendedor está generando más ventas.

Nuestro trabajo consiste en transformar esa necesidad en un indicador.

---

# Los 7 pasos para construir cualquier KPI

Todo KPI debe construirse siguiendo el mismo proceso.

```
1. Escuchar la necesidad

        ↓

2. Formular la pregunta

        ↓

3. Identificar los datos

        ↓

4. Elegir la operación

        ↓

5. Construir el cálculo

        ↓

6. Validar el resultado

        ↓

7. Publicarlo en el Dashboard
```

Si siempre sigues estos pasos, podrás construir prácticamente cualquier KPI.

---

# Ejemplo 1

## Paso 1

El usuario dice:

> Quiero saber cuántos clientes compraron.

---

## Paso 2

Convertimos esa necesidad en una pregunta.

```
¿Cuántos clientes diferentes realizaron compras?
```

Observa la palabra **diferentes**.

Esa palabra ya nos da una pista.

---

## Paso 3

Buscamos la información.

| Factura | Cliente |
|----------|----------|
|1001|Ana|
|1002|Luis|
|1003|Ana|

La columna importante es:

```
Cliente
```

---

## Paso 4

¿Qué operación responde esa pregunta?

No queremos contar compras.

Queremos contar clientes diferentes.

Entonces utilizamos:

```python
nunique()
```

---

## Paso 5

Construimos el cálculo.

```python
clientes = df["Cliente"].nunique()
```

---

## Paso 6

Validamos.

En Excel contamos los clientes únicos.

Si ambos resultados coinciden, el KPI es correcto.

---

## Paso 7

Lo mostramos.

```python
st.metric(

    "Clientes",

    clientes

)
```

---

# Ya construimos un KPI

Observa algo interesante.

Nunca empezamos escribiendo código.

Primero entendimos el problema.

---

# Ejemplo 2

El gerente pregunta:

> ¿Cuánto dinero vendimos?

---

## Pensamiento

¿Qué quiere saber?

El total de ventas.

---

## ¿Qué columna necesito?

```
Venta
```

---

## ¿Qué operación responde la pregunta?

```
sum()
```

---

## Código

```python
ventas = df["Venta"].sum()
```

---

## Dashboard

```python
st.metric(

    "Ventas",

    f"${ventas:,.0f}"

)
```

---

# Ejemplo 3

Pregunta.

> ¿Cuál fue la venta más alta?

---

Pensamiento.

```
Mayor valor.
```

Operación.

```python
max()
```

Código.

```python
venta_maxima = df["Venta"].max()
```

---

# Ejemplo 4

Pregunta.

> ¿Cuál fue el tiempo promedio?

---

Pensamiento.

```
Promedio.
```

Operación.

```python
mean()
```

Código.

```python
tiempo = df["Tiempo"].mean()
```

---

# Ejemplo 5

Pregunta.

> ¿Qué ciudad aparece más?

---

Pensamiento.

No necesito sumar.

No necesito promediar.

Necesito saber cuál aparece más veces.

Operación.

```python
mode()
```

o

```python
value_counts()
```

Dependiendo del análisis.

---

# La forma correcta de pensar

Cuando recibas un nuevo Dashboard nunca pienses:

```
Voy a usar groupby().
```

Piensa así.

```
¿Qué desea conocer el negocio?
```

↓

```
¿Qué columna contiene esa información?
```

↓

```
¿Qué operación matemática responde esa pregunta?
```

↓

```
Ahora sí escribo el código.
```

Ese es exactamente el proceso que sigue un Analista de Datos Senior.

---

# Regla de Oro

Nunca memorices funciones.

Memoriza preguntas.

Porque las preguntas del negocio son las que determinan el KPI.

---

# Ejercicio

Intenta resolver mentalmente las siguientes preguntas.

## Pregunta 1

¿Cuántos empleados trabajan actualmente?

¿Qué función utilizarías?

---

## Pregunta 2

¿Cuántos empleados diferentes aparecen en la base?

---

## Pregunta 3

¿Cuál fue el salario promedio?

---

## Pregunta 4

¿Cuál fue el salario más alto?

---

## Pregunta 5

¿Cuánto pagó la empresa en salarios?

---

## Pregunta 6

¿Cuál departamento tiene más empleados?

---

## Pregunta 7

¿Cuáles son los cinco departamentos con mayor nómina?

---

# Solución

| Pregunta | Función |
|-----------|----------|
| Total de empleados | count() |
| Empleados diferentes | nunique() |
| Salario promedio | mean() |
| Salario máximo | max() |
| Total salarios | sum() |
| Departamento más frecuente | value_counts() |
| Top departamentos | groupby() + sum() + sort_values() |

---

# Lección aprendida

El secreto para construir KPIs no consiste en memorizar Pandas.

Consiste en aprender a traducir preguntas del negocio en operaciones matemáticas.

Cuando domines esta habilidad, cualquier Dashboard dejará de ser un reto y se convertirá simplemente en un ejercicio de análisis y construcción de indicadores.

# Piensa como un Analista de Datos Senior

---

# Introducción

Cuando una empresa solicita un Dashboard, nunca dice:

> Necesito un `groupby()`.

o

> Quiero un `pivot_table()`.

Eso jamás ocurre.

Lo que realmente dice es algo como:

- ¿Cómo van las ventas?
- ¿Quién está vendiendo más?
- ¿Qué producto genera más ingresos?
- ¿Cuál es el promedio de atención?
- ¿Estamos cumpliendo la meta?
- ¿Dónde están los problemas?

Nuestro trabajo consiste en traducir esas preguntas en indicadores.

Ese es el verdadero trabajo de un Analista de Datos.

---

# El error de un desarrollador junior

Cuando un desarrollador tiene experiencia únicamente programando suele pensar así.

```
Necesito usar groupby().
```

o

```
Voy a hacer un pivot_table().
```

Está comenzando por la herramienta.

No por el problema.

---

# Cómo piensa un Analista Senior

El pensamiento cambia completamente.

```
¿Qué necesita conocer el negocio?
```

↓

```
¿Qué datos tengo disponibles?
```

↓

```
¿Qué operación responde esa pregunta?
```

↓

```
¿Cómo debo mostrar el resultado?
```

↓

```
Ahora escribo el código.
```

Observa que el código aparece al final.

No al principio.

---

# Método Oficial del Framework

Cada vez que construyas un KPI responde estas siete preguntas.

---

## Pregunta 1

### ¿Qué quiere saber el usuario?

Ejemplos.

- Total de clientes.
- Total de ventas.
- Tiempo promedio.
- Producto más vendido.

Nunca escribas código antes de responder esta pregunta.

---

## Pregunta 2

### ¿Dónde está esa información?

Identifica la columna.

Ejemplo.

| Cliente | Venta | Ciudad |
|----------|-------:|---------|

Si quieres calcular ventas.

La columna correcta será:

```
Venta
```

---

## Pregunta 3

### ¿Qué tipo de dato contiene?

Antes de calcular verifica.

¿Es texto?

¿Número?

¿Fecha?

¿Booleano?

No todas las funciones sirven para todos los tipos de datos.

---

## Pregunta 4

### ¿Qué operación matemática responde la pregunta?

Aquí es donde debes pensar.

No memorizar.

Pensar.

---

| Pregunta | Operación |
|----------|-----------|
|¿Cuántos?|count()|
|¿Cuántos diferentes?|nunique()|
|¿Cuánto?|sum()|
|¿Promedio?|mean()|
|¿Mayor?|max()|
|¿Menor?|min()|
|¿Más frecuente?|mode()|
|¿Ranking?|groupby()|
|¿Resumen?|pivot_table()|

---

## Pregunta 5

### ¿El dato necesita validación?

Ejemplos.

¿Existen registros duplicados?

¿Hay valores vacíos?

¿Existen negativos?

¿Hay fechas incorrectas?

Un KPI construido sobre datos incorrectos siempre será incorrecto.

---

## Pregunta 6

### ¿Cómo validaré el resultado?

Antes de publicar cualquier KPI intenta comprobarlo.

Puedes hacerlo mediante.

- Excel.
- SQL.
- Conteo manual.
- Reporte anterior.

Un KPI confiable siempre puede verificarse.

---

## Pregunta 7

### ¿Cuál es la mejor forma de mostrarlo?

No todo debe convertirse en una tarjeta.

---

# ¿Cuándo utilizar una tarjeta?

Cuando el usuario necesite conocer un único valor.

Ejemplos.

```
Ventas

$850.000
```

```
Clientes

325
```

```
Tiempo Promedio

5.8 días
```

---

# ¿Cuándo utilizar una tabla?

Cuando el usuario necesite consultar detalle.

Ejemplo.

```
Cliente

Ciudad

Venta
```

---

# ¿Cuándo utilizar un gráfico?

Cuando el usuario necesite comparar.

Ejemplos.

- Ventas por ciudad.
- Producción por planta.
- Clientes por categoría.

---

# ¿Cuándo utilizar un ranking?

Cuando el usuario quiera responder.

```
¿Quién vende más?
```

```
¿Cuáles son los mejores?
```

```
¿Cuáles son los peores?
```

---

# Un ejemplo completo

Supongamos que el gerente dice.

> Quiero saber cuál ciudad vende más.

No abras Python.

Primero piensa.

---

## Paso 1

¿Qué quiere saber?

```
La ciudad con mayores ventas.
```

---

## Paso 2

¿Qué columnas necesito?

```
Ciudad

Venta
```

---

## Paso 3

¿Qué operación debo utilizar?

Necesito agrupar.

```
groupby()
```

Luego sumar.

```
sum()
```

Después ordenar.

```
sort_values()
```

Finalmente obtener el primero.

```
head(1)
```

---

## Ahora sí escribimos el código

```python
ciudad_top = (

    df

    .groupby("Ciudad")["Venta"]

    .sum()

    .sort_values(

        ascending=False

    )

    .head(1)

)
```

Observa que el código apareció únicamente después del análisis.

---

# Otro ejemplo

Pregunta.

```
¿Cuánto compra en promedio cada cliente?
```

Pensamiento.

¿Qué necesito?

Ventas.

Clientes.

Operación.

```
Ventas Totales

/

Clientes Diferentes
```

Código.

```python
ventas = df["Venta"].sum()

clientes = df["Cliente"].nunique()

ticket = ventas / clientes
```

---

# El verdadero secreto

Con el tiempo descubrirás algo.

Los KPIs cambian.

Los negocios cambian.

Las columnas cambian.

Pero las preguntas siempre terminan siendo muy parecidas.

Si aprendes a interpretar preguntas, nunca tendrás problemas para construir indicadores.

---

# La regla de los cinco segundos

Antes de escribir código detente cinco segundos y pregúntate.

```
¿Qué desea saber realmente el usuario?
```

Esa pequeña pausa evitará la mayoría de errores en el desarrollo de Dashboards.

---

# Los errores más comunes

❌ Empezar escribiendo código.

❌ Elegir una función antes de entender el problema.

❌ No validar los datos.

❌ No comprobar el resultado.

❌ Mostrar métricas sin interpretación.

❌ Construir indicadores que nadie necesita.

---

# Checklist antes de crear un KPI

Antes de implementar un nuevo indicador verifica siempre:

☐ Comprendí la necesidad del negocio.

☐ Identifiqué la columna correcta.

☐ Elegí la operación matemática adecuada.

☐ Validé los datos.

☐ Verifiqué el resultado.

☐ Elegí la mejor visualización.

☐ El KPI responde realmente la pregunta del usuario.

Si todas las respuestas son "Sí", el indicador está listo para formar parte del Dashboard.

---

# Lección aprendida

La diferencia entre un desarrollador y un Analista de Datos no está en conocer más funciones de Pandas.

Está en la capacidad de transformar preguntas del negocio en indicadores confiables.

Cuando aprendas a pensar de esta manera, construir un Dashboard dejará de ser un ejercicio de programación y se convertirá en un proceso de análisis y toma de decisiones.

## PLANTILLAS KPIS

# ==========================================
# KPI
# Ventas Totales
# ==========================================

ventas_totales = df["Venta"].sum()

## Publicación en Streamlit
st.metric(

    label="💰 Ventas Totales",

    value=f"${ventas_totales:,.0f}"

)

