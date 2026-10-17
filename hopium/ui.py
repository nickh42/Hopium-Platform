"""Shared styling and layout helpers."""
import time

import streamlit as st

from hopium.graphics import BLUE, LOGO, NAVY, PINK_DARK

CSS = f"""
<style>
.stApp {{ background: #f4fbff; }}
h1, h2, h3, h4 {{ color: {NAVY}; overflow-wrap: break-word; word-break: normal; hyphens: auto; line-height: 1.2; }}
h1, h2, h3, h4, [data-testid="stHeading"], [data-testid="stHeadingWithActionElements"] {{ text-align: center !important; justify-content: center !important; }}
h1 {{ font-size: clamp(1.7rem, 5vw, 2.5rem) !important; }}
h2 {{ font-size: clamp(1.4rem, 4vw, 1.9rem) !important; }}
[data-testid="stSidebar"], [data-testid="stSidebarCollapsedControl"], [data-testid="stExpandSidebarButton"] {{ display: none !important; }}
[data-testid="stHeader"] {{ background: #f4fbff; border-bottom: 2px solid #000; }}
[data-testid="stHeader"] nav, [data-testid="stTopNavLinkContainer"] {{ margin-left: auto; justify-content: flex-end; }}
[data-testid="stTopNav"] a, [data-testid="stTopNav"] button {{ font-size: 1.15rem !important; padding: 10px 18px !important; white-space: nowrap; }}
[data-testid="stTopNav"] a p, [data-testid="stTopNav"] button p, [data-testid="stTopNav"] span {{ font-size: 1.15rem !important; font-weight: 600; }}
[data-testid="stHeader"] {{ min-height: 4rem; }}
.hp-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; margin: 8px 0 18px; }}
.hp-card {{ background: #fff; border: 2px solid #000; border-radius: 0; padding: 14px; text-align: center; min-width: 0; overflow: hidden; }}
.hp-card * {{ overflow-wrap: break-word; }}
.hp-card {{ display: flex; flex-direction: column; align-items: center; justify-content: flex-start; }}
.hp-card svg {{ flex: none; }}
.hp-card .t, .hp-card p {{ width: 100%; }}
.hp-card svg {{ width: 84px; height: 84px; }}
.hp-card .t {{ margin: 6px 0 4px; color: {NAVY}; font-size: 1rem; font-weight: 700; line-height: 1.25; }}
.hp-card p {{ margin: 0; font-size: .92rem; color: #33495f; }}
.hp-step .num {{ display: inline-block; background: {PINK_DARK}; color: #fff; width: 26px; height: 26px;
  line-height: 26px; border-radius: 50%; font-weight: 700; margin-bottom: 4px; }}
.hp-callout {{ background: #fff0f6; border: 2px solid #000; border-left: 6px solid #000; border-radius: 0; padding: 12px 16px; margin: 10px 0; color: {NAVY}; }}
.hp-device svg {{ width: 100%; max-width: 560px; display: block; margin: 0 auto; }}
.hp-header {{ display: flex; align-items: center; justify-content: center; gap: 14px; }}
.hp-header svg {{ width: 60px; height: 72px; }}
.hp-header span {{ font-size: clamp(1.6rem, 5vw, 2.2rem); font-weight: 800; color: {NAVY}; }}
#hp-splash {{ position: fixed; inset: 0; z-index: 999999; background: {BLUE}; display: flex; flex-direction: column;
  align-items: center; justify-content: center; animation: hp-fade 0.6s ease 2.3s forwards; }}
#hp-splash svg {{ width: 160px; height: 192px; animation: hp-pulse 1.4s ease-in-out infinite; }}
#hp-splash .name {{ font-size: 3.2rem; font-weight: 800; width: 100%; text-align: center; margin: 18px 0 0; color: {NAVY}; letter-spacing: .04em; }}
@keyframes hp-pulse {{ 0%,100% {{ transform: scale(1); }} 50% {{ transform: scale(1.07); }} }}
@keyframes hp-fade {{ to {{ opacity: 0; visibility: hidden; }} }}
[data-testid="stAlert"], [data-testid="stTextInput"] input, [data-baseweb="input"], [data-baseweb="base-input"], [data-baseweb="textarea"] {{ border-radius: 0 !important; }}
[data-testid="stAlert"] {{ border: 2px solid #000; }}
[data-baseweb="input"], [data-baseweb="base-input"], [data-baseweb="textarea"] {{ border: 2px solid #000 !important; }}
</style>
"""


def inject_css() -> None:
    st.markdown(CSS, unsafe_allow_html=True)


def splash_once() -> None:
    """Light blue loading screen with the logo, shown once per browser session."""
    if st.session_state.get("_splash_done"):
        return
    holder = st.empty()
    holder.markdown(
        f'<div id="hp-splash">{LOGO}<div class="name">Hopium</div></div>', unsafe_allow_html=True
    )
    time.sleep(2.8)
    holder.empty()
    st.session_state["_splash_done"] = True


def header() -> None:
    st.markdown(f'<div class="hp-header">{LOGO}<span>Hopium</span></div>', unsafe_allow_html=True)


def cards(items, step: bool = False) -> None:
    """items: list of (icon_svg, title, text). Renders a responsive grid of illustrated cards."""
    html = ['<div class="hp-grid">']
    for i, (icon, title, text) in enumerate(items, 1):
        num = f'<span class="num">{i}</span><br>' if step else ""
        cls = "hp-card hp-step" if step else "hp-card"
        html.append(f'<div class="{cls}">{num}{icon}<div class="t">{title}</div><p>{text}</p></div>')
    html.append("</div>")
    st.markdown("".join(html), unsafe_allow_html=True)


def callout(html: str) -> None:
    st.markdown(f'<div class="hp-callout">{html}</div>', unsafe_allow_html=True)



def large_layout() -> None:
    """Wider page with larger type and cards, used by the long-form guide pages."""
    st.markdown(
        """
<style>
.block-container { max-width: 1400px !important; padding-left: 4vw !important; padding-right: 4vw !important; }
.stMarkdown p, .stMarkdown li, .stMarkdown td, .stMarkdown th { font-size: 1.18rem !important; line-height: 1.6; }
[data-testid="stCaptionContainer"] { font-size: 1.05rem !important; }
.stMarkdown li { margin-bottom: .3rem; }
.stMarkdown table { margin: 0 auto; }
.stMarkdown th, .stMarkdown td { text-align: center !important; }
h1 { font-size: clamp(2.1rem, 4.2vw, 3.2rem) !important; }
h2 { font-size: clamp(1.7rem, 3.2vw, 2.35rem) !important; margin-top: 1.5rem; }
h3 { font-size: clamp(1.35rem, 2.4vw, 1.8rem) !important; }
.hp-grid { grid-template-columns: repeat(auto-fit, minmax(290px, 1fr)); gap: 20px; }
.hp-card { padding: 24px 20px; }
.hp-card svg { width: 112px; height: 112px; }
.hp-card .t { font-size: 1.27rem; margin: 10px 0 8px; }
.hp-card p { font-size: 1.08rem; line-height: 1.5; }
.hp-callout, .hp-callout * { font-size: 1.13rem; }
.hp-callout { padding: 16px 22px; }
.hp-step .num { width: 32px; height: 32px; line-height: 32px; font-size: 1.05rem; }
.hp-device svg { max-width: 760px; }
</style>
""",
        unsafe_allow_html=True,
    )
