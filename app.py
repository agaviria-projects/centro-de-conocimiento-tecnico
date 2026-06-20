import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Centro de Conocimiento Técnico",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Centro de Conocimiento Técnico")
st.caption("Base personal para explicar y defender los desarrollos implementados.")

opcion = st.sidebar.radio(
    "Selecciona un desarrollo",
    [
        "📊 Generador de Informes ANS",
        "🗺️ Mapa de Geolocalización",
        "📄 Compresor PDF",
        "💬 WhatsApp + ANS + Formularios",
        "🎓 Portal Formación Elite",
    ]
)

if opcion == "📊 Generador de Informes ANS":
    ruta = Path("docs/generador_informes_ans.md")
    st.markdown(ruta.read_text(encoding="utf-8"))
else:
    st.info("Este módulo se documentará después.")