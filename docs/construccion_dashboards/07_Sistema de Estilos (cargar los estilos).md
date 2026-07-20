# 🎨 Capítulo 07 - Sistema de Estilos (Carga de styles.css)

# Introducción

Después de construir la estructura principal del Dashboard mediante
**app.py**, **sidebar.py**, **banner.py**, **navigation.py** y
**subnavigation.py**, el siguiente paso consiste en definir la identidad
visual de la aplicación.

Dentro del Framework Dashboards Streamlit toda la apariencia del
Dashboard se centraliza en un único punto denominado **Sistema de
Estilos**.

Este sistema permite que todos los componentes compartan la misma
apariencia visual, facilitando el mantenimiento y garantizando una
experiencia uniforme para el usuario.

Por esta razón, ningún componente define sus propios estilos.

Todos los estilos son administrados desde un único archivo.

------------------------------------------------------------------------

# Objetivo

Construir un Sistema de Estilos reutilizable que permita aplicar una
identidad visual uniforme a cualquier Dashboard desarrollado con este
Framework.

------------------------------------------------------------------------

# Filosofía del Framework

> **Los componentes construyen la estructura.**

> **styles.py carga el Sistema de Estilos.**

> **styles.css construye la apariencia.**

Los componentes únicamente generan la estructura del Dashboard.

Toda la apariencia visual será responsabilidad exclusiva de
**styles.css**.

------------------------------------------------------------------------

# ¿Qué es styles.py?

El archivo **styles.py** no contiene estilos CSS.

Su única responsabilidad consiste en localizar e incorporar el archivo
**styles.css** dentro de Streamlit.

------------------------------------------------------------------------

# ¿Qué es styles.css?

El archivo **styles.css** constituye el Sistema de Diseño del Framework.

Desde este archivo se controlan:

-   Banner
-   Sidebar
-   Navigation
-   Subnavigation
-   Botones
-   KPIs
-   Tablas
-   AgGrid
-   Responsive

------------------------------------------------------------------------

# Arquitectura del Sistema de Estilos

``` text
app.py
    │
    ▼
styles.py
    │
    ▼
styles.css
    │
    ├── Banner
    ├── Sidebar
    ├── Navigation
    ├── Subnavigation
    ├── Botones
    ├── KPIs
    ├── Tablas
    ├── Gráficos
    └── Responsive
```

------------------------------------------------------------------------

# Flujo de carga

``` text
app.py
    ↓
cargar_estilos()
    ↓
styles.py
    ↓
styles.css
    ↓
Todos los componentes
```

------------------------------------------------------------------------

# Plantilla Oficial

``` python
import streamlit as st
from pathlib import Path

def cargar_estilos():

    css = (
        Path(__file__).parent.parent
        / "assets"
        / "styles.css"
    )

    with open(css, encoding="utf-8") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True,
        )
```

---

## Luego en app.py:

``` python
from components.styles import cargar_estilos

y después de st.set_page_config():

cargar_estilos()

```

---

------------------------------------------------------------------------

# ¿Qué debo personalizar?

Modificar únicamente **assets/styles.css**.

No modificar la función **cargar_estilos()**.

------------------------------------------------------------------------

# Componentes controlados

  Componente      Controlado
  --------------- ------------
  Banner          ✅
  Sidebar         ✅
  Navigation      ✅
  Subnavigation   ✅
  Botones         ✅
  KPIs            ✅
  Tablas          ✅
  AgGrid          ✅
  Responsive      ✅

------------------------------------------------------------------------

# Buenas prácticas

-   Un único archivo CSS.
-   Sin estilos embebidos.
-   Reutilizar el mismo Sistema de Estilos.

------------------------------------------------------------------------

# Checklist

-   [ ] Existe styles.py.
-   [ ] Existe assets/styles.css.
-   [ ] Banner usa los estilos.
-   [ ] Sidebar usa los estilos.
-   [ ] Navigation usa los estilos.
-   [ ] Subnavigation usa los estilos.

------------------------------------------------------------------------

# Próximo capítulo

Construiremos el contenido de **styles.css** para definir la identidad
visual oficial del Framework.
