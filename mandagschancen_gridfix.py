
import streamlit as st
import random

st.set_page_config(page_title="Mandagschancen 🎡", page_icon="🎠")
st.title("🎪 Mandagschancen - Klik på en Tivoli-emoji og vind!")

# 3x3 emoji grid med klik
emojis = ["🎢", "🎠", "🎟️", "🍿", "🎯", "🎡", "🎶", "😄", "☀️"]

if "result_shown" not in st.session_state:
    st.session_state.result_shown = False
if "clicked_emoji" not in st.session_state:
    st.session_state.clicked_emoji = None

if not st.session_state.result_shown:
    for row in range(3):
        cols = st.columns(3)
        for col in range(3):
            idx = row * 3 + col
            with cols[col]:
                if st.button(emojis[idx], key=f"emoji_{idx}") and st.session_state.clicked_emoji is None:
                    st.session_state.clicked_emoji = idx
                    result = random.choices([
                        ("🎉 Du har vundet en turbillet!", 0.1),
                        ("🍹 Du har vundet en valgfri drikkevare!", 0.2),
                        ("😢 Desværre, du vandt ikke denne gang.", 0.7)
                    ], weights=[0.1, 0.2, 0.7])[0][0]
                    st.session_state.result = result
                    st.session_state.result_shown = True

if st.session_state.result_shown:
    st.markdown("---")
    st.subheader(st.session_state.result)
    st.markdown("🗓️ Spil med igen næste mandag!")
