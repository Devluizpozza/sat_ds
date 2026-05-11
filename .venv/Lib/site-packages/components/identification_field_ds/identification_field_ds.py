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


def identification_field_ds(
    label: str,
    placeholder: str = "",
    value: str = "",
    key: str = "",
) -> str:
    """
    Reusable Identification Field component — input de texto estilizado.

    Args:
        label:       Label exibido acima do campo.
        placeholder: Texto de placeholder (ex: "00.000.000/0000-00").
        value:       Valor inicial do campo.
        key:         Chave única para o componente. Obrigatório quando o mesmo
                     campo aparece mais de uma vez na página.

    Returns:
        Valor digitado no campo (str).
    """
    _load_css()

    key_suffix = key if key else label
    container_key = f"identification_field_{key_suffix}"

    with st.container(key=container_key):
        return st.text_input(
            label,
            value=value,
            placeholder=placeholder,
            key=f"text_input_{key_suffix}" if key else None,
        )
