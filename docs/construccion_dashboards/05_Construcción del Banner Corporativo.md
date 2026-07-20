# 🟩 Capítulo 05 - Construcción del Banner Corporativo

# Introducción

Después de construir el **Sidebar**, el siguiente componente del Framework es el **Banner Corporativo**.

El Banner constituye la identidad visual del Dashboard y será el primer elemento que observará el usuario al ingresar a la aplicación.

Dentro del Framework ELITE el Banner es un componente reutilizable e independiente de cualquier proyecto específico.

---

# Objetivo

Construir un Banner corporativo reutilizable que pueda utilizarse en cualquier Dashboard desarrollado con este Framework.

---

# Filosofía del Framework

> **El Banner identifica.**

> **El Dashboard analiza.**

El Banner no calcula indicadores ni contiene lógica de negocio.

Su única responsabilidad es presentar la identidad del Dashboard.

---

# Responsabilidades

El Banner debe:

- Mostrar el nombre del Dashboard.
- Mostrar un subtítulo.
- Mostrar el estado del sistema.
- Mantener una apariencia corporativa.

---

# Qué NO debe contener

Nunca colocar dentro del Banner:

- KPIs.
- Gráficos.
- Tablas.
- AgGrid.
- Filtros.
- Botones de negocio.
- Lectura de datos.

---

# Arquitectura del Banner

```text
Icono

↓

Título

↓

Subtítulo

↓

Estado
```

---

# Plantilla Oficial del Framework

```python
import streamlit as st

def mostrar_banner(
    titulo: str,
    subtitulo: str,
    estado: str,
    icono: str = "📊",
):

    st.markdown(
        f'''
<div class="elite-banner">

<div>

<div class="elite-banner-title">
{icono} {titulo}
</div>

<div class="elite-banner-subtitle">
{subtitulo}
</div>

</div>

<div class="elite-banner-status">
{estado}
</div>

</div>
''',
        unsafe_allow_html=True,
    )
```

---

# ¿Por qué utilizar parámetros?

El Banner no debe contener información fija.

Cada Dashboard personaliza únicamente los datos enviados desde **app.py**.

Ejemplo:

```python
from components.banner import mostrar_banner

mostrar_banner(
    titulo="Dashboard FENIX ANS",
    subtitulo="Control de Acuerdos de Nivel de Servicio",
    estado="🟢 Operativo",
    icono="📈",
)
```

Con esta arquitectura el mismo componente podrá reutilizarse en cualquier Dashboard.

---

# Integración con styles.css

La apariencia visual del Banner depende del archivo:

```text
assets/

styles.css
```

El componente únicamente define la estructura HTML.

Los colores, tipografía, bordes, sombras y espaciados pertenecen al CSS del Framework.

---

# Buenas prácticas

- Mantener títulos cortos.
- Utilizar subtítulos descriptivos.
- Mostrar siempre el estado del sistema.
- Mantener la estructura HTML.
- Reutilizar el mismo componente.

---

# Errores comunes

- Copiar el Banner de otro proyecto.
- Escribir información fija dentro del componente.
- Agregar lógica de negocio.
- Modificar innecesariamente las clases CSS.
- Colocar KPIs o filtros en el Banner.

---

# Checklist

Antes de continuar verifica que:

- [ ] El Banner se muestra correctamente.
- [ ] El título cambia mediante parámetros.
- [ ] El subtítulo cambia mediante parámetros.
- [ ] El estado cambia mediante parámetros.
- [ ] El CSS del Framework se aplica correctamente.
- [ ] El componente no contiene lógica de negocio.

---

# Conclusión

El Banner constituye la identidad visual del Dashboard.

A partir de este capítulo todos los Dashboards desarrollados con el Framework reutilizarán el mismo componente, personalizando únicamente el icono, el título, el subtítulo y el estado desde **app.py**, manteniendo intacta la arquitectura oficial.
