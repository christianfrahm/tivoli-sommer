
import streamlit as st
import random

st.set_page_config(page_title="Mandagschancen 🎰", page_icon="🎠")
st.title("🎰 Mandagschancen - Prøv lykken!")

emojis = ["🎢", "🎠", "🎡", "🎯", "🍿", "🎟️"]

if "slots" not in st.session_state:
    st.session_state.slots = ["❔", "❔", "❔"]
if "result" not in st.session_state:
    st.session_state.result = ""

# Start spillet - kun vis knappen hvis man ikke allerede har spillet
if st.session_state.result == "":
    if st.button("🎲 Spil Mandagschancen"):
        st.session_state.slots = [random.choice(emojis) for _ in range(3)]
        final = st.session_state.slots
        if final[0] == final[1] == final[2]:
            st.session_state.result = "🎉 Du har vundet en turbillet!"
        elif final[0] == final[1] or final[1] == final[2] or final[0] == final[2]:
            st.session_state.result = "🍹 Du har vundet en valgfri drikkevare!"
        else:
            st.session_state.result = "😢 Desværre, du vandt ikke denne gang."

# Vis slots og resultat i mobilvenlig størrelse
cols = st.columns([1, 1, 1])
for i, col in enumerate(cols):
    col.markdown(
        f"""
        <div style='font-size: 40px; text-align: center; line-height: 1;'>
            {st.session_state.slots[i]}
        </div>
        """, unsafe_allow_html=True
    )

if st.session_state.result:
    st.markdown("---")
    st.header(st.session_state.result)
    st.markdown("🗓️ Spil med igen næste mandag!")
