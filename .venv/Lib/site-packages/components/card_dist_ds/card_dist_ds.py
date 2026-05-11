from pathlib import Path
import streamlit as st
from theme import ACURACIA_MEDIUM, inject_theme_css


def _load_css() -> None:
    """Injects component CSS on every render (required for @st.fragment compatibility)."""
    inject_theme_css()
    css_path = Path(__file__).parent / "css" / f"{Path(__file__).stem}.css"
    st.markdown(
        f"<style>{css_path.read_text(encoding='utf-8')}</style>",
        unsafe_allow_html=True,
    )


def card_dist_ds(
    title: str,
    value: str,
    percent: str,
    itens: str,
    companys: str,
    bb_color: str = ACURACIA_MEDIUM,
    percent_color: str = ACURACIA_MEDIUM,
) -> None:
    """
    Reusable Card de Distribuição por Ano component.

    Args:
        title:         Título do card — geralmente o ano (ex: "2021", "2022").
        value:         Valor principal formatado (ex: "R$ 35.267.179,46").
        percent:       Percentual formatado (ex: "30,2%").
        itens:         Quantidade de itens formatada (ex: "44.178.950").
        companys:      Quantidade de empresas formatada (ex: "3.640").
        bb_color:      Cor da borda inferior do card. Padrão: ACURACIA_MEDIUM (#E8BD00).
        percent_color: Cor do texto de percentual. Padrão: ACURACIA_MEDIUM (#E8BD00).
    """
    _load_css()

    st.markdown(
        f"""
        <div class="card-dist-ds" style="border-bottom-color:{bb_color}">
            <span class="card-dist-ds__title">{title}</span>
            <span class="card-dist-ds__value">{value}</span>
            <span class="card-dist-ds__percent" style="color:{percent_color}">{percent}</span>
            <div class="card-dist-ds__stats">
                <span class="card-dist-ds__meta">{itens} itens</span>
                <span class="card-dist-ds__meta">{companys} empresas</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
