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

# ¿Qué debo modificar?

Cuando reutilices esta plantilla normalmente solo será necesario modificar los siguientes elementos.

| Elemento | ¿Debe modificarse? |
|-----------|--------------------|
| page_title | ✅ Sí |
| page_icon | ✅ Sí |
| Banner | ✅ Sí |
| Sidebar | ✅ Sí |
| Lector de datos | ✅ Sí |
| Componentes del Dashboard | ✅ Sí |
| Navegación | ✅ Sí |

---

# ¿Qué NO debo modificar?

Se recomienda mantener siempre la siguiente estructura.

```text
Importaciones

↓

Configuración

↓

Estilos

↓

Banner

↓

Datos

↓

Sidebar

↓

Navegación

↓

Componentes
```

Este orden hace parte de la arquitectura oficial del Framework.

Modificarlo puede dificultar el mantenimiento del proyecto.

---

# Buenas prácticas

✔ Mantener app.py pequeño.

✔ Utilizar comentarios para dividir cada sección.

✔ Leer la información una única vez.

✔ Mantener siempre el mismo orden.

✔ Separar la lógica del negocio de la interfaz.

✔ Importar únicamente los componentes necesarios.

✔ Reutilizar esta plantilla en todos los proyectos.

---

# Errores comunes

Durante el desarrollo de diferentes Dashboards empresariales se identificaron los siguientes errores.

❌ Colocar toda la lógica dentro de app.py.

❌ Leer el mismo archivo Excel desde varios componentes.

❌ Mezclar estilos CSS con lógica Python.

❌ Crear componentes demasiado grandes.

❌ Duplicar funciones.

❌ Colocar la navegación dentro del Sidebar.

❌ Modificar el orden general del archivo.

---

# Lecciones aprendidas

Después de desarrollar diferentes Dashboards empresariales se adoptaron las siguientes reglas.

- app.py únicamente coordina la aplicación.

- Cada componente debe tener una única responsabilidad.

- Los estilos siempre se cargan antes del Banner.

- Los datos siempre se leen una única vez.

- La navegación principal nunca debe depender del Sidebar.

- Todo nuevo Dashboard debe comenzar reutilizando esta plantilla.

---

# Checklist

Antes de continuar con el siguiente capítulo verifica que:

☐ El Dashboard inicia correctamente.

☐ No existen errores en consola.

☐ El Banner aparece correctamente.

☐ El Sidebar carga la información.

☐ La navegación funciona.

☐ Los componentes responden correctamente.

☐ La estructura del app.py coincide con la arquitectura oficial del Framework.

---

# Conclusión

El archivo **app.py** representa el núcleo organizativo del Dashboard.

Aunque contiene muy poco código de negocio, define el flujo completo de la aplicación y coordina el funcionamiento de todos los componentes.

Una correcta organización desde este punto facilitará enormemente el crecimiento del proyecto.

En el siguiente capítulo construiremos el primer componente visual del Framework: **el Sidebar profesional**.