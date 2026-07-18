# Filtros Profesionales para Dashboards

---

# Objetivo

Los filtros permiten al usuario explorar la información sin modificar los datos originales.

Un Dashboard Ejecutivo debe ofrecer filtros intuitivos, rápidos y fáciles de utilizar para responder preguntas del negocio.

---

# Flujo General

```

Base de Datos

↓

DataFrame

↓

Filtros

↓

KPIs

↓

Gráficos

↓

Tablas

↓

Dashboard

```

---

# ¿Por qué utilizar filtros?

Los filtros permiten:

✔ Consultar información específica.

✔ Reducir el volumen de datos.

✔ Mejorar el rendimiento.

✔ Personalizar el análisis.

✔ Facilitar la toma de decisiones.

---

# Tipos de filtros

| Tipo | Uso |
|------|-----|
| Fecha | Día, Semana, Mes, Año |
| Texto | Ciudad, Cliente, Zona |
| Numérico | Rangos |
| Lista | Categorías |
| Estado | Activo, Pendiente, Cerrado |
| Booleano | Sí / No |

---

# Reglas del Framework

✔ Todos los filtros deben ubicarse en la parte superior.

✔ Deben ser fáciles de identificar.

✔ Mantener el mismo estilo visual.

✔ Deben afectar todos los componentes del Dashboard.

✔ Nunca modificar el DataFrame original.

---

# Arquitectura

```

DataFrame Original

↓

Filtros

↓

DataFrame Filtrado

↓

KPIs

↓

Gráficos

↓

Tablas

```

---

# Próximas Secciones

11.1 Selectbox

11.2 Multiselect

11.3 Date Input

11.4 Slider

11.5 Checkbox

11.6 Filtros Encadenados

11.7 Botón Limpiar

11.8 Buenas Prácticas

# 11.1 - Selectbox

---

# Objetivo

Permite seleccionar un único valor de una lista.

---

## Streamlit

```python
zona = st.selectbox(

    "Zona",

    sorted(df["ZONA"].unique())

)
```

---

## Aplicación

- Regional
- Ciudad
- Contratista
- Proyecto

---

## Filtrado

```python
df_filtrado = df[

    df["ZONA"] == zona

]
```

---

## Buenas prácticas

✔ Ordenar opciones.

✔ Incluir "Todos" cuando aplique.

✔ Mostrar etiquetas claras.

# 11.2 - Multiselect

---

# Objetivo

Permite seleccionar varios valores simultáneamente.

---

## Streamlit

```python
zonas = st.multiselect(

    "Zona",

    sorted(df["ZONA"].unique())

)
```

---

## Filtrado

```python
if zonas:

    df = df[

        df["ZONA"].isin(zonas)

    ]
```

---

## Casos

- Varias ciudades.

- Varias regionales.

- Varias actividades.

- Varios técnicos.

---

## Buenas prácticas

✔ Permitir seleccionar múltiples valores.

✔ Mantener orden alfabético.

# 11.3 - Date Input

---

# Objetivo

Filtrar información por fechas.

---

## Streamlit

```python
fecha_inicio,

fecha_fin = st.date_input(

    "Rango",

    value=(

        df.FECHA.min(),

        df.FECHA.max()

    )

)
```

---

## Filtrado

```python
df = df[

    (df["FECHA"] >= fecha_inicio)

    &

    (df["FECHA"] <= fecha_fin)

]
```

---

## Casos

- Mes.

- Semana.

- Año.

- Períodos.

# 11.4 - Slider

---

# Objetivo

Permite filtrar rangos numéricos.

---

## Streamlit

```python
rango = st.slider(

    "Valor",

    0,

    100,

    (10,80)

)
```

---

## Casos

- Costos.

- Edad.

- Horas.

- Cantidades.

# 11.5 - Checkbox

---

# Objetivo

Mostrar u ocultar información.

---

## Streamlit

```python
mostrar = st.checkbox(

    "Mostrar detalle"

)
```

---

## Ejemplo

```python
if mostrar:

    st.dataframe(df)
```

---

## Casos

- Mostrar detalle.

- Mostrar tabla.

- Mostrar mapa.

# 11.6 - Filtros Encadenados

---

# Objetivo

Un filtro depende del resultado del anterior.

---

## Ejemplo

```

Regional

↓

Ciudad

↓

Técnico

↓

Pedido

```

---

## Código

```python
regional = st.selectbox(...)

df1 = df[

    df["REGIONAL"] == regional

]

ciudad = st.selectbox(

    ...,

    df1["CIUDAD"].unique()

)
```

---

## Ventajas

✔ Menos opciones.

✔ Mayor velocidad.

✔ Mejor experiencia.

# 11.7 - Botón Limpiar

---

# Objetivo

Restablecer todos los filtros.

---

## Streamlit

```python
if st.button(

    "Limpiar Filtros"

):

    st.rerun()
```

---

## Buenas prácticas

Siempre ofrecer una forma rápida de volver al estado inicial.

# 11.8 - Buenas Prácticas

---

# Checklist

□ Filtros visibles.

□ Etiquetas claras.

□ Orden lógico.

□ Todos afectan el Dashboard.

□ No modificar el DataFrame original.

□ Validar valores nulos.

□ Evitar filtros innecesarios.

□ Mantener diseño uniforme.

---

# Filosofía del Framework

Los filtros deben ayudar al usuario a encontrar información, no complicar la navegación.

Un Dashboard profesional necesita pocos filtros, pero bien diseñados.

Mientras menos clics necesite el usuario para llegar a la información, mejor será la experiencia.

---

# Resumen

Los filtros son el punto de entrada al análisis de datos.

Un buen diseño de filtros mejora la usabilidad, el rendimiento y la calidad del Dashboard.
