# ⚙️ Capítulo 03 - Construcción del app.py

## Introducción

Después de diseñar la arquitectura del proyecto y crear la estructura de carpetas, llega el momento de construir el archivo más importante del Dashboard: **app.py**.

Este archivo será el punto de entrada de toda la aplicación y tendrá la responsabilidad de coordinar el funcionamiento general del sistema.

En este Framework todos los Dashboards comenzarán exactamente desde la misma estructura.

No importa si el proyecto corresponde a un Dashboard de logística, costos, inventarios, indicadores, ANS o ventas.

Todos seguirán la misma metodología.

Únicamente cambiarán los componentes propios del negocio.

---

# Objetivo

Construir el archivo principal del Dashboard siguiendo una arquitectura limpia, organizada y reutilizable.

Al finalizar este capítulo tendrás una plantilla profesional que servirá como base para cualquier nuevo proyecto desarrollado con Streamlit.

---

# ¿Qué es app.py?

El archivo **app.py** representa el punto de entrada de la aplicación.

Cuando un usuario ejecuta Streamlit, este será el primer archivo que se cargará.

Su responsabilidad consiste únicamente en coordinar el funcionamiento del Dashboard.

No debe convertirse en un archivo donde se desarrollen cálculos complejos ni donde se concentre toda la lógica del negocio.

Todo cálculo deberá vivir en componentes independientes.

---

# Filosofía del Framework

Existe una regla que seguiremos durante todo este Framework.

> **app.py coordina. Los componentes trabajan.**

Esto significa que el archivo principal únicamente organiza el flujo general de la aplicación.

Cada componente será responsable de realizar una única tarea.

Gracias a esta filosofía el proyecto podrá crecer sin perder organización.

---

# Flujo del app.py

Todos los Dashboards desarrollados con este Framework seguirán exactamente el siguiente flujo.

```text
Importaciones

↓

Configuración de Streamlit

↓

Carga de estilos

↓

Construcción del Banner

↓

Lectura de información

↓

Construcción del Sidebar

↓

Creación de la navegación

↓

Carga de componentes

↓

Footer (Opcional)
```

Este orden nunca deberá modificarse.

---

# Paso 1 - Importaciones

El primer bloque del archivo corresponde a todas las librerías y componentes necesarios para ejecutar el Dashboard.

Las importaciones deben organizarse de la siguiente manera:

• Librerías externas.

• Lectores de datos.

• Componentes visuales.

• Componentes analíticos.

• Próximos módulos (comentados).

Mantener este orden facilita localizar rápidamente cualquier dependencia del proyecto.

---

# Paso 2 - Configuración de Streamlit

Después de importar todos los módulos se configura Streamlit.

En esta etapa se define:

- Nombre del Dashboard.
- Icono.
- Distribución de la pantalla.
- Estado inicial del Sidebar.

Esta configuración siempre deberá realizarse al inicio del archivo.

Nunca debe ubicarse después de construir componentes visuales.

---

# Paso 3 - Cargar los estilos

Una vez configurado Streamlit se cargan los estilos CSS.

Los estilos siempre deberán cargarse antes de construir cualquier componente.

De esta forma todo el Dashboard utilizará la misma identidad visual desde el primer momento.

---

# Paso 4 - Construir el Banner

El Banner representa la cabecera del Dashboard.

Generalmente contiene:

- Nombre del Dashboard.
- Descripción.
- Estado del sistema.
- Información corporativa.

Este será el primer elemento visual que verá el usuario.

---

# Paso 5 - Leer la información

Antes de construir cualquier componente se debe cargar la información.

Una regla importante de este Framework será:

> **Leer la información una única vez.**

Uno de los errores más comunes consiste en volver a leer el mismo archivo Excel desde diferentes componentes.

Esto disminuye considerablemente el rendimiento de la aplicación.

---

# Paso 6 - Construir el Sidebar

Después de cargar la información se construye el Sidebar.

El Sidebar será responsable únicamente de:

- Mostrar el logo.
- Mostrar información del archivo.
- Permitir actualizar datos.
- Configuración inicial.

La navegación principal nunca deberá ubicarse aquí.

Durante el desarrollo de proyectos anteriores se identificó que el botón **<<** de Streamlit oculta completamente el Sidebar.

Si la navegación se encuentra allí, el usuario pierde el acceso al Dashboard.

Por esta razón la navegación principal siempre se ubicará en el área central de la aplicación.

---

# Paso 7 - Construir la navegación

Después del Sidebar se crea el menú principal del Dashboard.

La navegación será la responsable de cambiar entre los diferentes módulos.

Ejemplos:

- Datos.

- Indicadores.

- KPIs.

- Tablas.

- Gráficos.

- Reportes.

Más adelante construiremos diferentes tipos de navegación y aprenderemos cuándo utilizar cada una.

---

# Paso 8 - Mostrar los componentes

Finalmente se muestran los diferentes componentes del Dashboard.

Cada componente vivirá en un archivo independiente.

Esto permitirá que el proyecto sea mucho más fácil de mantener.

---

# ⭐ Plantilla Oficial del Framework

Una vez comprendida la función de cada bloque del archivo **app.py**, es momento de incorporar la plantilla oficial utilizada en todos los Dashboards desarrollados con este Framework.

Esta plantilla representa el resultado de diferentes proyectos empresariales y servirá como punto de partida para futuros desarrollos.

──────────────────────────────────────────────────────────────

📌 **ACCIÓN**

En este punto copie y pegue el archivo oficial **app.py** del proyecto.

Mantenga exactamente la misma estructura.

Únicamente deberán modificarse los componentes específicos del negocio.

```python
import streamlit as st

from data.lector_excel import leer_todas

from components.styles import cargar_estilos
from components.banner import mostrar_banner
from components.sidebar import mostrar_sidebar
from components.filtros import mostrar_filtros
from components.kpis import mostrar_kpis
from components.ranking_placas import mostrar_ranking_placas
from components.indicadores_mensuales import mostrar_indicadores_mensuales
from components.datos import mostrar_datos

# Próximas fases
# from components.comparativo import mostrar_comparativo
# from components.ranking_zonas import mostrar_ranking_zonas
# from components.ranking_conceptos import mostrar_ranking_conceptos
# from components.graficos import mostrar_graficos
# from components.hallazgos import mostrar_hallazgos
# from components.detalle import mostrar_detalle


# ==========================================================
# CONFIGURACIÓN
# ==========================================================

st.set_page_config(
    page_title="Analizador de Costos Operativos Servitravel",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# ESTILOS
# ==========================================================

cargar_estilos()

# ==========================================================
# HEADER
# ==========================================================

mostrar_banner()

# ==========================================================
# CARGAR INFORMACIÓN (UNA SOLA VEZ)
# ==========================================================

hojas = leer_todas()

# ==========================================================
# SIDEBAR
# ==========================================================

resultado = mostrar_sidebar(hojas)

if resultado is None:
    st.stop()

df = resultado["df"]
hoja = resultado["hoja"]


# ==========================================================
# NAVEGACIÓN
# ==========================================================

opcion = st.radio(
    "",
    [
        "📂 Datos",
        "📊 Resumen del período",
        "📈 Indicadores Mensuales",
        "🚗 Vehículos",
        "💰 Gastos Operativos",
        "🗺️ Zonas",
        "📋 Detalle",
    ],
    horizontal=True,
    label_visibility="collapsed"
)
# ==========================================================
# DATOS
# ==========================================================

if opcion == "📂 Datos":

     mostrar_datos(hojas)

# ==========================================================
# RESUMEN EJECUTIVO
# ==========================================================
if opcion == "📊 Resumen del período":

    df_filtrado = mostrar_filtros(
        df,
        key_prefix="resumen"
    )

    if df_filtrado.empty:

        st.warning("No existen registros para los filtros seleccionados.")

    else:

        mostrar_kpis(df_filtrado)

        st.divider()

        mostrar_ranking_placas(df_filtrado)

# ==========================================================
# INDICADORES MENSUALES
# ==========================================================

if opcion == "📈 Indicadores Mensuales":

    df_filtrado = mostrar_filtros(
        df,
        key_prefix="indicadores"
    )

    if df_filtrado.empty:

        st.warning("No existen registros para los filtros seleccionados.")

    else:

        mostrar_indicadores_mensuales(
            df,
            df_filtrado
        )
   

# ==========================================================
# VEHÍCULOS
# ==========================================================

if opcion == "🚗 Vehículos":

    st.info("Módulo en construcción.")

# ==========================================================
# GASTOS OPERATIVOS
# ==========================================================

if opcion == "💰 Gastos Operativos":

    st.info("Módulo en construcción.")

# ==========================================================
# ZONAS
# ==========================================================

if opcion == "🗺️ Zonas":

    st.info("Módulo en construcción.")

# ==========================================================
# DETALLE
# ==========================================================

if opcion == "📋 Detalle":

    st.info("Módulo en construcción.")
```

──────────────────────────────────────────────────────────────

---

# 🔄 ¿Qué debo personalizar al reutilizar esta plantilla?

Uno de los principales objetivos de este Framework es evitar comenzar cada Dashboard desde cero.

Cuando reutilices la plantilla oficial de **app.py**, no será necesario desarrollar nuevamente su arquitectura. Únicamente deberás personalizar aquellos elementos que dependen del proyecto que estás construyendo.

Los cambios normalmente se limitarán a los siguientes componentes.

| Componente | ¿Qué se personaliza? |
|------------|----------------------|
| **page_title** | Nombre del Dashboard que aparecerá en la pestaña del navegador. |
| **page_icon** | Ícono representativo del proyecto. |
| **Banner** | Título, subtítulo, estado del sistema o información corporativa. |
| **Sidebar** | Logo, nombre del Dashboard, archivo fuente, versión y demás información de contexto. |
| **Lector de datos** | Función encargada de leer archivos Excel, CSV, bases de datos u otros orígenes de información. |
| **Navegación** | Opciones del menú principal según los módulos del Dashboard. |
| **Componentes** | KPIs, tablas, gráficos, filtros, mapas, reportes y cualquier componente específico del negocio. |

> 💡 **Regla del Framework**
>
> Al crear un nuevo Dashboard **no construirás un nuevo `app.py`**.
>
> Lo que harás será **personalizar los componentes**, manteniendo siempre la arquitectura oficial del Framework.

---

# 🏛️ ¿Qué hace parte de la arquitectura del Framework?

Aunque el contenido de cada componente cambiará según el proyecto, la estructura general del archivo **app.py** debe mantenerse.

La siguiente secuencia representa la arquitectura oficial del Framework.

```text
Importaciones

↓

Configuración de Streamlit

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

Mantener este orden facilita la lectura del código, mejora el mantenimiento del proyecto y permite reutilizar la misma plantilla en cualquier Dashboard.

---

# 🧩 ¿Qué se personaliza y qué se conserva?

| Elemento | Personalizar | Conservar |
|-----------|:------------:|:---------:|
| page_title | ✅ | ❌ |
| page_icon | ✅ | ❌ |
| styles.css | ✅ Colores y estilos corporativos | ✅ Forma de cargar los estilos |
| banner.py | ✅ Contenido | ✅ Ubicación dentro del flujo del Dashboard |
| sidebar.py | ✅ Información mostrada | ✅ Organización general |
| lector_datos.py | ✅ Según el origen de los datos | ❌ |
| Navegación | ✅ Opciones del menú | ✅ Ubicación dentro del Dashboard |
| Componentes | ✅ | ❌ |
| Arquitectura de app.py | ❌ | ✅ Siempre debe mantenerse |

---

# Buenas prácticas

✔ Mantener **app.py** pequeño y fácil de leer.

✔ Utilizar comentarios para dividir claramente cada sección.

✔ Leer la información una única vez.

✔ Mantener siempre el mismo flujo de ejecución.

✔ Separar la lógica del negocio de la interfaz gráfica.

✔ Importar únicamente los componentes necesarios.

✔ Reutilizar la plantilla oficial del Framework en todos los nuevos proyectos.

✔ Crear un archivo independiente para cada componente visual.

---

# Errores comunes

Durante el desarrollo de diferentes Dashboards empresariales se identificaron los siguientes errores.

❌ Colocar toda la lógica del negocio dentro de **app.py**.

❌ Leer el mismo archivo Excel desde diferentes componentes.

❌ Mezclar estilos CSS con código Python.

❌ Crear componentes demasiado grandes y difíciles de mantener.

❌ Duplicar funciones entre módulos.

❌ Utilizar el Sidebar como menú principal del Dashboard.

❌ Alterar el orden de la arquitectura del Framework.

---

# Lecciones aprendidas

Después de desarrollar diferentes Dashboards empresariales se adoptaron las siguientes reglas.

- **app.py** únicamente coordina la aplicación.

- Cada componente debe tener una única responsabilidad.

- Los estilos siempre deben cargarse antes del Banner.

- La información debe leerse una única vez.

- El Sidebar proporciona información de contexto; la navegación principal pertenece al cuerpo del Dashboard.

- Todos los nuevos proyectos deben comenzar reutilizando la plantilla oficial del Framework.

- **No modificamos la arquitectura; personalizamos los componentes.**

---

# Checklist

Antes de continuar con el siguiente capítulo verifica que:

☐ El Dashboard inicia correctamente.

☐ No existen errores en consola.

☐ La configuración de Streamlit se aplica correctamente.

☐ Los estilos CSS se cargan sin errores.

☐ El Banner aparece correctamente.

☐ El Sidebar muestra la información esperada.

☐ La navegación funciona correctamente.

☐ Los componentes responden sin errores.

☐ La estructura del **app.py** coincide con la arquitectura oficial del Framework.

---

# Conclusión

El archivo **app.py** constituye el núcleo organizativo del Framework.

Aunque contiene muy poca lógica de negocio, define el flujo completo de ejecución del Dashboard y coordina el funcionamiento de todos los componentes.

La filosofía de este Framework es sencilla:

> **No modificamos la arquitectura; personalizamos los componentes.**

Aplicando esta metodología será posible construir nuevos Dashboards de forma mucho más rápida, manteniendo siempre una estructura uniforme, escalable y fácil de mantener.

En el siguiente capítulo construiremos el primer componente visual del Framework: el **Sidebar profesional**.