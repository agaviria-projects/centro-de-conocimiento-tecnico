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
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1100px;
}

h1 {
    font-size: clamp(1.8rem, 5vw, 3rem);
}

h2 {
    font-size: clamp(1.4rem, 4vw, 2.2rem);
}

h3 {
    font-size: clamp(1.1rem, 3vw, 1.5rem);
}

p, li {
    font-size: clamp(0.95rem, 2.5vw, 1.1rem);
    line-height: 1.6;
}

@media (max-width: 768px) {
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
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