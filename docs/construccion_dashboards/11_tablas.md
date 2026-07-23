# 11_tablas.md

# Tablas Profesionales

------------------------------------------------------------------------

# Objetivo

Las tablas representan la evidencia del Dashboard. Mientras los KPIs
resumen la información y los gráficos muestran tendencias, las tablas
permiten validar cada registro que compone dichos indicadores.

Dentro del Framework ELITE, **todas las tablas deben consumir el mismo
`df_filtrado`** generado por el módulo de filtros. Esto garantiza
consistencia entre KPIs, gráficos y detalle.

Este capítulo explica **cómo diseñar tablas profesionales**. La
implementación técnica de **AgGrid** se desarrollará en el capítulo
**12_aggrid.md**.

------------------------------------------------------------------------

# Arquitectura del Framework

``` text
Excel / Base de Datos
        │
        ▼
DataFrame Original
        │
        ▼
components/filtros.py
        │
        ▼
df_filtrado
        │
        ├── analytics/
        ├── KPIs
        ├── Gráficos
        └── Tabla Profesional
```

## Regla de Oro

> KPIs, gráficos y tablas siempre deben consumir el mismo `df_filtrado`.

------------------------------------------------------------------------

# El papel de la Tabla dentro del Dashboard

La tabla no es un elemento aislado.

Su función es permitir que el usuario pueda verificar el detalle de la
información mostrada por los indicadores.

Ejemplo:

``` text
Botón: A Tiempo

↓

df_filtrado

↓

KPIs

↓

Gráficos

↓

Tabla (Pedidos A Tiempo)
```

Al cambiar a **Vencidos**, la misma tabla muestra únicamente los pedidos
vencidos.

------------------------------------------------------------------------

# Anatomía de una Tabla Profesional

``` text
┌──────────────────────────────────────────────┐
 Encabezados
───────────────────────────────────────────────
 Filtros por columna
───────────────────────────────────────────────
 Registros
───────────────────────────────────────────────
 Paginación
└──────────────────────────────────────────────┘
```

Debe incluir:

-   Encabezados claros.
-   Ordenamiento.
-   Filtros.
-   Scroll.
-   Responsive.
-   Paginación.
-   Alto rendimiento.

------------------------------------------------------------------------

# Patrón 01 -- Tabla Dinámica

Una única tabla cambia según el filtro seleccionado.

``` text
Estados

├── A Tiempo
├── Alerta
├── Alerta 0 Días
└── Vencidos

↓

df_filtrado

↓

Tabla
```

No se crean cuatro tablas diferentes.

------------------------------------------------------------------------

# Patrón 02 -- Tabla Corporativa

Características recomendadas:

-   Encabezado destacado.
-   Hover.
-   Columnas redimensionables.
-   Filtros.
-   Ordenamiento.
-   Paginación.
-   Responsive.

Será la plantilla oficial del Framework.

------------------------------------------------------------------------

# Patrón 03 -- KPIs + Tabla

``` text
KPIs

↓

Tabla
```

Primero el resumen.

Después el detalle.

------------------------------------------------------------------------

# Integración con el Framework

## app.py

``` python
df = cargar_datos()

df_filtrado = mostrar_filtros(df)

kpis = calcular_kpis(df_filtrado)

mostrar_kpis(kpis)

mostrar_graficos(df_filtrado)

mostrar_tabla(df_filtrado)
```

## Responsabilidad de `components/tablas.py`

Debe únicamente:

-   Mostrar la tabla.
-   Configurar columnas.
-   Aplicar formato visual.
-   Mostrar paginación.

No debe:

-   Leer archivos.
-   Calcular KPIs.
-   Contener reglas de negocio.

------------------------------------------------------------------------

# Buenas prácticas

-   Utilizar un único `df_filtrado`.
-   Mostrar únicamente columnas útiles.
-   Formatear fechas, monedas y porcentajes.
-   Alinear texto a la izquierda.
-   Alinear números a la derecha.
-   Mantener un diseño consistente.

------------------------------------------------------------------------

# Errores comunes

-   Crear una tabla diferente para cada estado.
-   Calcular información dentro de la tabla.
-   Mostrar columnas técnicas al usuario.
-   No sincronizar la tabla con los filtros.

------------------------------------------------------------------------

# Plantilla Oficial

  Campo               Descripción
  ------------------- ---------------------------
  Nombre              Nombre de la tabla
  Objetivo            ¿Qué información muestra?
  DataFrame           Fuente (`df_filtrado`)
  Columnas visibles   Información mostrada
  Columnas ocultas    Campos internos
  Orden inicial       Columna principal
  Paginación          20, 30 o 50 registros
  Exportación         Sí / No

------------------------------------------------------------------------

# Checklist

-   [ ] Existe `components/tablas.py`.
-   [ ] La tabla recibe `df_filtrado`.
-   [ ] Responde a los filtros.
-   [ ] Mantiene formato corporativo.
-   [ ] Permite ordenamiento.
-   [ ] Permite filtros.
-   [ ] Tiene paginación.
-   [ ] Está lista para integrarse con AgGrid.

------------------------------------------------------------------------

# Conclusión

Las tablas representan la evidencia del Dashboard.

Todo KPI y todo gráfico debe poder verificarse mediante la tabla
correspondiente.

En el siguiente capítulo (**12_aggrid.md**) se implementará esta
arquitectura utilizando AgGrid, configurando temas, estilos,
GridOptionsBuilder, JsCode y todas las opciones necesarias para
construir tablas corporativas reutilizables.
