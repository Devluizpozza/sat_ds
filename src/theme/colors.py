# =============================================================================
# SAT Design System — Color Tokens
# Fonte única de verdade para todas as cores da aplicação.
# Uso em Python: from theme.colors import ACURACIA_HIGH
# Uso em CSS:    var(--color-high)  (após injeção de CSS_VARIABLES)
# =============================================================================

# ------------------------------------------------------------------------------
# Acurácia: ALTA (High Confidence) — Verde
# ------------------------------------------------------------------------------
ACURACIA_HIGH           = "#6A9B53"                  # ícones, borda inferior card, seta do accordeon
ACURACIA_HIGH_EMPHASIS  = "#375C38"                  # fundo e borda do botão principal
ACURACIA_HIGH_HOVER     = "#2d4d2e"                  # hover do botão principal
ACURACIA_HIGH_BORDER    = "#3B5A2D"                  # borda do nivel_card ALTA
ACURACIA_HIGH_BG        = "rgba(106, 155, 83, 0.09)" # fundo do nivel_card ALTA
ACURACIA_HIGH_DELTA     = "#4CAF50"                  # cor do delta/progress ALTA

# ------------------------------------------------------------------------------
# Acurácia: MÉDIA (Medium Confidence) — Amarelo
# ------------------------------------------------------------------------------
ACURACIA_MEDIUM         = "#E8BD00"                  # borda inferior card MÉDIA
ACURACIA_MEDIUM_BORDER  = "#A08200"                  # borda do nivel_card MÉDIA
ACURACIA_MEDIUM_BG      = "rgba(232, 189, 0, 0.09)"  # fundo do nivel_card MÉDIA
ACURACIA_MEDIUM_DELTA   = "#FF9800"                  # cor do delta/progress MÉDIA

# ------------------------------------------------------------------------------
# Acurácia: BAIXA (Low Confidence) — Vermelho
# ------------------------------------------------------------------------------
ACURACIA_LOW            = "#D94A48"                  # borda inferior card BAIXA
ACURACIA_LOW_BORDER     = "#9A3634"                  # borda do nivel_card BAIXA
ACURACIA_LOW_BG         = "rgba(217, 74, 72, 0.09)"  # fundo do nivel_card BAIXA
ACURACIA_LOW_DELTA      = "#f44336"                  # cor do delta/progress BAIXA

# ------------------------------------------------------------------------------
# Informação — Azul
# ------------------------------------------------------------------------------
INFO                    = "#3A87AD"                  # texto da info bar
INFO_BG                 = "#D9EDF7"                  # fundo da info bar
INFO_BORDER             = "#BCE8F1"                  # borda da info bar

# ------------------------------------------------------------------------------
# Escala de texto (do mais escuro ao mais claro)
# ------------------------------------------------------------------------------
TEXT_PRIMARY            = "#18181B"                  # valores principais (metric value)
TEXT_BODY               = "#333"                     # corpo de texto, listas
TEXT_SECONDARY          = "#727272"                  # títulos de seção, labels de abas
TEXT_LABEL              = "#71717A"                  # labels de metric cards
TEXT_MUTED              = "#777"                     # títulos de accordeon, captions
TEXT_SUBTLE             = "#ADADAD"                  # bordas de ícone, círculo da seta

# ------------------------------------------------------------------------------
# Bordas
# ------------------------------------------------------------------------------
BORDER                  = "#DDD"                     # borda padrão (panels, accordeons)
BORDER_INPUT            = "#CCC"                     # campos de input
BORDER_CARD             = "#E4E4E4"                  # cards de metric

# ------------------------------------------------------------------------------
# Fundos
# ------------------------------------------------------------------------------
BG_WHITE                = "#FFF"                     # fundo branco
BG_LIGHT                = "#F5F5F5"                  # fundo sutil (círculo da seta, hover)

# ------------------------------------------------------------------------------
# Sombra
# ------------------------------------------------------------------------------
SHADOW                  = "rgba(0, 0, 0, 0.05)"      # box-shadow padrão dos cards

# ==============================================================================
# CSS Custom Properties
# Injeta todas as cores como variáveis CSS globais no :root.
# Chamar via:  st.markdown(f"<style>{CSS_VARIABLES}</style>", unsafe_allow_html=True)
# ==============================================================================

CSS_VARIABLES = f"""
:root {{
    /* Acurácia: ALTA */
    --color-high:           {ACURACIA_HIGH};
    --color-high-emphasis:  {ACURACIA_HIGH_EMPHASIS};
    --color-high-hover:     {ACURACIA_HIGH_HOVER};
    --color-high-border:    {ACURACIA_HIGH_BORDER};
    --color-high-bg:        {ACURACIA_HIGH_BG};
    --color-high-delta:     {ACURACIA_HIGH_DELTA};

    /* Acurácia: MÉDIA */
    --color-medium:         {ACURACIA_MEDIUM};
    --color-medium-border:  {ACURACIA_MEDIUM_BORDER};
    --color-medium-bg:      {ACURACIA_MEDIUM_BG};
    --color-medium-delta:   {ACURACIA_MEDIUM_DELTA};

    /* Acurácia: BAIXA */
    --color-low:            {ACURACIA_LOW};
    --color-low-border:     {ACURACIA_LOW_BORDER};
    --color-low-bg:         {ACURACIA_LOW_BG};
    --color-low-delta:      {ACURACIA_LOW_DELTA};

    /* Informação */
    --color-info:           {INFO};
    --color-info-bg:        {INFO_BG};
    --color-info-border:    {INFO_BORDER};

    /* Escala de texto */
    --color-text-primary:   {TEXT_PRIMARY};
    --color-text-body:      {TEXT_BODY};
    --color-text-secondary: {TEXT_SECONDARY};
    --color-text-label:     {TEXT_LABEL};
    --color-text-muted:     {TEXT_MUTED};
    --color-text-subtle:    {TEXT_SUBTLE};

    /* Bordas */
    --color-border:         {BORDER};
    --color-border-input:   {BORDER_INPUT};
    --color-border-card:    {BORDER_CARD};

    /* Fundos */
    --color-bg-white:       {BG_WHITE};
    --color-bg-light:       {BG_LIGHT};

    /* Sombra */
    --color-shadow:         {SHADOW};
}}
"""
