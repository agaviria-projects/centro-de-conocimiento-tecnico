# Capítulo 12 - AgGrid

---

# Objetivo

AgGrid es el componente oficial utilizado por el Framework ELITE para visualizar DataFrames de forma profesional dentro de los Dashboards desarrollados en Streamlit.

Su principal objetivo es transformar grandes volúmenes de datos en tablas rápidas, organizadas e interactivas, permitiendo al usuario consultar, filtrar, ordenar y analizar información sin necesidad de exportarla a Excel.

---

# ¿Qué es AgGrid?

AgGrid es una librería especializada en la construcción de tablas interactivas.

Dentro del Framework actúa como la capa de presentación de los DataFrames generados por Pandas.

```

Excel

↓

Pandas

↓

DataFrame

↓

AgGrid

↓

Usuario

```

---

# ¿Por qué utilizar AgGrid?

Un DataFrame mostrado con:

```python
st.dataframe(df)
```

permite únicamente visualizar la información.

AgGrid agrega funcionalidades avanzadas como:

✔ Ordenamiento

✔ Filtros

✔ Búsqueda

✔ Scroll virtual

✔ Redimensionamiento

✔ Selección de texto

✔ Paginación

✔ Personalización visual

✔ Alto rendimiento

---

# Arquitectura

```

Excel

↓

Lectura

↓

Pandas

↓

DataFrame

↓

GridOptionsBuilder

↓

Configuración

↓

AgGrid

↓

Dashboard

```

---

# Flujo del Framework

```

DataFrame

↓

Configurar columnas

↓

Configurar Grid

↓

Aplicar estilos

↓

Mostrar Tabla

```

---

# Instalación

```bash
pip install streamlit-aggrid
```

---

# Importaciones

```python
from st_aggrid import (

    AgGrid,

    GridOptionsBuilder,

    ColumnsAutoSizeMode,

    JsCode

)
```

---

# Componentes principales

| Componente | Función |
|------------|----------|
| AgGrid | Renderiza la tabla |
| GridOptionsBuilder | Configura la tabla |
| JsCode | Personaliza estilos |
| ColumnsAutoSizeMode | Ajusta columnas |

---

# Filosofía del Framework

Toda tabla profesional debe construirse mediante un proceso organizado.

Nunca debe llamarse AgGrid directamente sin configurar previamente el Grid.

# 12.1 - GridOptionsBuilder

---

# Objetivo

GridOptionsBuilder permite construir toda la configuración de la tabla antes de visualizarla.

Es el corazón de AgGrid.

---

## Crear configuración

```python
gb = GridOptionsBuilder.from_dataframe(df)
```

A partir de este objeto se configuran todas las características de la tabla.

---

## ¿Qué permite configurar?

✔ Columnas

✔ Filtros

✔ Ordenamiento

✔ Paginación

✔ Altura

✔ Selección

✔ Eventos

✔ Estilos

---

## Flujo

```

DataFrame

↓

GridOptionsBuilder

↓

GridOptions

↓

AgGrid

```

---

## Buenas prácticas

✔ Crear siempre el GridOptionsBuilder al inicio.

✔ Configurar primero las columnas.

✔ Configurar luego la tabla.

✔ Aplicar estilos al final.

# 12.2 - Configuración de Columnas

---

# Objetivo

Las columnas representan la estructura de la información.

Una buena configuración mejora la lectura y la experiencia del usuario.

---

## Configuración general

```python
gb.configure_default_column(

    sortable=True,

    filter=True,

    editable=False,

    resizable=True

)
```

---

## Opciones más utilizadas

| Parámetro | Función |
|-----------|----------|
| sortable | Permite ordenar |
| filter | Activa filtros |
| editable | Permite editar |
| resizable | Cambiar ancho |
| floatingFilter | Filtro bajo el encabezado |
| minWidth | Ancho mínimo |

---

## Recomendación

Dentro del Framework todas las columnas deberán:

✔ Poder ordenarse.

✔ Poder filtrarse.

✔ Ser redimensionables.

✔ No ser editables por defecto.

# 12.3 - Configuración del Grid

---

# Objetivo

Controlar el comportamiento general de la tabla.

---

## Ejemplo

```python
gb.configure_grid_options(

    pagination=True,

    paginationPageSize=20,

    animateRows=True,

    rowHeight=38,

    headerHeight=42,

    enableCellTextSelection=True

)
```

---

## Opciones recomendadas

| Parámetro | Uso |
|-----------|-----|
| pagination | Activar paginación |
| paginationPageSize | Registros por página |
| animateRows | Animación |
| rowHeight | Alto filas |
| headerHeight | Alto encabezado |
| enableCellTextSelection | Copiar texto |

---

## Buenas prácticas

✔ Mantener alturas uniformes.

✔ Activar paginación.

✔ Permitir copiar información.

# 12.4 - Personalización con JsCode

---

# Objetivo

JsCode permite aplicar estilos avanzados directamente sobre la tabla.

Es especialmente útil cuando se requiere cambiar colores, alineaciones o formatos de las celdas.

---

## Ejemplo

```python
cellstyle = JsCode("""

function(params){

    return{

        textAlign:'center'

    }

}

""")
```

---

## Aplicaciones

✔ Centrar texto.

✔ Colorear filas.

✔ Formatear números.

✔ Resaltar estados.

✔ Aplicar reglas visuales.

---

## Recomendación

Utilizar JsCode únicamente cuando las opciones nativas de AgGrid no sean suficientes.

# 12.5 - Renderizar la Tabla

---

# Objetivo

Después de configurar el Grid, la tabla se presenta al usuario mediante AgGrid.

---

## Ejemplo

```python
AgGrid(

    df,

    gridOptions=gb.build(),

    theme="streamlit",

    allow_unsafe_jscode=True,

    columns_auto_size_mode=

    ColumnsAutoSizeMode.FIT_CONTENTS,

    height=500

)
```

---

## Parámetros importantes

| Parámetro | Función |
|-----------|----------|
| gridOptions | Configuración |
| theme | Tema visual |
| height | Altura |
| allow_unsafe_jscode | Habilita JsCode |
| columns_auto_size_mode | Ajuste automático |

---

## Resultado

El usuario obtiene una tabla profesional con filtros, ordenamiento, paginación y alto rendimiento.

# 12.6 - Optimización

---

# Recomendaciones

✔ Evitar columnas innecesarias.

✔ Filtrar antes de mostrar.

✔ Reducir cálculos dentro de AgGrid.

✔ Utilizar paginación.

✔ Evitar estilos excesivos.

✔ Mantener un número razonable de columnas visibles.

---

# Grandes volúmenes

Cuando el DataFrame contiene miles de registros:

```

Base de Datos

↓

Pandas

↓

Filtrar

↓

AgGrid

```

No es recomendable enviar información que el usuario no utilizará.

# 12.7 - Estándar Oficial del Framework

---

Toda tabla desarrollada para el Framework ELITE deberá cumplir con el siguiente estándar:

□ GridOptionsBuilder.

□ Columnas configuradas.

□ Filtros activos.

□ Ordenamiento activo.

□ Columnas redimensionables.

□ Paginación.

□ Selección de texto.

□ Alturas uniformes.

□ Tema corporativo.

□ Compatible con el diseño general del Dashboard.

---

# Conclusión

AgGrid constituye el componente oficial para la visualización tabular dentro del Framework ELITE.

Su correcta configuración garantiza una experiencia consistente en todos los módulos del Dashboard, permitiendo consultar grandes volúmenes de información de forma rápida, organizada y alineada con los estándares definidos para el proyecto.

