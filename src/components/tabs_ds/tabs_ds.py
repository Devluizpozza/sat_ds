from pathlib import Path
import streamlit as st
from theme import inject_theme_css


def _load_css() -> None:
    """Injects component CSS once per session."""
    inject_theme_css()
    key = f"_css_loaded_{__name__}"
    if key not in st.session_state:
        css_path = Path(__file__).parent / "css" / f"{Path(__file__).stem}.css"
        st.markdown(
            f"<style>{css_path.read_text(encoding='utf-8')}</style>",
            unsafe_allow_html=True,
        )
        st.session_state[key] = True


def tabs_ds(titulo: list[str]):
    """
    Reusable Tabs component.

    Args:
        titulo: Lista de títulos das abas (suporta texto, emoji e ícones Material).

    Returns:
        Lista de contextos de aba, idêntica ao retorno de st.tabs().

    Example:
        tab_a, tab_b = tabs_ds(["Aba A", "Aba B"])
        with tab_a:
            st.write("Conteúdo A")
    """
    _load_css()
    return st.tabs(titulo)
