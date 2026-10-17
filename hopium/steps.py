"""Shaded, labelled scene illustrations for each Narcan step. Pure inline SVG, no image files."""

W, H = 360, 250

DEFS = """
<defs>
  <linearGradient id="sg-skin" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f7d6bd"/><stop offset="1" stop-color="#dba37c"/></linearGradient>
  <linearGradient id="sg-skinv" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f3caa9"/><stop offset="1" stop-color="#d79a72"/></linearGradient>
  <linearGradient id="sg-hair" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#6b4630"/><stop offset="1" stop-color="#3a2416"/></linearGradient>
  <linearGradient id="sg-body" x1="0" x2="1"><stop offset="0" stop-color="#cfd8df"/><stop offset=".35" stop-color="#ffffff"/><stop offset=".7" stop-color="#f1f5f8"/><stop offset="1" stop-color="#b9c5ce"/></linearGradient>
  <linearGradient id="sg-label" x1="0" x2="1"><stop offset="0" stop-color="#075e86"/><stop offset=".45" stop-color="#1494c9"/><stop offset="1" stop-color="#075e86"/></linearGradient>
  <linearGradient id="sg-shirt" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7fb2dc"/><stop offset="1" stop-color="#4f86b3"/></linearGradient>
  <linearGradient id="sg-pack" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#dbe6ee"/></linearGradient>
  <radialGradient id="sg-shadow"><stop offset="0" stop-color="#000" stop-opacity=".28"/><stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient>
</defs>
"""

LABEL = 'font-family="Arial, sans-serif" font-size="13" font-weight="700" fill="#1f3b57"'


def _wrap(inner: str, label: str, caption: str) -> str:
    return (
        f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{label}">'
        f'{DEFS}<rect width="{W}" height="{H}" fill="#eaf6fd"/>{inner}'
        f'<text x="{W/2}" y="{H-10}" text-anchor="middle" {LABEL}>{caption}</text></svg>'
    )


def _device(x, y, rot=0, s=1.0, pressed=False) -> str:
    """The nasal spray device. Local origin is the nozzle tip, pointing up; body runs downward."""
    plunger_y = 196 if pressed else 214
    return f"""
<g transform="translate({x} {y}) rotate({rot}) scale({s})">
  <rect x="-11" y="0" width="22" height="72" rx="10" fill="url(#sg-body)" stroke="#8fa0ac" stroke-width="2"/>
  <ellipse cx="0" cy="6" rx="3.5" ry="2.5" fill="#6f808c"/>
  <rect x="-34" y="64" width="68" height="150" rx="14" fill="url(#sg-body)" stroke="#8fa0ac" stroke-width="2"/>
  <rect x="-50" y="80" width="100" height="14" rx="7" fill="url(#sg-body)" stroke="#8fa0ac" stroke-width="2"/>
  <rect x="-26" y="112" width="52" height="80" rx="5" fill="url(#sg-label)"/>
  <text x="0" y="136" font-size="11" font-weight="800" text-anchor="middle" fill="#fff" font-family="Arial, sans-serif" letter-spacing="1">NARCAN</text>
  <text x="0" y="172" font-size="16" font-weight="800" text-anchor="middle" fill="#fff" font-family="Arial, sans-serif">4 mg</text>
  <rect x="-18" y="{plunger_y}" width="36" height="{240 - plunger_y}" rx="6" fill="url(#sg-body)" stroke="#8fa0ac" stroke-width="2"/>
</g>"""


def _head(transform: str) -> str:
    """Side profile of a head. Drawn facing right and upright; the caller rotates it onto its back."""
    return f"""
<g transform="{transform}">
  <path d="M-8 150 L-8 250 L120 250 L120 150Z" fill="url(#sg-skinv)"/>
  <path d="M-30 20 C-84 20 -108 58 -108 100 C-108 112 -116 124 -122 136 C-128 146 -136 152 -134 160 C-130 168 -120 168 -112 168 C-110 176 -114 182 -110 188 C-112 194 -108 198 -108 202 C-110 210 -106 216 -100 222 C-96 236 -88 246 -70 252 L-10 252 L-10 150 Z" fill="url(#sg-skin)" stroke="#a96f4b" stroke-width="2"/>
  <path d="M-30 20 C-84 20 -108 58 -108 100 C-100 80 -84 52 -50 46 C-20 40 20 60 24 110 C26 60 10 20 -30 20Z" fill="url(#sg-hair)"/>
  <path d="M-110 168 L-134 160" stroke="#a96f4b" stroke-width="2"/>
  <ellipse cx="-118" cy="171" rx="5" ry="3" fill="#8e5638"/>
  <path d="M-96 98 Q-88 104 -80 98" stroke="#3a2416" stroke-width="3" fill="none" stroke-linecap="round"/>
  <path d="M-102 86 Q-90 80 -78 86" stroke="#4b2f1e" stroke-width="3" fill="none" stroke-linecap="round"/>
  <path d="M-114 196 Q-108 199 -104 196" stroke="#8e4a3a" stroke-width="2.5" fill="none" stroke-linecap="round"/>
  <ellipse cx="-34" cy="128" rx="14" ry="20" fill="#e8b690" stroke="#a96f4b" stroke-width="2"/>
</g>"""


def _lying_person(tilt=-105, hx=118, hy=150) -> str:
    """Person on their back, head at left. tilt rotates the head back (more negative = further)."""
    return f"""
<ellipse cx="220" cy="214" rx="150" ry="9" fill="url(#sg-shadow)"/>
<rect x="150" y="150" width="200" height="56" rx="26" fill="url(#sg-shirt)" stroke="#2f5a80" stroke-width="2"/>
<rect x="168" y="196" width="190" height="16" rx="8" fill="#41546a"/>
{_head(f"translate({hx} {hy}) rotate({tilt}) scale(-0.62 0.62)")}
"""


def step1() -> str:
    pack = """
<g transform="translate(70 40) rotate(-6 100 80)">
  <rect x="0" y="20" width="220" height="130" rx="10" fill="url(#sg-pack)" stroke="#8fa0ac" stroke-width="2"/>
  <rect x="14" y="34" width="192" height="102" rx="8" fill="#eef3f7" stroke="#b6c3cd"/>
  <path d="M30 120 L190 120" stroke="#cdd8e0" stroke-width="2"/>
  <g transform="translate(110 40) rotate(90) scale(0.38)">
    <rect x="-11" y="0" width="22" height="72" rx="10" fill="url(#sg-body)" stroke="#8fa0ac" stroke-width="3"/>
    <rect x="-34" y="64" width="68" height="150" rx="14" fill="url(#sg-body)" stroke="#8fa0ac" stroke-width="3"/>
    <rect x="-50" y="80" width="100" height="14" rx="7" fill="url(#sg-body)" stroke="#8fa0ac" stroke-width="3"/>
    <rect x="-26" y="112" width="52" height="80" rx="5" fill="url(#sg-label)"/>
  </g>
  <path d="M0 20 H220 V50 L150 20Z" fill="#fff" opacity=".0"/>
  <path d="M220 20 L186 20 Q200 40 220 50Z" fill="#f4f8fb" stroke="#8fa0ac" stroke-width="2"/>
</g>
<path d="M300 56 C320 36 336 54 322 74" stroke="#c2417f" stroke-width="3" fill="none" stroke-linecap="round" stroke-dasharray="1 7"/>
<path d="M318 60 L322 76 L306 72" stroke="#c2417f" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<text x="266" y="118" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#1f3b57">Peel the</text>
<text x="266" y="132" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#1f3b57">backing tab</text>
"""
    return _wrap(pack, "Peeling open the Narcan package", "1. Peel back the package")


def step2() -> str:
    hand = """
<g>
  <ellipse cx="180" cy="236" rx="70" ry="8" fill="url(#sg-shadow)"/>
  <path d="M120 150 C110 190 124 238 180 242 C236 238 250 190 240 150 Z" fill="url(#sg-skinv)" stroke="#a96f4b" stroke-width="2"/>
</g>"""
    dev = _device(180, 22, 0, 0.78)
    fingers = """
<g stroke="#a96f4b" stroke-width="2">
  <rect x="124" y="64" width="22" height="104" rx="11" fill="url(#sg-skin)"/>
  <rect x="214" y="64" width="22" height="104" rx="11" fill="url(#sg-skin)"/>
  <path d="M130 74 Q135 70 140 74 M220 74 Q225 70 230 74" stroke="#c08560" fill="none"/>
  <ellipse cx="180" cy="214" rx="26" ry="14" fill="url(#sg-skin)"/>
</g>"""
    lbl = """
<g font-family="Arial,sans-serif" font-size="12" fill="#1f3b57">
  <text x="30" y="84" font-weight="700">Two fingers</text><text x="30" y="98">either side of</text><text x="30" y="112">the nozzle</text>
  <path d="M92 90 H118" stroke="#1f3b57"/>
  <text x="256" y="206" font-weight="700">Thumb on the</text><text x="256" y="220">plunger</text>
  <path d="M254 212 H210" stroke="#1f3b57"/>
</g>"""
    return _wrap(hand + dev + fingers + lbl, "Holding the nasal spray correctly", "2. Hold it with a steady grip")


def step3() -> str:
    return _wrap(
        _lying_person()
        + '<path d="M96 196 C96 214 120 222 140 214" stroke="#a96f4b" stroke-width="2" fill="url(#sg-skin)"/>'
        + '<ellipse cx="118" cy="206" rx="26" ry="11" fill="url(#sg-skin)" stroke="#a96f4b" stroke-width="2"/>'
        + f'<g font-family="Arial,sans-serif" font-size="12" fill="#1f3b57">'
        f'<text x="20" y="48" font-weight="700">Head tilted back</text>'
        f'<text x="20" y="62">Support the neck</text>'
        f'<text x="200" y="120" font-weight="700">Lay them flat</text><text x="200" y="134">on their back</text></g>',
        "Person lying on their back with head tilted back",
        "3. Lay them on their back, tilt head back",
    )


def step4() -> str:
    # Large head close up, device entering the nostril from below the nose.
    head = _head("translate(190 40) rotate(-90) scale(-0.95 0.95)")
    dev = _device(60, 100, 90, 0.52)
    return _wrap(
        head + dev
        + '<g stroke="#a96f4b" stroke-width="2"><rect x="30" y="90" width="52" height="16" rx="8" fill="url(#sg-skin)" transform="rotate(0)"/></g>'
        + '<text x="220" y="70" font-family="Arial,sans-serif" font-size="12" font-weight="700" fill="#1f3b57">Nozzle in one nostril</text>'
        + '<text x="220" y="86" font-family="Arial,sans-serif" font-size="12" fill="#1f3b57">until fingers touch the nose</text>',
        "Inserting the nozzle into one nostril",
        "4. Insert the nozzle into one nostril",
    )


def step5() -> str:
    head = _head("translate(190 40) rotate(-90) scale(-0.95 0.95)")
    dev = _device(60, 100, 90, 0.52, pressed=True)
    arrow = '<path d="M20 100 H4 M12 92 L4 100 L12 108" stroke="#c2417f" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
    return _wrap(
        head + dev + arrow
        + '<text x="220" y="70" font-family="Arial,sans-serif" font-size="12" font-weight="700" fill="#1f3b57">Press the plunger</text>'
        + '<text x="220" y="86" font-family="Arial,sans-serif" font-size="12" fill="#1f3b57">firmly all the way in</text>',
        "Pressing the plunger firmly",
        "5. Press the plunger firmly, then remove",
    )


def step6() -> str:
    body = """
<ellipse cx="190" cy="214" rx="150" ry="9" fill="url(#sg-shadow)"/>
<path d="M120 170 C150 130 250 126 300 150 L330 178 C300 200 190 208 130 194Z" fill="url(#sg-shirt)" stroke="#2f5a80" stroke-width="2"/>
<path d="M300 150 C330 150 352 176 346 200 L330 200 L320 180 Z" fill="#41546a" stroke="#2f5a80" stroke-width="2"/>
<path d="M250 188 C270 150 300 140 316 120 L330 126 C316 156 292 176 276 202Z" fill="#41546a" stroke="#2f5a80" stroke-width="2"/>
<ellipse cx="108" cy="168" rx="38" ry="34" fill="url(#sg-skin)" stroke="#a96f4b" stroke-width="2"/>
<path d="M76 160 C76 130 120 126 140 148 C124 142 100 144 90 164Z" fill="url(#sg-hair)"/>
<path d="M92 170 Q100 175 108 170" stroke="#3a2416" stroke-width="3" fill="none" stroke-linecap="round"/>
<path d="M128 196 C150 178 190 150 230 150" stroke="#a96f4b" stroke-width="22" fill="none" stroke-linecap="round" opacity=".0"/>
<path d="M130 180 C170 150 210 138 244 142" stroke="url(#sg-skin)" stroke-width="22" fill="none" stroke-linecap="round"/>
<g font-family="Arial,sans-serif" font-size="12" fill="#1f3b57"><text x="20" y="44" font-weight="700">On their side</text><text x="20" y="58">Top knee bent, head</text><text x="20" y="72">resting on the arm</text></g>
"""
    return _wrap(body, "Person in the recovery position", "6. Turn them onto their side")


def step7() -> str:
    clock = """
<g transform="translate(70 120)">
  <circle r="46" fill="#fff" stroke="#1f3b57" stroke-width="4"/>
  <circle r="42" fill="none" stroke="#bfe3f7" stroke-width="2"/>
  <path d="M0 0 V-28 M0 0 L20 12" stroke="#1f3b57" stroke-width="4" stroke-linecap="round"/>
  <circle r="4" fill="#c2417f"/>
  <text y="68" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="700" fill="#1f3b57">2 to 3 min</text>
</g>"""
    nose = """
<g transform="translate(260 120)">
  <path d="M-34 -50 C-24 -10 -46 20 -48 36 C-44 52 -20 58 0 58 C20 58 44 52 48 36 C46 20 24 -10 34 -50Z" fill="url(#sg-skin)" stroke="#a96f4b" stroke-width="2"/>
  <ellipse cx="-18" cy="40" rx="11" ry="7" fill="#8e5638"/>
  <ellipse cx="18" cy="40" rx="11" ry="7" fill="#8e5638" stroke="#c2417f" stroke-width="3"/>
  <text y="86" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="700" fill="#1f3b57">New device, other nostril</text>
</g>"""
    dev = _device(206, 44, 0, 0.28)
    return _wrap(clock + nose + dev, "Waiting then repeating the dose in the other nostril", "7. Repeat if there's no response")


SCENES = [step1, step2, step3, step4, step5, step6, step7]
