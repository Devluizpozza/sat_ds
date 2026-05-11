import hashlib
from enum import Enum
from pathlib import Path
from typing import Literal
import streamlit as st
from theme import (
    ACURACIA_HIGH,
    ACURACIA_HIGH_DELTA,
    ACURACIA_MEDIUM,
    ACURACIA_LOW,
    inject_theme_css,
)


class CategoryType(str, Enum):
    HIGH   = "high"
    MEDIUM = "medium"
    LOW    = "low"


_CATEGORY_BORDER_COLOR: dict[CategoryType, str] = {
    CategoryType.HIGH:   ACURACIA_HIGH,
    CategoryType.MEDIUM: ACURACIA_MEDIUM,
    CategoryType.LOW:    ACURACIA_LOW,
}


def _load_css() -> None:
    """Injects component CSS on every render (required for @st.fragment compatibility)."""
    inject_theme_css()
    css_path = Path(__file__).parent / "css" / f"{Path(__file__).stem}.css"
    st.markdown(
        f"<style>{css_path.read_text(encoding='utf-8')}</style>",
        unsafe_allow_html=True,
    )


def card_metric_ds(
    title: str,
    value: str,
    icon: str = "",
    enabled_icon: bool = False,
    action: bool = False,
    delta: str = "",
    action_color: str = ACURACIA_HIGH_DELTA,
    tooltip_icon: str = "ℹ️",
    tooltip: str = "",
    key: str = "",
    category_type: CategoryType | None = None,
    size: Literal["sm", "md", "lg"] = "sm",
) -> None:
    """
    Reusable Metric Card component — wrapper customizado de st.metric.

    Args:
        title:         Label do metric (topo do card).
        value:         Valor principal do metric.
        icon:          Emoji/ícone exibido à direita do valor (quando enabled_icon=True).
        enabled_icon:  Se True, exibe o ícone à direita do valor. Padrão: False.
        action:        Se True, exibe o delta. Padrão: False.
        delta:         Texto do delta (usado quando action=True).
        action_color:  Cor do texto do delta. Padrão: "#4CAF50".
        tooltip_icon:  Não utilizado (st.metric usa seu próprio ícone de help). Mantido por compatibilidade.
        tooltip:       Texto do tooltip exibido ao passar o mouse no ícone de help do metric.
        key:           Chave única opcional. Obrigatório quando o mesmo título aparece mais de uma vez na página.
        category_type: Nível de acurácia do card (CategoryType.HIGH/MEDIUM/LOW).
                       Define a cor da borda inferior: HIGH=#6A9B53, MEDIUM=#E8BD00, LOW=#D94A48.
        size:          Tamanho do card. "sm" = padrão; "md" = padding e valor maiores; "lg" = ainda maior.
    """
    _load_css()

    # Chave do container: usa `key` explícito se fornecido, senão deriva do título via hash
    key_hash = key if key else hashlib.md5(title.encode()).hexdigest()[:8]
    container_key = f"card_metric_{key_hash}"

    # Overrides escopados por instância
    overrides: list[str] = []

    if action:
        overrides.append(f"""
[class*="st-key-{container_key}"] [data-testid="stMetricDelta"] {{
    color: {action_color} !important;
}}
""")

    if not enabled_icon:
        # Suprime qualquer ::after definido globalmente (ex: ícones SVG do GESSUPER.css)
        overrides.append(f"""
[class*="st-key-{container_key}"][class*="st-key-{container_key}"][class*="st-key-{container_key}"][class*="st-key-{container_key}"] [data-testid="stMetricValue"]::after {{
    content: none !important;
    display: none !important;
}}
""")
    elif icon:
        # Emoji ou caractere de texto
        overrides.append(f"""
[class*="st-key-{container_key}"][class*="st-key-{container_key}"][class*="st-key-{container_key}"][class*="st-key-{container_key}"] [data-testid="stMetricValue"]::after {{
    content: "{icon}";
    font-size: 1.4rem;
    opacity: 0.2;
    margin-left: 0.4rem;
    vertical-align: middle;
}}
""")

    if size == "md":
        overrides.append(f"""
[class*="st-key-{container_key}"] [data-testid="stMetric"] {{
    padding: 20px 16px !important;
}}
[class*="st-key-{container_key}"] [data-testid="stMetricValue"] {{
    font-size: 2rem !important;
}}
""")

    elif size == "lg":
        overrides.append(f"""
[class*="st-key-{container_key}"] [data-testid="stMetric"] {{
    padding: 28px 20px !important;
}}
[class*="st-key-{container_key}"] [data-testid="stMetricValue"] {{
    font-size: 2.6rem !important;
}}
""")

    if category_type is not None:
        border_color = _CATEGORY_BORDER_COLOR[CategoryType(category_type)]
        overrides.append(f"""
[class*="st-key-{container_key}"][class*="st-key-{container_key}"] [data-testid="stMetric"] {{
    border-bottom: 3px solid {border_color} !important;
}}
""")

    # Sempre injeta o bloco <style> (mesmo vazio) para que todos os cards
    # tenham a mesma quantidade de elementos Streamlit e fiquem alinhados nas colunas
    st.markdown(
        f"<style>{''.join(overrides)}</style>",
        unsafe_allow_html=True,
    )

    with st.container(key=container_key):
        st.metric(
            label=title,
            value=value,
            delta=delta if action else None,
            help=tooltip if tooltip else None,
        )
