
import streamlit as st
import random

st.set_page_config(page_title="Mandagschancen 🎡", page_icon="🎠")
st.title("🎪 Mandagschancen - Beskriv Tivoli med en emoji og vind!")

# 3x3 emoji grid
tivoli_emojis = ["🎢", "🎠", "🎟️", "🍿", "🎯", "🎡", "🎶", "😄", "☀️"]
cols = st.columns(3)

for i, emoji in enumerate(tivoli_emojis):
    with cols[i % 3]:
        st.markdown(f"<div style='font-size: 50px; text-align: center;'>{emoji}</div>", unsafe_allow_html=True)

st.markdown("---")

# Inputfelt til brugerens emoji-beskrivelse
user_emoji = st.text_input("Beskriv Tivoli med en emoji for en chance for at vinde 🎁")

if "result_shown" not in st.session_state:
    st.session_state.result_shown = False

if user_emoji and not st.session_state.result_shown:
    if st.button("Tjek om du har vundet"):
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
