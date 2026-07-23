# 10 - Filtros Profesionales para Dashboards

---

# Plantilla Oficial del Framework

# `components/filtros.py`

---

# Objetivo

Después de conocer los principales controles y patrones de diseño, el siguiente paso consiste en construir una plantilla reutilizable que sirva como punto de partida para cualquier Dashboard desarrollado con este Framework.

Esta plantilla reúne las mejores prácticas vistas durante el capítulo y establece una estructura estándar para implementar filtros de forma organizada y escalable.

La recomendación es reutilizar este archivo en todos los proyectos futuros, adaptando únicamente los nombres de las columnas y los filtros requeridos por cada Dashboard.

---

# Ubicación dentro del proyecto

```text
Proyecto

│

├── app.py

│

├── analytics/

│

├── components/

│      filtros.py

│      sidebar.py

│      banner.py

│      kpis.py

│      tablas.py

│      graficos.py
```

---

# Responsabilidad

El archivo `filtros.py` tiene una única responsabilidad:

✔ Mostrar los filtros.

✔ Aplicar los filtros.

✔ Devolver un único:

```python
df_filtrado
```

No debe:

- Calcular KPIs.
- Construir gráficos.
- Mostrar tablas.
- Leer archivos.
- Contener reglas de negocio.

---

# Flujo del Framework

```text
Excel

↓

DataFrame Original

↓

components/filtros.py

↓

DataFrame Filtrado

↓

analytics/

↓

components/

↓

Dashboard
```

---

# Estructura recomendada

```python
import streamlit as st

def mostrar_filtros(df):

    # ======================================================
    # BARRA DE FILTROS
    # ======================================================

    ...

    # ======================================================
    # APLICAR FILTROS
    # ======================================================

    ...

    return df_filtrado
```

La función debe ser sencilla, clara y fácil de mantener.

---

# Integración con app.py

```python
df = cargar_datos()

df_filtrado = mostrar_filtros(df)

kpis = calcular_kpis(df_filtrado)

mostrar_kpis(kpis)

mostrar_graficos(df_filtrado)

mostrar_tablas(df_filtrado)
```

Observe que `app.py` únicamente coordina el flujo del Dashboard.

---

# Orden recomendado de los filtros

Cuando el Dashboard tenga varios filtros, utilice el siguiente orden:

1. Fecha
2. Zona
3. Estado
4. Cliente
5. Proyecto
6. Técnico
7. Actividad
8. Otros filtros específicos

Este orden facilita la navegación y mantiene una experiencia consistente entre proyectos.

---

# Recomendaciones

✔ Utilizar un único `df_filtrado`.

✔ Mantener el DataFrame original sin modificaciones.

✔ Centralizar todos los filtros en un único archivo.

✔ Aplicar primero los filtros generales y luego los específicos.

✔ Utilizar nombres descriptivos para cada filtro.

✔ Reutilizar esta plantilla en todos los Dashboards.

---

# Checklist Final del Capítulo

Antes de comenzar un nuevo Dashboard verifica que:

☐ Existe el archivo `components/filtros.py`.

☐ Todos los filtros se implementan en ese archivo.

☐ `app.py` únicamente orquesta el proceso.

☐ Existe un único `df_filtrado`.

☐ Analytics recibe `df_filtrado`.

☐ KPIs utilizan `df_filtrado`.

☐ Gráficos utilizan `df_filtrado`.

☐ Tablas utilizan `df_filtrado`.

☐ No existen filtros duplicados.

☐ La arquitectura del Framework se mantiene.

---

# Introducción

Los filtros constituyen uno de los componentes más importantes de cualquier Dashboard empresarial.

Aunque visualmente parecen controles simples, como listas desplegables, calendarios o casillas de selección, representan el principal mecanismo de interacción entre el usuario y la información.

Un Dashboard sin filtros obliga al usuario a analizar la totalidad de los datos disponibles, incluso cuando únicamente necesita consultar una pequeña parte de ellos.

Por el contrario, un Dashboard correctamente diseñado permite reducir la información a un subconjunto específico mediante filtros intuitivos, obteniendo análisis más rápidos, claros y precisos.

Dentro del **Framework de Dashboards** desarrollado en este Centro de Conocimiento Técnico, los filtros forman parte de la arquitectura oficial y cumplen una responsabilidad claramente definida: producir un **DataFrame filtrado** que será utilizado por todos los componentes del Dashboard.

---

# Objetivo del capítulo

Al finalizar este capítulo el desarrollador será capaz de:

- Comprender la función de los filtros dentro del Framework.
- Identificar qué tipo de filtro utilizar según el escenario de negocio.
- Implementar filtros siguiendo la arquitectura oficial.
- Aplicar filtros sin modificar el DataFrame original.
- Construir Dashboards reutilizables mediante plantillas listas para copiar y pegar.

Este capítulo no pretende únicamente enseñar los controles disponibles en Streamlit, sino proporcionar una biblioteca de filtros profesionales que sirva como base para futuros desarrollos.

---

# ¿Por qué son importantes los filtros?

En un entorno empresarial es poco frecuente que un usuario necesite consultar toda la información disponible.

Generalmente necesita responder preguntas muy específicas.

Por ejemplo:

- Consultar únicamente la información de la zona **METROPOLITANO**.
- Revisar los pedidos con estado **Vencido**.
- Analizar únicamente el mes de junio.
- Visualizar la información correspondiente a un único cliente.
- Consultar únicamente una regional.
- Revisar los datos de un proyecto específico.

Sin filtros, el Dashboard mostraría miles de registros innecesarios, dificultando el análisis y aumentando el tiempo requerido para encontrar la información correcta.

Los filtros permiten reducir el conjunto de datos antes de realizar cualquier cálculo, logrando que los indicadores, gráficos y tablas reflejen únicamente la información solicitada por el usuario.

---

# Filosofía del Framework

Dentro de este Framework existe una regla fundamental:

> **Los filtros no calculan información.**

Su única responsabilidad consiste en determinar qué información será utilizada posteriormente por el Dashboard.

Por esta razón, un filtro nunca debe:

- Calcular indicadores.
- Construir gráficos.
- Generar tablas.
- Modificar reglas de negocio.
- Alterar el DataFrame original.

Su función consiste únicamente en producir un **DataFrame filtrado**.

Ese DataFrame será posteriormente utilizado por:

- KPIs
- Indicadores
- Gráficos
- Tablas
- Reportes

Esta separación de responsabilidades permite construir Dashboards escalables, fáciles de mantener y reutilizables.

---

# Responsabilidad de los filtros dentro del Framework

Los filtros representan el punto de entrada al análisis de datos.

Todo el Dashboard debe construirse a partir del resultado obtenido después de aplicar los filtros.

El flujo de trabajo siempre será el siguiente:

```text
Usuario

        │

        ▼

Selecciona filtros

        │

        ▼

DataFrame Filtrado

        │

 ┌──────┼─────────────┐

 ▼      ▼             ▼

KPIs  Gráficos     Tablas
```

Es importante comprender que los filtros no generan información nueva.

Únicamente reducen el conjunto de datos sobre el cual trabajará el resto del Dashboard.

---

# Beneficios de utilizar filtros

Implementar correctamente los filtros aporta múltiples ventajas al Dashboard.

## Mejor experiencia para el usuario

El usuario puede consultar únicamente la información que necesita, evitando navegar entre grandes volúmenes de datos.

---

## Mayor velocidad

Al trabajar sobre un subconjunto de registros, los cálculos, tablas y gráficos requieren menos tiempo de procesamiento.

---

## Indicadores más precisos

Todos los KPIs reflejan exactamente la información seleccionada por el usuario.

---

## Reutilización del código

Un mismo Dashboard puede adaptarse a diferentes escenarios sin modificar la lógica del negocio.

---

## Escalabilidad

La arquitectura basada en filtros facilita agregar nuevos módulos, indicadores y visualizaciones sin reescribir el código existente.

---

# Casos de uso más comunes

Durante el desarrollo de un Dashboard empresarial es habitual utilizar filtros como los siguientes:

| Tipo de filtro | Ejemplo |
|----------------|----------|
| Zona | METROPOLITANO, OCCIDENTE, ORIENTE, SUROESTE |
| Estado | A tiempo, Alerta, Alerta Cero Días, Vencidos |
| Cliente | Cliente A, Cliente B |
| Proyecto | Proyecto 1, Proyecto 2 |
| Fecha | Día, Mes, Año |
| Técnico | Juan Pérez |
| Regional | Norte, Centro, Sur |
| Actividad | Instalación, Retiro, Reparación |

Estos filtros podrán utilizarse de forma individual o combinada dependiendo de las necesidades del Dashboard.

---

# Qué aprenderemos en este capítulo

Durante este capítulo construiremos una **Biblioteca Oficial de Filtros** para el Framework.

Cada tipo de filtro incluirá:

- Explicación funcional.
- Cuándo utilizarlo.
- Arquitectura dentro del Framework.
- Flujo de funcionamiento.
- Plantilla oficial lista para copiar y pegar.
- Ejemplos reales.
- Buenas prácticas.
- Errores comunes.
- Recomendaciones de implementación.

El objetivo es que este documento sirva como una guía práctica para desarrollar cualquier Dashboard futuro, reutilizando plantillas previamente validadas.

---

# Regla de Oro del capítulo

> **Todo Dashboard debe trabajar sobre un único DataFrame filtrado.**

Nunca deben existir DataFrames diferentes para los KPIs, los gráficos y las tablas, ya que esto puede generar inconsistencias en la información mostrada al usuario.

Todos los componentes del Dashboard deben consumir exactamente el mismo **DataFrame filtrado**, garantizando que toda la información presentada sea consistente.

---

## Próximo tema

En la siguiente sección construiremos la **Arquitectura Oficial de los Filtros**, donde aprenderemos:

- Dónde deben implementarse los filtros dentro del Framework.
- Cómo interactúan `app.py`, `analytics` y `components`.
- Cuál es el flujo oficial desde el DataFrame original hasta el Dashboard.
- La primera plantilla oficial reutilizable para cualquier proyecto.


---

# Arquitectura Oficial de los Filtros

---

# Objetivo

Antes de implementar cualquier filtro es necesario comprender dónde debe ubicarse dentro de la arquitectura del Framework.

Uno de los errores más comunes al desarrollar Dashboards consiste en mezclar la lógica de los filtros con la lógica del negocio o con los componentes visuales.

El Framework propuesto en este Centro de Conocimiento Técnico establece una arquitectura clara, donde cada archivo tiene una única responsabilidad.

Esta separación facilita el mantenimiento del código, mejora la reutilización y permite escalar el Dashboard sin modificar la estructura existente.

---

# Arquitectura Oficial

El flujo oficial del Framework será el siguiente:

```text
Excel

        │

        ▼

DataFrame Original

        │

        ▼

app.py

(Muestra filtros)

        │

        ▼

DataFrame Filtrado

        │

        ▼

analytics/

(Calcula indicadores)

        │

        ▼

components/

(Muestra Dashboard)

        │

        ▼

Usuario
```

---

# Responsabilidad de cada carpeta

## app.py

Es el orquestador del Dashboard.

Sus responsabilidades son:

- Cargar la información.
- Mostrar los filtros.
- Aplicar los filtros.
- Obtener el DataFrame filtrado.
- Solicitar indicadores.
- Mostrar componentes.

Nunca debe contener reglas de negocio complejas.

---

## analytics/

Contiene toda la lógica del negocio.

Ejemplos:

```text
analytics/

indicadores.py

estadisticas.py

comparativos.py
```

Aquí se realizan cálculos como:

- Total de ventas.
- Promedios.
- Cantidades.
- Porcentajes.
- Rankings.
- KPIs.

Siempre reciben como entrada:

```python
df_filtrado
```

Nunca el DataFrame original.

---

## components/

Contiene únicamente componentes visuales.

Ejemplos:

```text
components/

sidebar.py

banner.py

navigation.py

subnavigation.py

kpis.py

graficos.py

tablas.py
```

Estos componentes nunca deben realizar cálculos.

Únicamente reciben información y la muestran al usuario.

---

# ¿Dónde deben implementarse los filtros?

Dentro del Framework existen dos alternativas.

## Alternativa 1

Dashboard pequeño.

Los filtros pueden implementarse directamente en:

```text
app.py
```

Es la opción recomendada cuando el Dashboard posee pocos filtros.

---

## Alternativa 2 (Recomendada)

Dashboard empresarial.

Crear un archivo exclusivo para los filtros.

```text
components/

filtros.py
```

Luego, desde `app.py`, únicamente se invoca la función correspondiente.

```python
df_filtrado = mostrar_filtros(df)
```

Esta arquitectura facilita el mantenimiento cuando el Dashboard crece.

---

# Plantilla Oficial Nº 1

## Dashboard pequeño

```text
app.py
```

```python
# ==========================================================
# CARGAR DATOS
# ==========================================================

df = cargar_datos()

# ==========================================================
# FILTROS
# ==========================================================

...

# ==========================================================
# APLICAR FILTROS
# ==========================================================

...

# ==========================================================
# CALCULAR INDICADORES
# ==========================================================

...

# ==========================================================
# MOSTRAR DASHBOARD
# ==========================================================

...
```

Esta plantilla es ideal para Dashboards con pocos filtros.

---

# Plantilla Oficial Nº 2

## Dashboard empresarial

Estructura recomendada:

```text
Proyecto

│

├── app.py

│

├── analytics/

│      indicadores.py

│      estadisticas.py

│

├── components/

│      filtros.py

│      banner.py

│      sidebar.py

│      kpis.py

│      graficos.py

│      tablas.py
```

---

## app.py

```python
df = cargar_datos()

df_filtrado = mostrar_filtros(df)

ventas = indicadores.calcular_ventas(df_filtrado)

clientes = indicadores.calcular_clientes(df_filtrado)

mostrar_kpis()

mostrar_graficos()

mostrar_tablas()
```

Observe que `app.py` nunca conoce cómo funciona cada filtro.

Únicamente recibe el DataFrame filtrado.

---

## components/filtros.py

Aquí se implementan todos los controles del usuario.

Por ejemplo:

```python
def mostrar_filtros(df):

    ...

    return df_filtrado
```

El resto del Dashboard nunca necesita conocer cómo fueron aplicados los filtros.

---

# Flujo Oficial del Framework

```text
DataFrame Original

        │

        ▼

mostrar_filtros(df)

        │

        ▼

DataFrame Filtrado

        │

 ┌──────┼─────────────┐

 ▼      ▼             ▼

KPIs  Gráficos     Tablas
```

Todos los componentes deben trabajar exactamente con el mismo DataFrame filtrado.

---

# Regla Arquitectónica

Dentro del Framework únicamente debe existir un DataFrame filtrado.

Nunca deben crearse diferentes filtros para:

- KPIs.
- Tablas.
- Gráficos.

Todos deben utilizar:

```python
df_filtrado
```

Esto garantiza que toda la información mostrada al usuario sea consistente.

---

# Próximo tema

En la siguiente sección construiremos la **Biblioteca Oficial de Plantillas de Filtros**, comenzando con el **Selectbox**, donde aprenderemos:

- Cuándo utilizarlo.
- En qué escenarios empresariales aplica.
- Cómo implementarlo.
- Variantes reutilizables.
- Buenas prácticas.
- Errores comunes.

# Biblioteca Oficial de Plantillas de Filtros

---

# Introducción

A partir de esta sección construiremos una colección de plantillas reutilizables para el Framework.

Cada plantilla ha sido diseñada siguiendo la arquitectura oficial presentada en los capítulos anteriores.

El objetivo consiste en que el desarrollador no tenga que escribir nuevamente la lógica de cada filtro, sino reutilizar plantillas previamente validadas y adaptarlas al nuevo Dashboard.

Cada plantilla responderá las siguientes preguntas:

- ¿Cuándo utilizar este filtro?
- ¿En qué archivo debe implementarse?
- ¿Qué información necesita?
- ¿Qué devuelve?
- ¿Cómo afecta el Dashboard?
- ¿Cuál es la mejor práctica recomendada?

---

# Plantilla Oficial 01

# Selectbox

---

# ¿Qué es?

El Selectbox permite que el usuario seleccione un único valor dentro de una lista de opciones.

Es el filtro más utilizado en Dashboards empresariales.

Cuando únicamente puede existir una selección activa, el Selectbox representa la mejor alternativa.

---

# ¿Cuándo utilizarlo?

Se recomienda utilizar un Selectbox cuando el usuario debe escoger un único elemento.

Por ejemplo:

- Zona
- Regional
- Cliente
- Proyecto
- Ciudad
- Estado
- Contratista
- Año
- Mes
- Centro de costos

---

# Ejemplo empresarial

Supongamos que el Dashboard contiene información de cuatro zonas operativas.

```text
METROPOLITANO

OCCIDENTE

ORIENTE

SUROESTE
```

El usuario únicamente desea consultar una de ellas.

En este escenario el Selectbox es el filtro más apropiado.

---

# ¿Dónde debe implementarse?

## Dashboard pequeño

```text
app.py
```

---

## Dashboard empresarial

```text
components/

└── filtros.py
```

Posteriormente será llamado desde:

```python
app.py
```

---

# Flujo del Selectbox

```text
Usuario

        │

        ▼

Selecciona

METROPOLITANO

        │

        ▼

Selectbox

        │

        ▼

DataFrame Filtrado

        │

 ┌──────┼───────────────┐

 ▼      ▼               ▼

KPIs  Gráficos      Tablas
```

Observe que el filtro nunca modifica el DataFrame original.

Únicamente produce un nuevo DataFrame filtrado.

---

# Información necesaria

Para implementar correctamente un Selectbox se requiere:

- Un DataFrame.
- Una columna sobre la cual filtrar.
- Un valor seleccionado por el usuario.

Ejemplo:

```python
df["ZONA"]
```

---

# Plantilla Oficial

```python
# ==========================================================
# FILTRO POR ZONA
# ==========================================================

zonas = [

    "Todas",

    *sorted(

        df["ZONA"]

        .dropna()

        .unique()

    )

]

zona = st.selectbox(

    "📍 Zona",

    zonas

)

df_filtrado = df.copy()

if zona != "Todas":

    df_filtrado = df_filtrado[

        df_filtrado["ZONA"] == zona

    ]
```

---

# ¿Qué hace esta plantilla?

## Paso 1

Obtiene todos los valores únicos de la columna.

```python
df["ZONA"].unique()
```

---

## Paso 2

Elimina valores nulos.

```python
.dropna()
```

---

## Paso 3

Ordena alfabéticamente.

```python
sorted(...)
```

---

## Paso 4

Agrega la opción:

```text
Todas
```

permitiendo visualizar el Dashboard completo.

---

## Paso 5

Crea una copia del DataFrame.

```python
df.copy()
```

Esto evita modificar la información original.

---

## Paso 6

Aplica el filtro.

```python
df_filtrado
```

El resto del Dashboard trabajará únicamente con este DataFrame.

---

# Integración con app.py

Después de aplicar el filtro, el flujo recomendado será:

```python
df = cargar_datos()

...

df_filtrado = aplicar_filtro_zona(df)

ventas = indicadores.calcular_ventas(

    df_filtrado

)

clientes = indicadores.calcular_clientes(

    df_filtrado

)

mostrar_kpis()

mostrar_graficos()

mostrar_tablas()
```

Observe que todos los componentes reciben exactamente el mismo DataFrame.

---

# Integración con analytics

Todas las funciones de negocio deben recibir:

```python
df_filtrado
```

Ejemplo:

```python
def calcular_ventas(df):

    return df["VENTA"].sum()
```

Nunca deben acceder al DataFrame original.

---

# Integración con components

Los componentes visuales únicamente reciben la información calculada.

Por ejemplo:

```python
mostrar_kpis(...)

mostrar_graficos(...)

mostrar_tablas(...)
```

No deben implementar filtros.

No deben modificar información.

No deben realizar cálculos.

---

# Buenas prácticas

✔ Utilizar siempre `df.copy()`.

✔ Agregar la opción **"Todas"**.

✔ Eliminar valores nulos.

✔ Ordenar las opciones.

✔ Mantener nombres claros.

✔ Utilizar emojis únicamente cuando mejoren la experiencia del usuario.

---

# Errores comunes

## Error 1

Modificar el DataFrame original.

```python
df = df[

    df["ZONA"] == zona

]
```

Incorrecto.

---

## Correcto

```python
df_filtrado = df.copy()

df_filtrado = df_filtrado[

    df_filtrado["ZONA"] == zona

]
```

---

## Error 2

Calcular KPIs antes del filtro.

Incorrecto.

Siempre:

```text
Filtro

↓

DataFrame Filtrado

↓

KPIs
```

---

## Error 3

Crear un filtro diferente para cada gráfico.

Todo el Dashboard debe utilizar exactamente el mismo:

```python
df_filtrado
```

---

# Checklist

Antes de utilizar un Selectbox verifique que:

□ Existe la columna.

□ Se eliminan los valores nulos.

□ Las opciones están ordenadas.

□ Existe la opción "Todas".

□ Se utiliza `df.copy()`.

□ El Dashboard trabaja con `df_filtrado`.

---

# Regla de Oro

> El Selectbox nunca modifica el DataFrame original.

Su única responsabilidad consiste en producir un DataFrame filtrado que será utilizado por todos los componentes del Dashboard.

---

# Próximo tema

En la siguiente sección construiremos la **Plantilla Oficial del Multiselect**, utilizada cuando el usuario necesita seleccionar múltiples valores simultáneamente.

---

# Plantilla Oficial 02

# Multiselect

---

# ¿Qué es?

El Multiselect permite al usuario seleccionar múltiples valores de una lista.

A diferencia del Selectbox, donde únicamente puede existir una opción activa, el Multiselect admite varias selecciones simultáneamente.

Es uno de los filtros más utilizados en análisis comparativos, ya que permite consultar varios elementos al mismo tiempo sin necesidad de ejecutar nuevamente el Dashboard.

---

# ¿Cuándo utilizarlo?

Utilice un Multiselect cuando el usuario necesite comparar varios elementos dentro del mismo análisis.

Ejemplos:

- Varias zonas.
- Varias regionales.
- Varios estados.
- Varios clientes.
- Varios proyectos.
- Varias ciudades.
- Varias actividades.
- Varios técnicos.

---

# Ejemplo empresarial

Supongamos que un gerente desea analizar únicamente las zonas:

```text
✔ METROPOLITANO

✔ OCCIDENTE

✖ ORIENTE

✔ SUROESTE
```

En este caso el Dashboard únicamente mostrará información correspondiente a esas tres zonas.

---

# ¿Dónde debe implementarse?

## Dashboard pequeño

```text
app.py
```

---

## Dashboard empresarial

```text
components/

└── filtros.py
```

Posteriormente será llamado desde:

```python
app.py
```

---

# Flujo del Multiselect

```text
Usuario

        │

        ▼

Selecciona

METROPOLITANO

OCCIDENTE

SUROESTE

        │

        ▼

Multiselect

        │

        ▼

DataFrame Filtrado

        │

 ┌──────┼───────────────┐

 ▼      ▼               ▼

KPIs  Gráficos      Tablas
```

---

# Información necesaria

Para implementar correctamente un Multiselect se requiere:

- Un DataFrame.
- Una columna.
- Una lista de valores seleccionados.

Ejemplo:

```python
df["ZONA"]
```

---

# Plantilla Oficial

```python
# ==========================================================
# FILTRO MULTIPLE POR ZONA
# ==========================================================

zonas = sorted(

    df["ZONA"]

    .dropna()

    .unique()

)

zonas_seleccionadas = st.multiselect(

    "📍 Zonas",

    options=zonas,

    default=zonas

)

df_filtrado = df.copy()

if zonas_seleccionadas:

    df_filtrado = df_filtrado[

        df_filtrado["ZONA"]

        .isin(zonas_seleccionadas)

    ]
```

---

# ¿Qué hace esta plantilla?

## Paso 1

Obtiene todos los valores únicos.

```python
.unique()
```

---

## Paso 2

Elimina valores nulos.

```python
.dropna()
```

---

## Paso 3

Ordena alfabéticamente.

```python
sorted(...)
```

---

## Paso 4

Selecciona inicialmente todos los registros.

```python
default=zonas
```

De esta forma el Dashboard inicia mostrando toda la información.

---

## Paso 5

Filtra utilizando:

```python
isin()
```

Este método verifica si cada registro pertenece al conjunto seleccionado.

---

# ¿Por qué utilizar isin()?

Cuando existe una única selección utilizamos:

```python
==
```

Pero cuando existen múltiples valores debemos utilizar:

```python
isin()
```

Ejemplo:

```python
df["ZONA"].isin(

    [

        "METROPOLITANO",

        "OCCIDENTE"

    ]

)
```

---

# Integración con app.py

```python
df = cargar_datos()

df_filtrado = mostrar_filtros(df)

ventas = indicadores.calcular_ventas(

    df_filtrado

)

mostrar_kpis()

mostrar_graficos()

mostrar_tablas()
```

Observe que el resto del Dashboard desconoce cuántas zonas fueron seleccionadas.

Siempre trabaja con:

```python
df_filtrado
```

---

# Integración con analytics

Las funciones analíticas permanecen exactamente iguales.

```python
def calcular_total(df):

    return len(df)
```

La lógica del negocio nunca cambia.

Únicamente recibe un DataFrame con menos registros.

---

# Integración con components

Los componentes visuales continúan recibiendo únicamente los resultados.

```python
mostrar_kpis()

mostrar_tablas()

mostrar_graficos()
```

Nunca deben implementar filtros.

---

# Casos empresariales

## Comparar varias zonas

```text
✔ METROPOLITANO

✔ OCCIDENTE
```

---

## Comparar varios clientes

```text
✔ Cliente A

✔ Cliente B

✔ Cliente C
```

---

## Comparar varios estados

```text
✔ A Tiempo

✔ Alerta

✔ Alerta Cero Días
```

---

## Comparar varias regionales

```text
✔ Norte

✔ Centro

✔ Sur
```

---

# Buenas prácticas

✔ Inicializar con todas las opciones seleccionadas.

✔ Ordenar los valores.

✔ Eliminar valores nulos.

✔ Utilizar siempre `isin()`.

✔ Trabajar con `df_filtrado`.

✔ Mantener nombres descriptivos.

---

# Errores comunes

## Error 1

Comparar utilizando:

```python
==
```

Incorrecto.

---

## Correcto

```python
.isin(...)
```

---

## Error 2

No seleccionar valores por defecto.

Esto provoca que el Dashboard aparezca vacío al iniciar.

---

## Error 3

Modificar el DataFrame original.

Siempre utilizar:

```python
df_filtrado
```

---

# Checklist

Antes de utilizar un Multiselect verifique que:

□ Existe la columna.

□ Se eliminaron los valores nulos.

□ Las opciones están ordenadas.

□ Se utiliza `default`.

□ Se utiliza `isin()`.

□ Todo el Dashboard trabaja con `df_filtrado`.

---

# Comparación Selectbox vs Multiselect

| Característica | Selectbox | Multiselect |
|----------------|-----------|-------------|
| Número de opciones | Una | Varias |
| Operador | `==` | `isin()` |
| Uso recomendado | Consulta individual | Comparaciones |
| Complejidad | Baja | Media |
| Escenarios | Zona, Estado, Cliente | Zonas, Clientes, Regionales |

---

# Regla de Oro

> Siempre que el usuario pueda seleccionar más de un valor, utilice un **Multiselect** y filtre mediante `isin()`.

Nunca utilice comparaciones con `==` para listas de valores.

---

# Próximo tema

En la siguiente sección construiremos la **Plantilla Oficial del Date Input**, uno de los filtros más importantes en dashboards empresariales, utilizado para consultar información por fechas, rangos de fechas, meses y años.

---

# Plantilla Oficial 03

# Date Input

---

# ¿Qué es?

El Date Input permite al usuario seleccionar una fecha o un rango de fechas para filtrar la información del Dashboard.

Es uno de los controles más utilizados en aplicaciones empresariales debido a que la mayoría de los indicadores de negocio dependen del tiempo.

Con este filtro es posible analizar únicamente la información correspondiente a un día, una semana, un mes, un trimestre o cualquier período específico.

---

# ¿Cuándo utilizarlo?

Utilice un Date Input cuando la información del Dashboard dependa de una fecha.

Ejemplos:

- Pedidos atendidos.
- Ventas.
- Facturación.
- Casos cerrados.
- Instalaciones.
- Visitas técnicas.
- Incidentes.
- Liquidaciones.

---

# Casos empresariales

## Caso 1

Consultar únicamente los pedidos del mes de junio.

---

## Caso 2

Analizar las ventas entre el 01 de enero y el 31 de marzo.

---

## Caso 3

Visualizar únicamente las instalaciones realizadas hoy.

---

## Caso 4

Comparar los indicadores de dos semanas consecutivas.

---

# ¿Dónde debe implementarse?

## Dashboard pequeño

```text
app.py
```

---

## Dashboard empresarial

```text
components/

└── filtros.py
```

Posteriormente será llamado desde:

```python
df_filtrado = mostrar_filtros(df)
```

---

# Flujo

```text
Usuario

        │

        ▼

Selecciona

01/01/2026

↓

31/01/2026

        │

        ▼

Date Input

        │

        ▼

DataFrame Filtrado

        │

 ┌──────┼─────────────┐

 ▼      ▼             ▼

KPIs  Gráficos     Tablas
```

---

# Información necesaria

Para implementar correctamente este filtro se requiere:

- Un DataFrame.
- Una columna de tipo fecha.
- Una fecha inicial.
- Una fecha final.

Ejemplo:

```python
df["FECHA"]
```

---

# Preparación de la información

Antes de aplicar cualquier filtro por fecha es obligatorio convertir la columna al tipo datetime.

```python
df["FECHA"] = pd.to_datetime(

    df["FECHA"]

)
```

Nunca filtre fechas tratándolas como texto.

---

# Plantilla Oficial

```python
# ==========================================================
# FILTRO POR RANGO DE FECHAS
# ==========================================================

fecha_inicio = df["FECHA"].min()

fecha_fin = df["FECHA"].max()

rango = st.date_input(

    "📅 Rango de fechas",

    value=(

        fecha_inicio,

        fecha_fin

    )

)

df_filtrado = df.copy()

if len(rango) == 2:

    inicio, fin = rango

    df_filtrado = df_filtrado[

        (

            df_filtrado["FECHA"]

            >= pd.to_datetime(inicio)

        )

        &

        (

            df_filtrado["FECHA"]

            <= pd.to_datetime(fin)

        )

    ]
```

---

# ¿Qué hace esta plantilla?

## Paso 1

Obtiene la fecha más antigua.

```python
.min()
```

---

## Paso 2

Obtiene la fecha más reciente.

```python
.max()
```

---

## Paso 3

Inicializa el calendario mostrando todo el rango disponible.

---

## Paso 4

El usuario selecciona el período.

---

## Paso 5

Se genera un nuevo:

```python
df_filtrado
```

---

# Integración con app.py

```python
df = cargar_datos()

df_filtrado = mostrar_filtros(df)

ventas = indicadores.calcular_ventas(

    df_filtrado

)

mostrar_kpis()

mostrar_graficos()

mostrar_tablas()
```

Observe que todo el Dashboard trabaja con el mismo DataFrame.

---

# Integración con analytics

```python
def calcular_total(df):

    return len(df)
```

La función desconoce completamente el rango seleccionado.

Simplemente recibe un DataFrame ya filtrado.

---

# Integración con components

Los componentes visuales únicamente muestran información.

Nunca realizan filtros.

Nunca convierten fechas.

Nunca modifican el DataFrame.

---

# Variantes de esta plantilla

## Fecha única

```python
fecha = st.date_input(

    "Fecha"

)
```

Ideal para:

- Producción diaria.
- Reportes diarios.
- Agenda.

---

## Rango de fechas

```python
st.date_input(

    value=(

        fecha_inicio,

        fecha_fin

    )

)
```

Ideal para:

- Dashboards empresariales.
- Comparativos.
- KPIs.

---

## Mes

Puede combinarse posteriormente con un Selectbox.

```text
Enero

Febrero

Marzo
```

---

## Año

Muy útil cuando existen varios años históricos.

```text
2024

2025

2026
```

---

# Buenas prácticas

✔ Convertir siempre las fechas utilizando:

```python
pd.to_datetime()
```

✔ Mostrar inicialmente todo el rango.

✔ Filtrar mediante operadores de comparación.

✔ Mantener el DataFrame original sin modificaciones.

✔ Trabajar únicamente con:

```python
df_filtrado
```

---

# Rendimiento

El filtrado por fechas utiliza operaciones vectorizadas de pandas.

Complejidad aproximada:

```text
O(n)
```

Incluso con cientos de miles de registros mantiene un excelente rendimiento.

---

# Compatibilidad

Compatible con:

✔ KPIs

✔ AgGrid

✔ Plotly

✔ Altair

✔ Folium

✔ ECharts

✔ Exportación Excel

✔ Exportación PDF

✔ Mapas

---

# Errores comunes

## Error 1

Guardar fechas como texto.

Incorrecto.

---

## Correcto

```python
pd.to_datetime()
```

---

## Error 2

Comparar cadenas.

```python
"01/01/2026"
```

Incorrecto.

---

## Error 3

Aplicar varios filtros de fecha en diferentes componentes.

Todo el Dashboard debe utilizar un único:

```python
df_filtrado
```

---

# Checklist

Antes de utilizar un Date Input verifique que:

□ La columna es datetime.

□ Existe un rango válido.

□ Se utiliza `pd.to_datetime()`.

□ El Dashboard trabaja con `df_filtrado`.

□ Todos los componentes reciben el mismo DataFrame.

---

# Regla de Oro

> Nunca filtre fechas tratándolas como texto.

Siempre convierta la columna a tipo datetime antes de realizar cualquier comparación.

---

# Próximo tema

En la siguiente sección construiremos la **Plantilla Oficial de Filtros Encadenados**, una técnica utilizada en dashboards profesionales donde un filtro depende del resultado de otro, por ejemplo:

Zona → Ciudad → Técnico

País → Departamento → Municipio

Cliente → Proyecto → Actividad

Esta arquitectura permite crear Dashboards mucho más intuitivos y escalables.

---

# Patrón de Diseño 01

# Barra Horizontal de Filtros

---

# Objetivo

La Barra Horizontal de Filtros es uno de los patrones más utilizados en Dashboards ejecutivos.

Consiste en agrupar los filtros principales en una única fila ubicada en la parte superior del Dashboard, inmediatamente después del Banner y antes de los indicadores (KPIs).

Este diseño permite que el usuario tenga acceso inmediato a todos los filtros sin ocupar espacio adicional en la pantalla.

Es el patrón utilizado por herramientas como:

- Power BI
- Tableau
- Looker
- Qlik Sense
- Dashboards corporativos desarrollados en Python

Dentro de este Framework, será el patrón recomendado para la mayoría de los proyectos.

---

# ¿Cuándo utilizar este patrón?

Utilice una Barra Horizontal cuando:

- El Dashboard tenga entre 2 y 6 filtros.
- Los filtros sean utilizados constantemente.
- Se desee una interfaz limpia y moderna.
- El espacio vertical sea importante.
- Los KPIs deban visualizarse inmediatamente después de los filtros.

---

# Ejemplo

```text
┌──────────────────────────────────────────────────────────────┐

                BANNER DEL DASHBOARD

└──────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐

📍 Zona

⚠ Estado

📅 Fecha

👤 Cliente

🛠 Actividad

└──────────────────────────────────────────────────────────────┘

KPIs

Gráficos

Tabla
```

Este diseño permite que el usuario comprenda inmediatamente cómo interactuar con el Dashboard.

---

# Arquitectura dentro del Framework

La arquitectura recomendada será la siguiente.

```text
Proyecto

│

├── app.py

│

├── analytics/

│

├── components/

│      banner.py

│      sidebar.py

│      filtros.py

│      navigation.py

│      kpis.py

│      tablas.py

│      graficos.py
```

Observe que la Barra Horizontal pertenece al archivo:

```text
components/filtros.py
```

No debe implementarse directamente dentro de los componentes de KPIs ni de gráficos.

---

# Flujo de funcionamiento

```text
Excel

↓

DataFrame

↓

components/filtros.py

↓

DataFrame Filtrado

↓

analytics/

↓

components/

↓

Dashboard
```

Todos los componentes consumirán exactamente el mismo DataFrame filtrado.

---

# Plantilla Oficial

## app.py

```python
# ==========================================================
# CARGAR INFORMACIÓN
# ==========================================================

df = cargar_datos()

# ==========================================================
# BARRA DE FILTROS
# ==========================================================

df_filtrado = mostrar_filtros(df)

# ==========================================================
# INDICADORES
# ==========================================================

kpis = calcular_kpis(df_filtrado)

# ==========================================================
# DASHBOARD
# ==========================================================

mostrar_kpis(kpis)

mostrar_graficos(df_filtrado)

mostrar_tablas(df_filtrado)
```

Observe que `app.py` únicamente orquesta el proceso.

---

## components/filtros.py

```python
import streamlit as st

def mostrar_filtros(df):

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        ...

    with col2:

        ...

    with col3:

        ...

    with col4:

        ...

    return df_filtrado
```

Toda la lógica relacionada con los filtros queda centralizada en un único archivo.

---

# Distribución recomendada

Cuando existan cuatro filtros principales, la distribución recomendada será:

```text
┌────────────┬────────────┬────────────┬────────────┐

 Zona          Estado        Fecha        Cliente

└────────────┴────────────┴────────────┴────────────┘
```

Si existen cinco filtros:

```text
┌────────┬────────┬────────┬────────┬────────┐

Zona      Estado    Fecha    Cliente   Proyecto

└────────┴────────┴────────┴────────┴────────┘
```

El objetivo es mantener una interfaz equilibrada y fácil de utilizar.

---

# Implementación en el Dashboard Servitravel

La Barra Horizontal puede implementarse utilizando los filtros más representativos del proyecto.

Ejemplo:

- 📍 Zona
- 🚦 Estado
- 📅 Mes
- 🚗 Placa

Estos filtros permitirán que el usuario reduzca la información antes de calcular los indicadores y mostrar las tablas.

---

# Buenas prácticas

✔ Ubicar la barra inmediatamente debajo del Banner.

✔ Mantener todos los filtros alineados.

✔ Utilizar el mismo ancho para todas las columnas.

✔ Evitar más de seis filtros en una misma fila.

✔ Si existen muchos filtros, dividirlos en dos filas o utilizar un Sidebar.

✔ Todos los filtros deben devolver un único `df_filtrado`.

---

# Errores comunes

## Error 1

Colocar filtros entre los gráficos.

Esto rompe el flujo visual del Dashboard.

---

## Error 2

Crear filtros independientes para cada componente.

Incorrecto.

Todos los componentes deben compartir el mismo DataFrame filtrado.

---

## Error 3

Distribuir los filtros sin alineación.

Una barra desordenada dificulta la experiencia del usuario y transmite una sensación de falta de organización.

---

# Checklist

Antes de implementar una Barra Horizontal verifique que:

□ Los filtros están ubicados debajo del Banner.

□ Existe un único archivo `components/filtros.py`.

□ Todos los filtros generan un único `df_filtrado`.

□ Los KPIs utilizan `df_filtrado`.

□ Los gráficos utilizan `df_filtrado`.

□ Las tablas utilizan `df_filtrado`.

---

# Regla de Oro

> La Barra Horizontal representa el punto de entrada al análisis del Dashboard.

Todo lo que el usuario visualiza posteriormente debe depender del resultado obtenido en esta barra de filtros.

---

# Próximo patrón

En la siguiente sección construiremos el **Patrón de Diseño 02 - Filtros Encadenados**, utilizado en Dashboards profesionales donde un filtro depende del valor seleccionado en otro, permitiendo interfaces más inteligentes y una mejor experiencia para el usuario.

# Patrón de Diseño 02

# Filtros Encadenados

---

# Objetivo

Los Filtros Encadenados permiten construir interfaces dinámicas donde un filtro depende del valor seleccionado en otro filtro.

En lugar de mostrar todas las opciones disponibles, cada filtro presenta únicamente la información relacionada con la selección realizada anteriormente.

Este patrón mejora significativamente la experiencia del usuario, reduce errores de selección y simplifica la navegación dentro del Dashboard.

Es uno de los patrones más utilizados en aplicaciones empresariales con grandes volúmenes de información.

---

# ¿Qué problema resuelve?

Supongamos que una empresa tiene la siguiente estructura:

```text
METROPOLITANO

    Medellín

    Bello

    Itagüí

----------------------------------

ORIENTE

    Rionegro

    La Ceja

    Marinilla

----------------------------------

OCCIDENTE

    Santa Fe de Antioquia

    Sopetrán

----------------------------------

SUROESTE

    Andes

    Jardín
```

Si el usuario selecciona:

```text
Zona

↓

ORIENTE
```

No tiene sentido seguir mostrando ciudades como:

- Medellín
- Bello
- Itagüí
- Jardín

El Dashboard debe mostrar únicamente:

```text
Rionegro

La Ceja

Marinilla
```

Eso es un filtro encadenado.

---

# ¿Cuándo utilizar este patrón?

Este patrón es ideal cuando existe una relación jerárquica entre los datos.

Ejemplos:

Zona → Ciudad

Ciudad → Técnico

Cliente → Proyecto

Proyecto → Actividad

País → Departamento

Departamento → Municipio

Categoría → Producto

Proveedor → Material

Regional → Supervisor

Supervisor → Técnico

---

# Arquitectura dentro del Framework

```text
Usuario

↓

Filtro 1

↓

Filtro 2

↓

Filtro 3

↓

DataFrame Filtrado

↓

Analytics

↓

Dashboard
```

Cada filtro depende del resultado del anterior.

---

# Implementación dentro del proyecto

La estructura recomendada continúa siendo:

```text
Proyecto

│

├── app.py

│

├── analytics/

│

├── components/

│      filtros.py

│      kpis.py

│      tablas.py

│      graficos.py
```

Toda la lógica de los filtros debe permanecer dentro de:

```text
components/filtros.py
```

---

# Plantilla Oficial

Supongamos que el DataFrame contiene:

```python
ZONA

CIUDAD
```

La implementación sería:

```python
zonas = sorted(

    df["ZONA"]

    .dropna()

    .unique()

)

zona = st.selectbox(

    "Zona",

    zonas

)

df_zona = df[

    df["ZONA"] == zona

]

ciudades = sorted(

    df_zona["CIUDAD"]

    .dropna()

    .unique()

)

ciudad = st.selectbox(

    "Ciudad",

    ciudades

)

df_filtrado = df_zona[

    df_zona["CIUDAD"] == ciudad

]
```

Observe que el segundo filtro utiliza el resultado del primero.

---

# Flujo del proceso

```text
DataFrame

↓

Seleccionar Zona

↓

DataFrame Zona

↓

Seleccionar Ciudad

↓

DataFrame Ciudad

↓

KPIs

↓

Gráficos

↓

Tabla
```

Cada paso reduce el conjunto de datos.

---

# Integración con app.py

```python
df = cargar_datos()

df_filtrado = mostrar_filtros(df)

kpis = calcular_kpis(df_filtrado)

mostrar_kpis(kpis)

mostrar_graficos(df_filtrado)

mostrar_tablas(df_filtrado)
```

Observe que `app.py` continúa siendo un orquestador.

No necesita conocer cómo funcionan los filtros.

---

# Implementación en Servitravel

Este patrón puede aplicarse fácilmente.

Ejemplo:

```text
Zona

↓

Placa

↓

Mes
```

Al seleccionar una zona, el filtro de placas únicamente mostrará las placas pertenecientes a esa zona.

Posteriormente, el filtro de mes podrá limitar aún más la información.

Esto hace que el Dashboard sea más intuitivo y evita que el usuario seleccione combinaciones que no existen.

---

# Beneficios

✔ Reduce la cantidad de opciones.

✔ Evita errores de selección.

✔ Hace el Dashboard más rápido.

✔ Mejora la experiencia del usuario.

✔ Facilita el análisis de la información.

✔ Produce interfaces mucho más profesionales.

---

# Buenas prácticas

✔ Cada filtro debe depender únicamente del anterior.

✔ Mantener la jerarquía del negocio.

✔ Utilizar nombres claros.

✔ Evitar más de cuatro niveles de dependencia.

✔ Continuar trabajando con un único `df_filtrado`.

---

# Errores comunes

## Error 1

Mostrar todas las ciudades sin importar la zona.

Esto genera listas demasiado largas y confusas.

---

## Error 2

Permitir seleccionar combinaciones inexistentes.

Ejemplo:

```text
Zona

ORIENTE

Ciudad

Medellín
```

Esta combinación nunca debería aparecer.

---

## Error 3

Crear un DataFrame diferente para cada componente.

Todo el Dashboard debe consumir el mismo:

```python
df_filtrado
```

---

# Rendimiento

Los filtros encadenados reducen progresivamente el volumen de datos.

En consecuencia:

- Los KPIs calculan menos registros.
- Las tablas cargan más rápido.
- Los gráficos responden mejor.
- El Dashboard se siente más fluido.

En proyectos grandes esta técnica puede mejorar considerablemente la experiencia del usuario.

---

# Compatibilidad

Compatible con:

✔ Selectbox

✔ Multiselect

✔ Date Input

✔ KPIs

✔ AgGrid

✔ Plotly

✔ Altair

✔ Exportación Excel

✔ Exportación PDF

✔ Mapas

---

# Checklist

Antes de implementar Filtros Encadenados verifique que:

□ Existe una relación jerárquica entre las columnas.

□ Cada filtro depende del anterior.

□ El usuario no puede seleccionar combinaciones inválidas.

□ El Dashboard utiliza un único `df_filtrado`.

□ La lógica se encuentra en `components/filtros.py`.

---

# Regla de Oro

> Un filtro nunca debe ofrecer opciones que no existan dentro del resultado del filtro anterior.

Esta simple regla hace que un Dashboard pase de ser una aplicación funcional a una herramienta profesional de análisis.

---

# Próximo patrón

En la siguiente sección construiremos el **Patrón de Diseño 03 - Barra Lateral de Filtros (Sidebar Inteligente)**, donde aprenderemos cuándo utilizar una barra horizontal y cuándo es más conveniente trasladar los filtros a un panel lateral para mantener una interfaz limpia y escalable.

# Patrón de Diseño 03

# Sidebar Inteligente de Filtros

---

# Objetivo

La Sidebar Inteligente consiste en trasladar todos los filtros del Dashboard a un panel lateral, liberando espacio para que los indicadores, gráficos y tablas ocupen la mayor parte de la pantalla.

Este patrón es ampliamente utilizado cuando el Dashboard posee una gran cantidad de filtros o cuando se desea mantener una interfaz limpia y organizada.

Dentro de este Framework será el patrón recomendado para Dashboards empresariales de gran tamaño.

---

# ¿Cuándo utilizar este patrón?

Utilice una Sidebar cuando:

- Existan más de seis filtros.
- El Dashboard tenga muchos gráficos.
- Se requiera aprovechar el ancho de la pantalla.
- Los filtros no necesiten estar visibles permanentemente.
- El usuario interactúe constantemente con múltiples criterios de búsqueda.

---

# ¿Cuándo NO utilizarlo?

No utilice una Sidebar cuando:

- El Dashboard únicamente tenga dos o tres filtros.
- Los filtros formen parte del análisis principal.
- Se trate de un Dashboard ejecutivo con pocos indicadores.

En estos casos es preferible utilizar una Barra Horizontal.

---

# Comparación

## Barra Horizontal

Ideal para:

- 2 a 6 filtros.
- Dashboards ejecutivos.
- KPIs visibles inmediatamente.

---

## Sidebar

Ideal para:

- Más de 6 filtros.
- Dashboards operativos.
- Gran cantidad de opciones.
- Consultas detalladas.

---

# Ejemplo visual

```text
┌──────────────┬────────────────────────────────────────────┐

  SIDEBAR             DASHBOARD

────────────────      KPIs

📍 Zona              ─────────────────────

🚦 Estado            Gráficos

📅 Fecha             ─────────────────────

👤 Cliente           Tabla

🚗 Placa

🛠 Actividad

────────────────

[ Limpiar ]

└──────────────┴────────────────────────────────────────────┘
```

Observe cómo toda la pantalla queda disponible para visualizar la información.

---

# Arquitectura dentro del Framework

```text
Proyecto

│

├── app.py

│

├── analytics/

│

├── components/

│      sidebar.py

│      filtros.py

│      kpis.py

│      graficos.py

│      tablas.py
```

La Sidebar únicamente aloja los filtros.

La lógica continúa implementándose dentro de:

```text
components/filtros.py
```

---

# Flujo del proceso

```text
Usuario

↓

Sidebar

↓

Filtros

↓

DataFrame Filtrado

↓

Analytics

↓

Dashboard
```

El flujo continúa siendo exactamente el mismo.

Únicamente cambia la ubicación visual de los filtros.

---

# Plantilla Oficial

## app.py

```python
df = cargar_datos()

df_filtrado = mostrar_filtros(df)

kpis = calcular_kpis(df_filtrado)

mostrar_kpis(kpis)

mostrar_graficos(df_filtrado)

mostrar_tablas(df_filtrado)
```

Observe que `app.py` no cambia.

---

## components/filtros.py

```python
import streamlit as st

def mostrar_filtros(df):

    with st.sidebar:

        ...

        ...

        ...

    return df_filtrado
```

Toda la lógica permanece centralizada en un único archivo.

---

# Implementación recomendada

Una Sidebar empresarial normalmente incluye:

```text
📍 Zona

🚦 Estado

📅 Fecha

👤 Cliente

🚗 Placa

🛠 Actividad

📦 Material

👨 Técnico
```

Todos estos filtros producirán un único:

```python
df_filtrado
```

---

# Implementación en Servitravel

Actualmente el Dashboard puede utilizar una Barra Horizontal.

Sin embargo, si en el futuro se agregan filtros como:

- Zona
- Estado
- Mes
- Año
- Placa
- Conductor
- Centro de Costos
- Tipo de Vehículo
- Proyecto

será recomendable migrarlos a una Sidebar para conservar una interfaz limpia y profesional.

---

# Beneficios

✔ Más espacio para gráficos.

✔ Mejor organización.

✔ Escalable.

✔ Fácil mantenimiento.

✔ Compatible con cualquier tamaño de pantalla.

✔ Reduce el desorden visual.

---

# Buenas prácticas

✔ Agrupar filtros relacionados.

✔ Utilizar títulos descriptivos.

✔ Mantener un orden lógico.

✔ Mostrar primero los filtros más utilizados.

✔ Mantener un único DataFrame filtrado.

---

# Errores comunes

## Error 1

Duplicar filtros en la Sidebar y en la Barra Horizontal.

Debe existir una única ubicación para los filtros.

---

## Error 2

Mezclar botones con filtros.

Los botones de exportación o actualización deben ubicarse al final de la Sidebar.

---

## Error 3

Colocar veinte filtros sin organización.

Agrupe los filtros por categorías cuando sean numerosos.

---

# Rendimiento

La ubicación de los filtros no afecta el rendimiento del Dashboard.

El beneficio principal es la organización visual y la facilidad de uso.

---

# Compatibilidad

Compatible con:

✔ Selectbox

✔ Multiselect

✔ Date Input

✔ KPIs

✔ AgGrid

✔ Plotly

✔ Altair

✔ Exportación Excel

✔ Exportación PDF

✔ Mapas

---

# Checklist

Antes de utilizar una Sidebar verifique que:

□ El Dashboard posee varios filtros.

□ Los filtros están organizados.

□ Existe un único `df_filtrado`.

□ Toda la lógica permanece en `components/filtros.py`.

□ `app.py` únicamente orquesta el flujo.

---

# Regla de Oro

> La Sidebar organiza los filtros, pero no modifica la arquitectura del Framework.

La ubicación visual puede cambiar, pero el flujo del Dashboard siempre debe permanecer igual.

---

# Próximo patrón

En la siguiente sección construiremos el **Patrón de Diseño 04 - Filtros Persistentes con `st.session_state`**, una técnica que permite conservar las selecciones del usuario al cambiar de pestaña, actualizar componentes o navegar entre módulos del Dashboard.

# Patrón de Diseño 04

# Filtros Persistentes (`st.session_state`)

---

# Objetivo

Los Filtros Persistentes permiten conservar las selecciones realizadas por el usuario mientras navega por el Dashboard.

Gracias a `st.session_state`, el usuario no tendrá que volver a seleccionar los mismos filtros cada vez que cambie de pestaña, actualice un componente o interactúe con la aplicación.

Este patrón mejora significativamente la experiencia de uso y es recomendado para la mayoría de los Dashboards empresariales.

---

# ¿Cuándo utilizar este patrón?

Utilice Filtros Persistentes cuando:

- El Dashboard tenga varias pestañas.
- Existan múltiples filtros.
- El usuario consulte constantemente la misma información.
- Se desee evitar repetir selecciones.

---

# ¿Cuándo NO utilizarlo?

No es necesario cuando:

- El Dashboard tiene únicamente un filtro.
- Se trata de una aplicación muy pequeña.
- El usuario realiza consultas rápidas sin necesidad de conservar el estado.

---

# Arquitectura

```text
Usuario

↓

Selecciona filtros

↓

st.session_state

↓

DataFrame Filtrado

↓

KPIs

↓

Gráficos

↓

Tabla
```

---

# Archivos involucrados

```text
Proyecto

│

├── app.py

│

├── components/

│      filtros.py
```

La implementación se realiza en:

```text
components/filtros.py
```

---

# Plantilla Oficial

```python
import streamlit as st

# Valor inicial

if "zona" not in st.session_state:

    st.session_state.zona = "Todas"

zona = st.selectbox(

    "Zona",

    options=zonas,

    key="zona"

)
```

Con esta implementación, Streamlit recordará automáticamente la última selección del usuario.

---

# Integración con app.py

```python
df = cargar_datos()

df_filtrado = mostrar_filtros(df)

mostrar_dashboard(df_filtrado)
```

No se requiere ninguna modificación adicional.

---

# Implementación en Servitravel

Ejemplo:

```text
Zona

↓

Estado

↓

Mes

↓

Placa
```

Si el usuario cambia entre módulos o pestañas, las selecciones permanecerán activas.

---

# Buenas prácticas

✔ Utilizar nombres de clave descriptivos.

```python
key="zona"

key="estado"

key="mes"
```

✔ Mantener una clave diferente para cada filtro.

✔ Inicializar únicamente cuando no exista la variable.

---

# Errores comunes

❌ Utilizar la misma `key` para varios filtros.

❌ Reinicializar el `session_state` en cada ejecución.

❌ Borrar el estado sin necesidad.

---

# Tiempo de implementación

**10 minutos**

---

# Dificultad

⭐⭐☆☆☆

---

# Regla de Oro

> Todo filtro que el usuario utilice frecuentemente debería conservar su estado mediante `st.session_state`.

# Resumen del capítulo

Durante este capítulo aprendimos a diseñar e implementar filtros siguiendo una arquitectura profesional.

Los filtros representan el punto de entrada al análisis de datos y son responsables de generar el DataFrame que alimentará todos los componentes del Dashboard.

La correcta implementación de esta arquitectura garantiza aplicaciones más organizadas, reutilizables y fáciles de mantener.

Más importante aún, permite que todos los indicadores, gráficos y tablas trabajen sobre la misma información, evitando inconsistencias y simplificando el desarrollo de nuevos proyectos.

---

