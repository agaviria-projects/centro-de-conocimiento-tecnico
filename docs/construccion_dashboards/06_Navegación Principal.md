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


# ==========================================================
# ESTILOS DE LA SUBNAVEGACIÓN
# ==========================================================

def cargar_estilos_subnavigation():

    st.markdown(
        """
        <style>

        /* Separación entre botones */
        .st-key-subnavigation [data-baseweb="button-group"] {
            gap: 12px;
        }

        /* Diseño general */
        .st-key-subnavigation button {
            min-height: 44px;
            padding: 9px 22px;
            border-radius: 10px !important;
            border-width: 2px !important;

            font-size: 14px !important;
            font-weight: 700 !important;

            transition:
                transform 0.20s ease,
                box-shadow 0.20s ease,
                background-color 0.20s ease;

            box-shadow: 0 4px 9px rgba(15, 23, 42, 0.15);
        }

        .st-key-subnavigation button p {
            font-size: 14px !important;
            font-weight: 700 !important;
            color: inherit !important;
        }


        /* ==================================================
           A TIEMPO — VERDE
        ================================================== */

        .st-key-subnavigation button:nth-child(1) {
            background-color: #22C55E !important;
            border-color: #16A34A !important;
            color: #FFFFFF !important;
        }

        .st-key-subnavigation button:nth-child(1):hover {
            background-color: #16A34A !important;
            border-color: #15803D !important;
            transform: translateY(-2px);
            box-shadow: 0 7px 15px rgba(22, 163, 74, 0.35);
        }

        .st-key-subnavigation
        button:nth-child(1)[data-testid$="Active"] {
            background-color: #15803D !important;
            border-color: #14532D !important;
            color: #FFFFFF !important;
            transform: translateY(-3px) scale(1.04);
            box-shadow:
                0 0 0 3px rgba(34, 197, 94, 0.25),
                0 8px 18px rgba(21, 128, 61, 0.45);
        }


        /* ==================================================
           ALERTA — AMARILLO
        ================================================== */

        .st-key-subnavigation button:nth-child(2) {
            background-color: #FACC15 !important;
            border-color: #EAB308 !important;
            color: #422006 !important;
        }

        .st-key-subnavigation button:nth-child(2):hover {
            background-color: #EAB308 !important;
            border-color: #CA8A04 !important;
            transform: translateY(-2px);
            box-shadow: 0 7px 15px rgba(234, 179, 8, 0.40);
        }

        .st-key-subnavigation
        button:nth-child(2)[data-testid$="Active"] {
            background-color: #CA8A04 !important;
            border-color: #854D0E !important;
            color: #FFFFFF !important;
            transform: translateY(-3px) scale(1.04);
            box-shadow:
                0 0 0 3px rgba(250, 204, 21, 0.30),
                0 8px 18px rgba(202, 138, 4, 0.45);
        }


        /* ==================================================
           ALERTA CERO DÍAS — NARANJA
        ================================================== */

        .st-key-subnavigation button:nth-child(3) {
            background-color: #F97316 !important;
            border-color: #EA580C !important;
            color: #FFFFFF !important;
        }

        .st-key-subnavigation button:nth-child(3):hover {
            background-color: #EA580C !important;
            border-color: #C2410C !important;
            transform: translateY(-2px);
            box-shadow: 0 7px 15px rgba(234, 88, 12, 0.40);
        }

        .st-key-subnavigation
        button:nth-child(3)[data-testid$="Active"] {
            background-color: #C2410C !important;
            border-color: #9A3412 !important;
            color: #FFFFFF !important;
            transform: translateY(-3px) scale(1.04);
            box-shadow:
                0 0 0 3px rgba(249, 115, 22, 0.25),
                0 8px 18px rgba(194, 65, 12, 0.45);
        }


        /* ==================================================
           VENCIDOS — ROJO
        ================================================== */

        .st-key-subnavigation button:nth-child(4) {
            background-color: #EF4444 !important;
            border-color: #DC2626 !important;
            color: #FFFFFF !important;
        }

        .st-key-subnavigation button:nth-child(4):hover {
            background-color: #DC2626 !important;
            border-color: #B91C1C !important;
            transform: translateY(-2px);
            box-shadow: 0 7px 15px rgba(220, 38, 38, 0.40);
        }

        .st-key-subnavigation
        button:nth-child(4)[data-testid$="Active"] {
            background-color: #B91C1C !important;
            border-color: #7F1D1D !important;
            color: #FFFFFF !important;
            transform: translateY(-3px) scale(1.04);
            box-shadow:
                0 0 0 3px rgba(239, 68, 68, 0.25),
                0 8px 18px rgba(185, 28, 28, 0.45);
        }

        </style>
        """,
        unsafe_allow_html=True,
    )


# ==========================================================
# MOSTRAR SUBNAVEGACIÓN
# ==========================================================

def mostrar_subnavigation(
    opciones,
    titulo=None,
):

    cargar_estilos_subnavigation()

    if titulo:
        st.caption(titulo)

    return st.segmented_control(
        label="Estados del ANS",
        options=opciones,
        selection_mode="single",
        default=opciones[0] if opciones else None,
        key="subnavigation",
        label_visibility="collapsed",
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
