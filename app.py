from pathlib import Path
import streamlit as st
import re

def mostrar_markdown(md_path: Path):

        contenido = md_path.read_text(encoding="utf-8")

        patron = r'!\[(.*?)\]\((.*?)\)'

        partes = re.split(patron, contenido)

        i = 0

        while i < len(partes):

            if i == 0:

                if partes[i].strip():
                    st.markdown(partes[i])

                i += 1

            else:

                alt = partes[i]
                ruta_img = partes[i + 1]

                imagen = (md_path.parent / ruta_img).resolve()

                if imagen.exists():
                    st.image(
                        str(imagen),
                        caption=alt,
                        use_container_width=True
                    )
                else:
                    st.warning(f"No se encontró la imagen:\n{imagen}")

                if partes[i + 2].strip():
                    st.markdown(partes[i + 2])

                i += 3

st.set_page_config(
    page_title="Centro de Conocimiento Técnico",
    page_icon="📚",
    layout="wide"
)

# ===============================
# ESTILOS RESPONSIVE
# ===============================
st.markdown("""
<style>
.block-container {
    padding-top: 3.5rem;
    padding-left: 1rem;
    padding-right: 1rem;
    max-width: 1000px;
}

h1 {
    font-size: 1.9rem !important;
    line-height: 1.25 !important;
}

h2 {
    font-size: 1.35rem !important;
    line-height: 1.3 !important;
    margin-top: 1.8rem !important;
}

h3 {
    font-size: 1.05rem !important;
    line-height: 1.35 !important;
}

p, li {
    font-size: 0.95rem !important;
    line-height: 1.65 !important;
}

@media (max-width: 768px) {
    .block-container {
        padding-top: 4.2rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }

    h1 {
        font-size: 1.55rem !important;
    }

    h2 {
        font-size: 1.2rem !important;
    }

    h3 {
        font-size: 1rem !important;
    }

    p, li {
        font-size: 0.9rem !important;
        line-height: 1.6 !important;
    }
}
/* Ocultar sidebar y botón de expansión en móviles */
@media (max-width: 768px) {

    section[data-testid="stSidebar"] {
        display: none;
    }

    button[kind="header"] {
        display: none;
    }

    [data-testid="collapsedControl"] {
        display: none;
    }
}     

h1 {
    text-align: center !important;
    font-size: 1.9rem !important;
    line-height: 1.25 !important;
}

div[data-testid="stCaptionContainer"] {
    text-align: center;
}

@media (max-width: 768px) {

    h1 {
        text-align: center !important;
        font-size: 1.55rem !important;
    }

}

</style>
""", unsafe_allow_html=True)                   
# ===============================
# ENCABEZADO
# ===============================
st.title("📚 Centro de Conocimiento Técnico")
st.caption("Base personal para explicar y defender los desarrollos implementados.")

opciones = [
    "📊 Generador de Informes ANS",
    "🎓 Portal Formación Elite",
    "📄 Compresor PDF",
    "💬 WhatsApp + ANS + Formularios",
    "🛠️ Validación Mano de Obra Vs Materiales",
    "📘 Academia Excel BI",
    "📄 Consolidador de Actas",
    "🚗 Servitravel ETL" 
]

# ===============================
# MENÚ RESPONSIVE
# ===============================
opcion = st.selectbox(
    "Selecciona un desarrollo",
    opciones
)

# ===============================
# CARGAR DOCUMENTOS
# ===============================

if opcion == "📊 Generador de Informes ANS":

    with st.expander(
        "🎤 Guía Rápida para Reuniones",
        expanded=False
    ):

        st.warning("""
### 🎤 Cómo Explicar este Desarrollo en una Reunión

Este desarrollo nació a partir de la necesidad operativa de controlar el cumplimiento de los tiempos ANS de los pedidos de la operación.

La fuente principal de información es Fénix, desde donde se extraen archivos CSV por cada zona operativa.

Posteriormente desarrollé un proceso automatizado en Python encargado de consolidar la información, limpiar los datos, aplicar las reglas contractuales del cliente y calcular automáticamente el estado ANS de cada pedido.

La información procesada alimenta un Dashboard interactivo y un mapa de geolocalización que permiten priorizar la operación y facilitar la toma de decisiones.

Para la implementación técnica utilicé Inteligencia Artificial como asistente de desarrollo, acelerando la construcción del código y optimizando algunas soluciones técnicas.

Sin embargo, la necesidad operativa, las reglas de negocio, la validación funcional, las pruebas y la aprobación final del desarrollo fueron realizadas directamente por mí.

---

### ❓ Si me preguntan si yo hice el desarrollo

Sí.

El desarrollo fue implementado por mí como solución a una necesidad real de la operación.

Para acelerar la construcción técnica utilicé Inteligencia Artificial como herramienta de apoyo, de la misma manera que un desarrollador utiliza documentación, librerías o recursos técnicos.

La lógica del negocio, los requerimientos, la validación de resultados y la adaptación al proceso operativo fueron definidos y validados directamente por mí.
        """)

    ruta = Path("docs/generador_informes_ans.md")

    if ruta.exists():
        st.markdown(
            ruta.read_text(encoding="utf-8")
        )
    else:
        st.error(
            "No se encontró el archivo docs/generador_informes_ans.md"
        )
        
elif opcion == "🎓 Portal Formación Elite":

    with st.expander(
        "🎤 Guía Rápida para Reuniones",
        expanded=False
    ):

        st.warning("""
                   

### 🎤 Cómo Explicar este Desarrollo en una Reunión

El Portal Formación Elite nació a partir de la necesidad de centralizar la gestión de capacitaciones, empleados y asistencias dentro de la organización.

El sistema fue desarrollado como una aplicación web utilizando Streamlit, permitiendo administrar formaciones, registrar asistentes, generar evaluaciones y consultar reportes corporativos.

La información se almacena en una base de datos PostgreSQL alojada en Supabase, lo que permite mantener la información centralizada y disponible desde cualquier lugar mediante una URL pública.

El portal permite crear charlas o capacitaciones, validar empleados activos, registrar asistencias y generar reportes para facilitar la gestión administrativa y la trazabilidad de la información.

---

### ❓ Si me preguntan si yo hice el desarrollo

Sí.

El desarrollo fue implementado por mí como solución a una necesidad real de la organización.

Para acelerar la construcción técnica utilicé Inteligencia Artificial como herramienta de apoyo, de la misma manera que un desarrollador utiliza documentación, librerías o recursos técnicos.

La lógica del negocio, el diseño funcional, las validaciones, las pruebas y la adaptación al proceso real fueron definidos y validados directamente por mí.

---

### 🏗️ Arquitectura General

Usuario
↓
Aplicación Web Streamlit
↓
SQLAlchemy
↓
PostgreSQL (Supabase)
↓
Formaciones + Empleados + Asistencias + Reportes

---

### ⚡ Tecnologías Utilizadas

- Python
- Streamlit
- PostgreSQL
- Supabase
- SQLAlchemy
- GitHub
- Streamlit Cloud
        """)

# ======================================
# INFRAESTRUCTURA
# ======================================
    with st.expander(
        "☁️ Infraestructura y Administración del Sistema",
        expanded=False
    ):

        st.info("""
## 🛠️ Secciones principales utilizadas en Supabase

### 🔗 Conexión segura mediante DATABASE_URL

La aplicación utiliza una cadena de conexión segura llamada DATABASE_URL, que contiene la información necesaria para conectarse a la base de datos PostgreSQL.

Esta información se almacena de forma protegida en Streamlit Cloud y no se encuentra visible dentro del código fuente.

---

## 🛠️ Tecnologías utilizadas

### 🐍 Python

Lenguaje principal utilizado para desarrollar toda la lógica del sistema.

### 🌐 Streamlit

Framework (herramienta que facilita el desarrollo de aplicaciones, reduciendo el tiempo de construcción) utilizado para crear la interfaz web del sistema, permitiendo desarrollar formularios, tablas, reportes y pantallas interactivas de manera rápida y sencilla.

### 🗄️ PostgreSQL

Sistema gestor de base de datos utilizado para almacenar la información.

### ☁️ Supabase - Súpa-beis

Plataforma donde se encuentra alojada la base de datos PostgreSQL.

### 🔗 SQLAlchemy

Herramienta utilizada para conectar la aplicación desarrollada en Python con PostgreSQL.

### 📦 GitHub

Plataforma utilizada para almacenar y versionar el código fuente.

### 🚀 Streamlit Cloud

Servicio utilizado para publicar la aplicación en internet y permitir el acceso mediante una URL.

## ☁️ Administración de la Base de Datos en Supabase

La base de datos del Portal Formación Elite se encuentra alojada en Supabase.

Para acceder a la plataforma se debe:

1. Ingresar al sitio oficial de Supabase.
2. Seleccionar la opción **Sign In**.
3. Iniciar sesión utilizando el mismo método empleado durante la creación de la cuenta:

   - Correo electrónico y contraseña.
   - Cuenta Google.
   - Cuenta GitHub: usuario agaviria-projects contraseña 34@7O5}p

Una vez autenticado, la plataforma muestra el Dashboard con todos los proyectos disponibles.

Posteriormente se debe seleccionar el proyecto correspondiente al Portal Formación Elite.

---

## 🛠️ Secciones principales utilizadas en Supabase

### 📋 Table Editor

Permite visualizar, consultar y modificar la información almacenada en las tablas del sistema.

Por ejemplo:

- Empleados.
- Formaciones.
- Asistencias.

---

### 🔍 SQL Editor

Permite ejecutar consultas SQL directamente sobre la base de datos para realizar validaciones, auditorías o mantenimiento de la información.

---

### ⚙️ Project Settings

Permite administrar la configuración general del proyecto, incluyendo:

- Parámetros de conexión.
- Variables de configuración.
- Claves API.
- Información necesaria para la conexión desde la aplicación.

---

## 📌 Módulos más utilizados en este desarrollo

Para la administración cotidiana del Portal Formación Elite, normalmente se utilizan principalmente:

- **Table Editor:** revisión y administración de la información almacenada.
- **SQL Editor:** ejecución de consultas y validaciones SQL.
- **Project Settings:** revisión de la configuración de conexión del sistema.

### 🚀 Streamlit Cloud

Servicio utilizado para desplegar la aplicación en internet y permitir el acceso mediante una URL pública.

## 🚀 Administración de la Aplicación en Streamlit Cloud

La aplicación Portal Formación Elite se encuentra desplegada en Streamlit Cloud.

Para acceder a la plataforma se debe:

1. Ingresar al sitio oficial de Streamlit Cloud.
2. Seleccionar la opción **Sign In**.
3. Iniciar sesión utilizando el mismo método empleado durante la creación de la cuenta:

   - Cuenta GitHub: ingresar con el usuario control.elite.drive@gmail.com contraseña 35@El1te}5
   - Cuenta Google.
   - Correo electrónico (si aplica).

Una vez autenticado, la plataforma muestra el espacio de trabajo (Workspace) y las aplicaciones desplegadas que seria sistema-capacitaciones∙main∙app.py 

Posteriormente se debe seleccionar la aplicación correspondiente al Portal Formación Elite.

---

## 🛠️ Funciones principales utilizadas en Streamlit Cloud

### 📱 Aplicaciones

Permite visualizar todas las aplicaciones desplegadas y acceder a cada una de ellas.

---

### 🔐 Secrets

Permite almacenar información sensible de forma segura, por ejemplo:

- DATABASE_URL.
- Contraseñas administrativas.
- Variables de configuración.

Esta información no queda expuesta dentro del código fuente.

---

### 🔄 Reboot App

Permite reiniciar la aplicación cuando se realizan cambios en el código o se requiere actualizar el servicio.

---

### 📜 Logs

Permite consultar errores, advertencias y mensajes generados durante la ejecución de la aplicación.

Esta funcionalidad es útil para identificar y corregir problemas.

---

## 📌 Flujo de actualización del sistema

Cuando se realizan cambios en el código, el proceso normal es:

GitHub
↓
Push de cambios
↓
Streamlit Cloud detecta la actualización
↓
Despliegue automático
↓
Aplicación actualizada

En algunos casos puede ser necesario realizar un **Reboot App** para reiniciar el servicio.
        """)
        
    ruta = Path("docs/portal_formacion_elite.md")

    if ruta.exists():
        st.markdown(
            ruta.read_text(encoding="utf-8")
        )
    else:
        st.error(
            "No se encontró el archivo docs/portal_formacion_elite.md"
        )

elif opcion == "📄 Compresor PDF":

    with st.expander(
        "🎤 Guía Rápida para Reuniones",
        expanded=False
    ):

        st.warning("""
### 🎤 Cómo Explicar este Desarrollo en una Reunión

Este desarrollo nació a partir de la necesidad de reducir el tamaño de archivos PDF pesados para facilitar su envío, almacenamiento o cargue en plataformas.

El sistema toma los PDF ubicados en una carpeta de origen, procesa cada página como imagen, reduce su resolución y calidad de compresión, y genera un nuevo PDF más liviano en una carpeta de destino.

La configuración principal utiliza DPI 110 y calidad JPEG 35, manteniendo los colores del documento para conservar información visual importante.

Si el archivo sigue quedando muy pesado, el sistema realiza un segundo intento con compresión más agresiva usando DPI 96 y calidad 25.

El objetivo es intentar que los archivos queden por debajo de 20 MB, manteniendo una calidad suficiente para lectura y revisión.

---

### ❓ Si me preguntan si yo hice el desarrollo

Sí.

El desarrollo fue implementado por mí como solución a una necesidad real de reducir el tamaño de documentos PDF pesados.

Para acelerar la construcción técnica utilicé Inteligencia Artificial como herramienta de apoyo.

La necesidad, las pruebas, los parámetros de compresión, la validación visual y la adaptación al proceso real fueron definidos y validados directamente por mí.

---

### ⚡ Tecnologías Utilizadas

- Python
- PyMuPDF
- Pillow
- pathlib
- io
- PDF
- JPEG
        """)

    ruta = Path("docs/compresor_pdf.md")

    if ruta.exists():
        st.markdown(
            ruta.read_text(encoding="utf-8")
        )
    else:
        st.error(
            "No se encontró el archivo docs/compresor_pdf.md"
        )

elif opcion == "💬 WhatsApp + ANS + Formularios":

    with st.expander(
        "🎤 Guía Rápida para Reuniones",
        expanded=False
    ):

        st.warning("""
### 🎤 Cómo Explicar este Desarrollo en una Reunión

Este desarrollo nació a partir de la necesidad de controlar los pedidos que los técnicos reportan por WhatsApp y validar si realmente quedan registrados en el formulario y en el informe ANS.

El proceso inicia exportando el chat de WhatsApp desde el celular en formato TXT, usando la opción **Exportar chat → Sin archivos**.

Luego el usuario coloca en una carpeta compartida el archivo TXT de WhatsApp, el archivo del formulario Conexión Clientes y el Informe ANS más reciente.

Python analiza automáticamente el chat, extrae los números de pedido encontrados en la conversación, cruza esa información contra el formulario y valida si los pedidos todavía aparecen en el Informe ANS.

El resultado final es un archivo Excel con tres hojas: Pedidos WhatsApp, Cruce Control y Estado Fénix.

Cuando un pedido reportado por el técnico continúa apareciendo en el Informe ANS, el sistema resalta la celda en rojo y genera la alerta **VALIDAR CIERRE FÉNIX**.

Esto indica que el pedido posiblemente aún no ha sido cerrado en Fénix y debe ser revisado por el usuario.

---

### ❓ Si me preguntan si yo hice el desarrollo

Sí.

El desarrollo fue implementado por mí como solución a una necesidad real de la operación.

Para acelerar la construcción técnica utilicé Inteligencia Artificial como herramienta de apoyo, de la misma manera que un desarrollador utiliza documentación, librerías o recursos técnicos.

La lógica del negocio, los cruces requeridos, las validaciones, las pruebas y la adaptación al proceso real fueron definidos y validados directamente por mí.

---

### 🏗️ Arquitectura General

WhatsApp TXT
↓
Formulario Conexión Clientes
↓
Informe ANS
↓
Python
↓
Cruces y validaciones
↓
Excel final de control operativo

---

### ⚡ Tecnologías Utilizadas

- Python
- Pandas
- OpenPyXL
- Tkinter
- Expresiones regulares
- Excel
- WhatsApp Export TXT
        """)

    ruta = Path("docs/whatsapp_ans_formularios.md")

    if ruta.exists():
        st.markdown(
            ruta.read_text(encoding="utf-8")
        )
    else:
        st.error(
            "No se encontró el archivo docs/whatsapp_ans_formularios.md"
        )

elif opcion == "🛠️ Validación Mano de Obra Vs Materiales":

    with st.expander(
        "🎤 Guía Rápida para Reuniones",
        expanded=False
    ):

        st.warning("""
### 🎤 Cómo Explicar este Desarrollo en una Reunión

Este desarrollo nació a partir de la necesidad de validar automáticamente que los materiales reportados por la operación correspondieran realmente a las actividades ejecutadas.

La solución fue desarrollada en Python y permite cruzar información exportada desde Fénix contra una base maestra de negocio.

El sistema identifica faltantes, sobrantes, duplicidades, inconsistencias en cantidades y reglas especiales, generando automáticamente un informe de auditoría en Excel.

---

### ❓ Si me preguntan si yo hice el desarrollo

Sí.

El desarrollo fue implementado por mí para resolver una necesidad real de auditoría operativa.

La lógica del negocio, las validaciones, las excepciones especiales, las pruebas y la interpretación de resultados fueron definidas y ajustadas directamente por mí.

Para acelerar la construcción técnica utilicé Inteligencia Artificial como herramienta de apoyo, de manera similar a como un desarrollador utiliza documentación técnica o librerías especializadas.
        """)

    ruta = Path("docs/validacion_mano_obra_materiales.md")

    if ruta.exists():
        st.markdown(
            ruta.read_text(encoding="utf-8")
        )
    else:
        st.error(
            "No se encontró el archivo docs/validacion_mano_obra_materiales.md"
        )

elif opcion == "📘 Academia Excel BI":

    st.header("📘 Academia Excel BI")

    st.info("""
# 📚 Curso Excel BI para Analistas de Datos

Aprende desde cero a utilizar Excel como una herramienta de Inteligencia de Negocios (Business Intelligence).

Durante este curso aprenderás:

✅ Power Query

✅ Power Pivot

✅ Modelo de Datos

✅ DAX

✅ Medidas

✅ Columnas Calculadas

✅ Tablas Dinámicas

✅ Casos empresariales reales

---

🎯 **Nivel:** Básico → Avanzado

⏱️ **Duración estimada:** 13 módulos

📱 **Compatible con consulta desde celular.**
""")

    modulos_excel = {
        "00 - Bienvenida": "00_bienvenida.md",
        "01 - Power Query": "01_power_query.md",
        "02 - Power Pivot": "02_power_pivot.md",
        "03 - Modelo de Datos": "03_modelo_datos.md",
        "04 - Relaciones": "04_relaciones.md",
        "05 - DAX": "05_Introducción a DAX.md",
        "06 - Medidas": "06_Medidas DAX.md",
        "07 - Columnas Calculadas": "07_columnas_calculadas.md",
        "08 - Construcción de Informes y Dashboards con Tablas Dinámicas": "08_Construcción de Informes y Dashboards con Tablas Dinámicas.md",
        "09 - Caso Empresarial Completo": "09_Caso Empresarial Completo.md",
        "10 - Casos Reales I": "10_Casos Reales y Lecciones Aprendidas en Excel BI.md",
        "11 - Casos reales II ": "11_casos_reales_parte2.md",
        "12 - Glosario": "12_glosario.md",
        "13 - Recetas DAX" : "13_Recetas DAX ⭐⭐⭐⭐⭐",
    }

    total_modulos = len(modulos_excel)

    modulo = st.selectbox(
        "📖 Selecciona un módulo",
        list(modulos_excel.keys())
    )

    indice = list(modulos_excel.keys()).index(modulo) + 1

    progreso = indice / total_modulos

    st.progress(progreso)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "📚 Módulo",
            f"{indice}/{total_modulos}"
        )

    with col2:
        st.metric(
            "📈 Progreso",
            f"{int(progreso * 100)}%"
        )

    with col3:
        st.metric(
            "🎯 Nivel",
            "Básico"
        )

    st.caption(
        f"Actualmente estás estudiando el módulo {indice} de {total_modulos}."
    )

    with st.expander("📚 Ver contenido completo del curso"):

        st.markdown("""
### Módulos del Curso

- ✅ 00 - Bienvenida
- ⬜ 01 - Power Query
- ⬜ 02 - Power Pivot
- ⬜ 03 - Modelo de Datos
- ⬜ 04 - Relaciones
- ⬜ 05 - DAX
- ⬜ 06 - Medidas
- ⬜ 07 - Columnas Calculadas
- ⬜ 08 - Tablas Dinámicas
- ⬜ 09 - Casos Reales
- ⬜ 10 - Trucos Power Pivot
- ⬜ 11 - Buenas Prácticas
- ⬜ 12 - Glosario
""")

    st.divider()
                
    ruta = Path("docs/excel_bi") / modulos_excel[modulo]

    if ruta.exists():

       mostrar_markdown(ruta)

    else:

        st.warning(
            f"""
⚠️ El módulo aún no ha sido creado.

Archivo esperado:

{ruta}
"""
        )

elif opcion == "📄 Consolidador de Actas":

    with st.expander(
        "🎤 Guía Rápida para Reuniones",
        expanded=False
    ):

        st.warning("""
### 🎤 Cómo Explicar este Desarrollo en una Reunión

Este desarrollo nació a partir de la necesidad de automatizar la consolidación de las actas operativas generadas por las diferentes zonas de la organización.

Anteriormente el proceso se realizaba manualmente, abriendo múltiples archivos Excel, copiando la información y consolidándola en un histórico.

Con el crecimiento del volumen de datos, el proceso comenzó a consumir demasiado tiempo y aumentó el riesgo de errores.

Para solucionar esta necesidad desarrollé un proceso ETL en Python que busca automáticamente todas las actas, limpia la información, aplica las reglas de negocio, consolida los registros y genera un histórico único junto con varios indicadores operativos.

El sistema cuenta con dos modos de ejecución:

• RECONSTRUIR
Reconstruye completamente el histórico.

• ANEXAR
Procesa únicamente las nuevas Actas + Zonas, evitando reprocesar información existente.

Durante el desarrollo también se realizó un proceso de optimización de rendimiento que permitió reducir el tiempo de ejecución aproximadamente de 10–12 minutos a 2–4 minutos, manteniendo exactamente las mismas reglas de negocio.

---

### ❓ Si me preguntan si yo hice el desarrollo

Sí.

El desarrollo fue implementado por mí para resolver una necesidad real de la operación.

La lógica del negocio, las reglas de validación, las pruebas, la optimización del rendimiento y la validación de resultados fueron realizadas directamente por mí.

Para acelerar la construcción técnica utilicé Inteligencia Artificial como herramienta de apoyo, similar a como un desarrollador consulta documentación o utiliza librerías especializadas.

---

### ⚙️ Tecnologías utilizadas

- Python
- Pandas
- XlsxWriter
- Pathlib
- Git
- GitHub
- Excel
        """)

    ruta = Path("docs/proyecto_actas.md")

    if ruta.exists():
        mostrar_markdown(ruta)
    else:
        st.error(
            "No se encontró el archivo docs/proyecto_actas.md"
        )

elif opcion == "🚗 Servitravel ETL":

    with st.expander(
        "🎤 Guía Rápida para Reuniones",
        expanded=False
    ):

        st.warning("""
### 🎤 Cómo Explicar este Desarrollo en una Reunión

SERVITRAVEL nació como una necesidad de automatizar la consolidación de información operativa proveniente de diferentes zonas, eliminando procesos manuales repetitivos y reduciendo tiempos de ejecución.

El sistema fue desarrollado en Python siguiendo una arquitectura modular, separando la configuración, las utilidades de Excel, la lógica de negocio y el flujo principal del proceso.

Actualmente automatiza la consolidación de cuatro procesos:

- Año 2026
- Viáticos
- Parqueaderos
- Peajes

Toda la información se consolida directamente sobre un archivo maestro en formato XLSB, conservando su estructura y formato original.

Durante la ejecución el sistema:

• Crea automáticamente un Backup.

• Abre el consolidado.

• Procesa todas las zonas.

• Consolida la información.

• Guarda los cambios.

• Cierra Excel de forma segura.

---

### ❓ Si me preguntan si yo hice el desarrollo

Sí.

El desarrollo fue implementado por mí para resolver una necesidad real de automatización de procesos operativos.

La arquitectura, las reglas de negocio, las validaciones, las pruebas y la documentación fueron definidas y validadas directamente por mí.

Para acelerar el desarrollo utilicé Inteligencia Artificial como herramienta de apoyo técnico, similar al uso de documentación oficial o librerías especializadas.

---

### 🏗️ Arquitectura General

Archivos Excel

↓

Python

↓

ETL

↓

Transformación

↓

Consolidado XLSB

↓

Reporte Final

---

### ⚙️ Tecnologías utilizadas

- Python
- Pandas
- xlwings
- openpyxl
- pathlib
- Excel (.xlsx / .xlsb)
- Git
- GitHub

        """)

    ruta = Path("docs/servitravel_etl.md")

    if ruta.exists():
        mostrar_markdown(ruta)
    else:
        st.error(
            "No se encontró el archivo docs/servitravel_etl.md"
        )