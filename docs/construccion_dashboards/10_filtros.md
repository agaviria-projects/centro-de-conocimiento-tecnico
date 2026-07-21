# Filtros Profesionales para Dashboards

Este archivo reemplaza la versión anterior.

## Objetivo

Los filtros permiten al usuario explorar la información sin modificar
los datos originales.

## Arquitectura

``` text
DataFrame Original
        │
        ▼
components/filtros.py
        │
        ▼
app.py
        │
        ▼
DataFrame Filtrado
        │
        ▼
analytics/
        │
        ▼
Dashboard
```

## Reglas

-   Todos los filtros deben ubicarse en la parte superior.
-   Nunca modificar el DataFrame original.
-   Todos los componentes deben trabajar sobre el DataFrame filtrado.

## Orden recomendado

``` text
Leer archivo
    │
    ▼
DataFrame
    │
    ▼
Aplicar filtros
    │
    ▼
DataFrame Filtrado
    │
    ▼
KPIs
    │
    ▼
Gráficos
    │
    ▼
Tablas
```

## Selectbox

``` python
zona = st.selectbox("Zona", sorted(df["ZONA"].unique()))

df_filtrado = df.copy()

if zona != "Todos":
    df_filtrado = df_filtrado[df_filtrado["ZONA"] == zona]
```

## Multiselect

``` python
zonas = st.multiselect("Zona", sorted(df["ZONA"].unique()))

if zonas:
    df_filtrado = df_filtrado[df_filtrado["ZONA"].isin(zonas)]
```

## Date Input

``` python
fecha_inicio, fecha_fin = st.date_input(
    "Rango",
    value=(df["FECHA"].min(), df["FECHA"].max())
)
```

## Slider

``` python
rango = st.slider("Valor",0,100,(10,80))
```

## Checkbox

``` python
mostrar = st.checkbox("Mostrar detalle")
```

## Filtros encadenados

``` text
Regional
  ↓
Ciudad
  ↓
Zona
  ↓
Técnico
```

## Limpiar filtros

``` python
if st.button("Limpiar filtros"):
    st.rerun()
```

## Regla de Oro

Los filtros únicamente producen un DataFrame filtrado que será utilizado
por KPIs, gráficos y tablas.
