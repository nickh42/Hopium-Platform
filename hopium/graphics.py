"""Inline SVG graphics for Hopium. Everything is drawn here so the app needs no image files."""

PINK = "#f06fa8"
PINK_DARK = "#c2417f"
PINK_LIGHT = "#ffd1e3"
BLUE = "#bfe3f7"
NAVY = "#1f3b57"

LOGO = f"""
<svg viewBox="0 0 200 230" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Hopium logo">
  <path d="M100 160 C98 185 104 205 100 225" stroke="#3f9b6a" stroke-width="7" fill="none" stroke-linecap="round"/>
  <path d="M100 168 C78 150 62 156 56 138 C80 138 96 148 100 168Z" fill="#4fb07c"/>
  <path d="M100 168 C122 150 138 156 144 138 C120 138 104 148 100 168Z" fill="#4fb07c"/>
  <path d="M100 18 C152 18 172 70 166 112 C160 152 130 168 100 168 C70 168 40 152 34 112 C28 70 48 18 100 18Z"
        fill="{PINK}" stroke="{PINK_DARK}" stroke-width="4"/>
  <path d="M100 18 C84 56 84 120 100 168" stroke="{PINK_DARK}" stroke-width="2.5" fill="none" opacity=".45"/>
  <path d="M100 18 C116 56 116 120 100 168" stroke="{PINK_DARK}" stroke-width="2.5" fill="none" opacity=".45"/>
  <path d="M100 132 C66 108 72 76 90 76 C96 76 100 81 100 87 C100 81 104 76 110 76 C128 76 134 108 100 132Z"
        fill="{PINK_LIGHT}" stroke="{PINK_DARK}" stroke-width="3"/>
</svg>
"""


def _svg(inner: str, view: str = "0 0 120 120") -> str:
    return f'<svg viewBox="{view}" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">{inner}</svg>'


ICONS = {
    # Effects
    "pain": _svg(
        f'<circle cx="60" cy="60" r="44" fill="{BLUE}"/>'
        f'<path d="M60 88 C30 66 36 38 52 38 C57 38 60 42 60 47 C60 42 63 38 68 38 C84 38 90 66 60 88Z" fill="{PINK}"/>'
    ),
    "drowsy": _svg(
        f'<circle cx="60" cy="60" r="44" fill="{BLUE}"/>'
        f'<path d="M40 56 Q50 64 60 56" stroke="{NAVY}" stroke-width="4" fill="none" stroke-linecap="round"/>'
        f'<path d="M64 56 Q74 64 84 56" stroke="{NAVY}" stroke-width="4" fill="none" stroke-linecap="round"/>'
        f'<text x="76" y="40" font-size="20" font-weight="700" fill="{NAVY}">z</text>'
        f'<text x="88" y="28" font-size="14" font-weight="700" fill="{NAVY}">z</text>'
    ),
    "breathing": _svg(
        f'<path d="M58 20 V70" stroke="{NAVY}" stroke-width="5" stroke-linecap="round"/>'
        f'<path d="M54 36 C30 36 18 70 20 92 C22 102 40 102 50 90 C56 82 56 60 54 36Z" fill="{PINK}"/>'
        f'<path d="M62 36 C86 36 98 70 96 92 C94 102 76 102 66 90 C60 82 60 60 62 36Z" fill="{PINK}"/>'
    ),
    "nausea": _svg(
        f'<circle cx="60" cy="60" r="44" fill="{BLUE}"/>'
        f'<circle cx="46" cy="52" r="4" fill="{NAVY}"/><circle cx="74" cy="52" r="4" fill="{NAVY}"/>'
        f'<path d="M44 80 Q52 72 60 80 T76 80" stroke="{NAVY}" stroke-width="4" fill="none" stroke-linecap="round"/>'
    ),
    "dependence": _svg(
        f'<rect x="18" y="46" width="84" height="28" rx="14" fill="{PINK}" transform="rotate(-30 60 60)"/>'
        f'<rect x="18" y="46" width="42" height="28" rx="14" fill="{PINK_LIGHT}" transform="rotate(-30 60 60)"/>'
    ),
    # Signs
    "pupils": _svg(
        f'<path d="M10 60 Q60 14 110 60 Q60 106 10 60Z" fill="#fff" stroke="{NAVY}" stroke-width="4"/>'
        f'<circle cx="60" cy="60" r="20" fill="#8a6a4f"/><circle cx="60" cy="60" r="4" fill="#000"/>'
    ),
    "blue_lips": _svg(
        '<path d="M16 62 Q38 38 60 52 Q82 38 104 62 Q82 92 60 90 Q38 92 16 62Z" fill="#5b6fd6"/>'
        '<path d="M16 62 Q60 74 104 62" stroke="#2c3a8f" stroke-width="3" fill="none"/>'
    ),
    "slow_breath": _svg(
        f'<path d="M8 60 H34 L42 40 L54 80 L62 60 H112" stroke="{PINK_DARK}" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round" opacity=".35"/>'
        f'<path d="M8 60 H112" stroke="{PINK_DARK}" stroke-width="4" stroke-dasharray="8 8" fill="none"/>'
    ),
    "unresponsive": _svg(
        f'<circle cx="26" cy="64" r="14" fill="{PINK_LIGHT}" stroke="{NAVY}" stroke-width="3"/>'
        f'<rect x="40" y="56" width="62" height="16" rx="8" fill="{BLUE}" stroke="{NAVY}" stroke-width="3"/>'
        f'<path d="M20 62 l4 3 M30 62 l-4 3" stroke="{NAVY}" stroke-width="2.5" stroke-linecap="round"/>'
        f'<path d="M12 90 H108" stroke="{NAVY}" stroke-width="3" stroke-linecap="round" opacity=".4"/>'
    ),
    "gurgle": _svg(
        f'<path d="M20 30 H100 Q108 30 108 38 V70 Q108 78 100 78 H56 L36 96 V78 H20 Q12 78 12 70 V38 Q12 30 20 30Z" fill="{BLUE}" stroke="{NAVY}" stroke-width="3"/>'
        f'<path d="M30 54 Q38 44 46 54 T62 54 T78 54 T94 54" stroke="{NAVY}" stroke-width="3.5" fill="none" stroke-linecap="round"/>'
    ),
    "cold": _svg(
        f'<path d="M60 14 C60 14 30 52 30 74 C30 92 43 104 60 104 C77 104 90 92 90 74 C90 52 60 14 60 14Z" fill="{BLUE}" stroke="{NAVY}" stroke-width="3"/>'
        f'<path d="M48 78 Q50 90 60 92" stroke="#fff" stroke-width="4" fill="none" stroke-linecap="round"/>'
    ),
    # Helping steps
    "wake": _svg(
        f'<circle cx="60" cy="40" r="16" fill="{PINK_LIGHT}" stroke="{NAVY}" stroke-width="3"/>'
        f'<path d="M30 104 Q30 66 60 66 Q90 66 90 104Z" fill="{BLUE}" stroke="{NAVY}" stroke-width="3"/>'
        f'<path d="M96 34 l10 -8 M100 46 h12 M96 58 l10 8" stroke="{PINK_DARK}" stroke-width="4" stroke-linecap="round"/>'
    ),
    "call": _svg(
        f'<rect x="34" y="10" width="52" height="100" rx="10" fill="{NAVY}"/>'
        f'<rect x="40" y="22" width="40" height="64" rx="3" fill="#fff"/>'
        f'<text x="60" y="62" font-size="20" font-weight="800" text-anchor="middle" fill="#d62828">911</text>'
        f'<circle cx="60" cy="98" r="5" fill="#fff"/>'
    ),
    "spray": _svg(
        f'<rect x="36" y="46" width="48" height="52" rx="8" fill="#fff" stroke="{NAVY}" stroke-width="3"/>'
        f'<rect x="44" y="26" width="32" height="24" rx="4" fill="{BLUE}" stroke="{NAVY}" stroke-width="3"/>'
        f'<rect x="54" y="8" width="12" height="20" rx="4" fill="{PINK}" stroke="{NAVY}" stroke-width="3"/>'
        f'<rect x="46" y="98" width="28" height="10" rx="3" fill="{PINK}" stroke="{NAVY}" stroke-width="3"/>'
    ),
    "side": _svg(
        f'<circle cx="26" cy="62" r="13" fill="{PINK_LIGHT}" stroke="{NAVY}" stroke-width="3"/>'
        f'<path d="M38 66 Q70 40 102 60 L102 78 Q70 84 38 80Z" fill="{BLUE}" stroke="{NAVY}" stroke-width="3"/>'
        f'<path d="M62 56 L58 38 M84 54 L90 38" stroke="{NAVY}" stroke-width="3" stroke-linecap="round"/>'
        f'<path d="M12 94 H108" stroke="{NAVY}" stroke-width="3" stroke-linecap="round" opacity=".4"/>'
    ),
    "stay": _svg(
        f'<circle cx="60" cy="60" r="44" fill="{BLUE}"/>'
        f'<path d="M60 36 V62 L78 74" stroke="{NAVY}" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
    ),
    # Narcan how-to
    "n_peel": _svg(
        f'<rect x="30" y="34" width="60" height="62" rx="6" fill="#fff" stroke="{NAVY}" stroke-width="3"/>'
        f'<path d="M30 34 L60 14 L90 34" fill="{BLUE}" stroke="{NAVY}" stroke-width="3" stroke-linejoin="round"/>'
        f'<path d="M44 66 H76" stroke="{PINK_DARK}" stroke-width="4" stroke-linecap="round"/>'
    ),
    "n_hold": _svg(
        f'<rect x="38" y="30" width="44" height="64" rx="10" fill="{BLUE}" stroke="{NAVY}" stroke-width="3"/>'
        f'<rect x="52" y="8" width="16" height="24" rx="5" fill="{PINK}" stroke="{NAVY}" stroke-width="3"/>'
        f'<circle cx="60" cy="108" r="9" fill="{PINK_DARK}"/>'
        f'<path d="M28 60 H38 M82 60 H92" stroke="{NAVY}" stroke-width="5" stroke-linecap="round"/>'
    ),
    "n_insert": _svg(
        f'<circle cx="40" cy="62" r="26" fill="{PINK_LIGHT}" stroke="{NAVY}" stroke-width="3"/>'
        f'<path d="M52 68 Q62 74 72 66" stroke="{NAVY}" stroke-width="3" fill="none" stroke-linecap="round"/>'
        f'<rect x="60" y="22" width="14" height="34" rx="5" fill="{PINK}" stroke="{NAVY}" stroke-width="3" transform="rotate(35 67 39)"/>'
        f'<rect x="76" y="50" width="26" height="14" rx="4" fill="{BLUE}" stroke="{NAVY}" stroke-width="3" transform="rotate(35 89 57)"/>'
    ),
    "n_press": _svg(
        f'<rect x="40" y="40" width="40" height="64" rx="10" fill="{BLUE}" stroke="{NAVY}" stroke-width="3"/>'
        f'<rect x="52" y="22" width="16" height="22" rx="5" fill="{PINK}" stroke="{NAVY}" stroke-width="3"/>'
        f'<path d="M60 4 V16 M52 10 L60 18 L68 10" stroke="{PINK_DARK}" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
    ),
    "n_repeat": _svg(
        f'<circle cx="60" cy="60" r="44" fill="{BLUE}"/>'
        f'<path d="M36 60 A24 24 0 0 1 80 46 M84 60 A24 24 0 0 1 40 74" stroke="{NAVY}" stroke-width="6" fill="none" stroke-linecap="round"/>'
        f'<path d="M82 34 V50 H66 M38 86 V70 H54" stroke="{NAVY}" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
    ),
}

# Labelled diagram of the Narcan nasal spray device.
NARCAN_DEVICE = f"""
<svg viewBox="0 0 360 220" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Narcan nasal spray diagram">
  <rect x="120" y="70" width="90" height="120" rx="14" fill="{BLUE}" stroke="{NAVY}" stroke-width="3"/>
  <rect x="142" y="20" width="46" height="54" rx="10" fill="#fff" stroke="{NAVY}" stroke-width="3"/>
  <rect x="155" y="2" width="20" height="22" rx="7" fill="{PINK}" stroke="{NAVY}" stroke-width="3"/>
  <rect x="136" y="190" width="58" height="20" rx="6" fill="{PINK}" stroke="{NAVY}" stroke-width="3"/>
  <text x="165" y="205" font-size="11" font-weight="700" text-anchor="middle" fill="#fff">PLUNGER</text>
  <path d="M165 112 L165 170" stroke="{NAVY}" stroke-width="2" stroke-dasharray="4 4"/>
  <line x1="175" y1="12" x2="262" y2="22" stroke="{NAVY}" stroke-width="1.5"/>
  <text x="266" y="26" font-size="13" fill="{NAVY}">Nozzle: into one nostril</text>
  <line x1="210" y1="100" x2="262" y2="94" stroke="{NAVY}" stroke-width="1.5"/>
  <text x="266" y="98" font-size="13" fill="{NAVY}">Two fingers either side of</text>
  <text x="266" y="114" font-size="13" fill="{NAVY}">the nozzle</text>
  <line x1="194" y1="200" x2="262" y2="200" stroke="{NAVY}" stroke-width="1.5"/>
  <text x="266" y="204" font-size="13" fill="{NAVY}">Thumb presses plunger</text>
</svg>
"""
