import streamlit as st
from pathlib import Path

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
    ruta = Path("docs/portal_formacion_elite.md")

    if ruta.exists():
        st.markdown(ruta.read_text(encoding="utf-8"))
    else:
        st.error(
            "No se encontró el archivo docs/portal_formacion_elite.md"
        )

elif opcion == "🗺️ Mapa de Geolocalización":
    st.info("Este módulo se documentará después.")

elif opcion == "📄 Compresor PDF":
    st.info("Este módulo se documentará después.")

elif opcion == "💬 WhatsApp + ANS + Formularios":
    st.info("Este módulo se documentará después.")

else:
    st.info("Este módulo se documentará después.")