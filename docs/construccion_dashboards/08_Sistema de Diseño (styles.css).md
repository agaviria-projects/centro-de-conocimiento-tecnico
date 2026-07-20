# 🎨 Capítulo 08 - Sistema de Diseño (styles.css)

# Introducción

Después de construir la arquitectura del Dashboard y el Sistema de
Estilos, el siguiente paso consiste en definir la identidad visual
oficial del Framework.

El archivo **styles.css** constituye el Sistema de Diseño del Framework
Dashboards Streamlit.

No es un archivo de ejemplo; es la plantilla oficial que servirá como
base para cualquier Dashboard desarrollado con este Framework.

------------------------------------------------------------------------

# Objetivo

Construir una identidad visual reutilizable, consistente y fácil de
mantener.

Todos los Dashboards compartirán la misma base visual, modificando
únicamente los bloques que requiera cada proyecto.

------------------------------------------------------------------------

# Filosofía del Sistema de Diseño

> **Los componentes construyen la estructura.**

> **styles.py carga el Sistema de Estilos.**

> **styles.css define la identidad visual.**

Esto permite mantener una apariencia uniforme en todos los proyectos.

------------------------------------------------------------------------

# Responsabilidad de styles.css

El archivo controla la apariencia de:

-   Banner
-   Sidebar
-   Navigation
-   Subnavigation
-   Botones
-   Inputs
-   SelectBox
-   KPIs
-   Tablas
-   AgGrid
-   Responsive

No contiene lógica de negocio ni procesamiento de datos.

------------------------------------------------------------------------

# Arquitectura

``` text
app.py
    │
    ▼
styles.py
    │
    ▼
assets/styles.css
    │
    ├── Banner
    ├── Sidebar
    ├── Navigation
    ├── Subnavigation
    ├── Botones
    ├── KPIs
    ├── Tablas
    ├── AgGrid
    └── Responsive
```

------------------------------------------------------------------------

# ⭐ Plantilla Oficial del Framework

Crear el archivo:

``` text
assets/
    styles.css
```

Copiar exactamente el contenido oficial del archivo CSS del Framework.

Esta plantilla fue refinada durante el desarrollo de Dashboards
empresariales y constituye la base visual oficial.

------------------------------------------------------------------------

# Antes de utilizar esta plantilla

El archivo **styles.css** forma parte del Framework.

No se recomienda crear un CSS nuevo para cada Dashboard.

El procedimiento recomendado consiste en reutilizar esta plantilla y
personalizar únicamente los bloques que requiera el nuevo proyecto.

------------------------------------------------------------------------

# Organización del archivo

El archivo se encuentra dividido en bloques independientes:

-   Fuente
-   Variables
-   Streamlit
-   Aplicación
-   Sidebar
-   Banner
-   Navigation
-   Subnavigation
-   Botones
-   Inputs
-   SelectBox
-   KPIs
-   Tabs
-   AgGrid
-   Responsive

Cada bloque posee una única responsabilidad.

------------------------------------------------------------------------

# ¿Qué debo personalizar?

Normalmente solo será necesario modificar:

-   Colores corporativos.
-   Logo.
-   Banner.
-   Variables CSS.
-   Componentes específicos del proyecto.

La estructura general deberá mantenerse.

------------------------------------------------------------------------

# ¿Qué NO debo modificar?

-   La organización del archivo.
-   La filosofía de bloques.
-   La separación de responsabilidades entre componentes y estilos.

------------------------------------------------------------------------

# Buenas prácticas

-   Mantener un único archivo **styles.css**.
-   Reutilizar la plantilla oficial.
-   Evitar estilos embebidos en componentes.
-   Centralizar todos los cambios visuales.

------------------------------------------------------------------------

# Errores comunes

-   Crear múltiples archivos CSS.
-   Duplicar reglas.
-   Escribir CSS dentro de `app.py`.
-   Modificar directamente la apariencia desde los componentes.

------------------------------------------------------------------------

# Regla del Framework

El archivo **styles.css** constituye la implementación oficial del
Sistema de Diseño.

Todo Dashboard nuevo deberá partir de esta plantilla y adaptar
únicamente los bloques necesarios, preservando la arquitectura visual
del Framework.

------------------------------------------------------------------------

# Checklist

-   [ ] Existe `assets/styles.css`.
-   [ ] `styles.py` carga correctamente el archivo.
-   [ ] Banner utiliza los estilos.
-   [ ] Sidebar utiliza los estilos.
-   [ ] Navigation utiliza los estilos.
-   [ ] Subnavigation utiliza los estilos.
-   [ ] No existen reglas CSS duplicadas.
-   [ ] El Dashboard mantiene una identidad visual uniforme.

------------------------------------------------------------------------

# Próximo capítulo

A partir del siguiente capítulo comenzará la construcción de los
componentes funcionales del Dashboard (filtros, KPIs, gráficos y
tablas), reutilizando el Sistema de Diseño definido en este capítulo.
