# Capítulo 12 - AgGrid

# AgGrid Profesional para el Framework ELITE

------------------------------------------------------------------------

# Objetivo

En el capítulo anterior aprendimos **cómo diseñar una tabla
profesional** dentro del Framework.

En este capítulo aprenderemos **cómo construirla** utilizando AgGrid.

La meta no es aprender todas las opciones de la librería, sino disponer
de una **plantilla oficial reutilizable** para cualquier Dashboard
desarrollado con Streamlit.

------------------------------------------------------------------------

# Arquitectura

``` text
Excel / Base de Datos
        │
        ▼
Pandas
        │
        ▼
DataFrame
        │
        ▼
analytics/
        │
        ▼
components/tablas.py
        │
        ▼
GridOptionsBuilder
        │
        ▼
AgGrid
        │
        ▼
Dashboard
```

------------------------------------------------------------------------

# Filosofía del Framework

AgGrid es únicamente el motor que renderiza la tabla.

Toda la lógica del negocio ya debe estar resuelta antes de llegar a
AgGrid.

``` text
Filtros

↓

df_filtrado

↓

Analytics

↓

AgGrid
```

Nunca utilizar AgGrid para calcular información.

------------------------------------------------------------------------

# Instalación

``` bash
pip install streamlit-aggrid
```

------------------------------------------------------------------------

# Importaciones Oficiales

``` python
from st_aggrid import (
    AgGrid,
    GridOptionsBuilder,
    ColumnsAutoSizeMode,
    JsCode,
)
```

------------------------------------------------------------------------

# Flujo Oficial

``` text
DataFrame

↓

Configurar Columnas

↓

Configurar Grid

↓

Aplicar Estilos

↓

Renderizar AgGrid
```

------------------------------------------------------------------------

# Plantilla Oficial del Framework

Esta es la estructura recomendada para **components/tablas.py**.

``` python
from st_aggrid import (
    AgGrid,
    GridOptionsBuilder,
    ColumnsAutoSizeMode,
    JsCode,
)

import pandas as pd


def mostrar_tabla(
    df: pd.DataFrame,
    height: int = 420,
):

    if df is None or df.empty:
        return

    gb = GridOptionsBuilder.from_dataframe(df)

    # ======================================================
    # COLUMNAS
    # ======================================================

    gb.configure_default_column(
        sortable=True,
        filter=True,
        floatingFilter=True,
        editable=False,
        resizable=True,
    )

    # ======================================================
    # GRID
    # ======================================================

    gb.configure_grid_options(
        pagination=True,
        paginationPageSize=20,
        animateRows=True,
        rowHeight=38,
        headerHeight=42,
        enableCellTextSelection=True,
    )

    # ======================================================
    # TABLA
    # ======================================================

    AgGrid(
        df,
        gridOptions=gb.build(),
        theme="streamlit",
        height=height,
        allow_unsafe_jscode=True,
        columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS,
    )
```

------------------------------------------------------------------------

# ¿Por qué esta plantilla?

Porque ya incorpora los estándares del Framework:

-   Ordenamiento.
-   Filtros.
-   Responsive.
-   Paginación.
-   Selección de texto.
-   Autoajuste de columnas.

Será el punto de partida para todos los proyectos.

------------------------------------------------------------------------

# Configuración de Columnas

``` python
gb.configure_default_column(
    sortable=True,
    filter=True,
    floatingFilter=True,
    editable=False,
    resizable=True,
)
```

Recomendaciones:

-   Todas las columnas deben ordenarse.
-   Todas deben permitir filtros.
-   No deben ser editables por defecto.

------------------------------------------------------------------------

# Configuración del Grid

``` python
gb.configure_grid_options(
    pagination=True,
    paginationPageSize=20,
    animateRows=True,
    rowHeight=38,
    headerHeight=42,
    enableCellTextSelection=True,
)
```

------------------------------------------------------------------------

# Personalización con JsCode

Utilizar `JsCode` únicamente para reglas visuales como:

-   Estados.
-   Colores.
-   Alineaciones.
-   Formatos especiales.

Evitar colocar lógica de negocio.

------------------------------------------------------------------------

# Renderizar la Tabla

``` python
AgGrid(
    df,
    gridOptions=gb.build(),
    theme="streamlit",
    allow_unsafe_jscode=True,
    columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS,
    height=420,
)
```

------------------------------------------------------------------------

# Buenas prácticas

-   Filtrar antes de mostrar.
-   Mostrar únicamente columnas necesarias.
-   Mantener alturas uniformes.
-   Utilizar un único estilo corporativo.
-   Reutilizar siempre la plantilla oficial.

------------------------------------------------------------------------

# Errores comunes

-   Crear AgGrid sin configurar GridOptionsBuilder.
-   Calcular datos dentro de la tabla.
-   Mostrar columnas técnicas.
-   No utilizar paginación.
-   Mezclar lógica de negocio con presentación.

------------------------------------------------------------------------

# Checklist

-   [ ] Existe `components/tablas.py`.
-   [ ] Se utiliza la plantilla oficial.
-   [ ] GridOptionsBuilder está configurado.
-   [ ] Filtros activos.
-   [ ] Ordenamiento activo.
-   [ ] Paginación activa.
-   [ ] Responsive.
-   [ ] Compatible con el diseño corporativo.

------------------------------------------------------------------------

# Conclusión

AgGrid constituye la implementación oficial de tablas del Framework
ELITE.

A partir de esta plantilla podrás construir tablas reutilizables para
cualquier Dashboard, manteniendo una arquitectura limpia, consistente y
fácil de mantener.
