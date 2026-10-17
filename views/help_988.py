import streamlit as st

st.markdown(
    """
<style>
.st-key-sos button {
    width: 260px; height: 260px; border-radius: 50%; border: 8px solid #8f0d0d;
    background: radial-gradient(circle at 35% 30%, #ff5a5a, #d62828 60%, #a50f0f);
    box-shadow: 0 10px 24px rgba(160, 15, 15, .45); margin: 24px auto; display: block;
}
.st-key-sos button p { font-size: 150px; font-weight: 900; color: #fff; line-height: 1; }
.st-key-sos button:hover { filter: brightness(1.08); border-color: #8f0d0d; }
.st-key-sos { display: flex; justify-content: center; width: 100%; }
</style>
""",
    unsafe_allow_html=True,
)


@st.dialog("Are you sure?")
def confirm() -> None:
    st.warning("This will start a call to the 988 Suicide & Crisis Lifeline.")
    st.markdown(
        '<a href="tel:988" style="display:block;text-align:center;background:#d62828;color:#fff;'
        'padding:14px;border-radius:10px;font-weight:700;text-decoration:none;font-size:1.1rem;">'
        "Yes, call 988</a>",
        unsafe_allow_html=True,
    )
    st.caption("On a computer? Use the chat instead: https://988lifeline.org/chat/")
    if st.button("Cancel", use_container_width=True):
        st.rerun()


st.title("Need help now?")
st.write("Press the button to reach the 988 Suicide & Crisis Lifeline. Free, confidential, 24/7.")

if st.button("!", key="sos"):
    confirm()
