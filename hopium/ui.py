"""Shared styling and layout helpers."""
import time

import streamlit as st

from hopium.graphics import BLUE, LOGO, NAVY, PINK_DARK

CSS = f"""
<style>
.stApp {{ background: #f4fbff; }}
h1, h2, h3 {{ color: {NAVY}; }}
.hp-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(190px, 1fr)); gap: 14px; margin: 8px 0 18px; }}
.hp-card {{ background: #fff; border: 2px solid {BLUE}; border-radius: 16px; padding: 14px; text-align: center; }}
.hp-card svg {{ width: 84px; height: 84px; }}
.hp-card h4 {{ margin: 6px 0 4px; color: {NAVY}; font-size: 1.05rem; }}
.hp-card p {{ margin: 0; font-size: .92rem; color: #33495f; }}
.hp-step .num {{ display: inline-block; background: {PINK_DARK}; color: #fff; width: 26px; height: 26px;
  line-height: 26px; border-radius: 50%; font-weight: 700; margin-bottom: 4px; }}
.hp-callout {{ background: #fff0f6; border-left: 6px solid {PINK_DARK}; border-radius: 8px; padding: 12px 16px; margin: 10px 0; color: {NAVY}; }}
.hp-device svg {{ width: 100%; max-width: 560px; display: block; margin: 0 auto; }}
.hp-header {{ display: flex; align-items: center; gap: 14px; }}
.hp-header svg {{ width: 56px; height: 64px; }}
.hp-header span {{ font-size: 2.2rem; font-weight: 800; color: {NAVY}; }}
#hp-splash {{ position: fixed; inset: 0; z-index: 999999; background: {BLUE}; display: flex; flex-direction: column;
  align-items: center; justify-content: center; animation: hp-fade 0.6s ease 2.3s forwards; }}
#hp-splash svg {{ width: 150px; height: 172px; animation: hp-pulse 1.4s ease-in-out infinite; }}
#hp-splash h1 {{ font-size: 3.2rem; margin: 18px 0 0; color: {NAVY}; letter-spacing: .04em; }}
@keyframes hp-pulse {{ 0%,100% {{ transform: scale(1); }} 50% {{ transform: scale(1.07); }} }}
@keyframes hp-fade {{ to {{ opacity: 0; visibility: hidden; }} }}
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
        f'<div id="hp-splash">{LOGO}<h1>Hopium</h1></div>', unsafe_allow_html=True
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
        html.append(f'<div class="{cls}">{num}{icon}<h4>{title}</h4><p>{text}</p></div>')
    html.append("</div>")
    st.markdown("".join(html), unsafe_allow_html=True)
