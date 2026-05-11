from pathlib import Path
import streamlit as st
from theme import INFO_BG, INFO_BORDER, inject_theme_css


def _load_css() -> None:
    """Injects component CSS on every render (required for @st.fragment compatibility)."""
    inject_theme_css()
    css_path = Path(__file__).parent / "css" / f"{Path(__file__).stem}.css"
    st.markdown(
        f"<style>{css_path.read_text(encoding='utf-8')}</style>",
        unsafe_allow_html=True,
    )


def info_bar_ds(
    text: str,
    bg_color: str = INFO_BG,
    border: str = f"1.5px solid {INFO_BORDER}",
    margin_bottom: str = "",
) -> None:
    """
    Reusable Info Bar component.

    Args:
        text:          Texto exibido na barra.
        bg_color:      Cor de fundo da barra. Padrão: "#D9EDF7" (azul claro).
        border:        Borda da barra (valor CSS completo). Padrão: "1.5px solid #BCE8F1".
        margin_bottom: Espaço abaixo da barra (valor CSS). Padrão: "" (nenhum).
    """
    _load_css()

    margin_style = f";margin-bottom:{margin_bottom}" if margin_bottom else ""

    st.markdown(
        f'<div class="info-bar-ds" style="background:{bg_color};border:{border}{margin_style}">'
        f"{text}"
        f"</div>",
        unsafe_allow_html=True,
    )
