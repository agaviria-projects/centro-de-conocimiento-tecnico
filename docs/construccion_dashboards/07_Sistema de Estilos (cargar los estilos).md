# 🎨 Capítulo 07 - Construcción de styles.py

## Introducción

Después de construir la estructura principal del Dashboard mediante **app.py**, **sidebar.py**, **banner.py** y **navegacion.py**, el siguiente paso consiste en definir la identidad visual de la aplicación.

Dentro del Framework Dashboards Streamlit toda la apariencia del Dashboard se centraliza en un único punto denominado **Sistema de Estilos**.

Este sistema permite que todos los componentes compartan la misma apariencia visual, facilitando el mantenimiento y garantizando una experiencia uniforme para el usuario.

Por esta razón, ningún componente define sus propios estilos.

Todos los estilos son administrados desde un único archivo.

---

# Objetivo

Construir un sistema de estilos reutilizable que permita aplicar una identidad visual uniforme a cualquier Dashboard desarrollado con este Framework.

Al finalizar este capítulo tendrás una plantilla oficial que podrá reutilizarse en todos tus proyectos sin necesidad de volver a definir estilos para cada componente.

---

# Filosofía del Framework

Existe una regla muy importante dentro de este Framework.

> **Los componentes construyen la estructura.**

> **styles.css construye la apariencia.**

Esto significa que los archivos:

- app.py
- sidebar.py
- banner.py
- navegacion.py
- kpis.py
- tablas.py

únicamente generan la estructura del Dashboard.

La apariencia visual será responsabilidad exclusiva del archivo **styles.css**.

---

# ¿Qué es styles.css?

El archivo **styles.css** constituye el Sistema de Diseño del Framework.

No contiene lógica de negocio.

No procesa información.

No calcula indicadores.

Su única responsabilidad consiste en controlar la apariencia visual de toda la aplicación.

Desde este archivo se definen aspectos como:

- Colores corporativos.
- Tipografía.
- Espaciados.
- Bordes.
- Sombras.
- Responsive.
- Banner.
- Sidebar.
- Navegación.
- Botones.
- KPIs.
- Tablas.
- AgGrid.

---

# Arquitectura del Sistema de Estilos

```text
app.py

↓

cargar_estilos()

↓

styles.css

↓

Banner

↓

Sidebar

↓

Navegación

↓

KPIs

↓

Tablas

↓

Gráficos

↓

Responsive
```

Todos los componentes utilizan exactamente el mismo archivo de estilos.

---

# ¿Por qué centralizar los estilos?

Durante el desarrollo de diferentes Dashboards empresariales se identificó que definir estilos directamente dentro de cada componente ocasionaba varios inconvenientes.

Entre ellos:

❌ Código duplicado.

❌ Difícil mantenimiento.

❌ Apariencia inconsistente.

❌ Cambios repetitivos.

❌ Mayor tiempo de desarrollo.

Por esta razón el Framework adopta una única fuente de estilos para toda la aplicación.

---

# Resultado esperado

Al finalizar este capítulo el Dashboard deberá mostrar una apariencia uniforme y profesional.

Todos los componentes deberán compartir:

- Colores corporativos.
- Tipografía.
- Espaciados.
- Bordes.
- Sombras.
- Diseño responsive.

---

# ⭐ Plantilla Oficial del Framework

Una vez comprendida la filosofía del Sistema de Estilos es momento de incorporar el archivo oficial utilizado por el Framework.

──────────────────────────────────────────────

📌 ACCIÓN

Crear el archivo:

**styles.py**

Copiar la siguiente plantilla.

```python
import streamlit as st
from pathlib import Path


# ==========================================================
# CARGAR STYLES.CSS
# ==========================================================

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

──────────────────────────────────────────────

---

# 📌 Antes de copiar esta plantilla

Esta plantilla corresponde al cargador oficial del Sistema de Estilos del Framework.

Su única responsabilidad consiste en cargar el archivo **styles.css** dentro de Streamlit.

El archivo **styles.py** no contiene estilos.

Únicamente se encarga de incorporarlos al Dashboard.

---

# ¿Qué debo personalizar?

Normalmente no será necesario modificar este archivo.

Únicamente deberá verificarse la ubicación del archivo:

```text
assets/
    styles.css
```

Si el proyecto mantiene la estructura oficial del Framework, no será necesario realizar ningún cambio.

---

# ¿Qué NO debo modificar?

No modificar la función:

```python
cargar_estilos()
```

No modificar:

```python
unsafe_allow_html=True
```

No modificar la forma en que se carga el archivo CSS.

Toda personalización deberá realizarse exclusivamente dentro de **styles.css**.

---

# Componentes controlados por styles.css

El Sistema de Estilos controla la apariencia de los siguientes componentes.

| Componente | Controlado por styles.css |
|------------|--------------------------|
| Banner | ✅ |
| Sidebar | ✅ |
| Navegación | ✅ |
| Botones | ✅ |
| KPIs | ✅ |
| Tablas | ✅ |
| AgGrid | ✅ |
| Responsive | ✅ |

---

# Buenas prácticas

✔ Mantener todos los estilos dentro de **styles.css**.

✔ Utilizar una única función para cargar los estilos.

✔ Reutilizar el mismo archivo en todos los Dashboards.

✔ Mantener una identidad visual uniforme.

✔ Evitar estilos embebidos dentro de los componentes.

---

# Errores comunes

❌ Definir estilos CSS dentro de app.py.

❌ Copiar bloques `<style>` en diferentes archivos.

❌ Duplicar reglas CSS.

❌ Modificar estilos directamente en Banner o Sidebar.

❌ Cargar varios archivos CSS para un mismo Dashboard.

---

# Lecciones aprendidas

Después de desarrollar diferentes Dashboards empresariales se comprobó que centralizar todos los estilos en un único archivo facilita considerablemente el mantenimiento del proyecto.

Un cambio realizado en **styles.css** se refleja automáticamente en todos los componentes del Dashboard.

Esta decisión se convirtió en uno de los principios fundamentales del Framework Dashboards Streamlit.

---

# Checklist

Antes de continuar verifica que:

☐ styles.py carga correctamente.

☐ El archivo styles.css existe dentro de assets.

☐ Banner utiliza los estilos correctamente.

☐ Sidebar utiliza los estilos correctamente.

☐ La navegación mantiene la apariencia esperada.

☐ No existen bloques CSS duplicados.

☐ Todos los componentes comparten la misma identidad visual.

---

# Próximo capítulo

En el siguiente capítulo construiremos el Diseño Visual del Dashboard.

Aprenderemos cómo organizar visualmente los componentes para conseguir una interfaz limpia, corporativa y fácil de utilizar.