import time

import streamlit as st

st.set_page_config(page_title="Hopium", page_icon="💊", layout="wide")

st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;800&display=swap');
        html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
            background: linear-gradient(180deg, #dff4ff 0%, #d3ecff 100%);
            color: #123b5d;
            font-family: 'Times New Roman', Times, serif;
        }
        [data-testid="stSidebar"], [data-testid="stSidebarNav"], section[data-testid="stSidebar"] {
            display: none !important;
        }
        .hopium-splash {
            position: fixed;
            inset: 0;
            z-index: 9999;
            display: flex;
            align-items: center;
            justify-content: center;
            background: linear-gradient(180deg, #dff4ff 0%, #cfe9ff 100%);
        }
        .hopium-card {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            gap: 0.75rem;
            text-align: center;
            transform: translateY(-0.5rem);
        }
        .hopium-heart {
            width: 220px;
            height: 220px;
            display: block;
            filter: drop-shadow(0 14px 18px rgba(235, 117, 175, 0.22));
        }
        .hopium-title {
            font-family: 'Times New Roman', Times, serif;
            font-size: 5.5rem;
            font-weight: 700;
            letter-spacing: 0.04em;
            color: #123b5d;
            margin: 0;
            line-height: 1;
            text-align: center;
        }
        .hopium-plant {
            filter: drop-shadow(0 10px 16px rgba(236, 117, 170, 0.3));
        }
        .reveal {
            opacity: 0;
            transform: scaleX(0.7);
            transform-origin: center;
            animation: revealSquish 0.9s cubic-bezier(0.22, 1, 0.36, 1) forwards;
        }
        @keyframes revealSquish {
            0% { opacity: 0; transform: scaleX(0.7) scaleY(0.9); filter: blur(1.4px); }
            55% { opacity: 1; transform: scaleX(0.96) scaleY(1); filter: blur(0.25px); }
            100% { opacity: 1; transform: scaleX(1) scaleY(1); filter: blur(0); }
        }
    </style>
    """,
    unsafe_allow_html=True,
)

if "hopium_loaded" not in st.session_state:
    st.markdown(
        """
        <div class="hopium-splash">
            <div class="hopium-card">
                <svg class="hopium-heart" viewBox="0 0 320 260" xmlns="http://www.w3.org/2000/svg" aria-label="Hopium logo">
                    <g stroke="#ee6ca5" stroke-width="8" fill="none">
                        <path d="M160 222 C138 202, 84 176, 54 135 C18 89, 28 44, 72 32 C101 24, 127 39, 146 64 C152 72, 156 80, 160 88 C164 80, 168 72, 174 64 C193 39, 219 24, 248 32 C292 44, 302 89, 266 135 C236 176, 182 202, 160 222 Z" fill="#f7cfe0" fill-opacity="0.96"/>
                        <g class="hopium-plant" stroke="#e76aa7" stroke-width="8" fill="none" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M112 88 C96 72, 78 62, 66 38"/>
                            <path d="M118 102 C90 89, 72 73, 60 52"/>
                            <path d="M208 88 C224 72, 242 62, 254 38"/>
                            <path d="M202 102 C230 89, 248 73, 260 52"/>
                            <path d="M145 62 C152 42, 158 32, 160 16"/>
                            <path d="M175 62 C168 42, 162 32, 160 16"/>
                        </g>
                        <g fill="#fbe3f0">
                            <ellipse cx="96" cy="134" rx="18" ry="32"/>
                            <ellipse cx="224" cy="134" rx="18" ry="32"/>
                            <ellipse cx="160" cy="154" rx="18" ry="36"/>
                        </g>
                    </g>
                </svg>
                <div class="reveal"><h1 class="hopium-title">Hopium</h1></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    time.sleep(1.4)
    st.session_state.hopium_loaded = True
    st.rerun()

st.switch_page("pages/1_Info.py")
