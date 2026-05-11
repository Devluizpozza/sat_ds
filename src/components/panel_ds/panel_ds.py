from contextlib import contextmanager
from pathlib import Path
import streamlit as st
from theme import BORDER, inject_theme_css


def _load_css() -> None:
    """Injects component CSS on every render (required for @st.fragment compatibility)."""
    inject_theme_css()
    css_path = Path(__file__).parent / "css" / f"{Path(__file__).stem}.css"
    st.markdown(
        f"<style>{css_path.read_text(encoding='utf-8')}</style>",
        unsafe_allow_html=True,
    )


@contextmanager
def panel_ds(
    key: str,
    border_color: str = BORDER,
    border_radius: str = "12px",
    gap: str = "",
    padding: str = "",
    overflow: str = "",
):
    """
    Reusable Panel component — container com borda estilizada que se adapta ao conteúdo.

    Args:
        key:           Chave única do container. Obrigatório.
        border_color:  Cor da borda. Padrão: BORDER (#DDD).
        border_radius: Raio da borda. Padrão: "12px".
        gap:           Gap entre elementos filhos (ex: "10px"). Padrão: "" (não definido).
        padding:       Padding interno (ex: "0" para remover). Padrão: "" (padrão do Streamlit).
        overflow:      Comportamento de overflow (ex: "hidden"). Padrão: "" (não definido).
    """
    _load_css()

    rules: list[str] = [
        f"border-style: solid !important;",
        f"border-color: {border_color} !important;",
        f"border-width: 2px 1px 1px 1px !important;",
        f"border-radius: {border_radius} !important;",
    ]
    if gap:
        rules.append(f"gap: {gap} !important;")
    if padding:
        rules.append(f"padding: {padding} !important;")
    if overflow:
        rules.append(f"overflow: {overflow} !important;")

    st.markdown(
        f"<style>[class*=\"st-key-{key}\"] {{ {''.join(rules)} }}</style>",
        unsafe_allow_html=True,
    )

    with st.container(border=True, key=key):
        yield
