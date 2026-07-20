# 🧭 Capítulo 06 - Navegación Principal

# Introducción

Después de construir el **Banner** y el **Sidebar**, el siguiente componente del Framework es la **Navegación Principal**.

Su responsabilidad consiste en permitir que el usuario acceda a los diferentes módulos del Dashboard sin depender del Sidebar.

Dentro del Framework ELITE la navegación es un componente reutilizable e independiente de la lógica del negocio.

---

# Objetivo

Construir una navegación profesional, desacoplada y reutilizable que pueda utilizarse en cualquier Dashboard desarrollado con este Framework.

---

# Filosofía del Framework

> **El Banner identifica.**

> **El Sidebar informa.**

> **La Navegación dirige.**

> **El Contenido genera valor.**

La navegación nunca calcula indicadores ni procesa información.

---

# Responsabilidades

La Navegación Principal únicamente debe:

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
- Consultas SQL.
- Lectura de archivos.
- Lógica de negocio.
- Cálculos.

---

# Arquitectura

```text
Banner

↓

Sidebar

↓

Navigation Principal

↓

Subnavigation (Opcional)

↓

Contenido
```

---

# Niveles de Navegación

## Nivel 1 - Navegación Principal

Es obligatoria en todos los Dashboards.

Permite acceder a los módulos principales.

Ejemplo:

```text
📂 Datos

📊 KPIs

📈 Indicadores

📋 Reportes
```

Archivo oficial:

```text
components/

navigation.py
```

---

## Nivel 2 - Navegación Secundaria (Opcional)

Algunos módulos requieren dividir su contenido.

Ejemplo:

```text
📂 Datos

↓

Rodamientos

Viáticos

Parqueaderos

Peajes
```

Otro ejemplo:

```text
💰 Finanzas

↓

Ingresos

Costos

Utilidad

Presupuesto
```

Archivo recomendado:

```text
components/

subnavigation.py
```

Este componente solo deberá utilizarse cuando un módulo necesite subdividir su contenido.

---

# Regla del Framework

Todo Dashboard deberá tener una **Navegación Principal**.

La **Navegación Secundaria** será opcional.

---

# Archivo del Framework

Crear:

```text
components/

navigation.py
```

---

# Plantilla Oficial en navigation.py

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

La navegación únicamente devuelve la opción seleccionada.

`app.py` será el responsable de decidir qué componente cargar.

---
### Navegación Secundaria (Opcional)

```python

import streamlit as st

def mostrar_subnavigation(
    opciones,
    titulo=None,
):

    if titulo:
        st.caption(titulo)

    return st.segmented_control(
        "",
        options=opciones,
        selection_mode="single",
        default=opciones[0] if opciones else None,
        key="subnavigation",
    )

```

---

# Integración con app.py

```python

from components.subnavigation import mostrar_subnavigation


if opcion == "📂 Estados del ANS":

    subopcion = mostrar_subnavigation(

        titulo="Origen de información",

        opciones=[

            "A tiempo",

            "Alerta",

            "Alerta Cero Días",

            "Vencidos",

        ],

    )

```

----

## Lo que Sigue debajo

Una vez construida la navegación Principal, el siguiente paso consiste en mostrar el contenido correspondiente a la opción seleccionada.

OJO:  con la indentación debe ser debajo del )
por ejemplo:

```python

    # ==========================================================
    # MOSTRAR SUB-NAVIGATION
    # ==========================================================
    if subopcion == "A tiempo":

        st.write("Aquí irá la información de A tiempo.")

    elif subopcion == "Alerta":

        st.write("Aquí irá la información de Alerta.")

    elif subopcion == "Alerta Cero Días":

        st.write("Aquí irá la información de Alerta Cero Días.")

    elif subopcion == "Vencidos":

        st.write("Aquí irá la información de Vencidos.") 

```
---

## Entocnes:

El lector entiende:

A tiempo

↓

muestra

Tabla Rodamientos
A tiempo

↓

muestra

Tabla Viáticos
Alerta

↓

muestra

Tabla Alerta

---


# Personalización

Puede modificarse:

- El título.
- Las opciones.
- La iconografía.

La estructura del componente debe mantenerse.

---

# Buenas prácticas

- Mantener pocas opciones por nivel.
- Utilizar iconografía consistente.
- Mantener la navegación siempre visible.
- Reutilizar el mismo componente.
- Enviar las opciones mediante parámetros.

---

# Errores comunes

- Escribir opciones fijas dentro del componente.
- Colocar la navegación en el Sidebar.
- Mezclar navegación con lógica de negocio.
- Agregar consultas o cálculos.
- Duplicar menús.

---

# Checklist

- [ ] Existe `components/navigation.py`.
- [ ] La navegación devuelve la opción seleccionada.
- [ ] No contiene lógica de negocio.
- [ ] Se integra correctamente con `app.py`.
- [ ] Las opciones se reciben mediante parámetros.
- [ ] La arquitectura contempla una Subnavigation opcional.

---

# Conclusión

La Navegación Principal constituye el primer nivel de acceso a los módulos del Dashboard.

Cuando un módulo requiera subdividir su contenido, el Framework incorpora una **Navegación Secundaria** como componente opcional, manteniendo una arquitectura escalable, organizada y reutilizable.

A partir de este capítulo todos los Dashboards desarrollados con el Framework reutilizarán esta misma arquitectura de navegación.
