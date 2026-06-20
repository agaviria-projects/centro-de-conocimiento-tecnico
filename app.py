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
    "🗺️ Mapa de Geolocalización",
    "📄 Compresor PDF",
    "💬 WhatsApp + ANS + Formularios",
    "🎓 Portal Formación Elite",
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
    ruta = Path("docs/generador_informes_ans.md")

    if ruta.exists():
        st.markdown(ruta.read_text(encoding="utf-8"))
    else:
        st.error("No se encontró el archivo docs/generador_informes_ans.md")
else:
    st.info("Este módulo se documentará después.")