
# Capítulo 09 - KPIs
## Parte 1 - Fundamentos para la Construcción de KPIs

> Framework Dashboards Streamlit con Python

---

# 1. Introducción

Este capítulo no enseña únicamente a crear indicadores en Streamlit. Su propósito es enseñar **cómo pensar, diseñar y construir cualquier KPI** antes de escribir código.

La metodología presentada puede aplicarse en proyectos de logística, inventarios, ANS, ventas, finanzas, recursos humanos, mantenimiento o cualquier otro dominio.

---

# 2. Objetivo

Al finalizar esta primera parte podrás:

- Comprender qué es realmente un KPI.
- Aprender la arquitectura que sigue un indicador profesional.
- Entender el flujo de construcción desde el dato hasta el Dashboard.
- Diseñar un KPI antes de programarlo.
- Utilizar una plantilla de análisis reutilizable.

---

# 3. ¿Qué es un KPI?

Un KPI (Key Performance Indicator) es un indicador que resume el comportamiento de un proceso mediante una regla matemática aplicada sobre datos confiables.

Un KPI no comienza en Streamlit.

Comienza cuando alguien formula una pregunta de negocio.

Ejemplos:

- ¿Cuántos pedidos atendimos?
- ¿Cuál fue el costo total?
- ¿Qué porcentaje cumplimos?
- ¿Cuál vehículo tuvo más servicios?

Cada pregunta necesita un cálculo diferente.

---

# 4. Arquitectura de un KPI

Todo KPI profesional sigue la misma arquitectura.

```
Necesidad del negocio
        │
        ▼
Fuente de datos
        │
        ▼
DataFrame
        │
        ▼
Validación
        │
        ▼
Limpieza
        │
        ▼
Transformación
        │
        ▼
Operación matemática
        │
        ▼
Formato
        │
        ▼
Visualización
```

Nunca empieces creando un `st.metric()`.

Primero diseña el indicador.

---

# 5. Flujo de construcción

Antes de escribir código responde estas preguntas.

## Paso 1
### ¿Qué quiero medir?

Describe el objetivo.

Ejemplo:

"Quiero conocer cuántos vehículos fueron utilizados durante el mes."

---

## Paso 2
### ¿Dónde está el dato?

Archivo.

Tabla.

DataFrame.

Columnas.

---

## Paso 3
### ¿Qué operación representa mejor el negocio?

¿Contar?

¿Sumar?

¿Promediar?

¿Calcular porcentaje?

¿Construir un ranking?

---

## Paso 4
### ¿Qué validaciones debo realizar?

- Existe la columna.
- Tiene datos.
- Es numérica.
- No existen nulos críticos.
- No habrá división entre cero.

---

## Paso 5
### ¿Cómo verá el usuario el resultado?

Número.

Moneda.

Porcentaje.

Tiempo.

Fecha.

---

# 6. Metodología para construir un KPI

Aplica siempre el siguiente proceso.

```
Buscar columna
      │
Validar existencia
      │
Limpiar datos
      │
Convertir tipo
      │
Aplicar operación matemática
      │
Validar resultado
      │
Formatear
      │
Mostrar KPI
```

Esta metodología será utilizada en todos los ejemplos del Framework.

---

# 7. Plantilla Oficial de Diseño de KPI

Completa esta plantilla antes de programar.

```
══════════════════════════════════════════════
DISEÑO DEL KPI
══════════════════════════════════════════════

Nombre del KPI
____________________________________

¿Qué quiero medir?
____________________________________

¿Por qué es importante?
____________________________________

Fuente de datos
□ Excel
□ CSV
□ SQL
□ API
□ Otro

Archivo
____________________________________

DataFrame
____________________________________

Columnas necesarias
□ __________________
□ __________________
□ __________________

Tipo de dato
□ Texto
□ Número
□ Fecha

Operación matemática
□ count()
□ nunique()
□ sum()
□ mean()
□ median()
□ mode()
□ max()
□ min()
□ groupby()
□ porcentaje
□ personalizada

Fórmula del negocio
____________________________________

Regla de negocio
____________________________________

Validaciones
□ Existe columna
□ Sin nulos
□ Tipo correcto
□ División entre cero
□ Datos consistentes

Formato
□ Entero
□ Decimal
□ Moneda
□ %
□ Tiempo

Nombre visible del KPI
____________________________________

Icono
____________________________________

Observaciones
____________________________________
```

---

# 8. Ejemplo de aplicación

## Necesidad

Conocer el valor total facturado.

## Diseño

Operación: `sum()`

Columna: `VALOR_FACTURA`

Formato: Moneda

Nombre del KPI: **Ventas Totales**

Solo después de completar este análisis comienza la programación.

---

# 9. Buenas prácticas

- Diseña el KPI antes de escribir código.
- Documenta la regla de negocio.
- Valida las columnas.
- Separa cálculo y visualización.
- Reutiliza funciones.

---

# 10. Próxima parte

En la Parte 2 se estudiarán una por una las operaciones matemáticas más utilizadas en Pandas:

- count()
- nunique()
- sum()
- mean()
- median()
- mode()
- max()
- min()
- groupby()
- agg()
- pivot_table()
- cumsum()

Cada una incluirá:

- Qué hace.
- Qué construye.
- Cuándo utilizarla.
- Cuándo no utilizarla.
- Sintaxis.
- Parámetros.
- Valor devuelto.
- Ejemplos sencillos.
- Casos empresariales.
- Implementación en Python.
- Errores comunes.
- Buenas prácticas.


---

# Parte 2.1 - Funciones de Conteo

# Introducción

Antes de construir un KPI es necesario identificar qué tipo de información necesita el negocio.

Muchos indicadores no requieren sumar dinero ni calcular promedios.

Simplemente necesitan responder preguntas como:

- ¿Cuántos pedidos existen?
- ¿Cuántos clientes atendimos?
- ¿Cuántos vehículos participaron?
- ¿Cuántos técnicos trabajaron?
- ¿Cuántas actas fueron generadas?

En estos casos, las funciones de conteo son la herramienta adecuada.

Las dos funciones más utilizadas en Pandas son:

- `count()`
- `nunique()`

Aunque parecen similares, resuelven problemas completamente diferentes.

Comprender esta diferencia evitará errores en la construcción de indicadores.

---

# Arquitectura de un KPI de Conteo

```
Necesidad del negocio

        │

        ▼

Identificar la columna

        │

        ▼

¿Deseo contar registros?

        │

   Sí ─────────► count()

        │

        ▼

¿Deseo contar valores diferentes?

        │

   Sí ─────────► nunique()

        │

        ▼

Formatear

        │

        ▼

Mostrar KPI
```

---

# ¿Cuándo utilizar count() y cuándo utilizar nunique()?

| Necesidad del negocio | Función |
|------------------------|----------|
| Contar registros | count() |
| Contar valores únicos | nunique() |

Ejemplo.

Supongamos el siguiente DataFrame.

| Pedido | Cliente |
|---------|----------|
|1001|Juan|
|1002|Pedro|
|1003|Juan|
|1004|Ana|
|1005|Pedro|

Si aplicamos:

```python
df["Cliente"].count()
```

Resultado

```
5
```

Porque existen cinco registros.

Si aplicamos:

```python
df["Cliente"].nunique()
```

Resultado

```
3
```

Porque solamente existen tres clientes diferentes.

---

# Función count()

## ¿Qué hace?

Cuenta la cantidad de valores existentes dentro de una columna.

No cuenta valores nulos (`NaN`).

---

## ¿Qué construye?

Permite construir indicadores como:

- Total de pedidos
- Total de facturas
- Total de servicios
- Total de mantenimientos
- Total de técnicos
- Total de registros

---

## ¿Cuándo utilizarla?

Cuando cada fila representa un evento independiente.

Ejemplo.

Cada fila representa un pedido.

Cada fila representa una factura.

Cada fila representa una visita.

---

## ¿Cuándo NO utilizarla?

Cuando necesitas conocer la cantidad de elementos diferentes.

Por ejemplo.

Clientes.

Vehículos.

Placas.

Ciudades.

En estos casos debes utilizar `nunique()`.

---

## Sintaxis

```python
df["PEDIDO"].count()
```

---

## Parámetros

No requiere parámetros obligatorios.

---

## Valor devuelto

Devuelve un número entero.

Ejemplo.

```
2500
```

---

## Ejemplo sencillo

DataFrame

| Pedido |
|----------|
|1001|
|1002|
|1003|

Resultado

```python
df["Pedido"].count()
```

```
3
```

---

## Ejemplo empresarial

### Dashboard Comercial

Pregunta

¿Cuántas facturas fueron emitidas?

```python
total_facturas = df["FACTURA"].count()
```

KPI

```
Facturas Emitidas
```

---

### Dashboard Logístico

Pregunta

¿Cuántos servicios fueron ejecutados?

```python
servicios = df["SERVICIO"].count()
```

---

### Dashboard ANS

Pregunta

¿Cuántos pedidos fueron recibidos?

```python
pedidos = df["PEDIDO"].count()
```

---

### Dashboard Servitravel

Pregunta

¿Cuántos registros existen en Rodamientos?

```python
rodamientos = df["PLACA"].count()
```

---

## SQL equivalente

```sql
SELECT COUNT(*)
FROM pedidos;
```

---

## Power BI equivalente

```DAX
COUNT(Tabla[Pedido])
```

---

## Errores comunes

❌ Utilizar count() para contar clientes.

Esto contará registros y no clientes diferentes.

---

❌ No validar valores nulos.

Los valores vacíos no serán contabilizados.

---

## Buenas prácticas

✔ Validar que la columna exista.

✔ Confirmar que cada fila represente un único evento.

✔ Documentar qué representa cada registro.

---

## Plantilla Oficial del Framework

```python
# ======================================================
# KPI DE CONTEO
# ======================================================

if "COLUMNA" in df.columns:

    total = df["COLUMNA"].count()

else:

    total = 0

st.metric(

    "Nombre KPI",

    f"{total:,}"

)
```

---

## Checklist

Antes de utilizar count()

□ Quiero contar registros.

□ Cada fila representa un evento.

□ No necesito valores únicos.

□ La columna existe.

□ Los datos fueron limpiados.

---

# Función nunique()

## ¿Qué hace?

Cuenta la cantidad de valores diferentes dentro de una columna.

Los valores repetidos solamente se contabilizan una vez.

---

## ¿Qué construye?

Permite crear indicadores como:

- Clientes únicos
- Vehículos utilizados
- Técnicos activos
- Placas diferentes
- Ciudades atendidas
- Productos vendidos

---

## ¿Cuándo utilizarla?

Siempre que el negocio necesite conocer elementos distintos.

---

## ¿Cuándo NO utilizarla?

Cuando el objetivo sea conocer el número total de registros.

---

## Sintaxis

```python
df["CLIENTE"].nunique()
```

---

## Parámetros

No requiere parámetros obligatorios.

---

## Valor devuelto

Devuelve un entero.

---

## Ejemplo sencillo

| Cliente |
|----------|
|Juan|
|Pedro|
|Juan|
|Ana|
|Pedro|

Resultado

```python
df["Cliente"].nunique()
```

```
3
```

---

## Ejemplo empresarial

### Dashboard Comercial

¿Cuántos clientes compraron?

```python
clientes = df["CLIENTE"].nunique()
```

---

### Dashboard Servitravel

¿Cuántos vehículos participaron?

```python
vehiculos = df["PLACA"].nunique()
```

---

### Dashboard ANS

¿Cuántos técnicos diferentes atendieron pedidos?

```python
tecnicos = df["TECNICO"].nunique()
```

---

## SQL equivalente

```sql
SELECT COUNT(DISTINCT CLIENTE)
FROM ventas;
```

---

## Power BI equivalente

```DAX
DISTINCTCOUNT(Tabla[CLIENTE])
```

---

## Errores comunes

❌ Utilizar nunique() cuando realmente deseas contar registros.

---

❌ Aplicarlo sobre columnas que contienen errores de digitación.

Ejemplo.

```
Juan

JUAN

juan
```

Serán considerados tres valores distintos.

---

## Buenas prácticas

✔ Normalizar texto.

✔ Eliminar espacios.

✔ Convertir mayúsculas.

```python
df["CLIENTE"] = (

    df["CLIENTE"]

    .str.upper()

    .str.strip()

)
```

---

## Plantilla Oficial del Framework

```python
# ======================================================
# KPI DE VALORES ÚNICOS
# ======================================================

if "COLUMNA" in df.columns:

    total = df["COLUMNA"].nunique()

else:

    total = 0

st.metric(

    "Nombre KPI",

    f"{total:,}"

)
```

---

# Comparativa count() vs nunique()

| Característica | count() | nunique() |
|----------------|----------|-----------|
| Cuenta registros | ✔ | ❌ |
| Cuenta valores únicos | ❌ | ✔ |
| Ignora valores nulos | ✔ | ✔ |
| Muy utilizada en KPIs | ✔ | ✔ |
| Ideal para totales | ✔ | ❌ |
| Ideal para clientes únicos | ❌ | ✔ |
| Ideal para vehículos | ❌ | ✔ |
| Ideal para placas | ❌ | ✔ |

---

# Árbol de decisión

```
¿Qué deseas medir?

        │

        ▼

¿Cantidad de registros?

        │

      Sí

        │

     count()

        │

      No

        │

        ▼

¿Cantidad de valores diferentes?

        │

      Sí

        │

   nunique()
```

---

# Lecciones aprendidas

Antes de escribir una sola línea de código responde siempre:

> ¿Quiero contar registros o quiero contar elementos diferentes?

Responder correctamente esta pregunta evitará una gran cantidad de errores en la construcción de KPIs.

---

# Próxima parte

En la Parte 2.2 aprenderemos las funciones de agregación:

- sum()
- mean()
- median()
- mode()
- max()
- min()

Estas funciones constituyen la base para construir indicadores financieros, operativos, logísticos y de productividad.

---

# Parte 2.2.1 - Función `sum()`

# Introducción

Dentro de la construcción de KPIs, una de las preguntas más frecuentes que realiza un usuario de negocio es:

- ¿Cuánto vendimos?
- ¿Cuánto gastamos?
- ¿Cuántas horas extras se pagaron?
- ¿Cuál fue el costo total?
- ¿Cuántos kilómetros recorrimos?
- ¿Cuál fue el valor total de los viáticos?

Todas estas preguntas tienen algo en común.

No desean conocer una cantidad de registros.

Desean conocer un **TOTAL**.

La función `sum()` es la operación matemática encargada de calcular ese total.

Es una de las funciones más utilizadas en Pandas y probablemente la más utilizada en cualquier Dashboard Empresarial.

---

# ¿Qué hace `sum()`?

La función `sum()` recorre todos los valores numéricos de una columna y devuelve la suma total.

Ejemplo.

| Valor |
|-------:|
|100|
|200|
|350|
|150|

Resultado

```
800
```

---

# ¿Qué construye?

Con `sum()` podemos construir KPIs como:

- Ventas Totales
- Costos Totales
- Horas Extras
- Valor de Viáticos
- Valor de Parqueaderos
- Valor de Peajes
- Kilómetros Recorridos
- Producción Total
- Inventario Total
- Material Consumido
- Tiempo Total
- Facturación Total

En pocas palabras...

**Siempre que el negocio quiera conocer un acumulado, `sum()` será uno de los primeros candidatos.**

---

# Arquitectura del KPI

```
Necesidad del negocio

        │

        ▼

Identificar columna numérica

        │

        ▼

Validar datos

        │

        ▼

Aplicar sum()

        │

        ▼

Formatear

        │

        ▼

Mostrar KPI
```

---

# ¿Cuándo utilizar `sum()`?

Utiliza `sum()` cuando necesites conocer un total acumulado.

Ejemplos.

✔ Total de ventas

✔ Total de costos

✔ Total de horas

✔ Total de kilómetros

✔ Total de materiales

✔ Total de pedidos facturados

---

# ¿Cuándo NO utilizar `sum()`?

No utilices `sum()` cuando el indicador represente:

- Promedio
- Cantidad de registros
- Cantidad única
- Porcentaje
- Ranking

Cada uno de estos casos posee una función diferente.

---

# Sintaxis

```python
df["VENTAS"].sum()
```

---

# Parámetros

No requiere parámetros obligatorios.

---

# Valor devuelto

Devuelve un único valor numérico.

Ejemplo.

```
25896325
```

---

# Ejemplo sencillo

DataFrame

| Venta |
|-------:|
|120|
|350|
|180|
|250|

Código

```python
total = df["Venta"].sum()
```

Resultado

```
900
```

---

# Ejemplo Empresarial

## Dashboard Comercial

Pregunta

¿Cuánto dinero se vendió este mes?

```python
ventas = df["VALOR_FACTURA"].sum()
```

Resultado

```
$ 328.590.250
```

---

## Dashboard Servitravel

Pregunta

¿Cuánto costaron las horas extras?

```python
extras = df["HORAS_EXTRA"].sum()
```

KPI

```
Horas Extras Totales
```

---

Pregunta

¿Cuánto dinero se pagó en viáticos?

```python
viaticos = df["VALOR"].sum()
```

---

Pregunta

¿Cuánto dinero se pagó en peajes?

```python
peajes = df["VALOR"].sum()
```

---

Pregunta

¿Cuánto dinero se pagó en parqueaderos?

```python
parqueaderos = df["VALOR"].sum()
```

---

## Dashboard Inventarios

Pregunta

¿Cuál es el valor total del inventario?

```python
inventario = df["VALOR_TOTAL"].sum()
```

---

## Dashboard ANS

Pregunta

¿Cuántos días de atraso existen?

```python
dias = df["DIAS_ATRASO"].sum()
```

---

# SQL equivalente

```sql
SELECT

SUM(VALOR)

FROM VENTAS;
```

---

# Power BI (DAX)

```DAX
Ventas Totales =

SUM(

Ventas[VALOR]

)
```

---

# Excel equivalente

```excel
=SUMA(B2:B350)
```

---

# Errores comunes

## Error 1

Aplicar `sum()` sobre texto.

Ejemplo.

```
Juan

Pedro

Ana
```

No tiene sentido sumar texto.

---

## Error 2

No convertir la columna a numérica.

Ejemplo.

```
"$ 2.500"

"$ 3.800"
```

Primero debe limpiarse la información.

---

## Error 3

Olvidar valores nulos.

Siempre validar la calidad de los datos.

---

# Buenas prácticas

✔ Validar que la columna exista.

✔ Convertir a número.

```python
df["VALOR"] = pd.to_numeric(

    df["VALOR"],

    errors="coerce"

)
```

✔ Reemplazar nulos.

```python
.fillna(0)
```

✔ Separar cálculo y visualización.

---

# Plantilla Oficial del Framework

```python
# =====================================================
# KPI DE SUMA
# =====================================================

if "VALOR" in df.columns:

    total = (

        pd.to_numeric(

            df["VALOR"],

            errors="coerce"

        )

        .fillna(0)

        .sum()

    )

else:

    total = 0

st.metric(

    label="Nombre del KPI",

    value=f"$ {total:,.0f}"

)
```

---

# ¿Qué KPIs puedo construir con `sum()`?

| Área | KPI |
|------|-----|
| Comercial | Ventas Totales |
| Comercial | Facturación |
| Finanzas | Costos Totales |
| Finanzas | Gastos Totales |
| Logística | Kilómetros |
| Logística | Horas Extras |
| Logística | Viáticos |
| Logística | Peajes |
| Logística | Parqueaderos |
| Inventarios | Valor Inventario |
| Inventarios | Material Consumido |
| Producción | Producción Total |
| ANS | Días de atraso |
| RRHH | Horas Laboradas |

---

# Árbol de decisión

```
¿Qué deseas conocer?

        │

        ▼

¿Un TOTAL?

        │

      Sí

        │

        ▼

¿Existe una columna numérica?

        │

      Sí

        │

        ▼

Utiliza

sum()
```

---

# Checklist

Antes de utilizar `sum()` verifica:

□ La columna existe.

□ Es numérica.

□ Los datos fueron limpiados.

□ No existen errores de formato.

□ Los nulos fueron tratados.

□ El negocio realmente necesita un TOTAL.

---

# Lecciones aprendidas

No utilices `sum()` únicamente porque conoces la función.

Utilízala porque responde correctamente una pregunta del negocio.

Un KPI profesional nunca comienza escribiendo código.

Comienza entendiendo qué información necesita el usuario.

---

# Resumen

La función `sum()` es la base para construir indicadores financieros, operativos y logísticos.

Siempre que el negocio necesite conocer un valor acumulado, `sum()` será la operación matemática más adecuada.

Antes de utilizarla valida:

- La calidad de los datos.
- El tipo de dato.
- La regla de negocio.
- El formato de salida.

Solo entonces construye el KPI.

---

# Próxima parte

En la Parte **2.2.2** aprenderemos la función **`mean()`**, una de las operaciones más utilizadas para construir indicadores de productividad, rendimiento, tiempos promedio, costos promedio y análisis estadísticos.

---

# Parte 2.2.2 - Función `mean()`

# Introducción

Después de conocer los valores totales mediante `sum()`, normalmente el siguiente paso es responder preguntas como:

- ¿Cuál fue el tiempo promedio de atención?
- ¿Cuál fue el costo promedio por servicio?
- ¿Cuántas horas extras, en promedio, realizó cada técnico?
- ¿Cuál fue el consumo promedio de combustible?

Para responder este tipo de preguntas utilizamos la función **`mean()`**, que calcula el promedio aritmético de una columna numérica.

---

# ¿Qué hace `mean()`?

Calcula el promedio de todos los valores numéricos de una columna.

Ejemplo.

| Horas |
|------:|
|8|
|10|
|6|
|12|

Resultado

```
9
```

Porque:

```
(8 + 10 + 6 + 12) / 4 = 9
```

---

# ¿Qué construye?

Con `mean()` podemos construir indicadores como:

- Tiempo promedio
- Costo promedio
- Horas promedio
- Consumo promedio
- Producción promedio
- Ticket promedio
- Valor promedio por pedido

---

# ¿Cuándo utilizarla?

Utiliza `mean()` cuando el negocio necesite conocer un comportamiento promedio.

Ejemplos:

✔ Tiempo promedio de atención.

✔ Valor promedio por factura.

✔ Horas extras promedio.

✔ Kilómetros promedio por vehículo.

---

# ¿Cuándo NO utilizarla?

No utilices `mean()` cuando necesites:

- Totales (`sum()`)
- Conteos (`count()`)
- Valores únicos (`nunique()`)
- Valores máximos (`max()`)
- Valores mínimos (`min()`)

---

# Sintaxis

```python
df["HORAS"].mean()
```

---

# Ejemplo sencillo

```python
promedio = df["HORAS"].mean()
```

Resultado

```
9
```

---

# Ejemplo empresarial

### Dashboard Servitravel

¿Cuántas horas extras realiza, en promedio, cada vehículo?

```python
promedio = df["HORAS_EXTRA"].mean()
```

---

### Dashboard Comercial

¿Cuál fue el valor promedio de las facturas?

```python
ticket_promedio = df["VALOR_FACTURA"].mean()
```

---

### Dashboard ANS

¿Cuántos días tarda, en promedio, la atención de un pedido?

```python
dias = df["DIAS_ATENCION"].mean()
```

---

# SQL equivalente

```sql
SELECT AVG(HORAS)
FROM SERVICIOS;
```

---

# Power BI (DAX)

```DAX
Promedio Horas =

AVERAGE(

Tabla[HORAS]

)
```

---

# Excel equivalente

```excel
=PROMEDIO(B2:B100)
```

---

# Errores comunes

❌ Calcular promedios sobre columnas de texto.

❌ No convertir la columna a numérica.

❌ Promediar datos que contienen errores o registros duplicados.

---

# Buenas prácticas

✔ Validar el tipo de dato.

✔ Limpiar valores nulos.

✔ Verificar que el promedio tenga sentido para el negocio.

---

# Plantilla Oficial del Framework

```python
# =====================================================
# KPI DE PROMEDIO
# =====================================================

if "HORAS" in df.columns:

    promedio = (

        pd.to_numeric(

            df["HORAS"],

            errors="coerce"

        )

        .mean()

    )

else:

    promedio = 0

st.metric(

    "Promedio",

    f"{promedio:,.2f}"

)
```

---

# KPIs que puedo construir con `mean()`

| Área | KPI |
|------|-----|
| Comercial | Ticket Promedio |
| Comercial | Venta Promedio |
| Logística | Horas Promedio |
| Logística | Kilómetros Promedio |
| Inventarios | Consumo Promedio |
| RRHH | Horas Extras Promedio |
| ANS | Tiempo Promedio de Atención |
| Producción | Producción Promedio |

---

# Resumen

La función **`mean()`** permite conocer el comportamiento promedio de una variable.

Es una de las funciones más utilizadas para construir indicadores de productividad, eficiencia y rendimiento.

Siempre que el negocio pregunte **"¿En promedio cuánto?"**, la respuesta normalmente será **`mean()`**.

---

# Próxima parte

En la siguiente sección aprenderemos las funciones:

- `median()`
- `mode()`

y comprenderemos cuándo un promedio puede ser engañoso y por qué, en algunos casos, la mediana representa mejor la realidad del negocio.

---

# Parte 2.2.3 - Funciones `median()` y `mode()`

## Función `median()`

### ¿Qué hace?

Devuelve el valor central de un conjunto de datos ordenados.

Es útil cuando existen valores extremos que afectan el promedio.

### Sintaxis

```python
df["VALOR"].median()
```

### Ejemplo

| Valores |
|---------:|
|10|
|12|
|14|
|15|
|200|

Resultado

```
14
```

### Casos de uso

- Tiempo típico de atención.
- Salario típico.
- Valor típico de una compra.
- Duración típica de un servicio.

### SQL

```sql
MEDIAN(VALOR)
```

*(Disponible en algunos motores de base de datos).*

### Excel

```excel
=MEDIANA(A2:A100)
```

### Power BI

```DAX
MEDIAN(Tabla[VALOR])
```

### Plantilla

```python
mediana = df["VALOR"].median()

st.metric(

    "Mediana",

    f"{mediana:,.2f}"

)
```

---

## Función `mode()`

### ¿Qué hace?

Obtiene el valor que más veces se repite.

### Sintaxis

```python
df["CIUDAD"].mode()
```

### Ejemplo

| Ciudad |
|---------|
|Medellín|
|Bogotá|
|Medellín|
|Cali|
|Medellín|

Resultado

```
Medellín
```

### Casos de uso

- Ciudad con más pedidos.
- Material más utilizado.
- Actividad más frecuente.
- Tipo de servicio más realizado.

### SQL

Se obtiene mediante:

```sql
GROUP BY

ORDER BY COUNT(*) DESC
```

### Excel

```excel
=MODA()
```

### Power BI

Puede construirse mediante TOPN + COUNTROWS.

### Plantilla

```python
moda = df["CIUDAD"].mode()

if not moda.empty:

    valor = moda.iloc[0]

else:

    valor = ""

st.metric(

    "Moda",

    valor

)
```

---

## Resumen

| Función | Uso |
|----------|-----|
| median() | Valor central |
| mode() | Valor más frecuente |

---

# Parte 2.2.4 - Funciones `max()` y `min()`

## Función `max()`

### ¿Qué hace?

Obtiene el valor más alto de una columna.

### Sintaxis

```python
df["VALOR"].max()
```

### Casos de uso

- Venta más alta.
- Mayor costo.
- Mayor tiempo.
- Máxima producción.

### SQL

```sql
SELECT MAX(VALOR)
```

### Excel

```excel
=MAX(A2:A100)
```

### Power BI

```DAX
MAX(Tabla[VALOR])
```

### Plantilla

```python
mayor = df["VALOR"].max()

st.metric(

    "Valor Máximo",

    f"{mayor:,.0f}"

)
```

---

## Función `min()`

### ¿Qué hace?

Obtiene el valor más pequeño de una columna.

### Sintaxis

```python
df["VALOR"].min()
```

### Casos de uso

- Menor venta.
- Menor costo.
- Menor tiempo.
- Menor consumo.

### SQL

```sql
SELECT MIN(VALOR)
```

### Excel

```excel
=MIN(A2:A100)
```

### Power BI

```DAX
MIN(Tabla[VALOR])
```

### Plantilla

```python
menor = df["VALOR"].min()

st.metric(

    "Valor Mínimo",

    f"{menor:,.0f}"

)
```

---

## Comparativa

| Función | Devuelve |
|----------|----------|
| max() | Valor más alto |
| min() | Valor más bajo |

---

## Resumen

Estas funciones permiten identificar rápidamente los extremos de un conjunto de datos y son muy utilizadas para construir KPIs de control, desempeño y monitoreo.


---

# Parte 2.3 - Función `groupby()`

## Introducción

La función `groupby()` permite agrupar registros según una o varias columnas para calcular indicadores por categorías.

Es una de las funciones más utilizadas en análisis de datos y la base para construir rankings, tablas resumen y la mayoría de los KPIs empresariales.

---

## ¿Qué hace?

Agrupa la información y permite aplicar operaciones como:

- sum()
- mean()
- count()
- max()
- min()

sobre cada grupo.

---

## Sintaxis

```python
df.groupby("COLUMNA")
```

Con agregación.

```python
df.groupby("ZONA")["VENTAS"].sum()
```

---

## Ejemplo

### Datos

| Zona | Venta |
|------|-------:|
| Norte | 100 |
| Norte | 200 |
| Sur | 150 |
| Sur | 120 |

Código

```python
ventas = (

    df

    .groupby("ZONA")["VENTAS"]

    .sum()

)
```

Resultado

| Zona | Total |
|------|-------:|
| Norte | 300 |
| Sur | 270 |

---

## Casos de uso

- Ventas por ciudad
- Costos por centro de trabajo
- Horas extras por vehículo
- Pedidos por técnico
- Material instalado por contratista
- Servicios por actividad

---

## SQL equivalente

```sql
SELECT

ZONA,

SUM(VENTAS)

FROM VENTAS

GROUP BY ZONA;
```

---

## Excel equivalente

Tabla dinámica.

---

## Power BI

Visual agrupado o mediante SUMMARIZE().

---

## Plantilla Oficial

```python
resultado = (

    df

    .groupby("ZONA")

    .agg(

        Total=("VENTAS","sum")

    )

    .reset_index()

)
```

---

## Buenas prácticas

✔ Agrupar únicamente por columnas categóricas.

✔ Utilizar `reset_index()` para obtener un DataFrame limpio.

✔ Nombrar claramente las columnas calculadas.

---

## KPIs que puedo construir

- Ventas por zona
- Horas extras por placa
- Pedidos por municipio
- Técnicos por regional
- Costos por proyecto

---

## Resumen

`groupby()` es la función que transforma datos detallados en información resumida para la toma de decisiones.

---

# Parte 2.4 - Función `agg()`

## Introducción

Después de agrupar la información, normalmente se requiere calcular varios indicadores al mismo tiempo.

La función `agg()` permite realizar múltiples operaciones en una sola instrucción.

---

## ¿Qué hace?

Calcula varias métricas sobre un mismo grupo.

Ejemplo:

- Suma
- Promedio
- Máximo
- Mínimo
- Conteo

---

## Sintaxis

```python
df.groupby("ZONA").agg({

    "VENTAS":"sum",

    "HORAS":"mean"

})
```

---

## Ejemplo

```python
resumen = (

    df

    .groupby("ZONA")

    .agg(

        Total_Ventas=("VENTAS","sum"),

        Promedio=("VENTAS","mean"),

        Mayor=("VENTAS","max"),

        Menor=("VENTAS","min"),

        Registros=("VENTAS","count")

    )

    .reset_index()

)
```

---

## Resultado

| Zona | Total | Promedio | Mayor | Menor | Registros |
|------|-------:|---------:|-------:|-------:|-----------:|

---

## Casos de uso

- Resumen financiero
- Resumen operativo
- Dashboard comercial
- KPIs logísticos
- Indicadores ANS

---

## SQL equivalente

```sql
SELECT

ZONA,

SUM(VENTAS),

AVG(VENTAS),

MAX(VENTAS),

MIN(VENTAS),

COUNT(*)

FROM VENTAS

GROUP BY ZONA;
```

---

## Excel equivalente

Tabla dinámica con múltiples cálculos.

---

## Plantilla Oficial

```python
resultado = (

    df

    .groupby("ZONA")

    .agg(

        Total=("VALOR","sum"),

        Promedio=("VALOR","mean"),

        Maximo=("VALOR","max"),

        Minimo=("VALOR","min")

    )

    .reset_index()

)
```

---

## Buenas prácticas

✔ Asignar nombres descriptivos.

✔ Evitar columnas duplicadas.

✔ Mantener una estructura uniforme.

---

## KPIs que puedo construir

- Resumen por ciudad
- Resumen por técnico
- Resumen por vehículo
- Resumen por contratista
- Resumen por proyecto

---

## Resumen

`agg()` permite construir varias métricas en un único proceso, reduciendo código y mejorando la legibilidad.

---

# Parte 2.5 - Función `pivot_table()`

## Introducción

Cuando se necesita construir tablas resumen similares a las Tablas Dinámicas de Excel, la función recomendada es `pivot_table()`.

Es una de las herramientas más poderosas para generar reportes ejecutivos.

---

## ¿Qué hace?

Resume información cruzando filas y columnas.

Permite calcular:

- sum()
- mean()
- count()
- max()
- min()

---

## Sintaxis

```python
pd.pivot_table(

    df,

    values="VENTAS",

    index="ZONA",

    columns="MES",

    aggfunc="sum"

)
```

---

## Ejemplo

### Datos

| Zona | Mes | Venta |
|------|-----|-------:|
| Norte | Enero |100|
| Norte | Febrero|200|
| Sur | Enero |150|
| Sur | Febrero|180|

Resultado

| Zona | Enero | Febrero |
|------|-------:|---------:|
| Norte |100|200|
| Sur|150|180|

---

## Casos de uso

- Ventas por mes
- Costos por año
- Horas por técnico
- Producción por planta
- Pedidos por regional
- Material por actividad

---

## SQL equivalente

Se obtiene mediante:

```sql
PIVOT
```

(o mediante SUM + GROUP BY según el motor).

---

## Excel equivalente

Tabla Dinámica.

---

## Plantilla Oficial

```python
tabla = pd.pivot_table(

    df,

    values="VALOR",

    index="ZONA",

    columns="MES",

    aggfunc="sum",

    fill_value=0

)
```

---

## Buenas prácticas

✔ Utilizar `fill_value=0`.

✔ Nombrar correctamente filas y columnas.

✔ Ordenar los índices antes de mostrar la tabla.

---

## KPIs que puedo construir

- Ventas por mes
- Costos por regional
- Horas por vehículo
- Material instalado por contratista
- Producción mensual
- Indicadores ANS por período

---

## Resumen

`pivot_table()` es el equivalente en Pandas a una Tabla Dinámica de Excel y una de las herramientas más importantes para construir reportes ejecutivos y dashboards empresariales.

---

# Parte 3 - Construcción de KPIs Empresariales

## Objetivo

Un KPI no es únicamente una operación matemática. Es la representación de una necesidad del negocio mediante datos confiables.

Todo KPI debe responder una pregunta específica.

---

# Flujo de construcción

```

Necesidad del negocio

↓

Fuente de datos

↓

Limpieza

↓

Validación

↓

Cálculo

↓

Formato

↓

Visualización

↓

Interpretación

```

---

# Plantilla Oficial del Framework

| Campo | Descripción |
|--------|-------------|
| Nombre del KPI | Nombre del indicador |
| Objetivo | ¿Qué mide? |
| Fuente | Archivo o Base de Datos |
| Columnas | Datos utilizados |
| Fórmula | Operación matemática |
| Tipo | Conteo, Suma, Promedio, etc. |
| Formato | Número, %, $, Tiempo |
| Frecuencia | Diario, Semanal, Mensual |
| Responsable | Área propietaria |

---

# KPIs Financieros

Ejemplos

- Ventas Totales
- Costos Totales
- Utilidad
- Ticket Promedio
- Rentabilidad

Funciones utilizadas

```python
sum()

mean()

groupby()
```

---

# KPIs Logísticos

Ejemplos

- Vehículos utilizados
- Horas Extras
- Kilómetros recorridos
- Viáticos
- Peajes
- Parqueaderos

Funciones utilizadas

```python
sum()

count()

groupby()
```

---

# KPIs de ANS

Ejemplos

- Pedidos Atendidos
- Tiempo Promedio
- Pedidos Vencidos
- Nivel de Cumplimiento
- Alertas

Funciones utilizadas

```python
count()

mean()

groupby()
```

---

# KPIs de Inventario

Ejemplos

- Material instalado
- Material reintegrado
- Stock actual
- Valor Inventario
- Material pendiente

Funciones utilizadas

```python
sum()

groupby()

pivot_table()
```

---

# KPIs de Productividad

Ejemplos

- Servicios por técnico
- Producción diaria
- Producción mensual
- Tiempo promedio
- Rendimiento

---

# Buenas prácticas

✔ Un KPI debe responder una pregunta.

✔ Un KPI debe ser verificable.

✔ Debe existir una regla de negocio documentada.

✔ Debe poder recalcularse manualmente.

---

# Resumen

Los KPIs empresariales transforman datos operativos en información útil para la toma de decisiones.

---

# Parte 4 - Diseño Visual de KPIs

## Objetivo

Un buen KPI no solamente debe calcularse correctamente.

También debe presentarse de manera clara y profesional.

---

# Componentes de una Card

```

┌──────────────────────┐

📊 Total Ventas

$ 285.000.000

▲ +8%

└──────────────────────┘

```

---

# Elementos de una Card

- Icono
- Nombre
- Valor
- Tendencia
- Color

---

# Colores recomendados

| Estado | Color |
|---------|--------|
| Excelente | 🟢 Verde |
| Advertencia | 🟡 Amarillo |
| Crítico | 🔴 Rojo |
| Informativo | 🔵 Azul |
| Neutro | ⚪ Gris |

---

# Iconografía

| Tipo | Icono |
|-------|--------|
| Dinero | 💰 |
| Tiempo | ⏱ |
| Vehículos | 🚚 |
| Inventario | 📦 |
| Usuarios | 👤 |
| Producción | 🏭 |
| Alertas | ⚠ |
| Calidad | ✅ |

---

# Distribución recomendada

Fila 1

```

KPI KPI KPI KPI

```

Fila 2

```

Gráfico Gráfico

Tabla

```

Fila 3

```

Detalle

```

---

# Formatos

Dinero

```
$ 2.350.000
```

Cantidad

```
2.350
```

Porcentaje

```
87.5 %
```

Tiempo

```
2.5 días
```

---

# Buenas prácticas

✔ Máximo 6 KPIs por fila.

✔ Mantener la misma altura.

✔ Utilizar colores consistentes.

✔ Evitar exceso de información.

✔ Mostrar siempre unidades.

---

# Resumen

Un Dashboard profesional comunica información en pocos segundos.

La simplicidad mejora la interpretación.

---

# Parte 5 - KPIs Avanzados

## Objetivo

Muchos indicadores requieren operaciones adicionales además de una simple suma o promedio.

---

# Porcentajes

Ejemplo

```
Pedidos Cumplidos

─────────────── x 100

Pedidos Totales
```

Python

```python
cumplimiento = (

cumplidos

/

total

) * 100
```

---

# Variaciones

Ejemplo

```
Mes Actual

-

Mes Anterior
```

Python

```python
variacion = actual - anterior
```

---

# Variación %

```python
variacion = (

(actual-anterior)

/

anterior

) * 100
```

---

# Acumulados

```python
df["ACUMULADO"] = (

df["VENTAS"]

.cumsum()

)
```

---

# Rankings

Top 10

```python
df.nlargest(

10,

"VENTAS"

)
```

Bottom 10

```python
df.nsmallest(

10,

"VENTAS"

)
```

---

# Comparativos

Ejemplos

- Año vs Año
- Mes vs Mes
- Región vs Región
- Técnico vs Técnico

---

# Semáforos

| Valor | Estado |
|--------|---------|
| >95% | 🟢 Excelente |
| 80-95% | 🟡 Atención |
| <80% | 🔴 Crítico |

---

# Top N

Top Clientes

Top Técnicos

Top Vehículos

Top Productos

Top Municipios

---

# KPIs Compuestos

Ejemplo

```
Costo por Servicio

=

Costo Total

/

Servicios Ejecutados
```

---

# Checklist

Antes de publicar un KPI

□ Fórmula validada

□ Datos limpios

□ Resultado verificado

□ Regla documentada

□ Formato correcto

□ Responsable definido

---

# Conclusión

Los KPIs avanzados permiten construir dashboards ejecutivos capaces de medir desempeño, tendencias, productividad y cumplimiento mediante indicadores comparables y fáciles de interpretar.

# Capítulo 10 - Visualizaciones Profesionales para Dashboards

---

# Objetivo

Después de construir los KPIs, el siguiente paso es presentarlos de forma clara para facilitar la toma de decisiones.

Una buena visualización permite identificar tendencias, comparaciones y anomalías en pocos segundos.

El objetivo de este capítulo es documentar los gráficos más utilizados en dashboards empresariales desarrollados con Python, Streamlit y Plotly.

---

# Flujo de Visualización

```

Datos

↓

Limpieza

↓

Cálculos

↓

KPIs

↓

Gráficos

↓

Dashboard

↓

Toma de decisiones

```

---

# Principios de Diseño

Un gráfico debe responder una pregunta.

No debe utilizarse únicamente porque "se vea bonito".

Antes de construir cualquier gráfico pregúntese:

- ¿Qué quiero mostrar?
- ¿Qué decisión ayudará a tomar?
- ¿Existe un gráfico más simple?

---

# Tipos de Visualización

| Tipo | Uso |
|-------|-----|
| Barras | Comparar categorías |
| Líneas | Mostrar tendencias |
| Áreas | Evolución acumulada |
| Dona | Participación porcentual |
| Dispersión | Relaciones entre variables |
| Heatmap | Concentración de datos |
| Tabla | Información detallada |
| KPI Card | Indicadores principales |
| Gauge | Cumplimiento de metas |
| Mapa | Distribución geográfica |

---

# Reglas del Framework

✔ Utilizar máximo un objetivo por gráfico.

✔ Evitar gráficos innecesarios.

✔ Utilizar colores corporativos.

✔ Mantener la misma tipografía.

✔ Mostrar siempre títulos claros.

✔ Indicar unidades de medida.

✔ Evitar fondos recargados.

---

# Paleta Corporativa Recomendada

| Color | Uso |
|--------|-----|
| Verde | Valores positivos |
| Rojo | Alertas |
| Amarillo | Advertencias |
| Azul | Información |
| Gris | Valores neutros |

---

# Distribución Recomendada

Fila 1

KPIs

Fila 2

Gráficos principales

Fila 3

Tablas

Fila 4

Detalle

---

# Próximas Secciones

10.1 Gráficos de Barras

10.2 Gráficos de Líneas

10.3 Gráficos de Áreas

10.4 Gráficos Circulares

10.5 Heatmaps

10.6 Tablas Profesionales

10.7 Mapas

10.8 Dashboard Ejecutivo

---

# 10.1 - Gráficos de Barras

## Objetivo

Comparar valores entre diferentes categorías.

Es uno de los gráficos más utilizados en análisis empresarial.

---

## ¿Cuándo utilizarlo?

✔ Comparar ciudades.

✔ Comparar técnicos.

✔ Comparar vehículos.

✔ Comparar costos.

✔ Comparar ventas.

---

## Ejemplo

Ventas por ciudad

```

Medellín ██████████

Bogotá ███████

Cali █████

```

---

## Plotly

```python
import plotly.express as px

fig = px.bar(

    df,

    x="CIUDAD",

    y="VENTAS",

    color="CIUDAD"

)

st.plotly_chart(

    fig,

    use_container_width=True

)
```

---

## Buenas prácticas

✔ Ordenar de mayor a menor.

✔ Mostrar etiquetas.

✔ Utilizar pocos colores.

✔ Evitar demasiadas categorías.

---

## Casos Empresariales

- Ventas por ciudad.

- Horas extras por vehículo.

- Pedidos por técnico.

- Material instalado por contratista.

---

## Resumen

El gráfico de barras es el más utilizado para comparar categorías.

---

# 10.2 - Gráficos de Líneas

## Objetivo

Mostrar tendencias en el tiempo.

---

## ¿Cuándo utilizarlo?

✔ Ventas mensuales.

✔ Producción diaria.

✔ ANS por semana.

✔ Costos por mes.

---

## Plotly

```python
fig = px.line(

    df,

    x="MES",

    y="VENTAS",

    markers=True

)

st.plotly_chart(

    fig,

    use_container_width=True

)
```

---

## Casos Empresariales

- Evolución de ventas.

- Horas extras por mes.

- Servicios ejecutados.

- Cumplimiento ANS.

---

## Buenas prácticas

✔ Orden cronológico.

✔ No utilizar demasiadas líneas.

✔ Mostrar marcadores.

✔ Agregar etiquetas.

---

## Resumen

Ideal para mostrar comportamiento histórico.

---

# 10.3 - Gráfico de Áreas

## Objetivo

Mostrar evolución acumulada.

---

## Ejemplo

Producción acumulada.

Ventas acumuladas.

Costos acumulados.

---

## Plotly

```python
fig = px.area(

    df,

    x="MES",

    y="VENTAS"

)
```

---

## Uso

✔ Tendencias acumuladas.

✔ Producción.

✔ Inventarios.

---

## Resumen

Muy útil para representar crecimiento.

---

# 10.4 - Gráfico Dona / Pastel

## Objetivo

Mostrar participación porcentual.

---

## ¿Cuándo utilizarlo?

✔ Participación por regional.

✔ Participación por actividad.

✔ Distribución de costos.

---

## Plotly

```python
fig = px.pie(

    df,

    names="ZONA",

    values="VENTAS",

    hole=.55

)
```

---

## Buenas prácticas

✔ Máximo 6 categorías.

✔ Mostrar porcentaje.

✔ Preferir Dona sobre Pastel.

---

## Evitar

Más de 8 categorías.

Comparaciones complejas.

---

## Resumen

Ideal para mostrar participación.

# 10.5 - Heatmaps

---

# Objetivo

Un Heatmap (Mapa de Calor) permite identificar rápidamente concentraciones, patrones y zonas críticas mediante colores.

Es ideal para detectar comportamientos que serían difíciles de observar en una tabla.

---

# ¿Cuándo utilizarlo?

✔ Cumplimiento ANS por municipio.

✔ Producción por día y técnico.

✔ Ventas por ciudad y mes.

✔ Material instalado por regional.

✔ Actividades por contratista.

---

# Ejemplo

```

             Enero   Febrero   Marzo

Medellín       🟢        🟢       🟡

Bogotá         🔴        🟡       🟢

Cali           🟢        🟢       🟢

```

---

# Plotly

```python
import plotly.express as px

fig = px.imshow(

    matriz,

    text_auto=True,

    color_continuous_scale="Greens"

)

st.plotly_chart(

    fig,

    use_container_width=True

)
```

---

# Buenas prácticas

✔ Utilizar pocas escalas de color.

✔ Mostrar valores.

✔ Ordenar filas y columnas.

✔ Utilizar títulos descriptivos.

---

# Casos Empresariales

- Dashboard ANS
- Dashboard Comercial
- Dashboard Producción
- Dashboard Inventarios

---

# Resumen

Los Heatmaps permiten descubrir patrones visuales rápidamente y facilitan la identificación de zonas críticas.


# 10.6 - Tablas Profesionales (AgGrid)

---

# Objetivo

Aunque los gráficos resumen la información, las tablas permiten consultar el detalle de los datos.

AgGrid es la herramienta recomendada para construir tablas profesionales en Streamlit.

---

# Funcionalidades

✔ Ordenamiento

✔ Filtros

✔ Búsqueda

✔ Redimensionamiento

✔ Selección

✔ Exportación

✔ Paginación

---

# Arquitectura

```

DataFrame

↓

AgGrid

↓

Tabla Profesional

```

---

# Ejemplo

```python
AgGrid(

    df,

    gridOptions=gb.build(),

    theme="streamlit",

    fit_columns_on_grid_load=True,

    allow_unsafe_jscode=True

)
```

---

# Buenas prácticas

✔ Encabezados claros.

✔ Columnas alineadas.

✔ Números formateados.

✔ Congelar columnas importantes.

✔ Mostrar filtros.

✔ Activar paginación.

---

# Casos Empresariales

- Detalle de pedidos.

- Inventario.

- Horas extras.

- Costos.

- Material instalado.

- ANS.

---

# Resumen

Toda visualización debe tener una tabla de respaldo para validar la información.


# 10.7 - Mapas Interactivos

---

# Objetivo

Los mapas permiten representar información geográfica de manera visual.

Son ideales para proyectos donde la ubicación es importante.

---

# Herramientas

| Librería | Uso |
|----------|-----|
| Plotly | Mapas rápidos |
| Folium | Mapas interactivos |
| Leaflet | Dashboards Web |

---

# Casos de uso

✔ Pedidos por municipio.

✔ Técnicos en campo.

✔ Vehículos.

✔ Instalaciones.

✔ Cobertura.

✔ Rutas.

---

# Plotly

```python
fig = px.scatter_map(

    df,

    lat="LAT",

    lon="LON",

    color="ESTADO",

    zoom=8

)
```

---

# Folium

```python
import folium

mapa = folium.Map(

    location=[6.24,-75.57],

    zoom_start=11

)
```

---

# Buenas prácticas

✔ Utilizar coordenadas válidas.

✔ Agrupar marcadores.

✔ Colores según estado.

✔ Información emergente (Popup).

✔ Leyenda.

---

# Casos Empresariales

- Dashboard ANS.

- Dashboard Servitravel.

- Cobertura Comercial.

- Inventario Geográfico.

---

# Resumen

Los mapas convierten datos geográficos en información fácil de interpretar.


# 10.8 - Diseño de Dashboards Ejecutivos

---

# Objetivo

Un Dashboard Ejecutivo debe comunicar el estado del negocio en pocos segundos.

No debe ser únicamente bonito; debe facilitar la toma de decisiones.

---

# Arquitectura Recomendada

```

HEADER

↓

Filtros

↓

KPIs

↓

Gráficos

↓

Tablas

↓

Detalle

↓

Footer

```

---

# Distribución Recomendada

```

┌──────────────────────────────────────────────┐

HEADER

└──────────────────────────────────────────────┘

Filtros

┌──────┬──────┬──────┬──────┐

 KPI    KPI    KPI    KPI

└──────┴──────┴──────┴──────┘

┌──────────────┬──────────────┐

 Gráfico 1     Gráfico 2

└──────────────┴──────────────┘

┌──────────────────────────────┐

 Tabla Profesional

└──────────────────────────────┘

Footer

```

---

# Reglas del Framework

✔ Máximo 6 KPIs.

✔ Máximo 2 gráficos por fila.

✔ Mostrar filtros en la parte superior.

✔ Mantener la misma paleta de colores.

✔ Tipografía uniforme.

✔ Espacios suficientes.

✔ No saturar la pantalla.

---

# Checklist

Antes de publicar un Dashboard

□ KPIs validados.

□ Fórmulas documentadas.

□ Datos consistentes.

□ Colores corporativos.

□ Navegación sencilla.

□ Buen rendimiento.

□ Responsive.

□ Información verificable.

---

# Filosofía del Framework

Todo Dashboard debe cumplir cuatro principios:

- Exactitud.
- Claridad.
- Rapidez.
- Facilidad de uso.

Si un usuario necesita más de unos segundos para comprender el estado del negocio, el Dashboard debe simplificarse.

---

# Conclusión

Un Dashboard Ejecutivo no consiste únicamente en mostrar datos. Su propósito es transformar información compleja en conocimiento útil para apoyar decisiones rápidas y fundamentadas.

Con este capítulo se completa el ciclo del Framework:

**Datos → Transformación → KPIs → Visualización → Dashboard Ejecutivo.**
