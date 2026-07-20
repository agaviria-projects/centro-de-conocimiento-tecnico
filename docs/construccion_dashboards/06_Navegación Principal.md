# 🧭 Capítulo 06 - Navegación Principal

# Introducción

Después de construir el **Banner** y el **Sidebar**, el siguiente componente del Framework es la **Navegación Principal**.

La navegación tiene una única responsabilidad: permitir que el usuario seleccione el módulo que desea visualizar.

Dentro del Framework ELITE la navegación es un componente independiente y reutilizable.

---

# Objetivo

Construir un componente de navegación desacoplado de la lógica del negocio y reutilizable en cualquier Dashboard.

---

# Filosofía del Framework

> **El Banner identifica.**

> **El Sidebar informa.**

> **La Navegación dirige.**

> **El Contenido genera valor.**

La navegación nunca realiza cálculos ni procesa información.

---

# Responsabilidades

La navegación únicamente debe:

- Mostrar los módulos disponibles.
- Permitir seleccionar un módulo.
- Devolver la opción seleccionada.

Nada más.

---

# Qué NO debe contener

Nunca colocar en este componente:

- KPIs.
- Gráficos.
- Tablas.
- Lectura de Excel.
- SQL.
- Lógica de negocio.
- Cálculos.

---

# Arquitectura

```text
Banner

↓

Sidebar

↓

Navigation

↓

Contenido
```

---

# Archivo del Framework

Crear el archivo:

```text
components/

navigation.py
```

---

# Plantilla Oficial

```python
import streamlit as st


def mostrar_navigation(
    opciones,
    titulo=None,
):

    if titulo:
        st.subheader(titulo)

    return st.radio(
        "",
        opciones,
        horizontal=True,
        label_visibility="collapsed",
        key="navigation",
    )
```

---

# Integración con app.py

```python
from components.navigation import mostrar_navigation

opcion = mostrar_navigation(

    titulo="Módulos",

    opciones=[
        "📂 Datos",
        "📊 KPIs",
        "📈 Indicadores",
        "📋 Reportes",
    ],
)
```

La navegación solo devuelve la opción seleccionada.

La decisión sobre qué componente mostrar pertenece exclusivamente a `app.py`.

---

# Personalización

Puede modificarse:

- Título.
- Lista de opciones.
- Iconografía.

La estructura del componente debe mantenerse.

---

# Buenas prácticas

- Mantener pocas opciones por nivel.
- Utilizar iconografía consistente.
- Mantener la navegación visible.
- Reutilizar el mismo componente en todos los proyectos.
- Enviar las opciones mediante parámetros.

---

# Errores comunes

- Escribir opciones fijas dentro del componente.
- Mezclar navegación con lógica de negocio.
- Agregar consultas o cálculos.
- Duplicar menús en distintos lugares.

---

# Checklist

- [ ] Existe `components/navigation.py`.
- [ ] La navegación devuelve la opción seleccionada.
- [ ] No contiene lógica de negocio.
- [ ] Se integra correctamente con `app.py`.
- [ ] Las opciones se reciben mediante parámetros.

---

# Conclusión

La navegación constituye el punto de unión entre la estructura del Dashboard y sus módulos.

A partir de este capítulo todos los Dashboards desarrollados con el Framework utilizarán el mismo componente de navegación, personalizando únicamente las opciones mostradas y manteniendo intacta su arquitectura.
