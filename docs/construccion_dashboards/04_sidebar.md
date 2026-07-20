# 🧭 Capítulo 04 - Construcción del Sidebar

# Introducción

Después de construir el archivo **app.py**, el siguiente componente del Framework es el **Sidebar**.

Dentro del Framework ELITE el Sidebar no es un menú principal. Su función consiste en ofrecer información de contexto al usuario y mantener una identidad visual uniforme en todos los Dashboards.

Este componente será reutilizado en todos los proyectos desarrollados con este Framework.

---

# Objetivo

Construir un Sidebar profesional, limpio y reutilizable que pueda incorporarse a cualquier Dashboard sin depender del origen de los datos ni de un proyecto específico.

---

# Filosofía del Framework

> **El Sidebar informa.**

> **El Dashboard trabaja.**

El Sidebar nunca será responsable de realizar cálculos, leer archivos, consultar bases de datos o controlar la navegación principal.

---

# Responsabilidades

El Sidebar debe:

- Mostrar el logo.
- Mostrar el nombre del Dashboard.
- Mostrar una breve descripción.
- Mostrar el estado del sistema.
- Mostrar información de contexto.
- Mostrar la versión.
- Ofrecer acciones secundarias (como actualizar).

---

# Qué NO debe contener

Nunca colocar en el Sidebar:

- KPIs.
- Gráficos.
- Tablas.
- AgGrid.
- Lógica de negocio.
- Lectura de Excel.
- Consultas SQL.
- Navegación principal.

---

# Arquitectura del Sidebar

```text
Logo

↓

Nombre del Dashboard

↓

Descripción

↓

Estado

↓

Información

↓

Acciones

↓

Versión
```

---

# Plantilla Oficial del Framework

```python
from pathlib import Path

import streamlit as st

# ==========================================================
# PERSONALIZACIÓN
# ==========================================================

NOMBRE_DASHBOARD = "Dashboard"

SUBTITULO = "Descripción del Dashboard"

VERSION = "1.0"

ESTADO = "🟢 Operativo"

LOGO = (
    Path(__file__).resolve().parent.parent
    / "assets"
    / "logo_elite.png"
)

# ==========================================================
# SIDEBAR
# ==========================================================

def mostrar_sidebar():

    with st.sidebar:

        if LOGO.exists():
            st.image(str(LOGO), use_container_width=True)

        st.title(NOMBRE_DASHBOARD)

        st.caption(SUBTITULO)

        st.divider()

        st.info(ESTADO)

        if st.button(
            "🔄 Actualizar",
            use_container_width=True
        ):
            st.rerun()

        st.divider()

        st.caption(f"Versión {VERSION}")
```

---

# ¿Qué debo personalizar?

| Elemento | ¿Debe modificarse? |
|-----------|:------------------:|
| Logo | ✅ |
| Nombre del Dashboard | ✅ |
| Descripción | ✅ |
| Estado | ✅ |
| Versión | ✅ |

La estructura del componente no debe modificarse.

---

# Integración con app.py

Una vez creado el componente, basta con importarlo y llamarlo desde `app.py`.

```python
from components.sidebar import mostrar_sidebar

mostrar_sidebar()
```

---

# Buenas prácticas

- Mantener el Sidebar pequeño.
- Mostrar únicamente información relevante.
- Utilizar separadores.
- Mantener una apariencia corporativa.
- Reutilizar el mismo componente en todos los proyectos.

---

# Errores comunes

- Convertir el Sidebar en un menú gigante.
- Colocar lógica de negocio.
- Leer archivos desde el Sidebar.
- Agregar demasiados botones.
- Duplicar información mostrada en el Banner.

---

# Checklist

Antes de continuar verifica que:

- [ ] El logo carga correctamente.
- [ ] El título se visualiza.
- [ ] La descripción es correcta.
- [ ] El estado se muestra.
- [ ] El botón Actualizar funciona.
- [ ] La versión aparece correctamente.
- [ ] El Sidebar no contiene lógica de negocio.

---

# Conclusión

El Sidebar constituye el panel de contexto del Dashboard.

Su misión es ofrecer información útil al usuario manteniendo una interfaz limpia y homogénea. A partir de este capítulo todos los Dashboards desarrollados con el Framework reutilizarán este mismo componente, personalizando únicamente su contenido y conservando siempre la arquitectura oficial.
