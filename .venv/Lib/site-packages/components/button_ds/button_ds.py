import hashlib
from pathlib import Path
from urllib.parse import quote
import streamlit as st
from theme import ACURACIA_HIGH_EMPHASIS, inject_theme_css


def _load_css() -> None:
    """Injects component CSS on every render (required for @st.fragment compatibility)."""
    inject_theme_css()
    css_path = Path(__file__).parent / "css" / f"{Path(__file__).stem}.css"
    st.markdown(
        f"<style>{css_path.read_text(encoding='utf-8')}</style>",
        unsafe_allow_html=True,
    )


_ICON_SEARCH = "<svg width='14' height='14' viewBox='0 0 14 14' fill='none' xmlns='http://www.w3.org/2000/svg'><path d='M5.54167 9.33333C4.48194 9.33333 3.58507 8.96632 2.85104 8.23229C2.11701 7.49826 1.75 6.60139 1.75 5.54167C1.75 4.48194 2.11701 3.58507 2.85104 2.85104C3.58507 2.11701 4.48194 1.75 5.54167 1.75C6.60139 1.75 7.49826 2.11701 8.23229 2.85104C8.96632 3.58507 9.33333 4.48194 9.33333 5.54167C9.33333 5.96944 9.26528 6.37292 9.12917 6.75208C8.99306 7.13125 8.80833 7.46667 8.575 7.75833L11.8417 11.025C11.9486 11.1319 12.0021 11.2681 12.0021 11.4333C12.0021 11.5986 11.9486 11.7347 11.8417 11.8417C11.7347 11.9486 11.5986 12.0021 11.4333 12.0021C11.2681 12.0021 11.1319 11.9486 11.025 11.8417L7.75833 8.575C7.46667 8.80833 7.13125 8.99306 6.75208 9.12917C6.37292 9.26528 5.96944 9.33333 5.54167 9.33333ZM5.54167 8.16667C6.27083 8.16667 6.89063 7.91146 7.40104 7.40104C7.91146 6.89063 8.16667 6.27083 8.16667 5.54167C8.16667 4.8125 7.91146 4.19271 7.40104 3.68229C6.89063 3.17188 6.27083 2.91667 5.54167 2.91667C4.8125 2.91667 4.19271 3.17188 3.68229 3.68229C3.17188 4.19271 2.91667 4.8125 2.91667 5.54167C2.91667 6.27083 3.17188 6.89063 3.68229 7.40104C4.19271 7.91146 4.8125 8.16667 5.54167 8.16667Z' fill='#ffffff'/></svg>"


def button_ds(
    title_button: str = "Buscar",
    bg_color: str = ACURACIA_HIGH_EMPHASIS,
    enabled_icon: bool = False,
    icon: str = _ICON_SEARCH,
    key: str = "",
) -> bool:
    """
    Reusable Button component — botão pill estilizado com ícone SVG opcional.

    Args:
        title_button: Texto exibido no botão. Padrão: "Buscar".
        bg_color:     Cor de fundo (e borda) do botão. Padrão: "#375C38".
        enabled_icon: Se True, exibe o ícone SVG antes do texto. Padrão: False.
        icon:         SVG bruto exibido antes do texto (usado quando enabled_icon=True).
        key:          Chave única. Obrigatório quando o mesmo botão aparece mais de uma vez na página.

    Returns:
        True se o botão foi clicado, False caso contrário.
    """
    _load_css()

    key_suffix = key if key else hashlib.md5(title_button.encode()).hexdigest()[:8]
    container_key = f"button_ds_{key_suffix}"

    overrides: list[str] = []

    overrides.append(f"""
[class*="st-key-{container_key}"] button {{
    background: {bg_color} !important;
    border-color: {bg_color} !important;
}}
""")

    if enabled_icon and icon:
        encoded_icon = quote(icon, safe="'")
        overrides.append(f"""
[class*="st-key-{container_key}"] button > div::before {{
    content: '' !important;
    display: inline-block !important;
    width: 14px !important;
    height: 14px !important;
    flex-shrink: 0 !important;
    background-repeat: no-repeat !important;
    background-size: contain !important;
    background-image: url("data:image/svg+xml,{encoded_icon}") !important;
}}
""")

    st.markdown(
        f"<style>{''.join(overrides)}</style>",
        unsafe_allow_html=True,
    )

    with st.container(key=container_key):
        return st.button(
            title_button,
            type="primary",
            key=f"btn_{key_suffix}" if key else None,
        )
