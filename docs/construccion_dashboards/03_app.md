# ⚙️ Capítulo 03 - Construcción del app.py

# Introducción

Después de crear la arquitectura del proyecto y organizar sus carpetas, el siguiente paso consiste en construir el archivo principal del Dashboard: **app.py**.

Este archivo representa el punto de entrada de toda la aplicación.

En el Framework ELITE, **app.py no contiene la lógica del negocio**. Su única responsabilidad es coordinar el funcionamiento general del Dashboard.

---

# Objetivo

Construir un **app.py** limpio, escalable y reutilizable que sirva como base para cualquier Dashboard desarrollado con este Framework.

La filosofía es sencilla:

> **app.py coordina. Los componentes trabajan.**

---

# Responsabilidad de app.py

El archivo principal únicamente debe:

- Configurar Streamlit.
- Inicializar el Dashboard.
- Cargar estilos.
- Construir el Banner.
- Construir el Sidebar.
- Controlar la navegación.
- Llamar los componentes.

Nunca debe realizar cálculos de negocio.

---

# Flujo Oficial del Framework

```text
Importaciones

↓

Configuración Streamlit

↓

Carga de estilos

↓

Banner

↓

Carga de datos

↓

Sidebar

↓

Navegación

↓

Componentes

↓

Footer (Opcional)
```

Este flujo siempre deberá mantenerse.

---

# Paso 1 - Instalar Streamlit

Antes de construir el Dashboard se debe instalar Streamlit.

```bash
pip install streamlit
```

O utilizando el archivo de dependencias:

```bash
pip install -r requirements.txt
```

---

# Paso 2 - Crear el archivo app.py

Inicialmente el archivo será muy pequeño.

No intentaremos construir todo el Dashboard desde el primer día.

El Framework irá agregando componentes capítulo por capítulo.

---

# Plantilla Oficial Inicial

```python
import streamlit as st

# ==========================================================
# CONFIGURACIÓN
# ==========================================================

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

```

---

# ¿Por qué esta plantilla es tan pequeña?

Porque todavía no existen:

- banner.py
- sidebar.py
- filtros.py
- kpis.py
- graficos.py
- tablas.py

Cada uno será desarrollado en su capítulo correspondiente.

El Framework crecerá de forma progresiva.

---

# Evolución del app.py

## Capítulo 03

```text
Configuración Streamlit
```

## Capítulo 04

```text
+ Banner
```

## Capítulo 05

```text
+ Sidebar
```

## Capítulo 06

```text
+ Navegación
```

## Capítulo 07

```text
+ Estilos CSS
```

## Capítulos siguientes

```text
+ Datos
+ KPIs
+ Filtros
+ Tablas
+ Gráficos
```

De esta manera el Dashboard irá creciendo junto con el Framework.

---

# Qué NO debe contener

- Lectura directa de Excel.
- Consultas SQL.
- KPIs.
- Gráficos.
- CSS embebido.
- Funciones de negocio.

---

# Buenas prácticas

- Mantener `app.py` pequeño.
- Una única responsabilidad.
- Cargar datos una sola vez.
- Importar únicamente lo necesario.
- Delegar el trabajo a los componentes.

---

# Errores comunes

- Copiar un `app.py` de otro proyecto.
- Mezclar lógica de negocio con interfaz.
- Construir todo el Dashboard dentro de un solo archivo.
- Importar componentes que aún no existen.

---

# Checklist

Antes de continuar verifica que:

- [ ] Streamlit está instalado.
- [ ] El entorno virtual está activo.
- [ ] `app.py` ejecuta sin errores.
- [ ] Se muestra el título del Dashboard.
- [ ] La configuración de Streamlit funciona correctamente.

---

# Conclusión

Este capítulo construye únicamente la base del Dashboard.

A partir del siguiente capítulo comenzaremos a incorporar los componentes oficiales del Framework, manteniendo siempre la misma arquitectura y haciendo crecer el proyecto de forma ordenada.
