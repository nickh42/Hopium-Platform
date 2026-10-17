"""Inline SVG graphics for Hopium. Everything is drawn here so the app needs no image files."""

PINK = "#f06fa8"
PINK_DARK = "#c2417f"
PINK_LIGHT = "#ffd1e3"
BLUE = "#bfe3f7"
NAVY = "#1f3b57"

def _heart_logo() -> str:
    """Poppy bud drawn as a heart: a ruffled petal frill follows the heart outline, with folds converging at the tip."""
    import math

    cx, cy, k = 100.0, 92.0, 5.0

    def pt(t, scale=1.0, wave=0.0, n=0):
        x = 16 * math.sin(t) ** 3
        y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
        f = scale * (1 + wave * math.sin(n * t))
        return cx + k * x * f, cy - k * y * f

    def path(scale, wave=0.0, n=0, steps=360, close=True):
        pts = [pt(2 * math.pi * i / steps, scale, wave, n) for i in range(steps)]
        d = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts)
        return d + ("Z" if close else "")

    frill_outer = path(1.13, 0.035, 28)
    frill_mid = path(1.07, 0.03, 20)
    heart = path(1.0)
    folds = "".join(
        f'<path d="{path(sc)}" fill="none" stroke="{PINK_DARK}" stroke-width="2" opacity="{op}"/>'
        for sc, op in ((0.8, 0.55), (0.6, 0.4), (0.4, 0.3))
    )
    bottom = pt(math.pi, 1.0)
    top = pt(0.0, 1.0)
    return f"""
<svg viewBox="0 0 200 240" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Hopium logo">
  <path d="M{bottom[0]:.0f} {bottom[1]+4:.0f} C96 205 106 220 100 236" stroke="#3f9b6a" stroke-width="7" fill="none" stroke-linecap="round"/>
  <path d="{frill_outer}" fill="#e0508f" stroke="{PINK_DARK}" stroke-width="2.5" stroke-linejoin="round"/>
  <path d="{frill_mid}" fill="#ee6aa5" stroke="{PINK_DARK}" stroke-width="2" stroke-linejoin="round"/>
  <path d="{heart}" fill="{PINK}" stroke="{PINK_DARK}" stroke-width="2.5" stroke-linejoin="round"/>
  {folds}
  <path d="M{top[0]:.0f} {top[1]:.0f} Q{top[0]+4:.0f} {(top[1]+bottom[1])/2:.0f} {bottom[0]:.0f} {bottom[1]:.0f}" stroke="{PINK_DARK}" stroke-width="2" fill="none" opacity=".5"/>
  <path d="M52 62 Q60 48 76 50" stroke="#fff" stroke-width="5" fill="none" stroke-linecap="round" opacity=".55"/>
  <path d="M100 {bottom[1]+4:.0f} C78 {bottom[1]+4:.0f} 70 {bottom[1]+22:.0f} 64 {bottom[1]+20:.0f} C66 {bottom[1]+4:.0f} 84 {bottom[1]-2:.0f} 100 {bottom[1]+4:.0f}Z" fill="#4fb07c"/>
  <path d="M100 {bottom[1]+4:.0f} C122 {bottom[1]+4:.0f} 130 {bottom[1]+22:.0f} 136 {bottom[1]+20:.0f} C134 {bottom[1]+4:.0f} 116 {bottom[1]-2:.0f} 100 {bottom[1]+4:.0f}Z" fill="#4fb07c"/>
</svg>
"""


LOGO = _heart_logo()


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

# Realistic, labelled illustration of a 4 mg naloxone nasal spray device (shaded, with label art).
NARCAN_DEVICE = """
<svg viewBox="0 0 560 330" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Narcan nasal spray device diagram">
  <defs>
    <linearGradient id="nb" x1="0" x2="1"><stop offset="0" stop-color="#cfd8df"/><stop offset=".35" stop-color="#ffffff"/><stop offset=".7" stop-color="#f1f5f8"/><stop offset="1" stop-color="#b9c5ce"/></linearGradient>
    <linearGradient id="nz" x1="0" x2="1"><stop offset="0" stop-color="#c3ced6"/><stop offset=".4" stop-color="#fbfdff"/><stop offset="1" stop-color="#aebbc5"/></linearGradient>
    <linearGradient id="nl" x1="0" x2="1"><stop offset="0" stop-color="#075e86"/><stop offset=".45" stop-color="#1494c9"/><stop offset="1" stop-color="#075e86"/></linearGradient>
    <linearGradient id="np" x1="0" x2="1"><stop offset="0" stop-color="#b7c3cc"/><stop offset=".4" stop-color="#eef3f6"/><stop offset="1" stop-color="#a3b1bc"/></linearGradient>
    <radialGradient id="sh"><stop offset="0" stop-color="#000" stop-opacity=".28"/><stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient>
  </defs>
  <ellipse cx="170" cy="312" rx="86" ry="10" fill="url(#sh)"/>
  <!-- nozzle -->
  <path d="M154 96 V44 Q154 14 170 14 Q186 14 186 44 V96Z" fill="url(#nz)" stroke="#8fa0ac" stroke-width="2"/>
  <ellipse cx="170" cy="22" rx="4" ry="3" fill="#6f808c"/>
  <!-- body -->
  <path d="M132 96 H208 Q222 96 222 112 V262 Q222 276 208 276 H132 Q118 276 118 262 V112 Q118 96 132 96Z" fill="url(#nb)" stroke="#8fa0ac" stroke-width="2"/>
  <!-- finger flanges -->
  <rect x="96" y="112" width="148" height="16" rx="8" fill="url(#nb)" stroke="#8fa0ac" stroke-width="2"/>
  <!-- label -->
  <rect x="130" y="148" width="80" height="104" rx="6" fill="url(#nl)"/>
  <text x="170" y="178" font-size="14" font-weight="800" text-anchor="middle" fill="#fff" font-family="Arial, sans-serif" letter-spacing="1">NARCAN</text>
  <text x="170" y="196" font-size="9" text-anchor="middle" fill="#dff3fb" font-family="Arial, sans-serif">NASAL SPRAY</text>
  <text x="170" y="236" font-size="22" font-weight="800" text-anchor="middle" fill="#fff" font-family="Arial, sans-serif">4 mg</text>
  <path d="M138 156 H202" stroke="#fff" stroke-opacity=".5"/>
  <!-- plunger -->
  <path d="M146 276 V298 Q146 306 154 306 H186 Q194 306 194 298 V276Z" fill="url(#np)" stroke="#8fa0ac" stroke-width="2"/>
  <path d="M154 286 H186 M154 292 H186" stroke="#8fa0ac" stroke-width="1.5"/>
  <!-- callouts -->
  <g font-family="Arial, sans-serif" font-size="14" fill="#1f3b57">
    <line x1="186" y1="30" x2="300" y2="30" stroke="#1f3b57"/><circle cx="186" cy="30" r="3" fill="#1f3b57"/>
    <text x="308" y="26" font-weight="700">Nozzle</text><text x="308" y="44">Goes in one nostril</text>
    <line x1="244" y1="120" x2="300" y2="120" stroke="#1f3b57"/><circle cx="244" cy="120" r="3" fill="#1f3b57"/>
    <text x="308" y="116" font-weight="700">Finger flanges</text><text x="308" y="134">First and middle finger here</text>
    <line x1="210" y1="200" x2="300" y2="200" stroke="#1f3b57"/><circle cx="210" cy="200" r="3" fill="#1f3b57"/>
    <text x="308" y="196" font-weight="700">One dose per device</text><text x="308" y="214">Do not test or prime</text>
    <line x1="194" y1="296" x2="300" y2="296" stroke="#1f3b57"/><circle cx="194" cy="296" r="3" fill="#1f3b57"/>
    <text x="308" y="292" font-weight="700">Plunger</text><text x="308" y="310">Thumb pushes firmly to the end</text>
  </g>
</svg>
"""
