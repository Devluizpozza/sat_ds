import streamlit as st

from .colors import (
    ACURACIA_HIGH,
    ACURACIA_HIGH_EMPHASIS,
    ACURACIA_HIGH_HOVER,
    ACURACIA_HIGH_BORDER,
    ACURACIA_HIGH_BG,
    ACURACIA_HIGH_DELTA,
    ACURACIA_MEDIUM,
    ACURACIA_MEDIUM_BORDER,
    ACURACIA_MEDIUM_BG,
    ACURACIA_MEDIUM_DELTA,
    ACURACIA_LOW,
    ACURACIA_LOW_BORDER,
    ACURACIA_LOW_BG,
    ACURACIA_LOW_DELTA,
    INFO,
    INFO_BG,
    INFO_BORDER,
    TEXT_PRIMARY,
    TEXT_BODY,
    TEXT_SECONDARY,
    TEXT_LABEL,
    TEXT_MUTED,
    TEXT_SUBTLE,
    BORDER,
    BORDER_INPUT,
    BORDER_CARD,
    BG_WHITE,
    BG_LIGHT,
    SHADOW,
    CSS_VARIABLES,
)

_THEME_CSS_KEY = "_sat_ds_theme_css_loaded"


def inject_theme_css() -> None:
    """Injeta as variáveis CSS do tema (:root) uma vez por sessão."""
    if _THEME_CSS_KEY not in st.session_state:
        st.markdown(f"<style>{CSS_VARIABLES}</style>", unsafe_allow_html=True)
        st.session_state[_THEME_CSS_KEY] = True
