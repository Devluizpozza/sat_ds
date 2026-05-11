from contextlib import contextmanager
from pathlib import Path
import streamlit as st
from theme import inject_theme_css


def _load_css() -> None:
    """Injects component CSS on every render (required for @st.fragment compatibility)."""
    inject_theme_css()
    css_path = Path(__file__).parent / "css" / f"{Path(__file__).stem}.css"
    st.markdown(
        f"<style>{css_path.read_text(encoding='utf-8')}</style>",
        unsafe_allow_html=True,
    )


@contextmanager
def accordeon(label: str, expanded: bool = False):
    """
    Reusable Accordeon component.

    Args:
        label: Título do expander (suporta ícones Material, ex: `:material/bar_chart: Título`).
        expanded: Se o expander deve iniciar aberto. Padrão: False.
    """
    _load_css()
    with st.expander(label, expanded=expanded):
        yield
