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
    padding-top: 1rem;
    padding-left: 1rem;
    padding-right: 1rem;
    max-width: 1000px;
}

h1 {
    font-size: clamp(1.6rem, 6vw, 2.6rem) !important;
    line-height: 1.15;
}

h2 {
    font-size: clamp(1.25rem, 5vw, 2rem) !important;
    line-height: 1.2;
    margin-top: 1.4rem;
}

h3 {
    font-size: clamp(1rem, 4vw, 1.35rem) !important;
    line-height: 1.25;
}

p, li {
    font-size: clamp(0.88rem, 3.4vw, 1rem) !important;
    line-height: 1.45;
}

.stMarkdown {
    max-width: 100%;
}

@media (max-width: 768px) {
    .block-container {
        padding-top: 0.8rem;
        padding-left: 0.8rem;
        padding-right: 0.8rem;
    }

    h1 {
        font-size: 1.7rem !important;
    }

    h2 {
        font-size: 1.35rem !important;
    }

    h3 {
        font-size: 1.05rem !important;
    }

    p, li {
        font-size: 0.88rem !important;
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

st.sidebar.title("📌 Desarrollos")
st.sidebar.write("Usa el selector principal para navegar mejor desde el celular.")

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