
import streamlit as st
import random
import time

st.set_page_config(page_title="Mandagschancen 🎰", page_icon="🎠")
st.title("🎰 Mandagschancen - Prøv lykken!")

emojis = ["🎢", "🎠", "🎡", "🎯", "🍿", "🎟️"]

if "spinning" not in st.session_state:
    st.session_state.spinning = False
if "slots" not in st.session_state:
    st.session_state.slots = ["❔", "❔", "❔"]
if "result" not in st.session_state:
    st.session_state.result = ""

# Start spillet
if st.button("🎲 Spil Mandagschancen") and not st.session_state.spinning:
    st.session_state.spinning = True
    for i in range(15):
        st.session_state.slots = [random.choice(emojis) for _ in range(3)]
        time.sleep(0.1)
        st.experimental_rerun()

# Når spinning stopper
if st.session_state.spinning:
    st.session_state.spinning = False
    final = st.session_state.slots
    if final[0] == final[1] == final[2]:
        st.session_state.result = "🎉 Du har vundet en turbillet!"
    elif final[0] == final[1] or final[1] == final[2] or final[0] == final[2]:
        st.session_state.result = "🍹 Du har vundet en valgfri drikkevare!"
    else:
        st.session_state.result = "😢 Desværre, du vandt ikke denne gang."

# Vis slots og resultat
cols = st.columns(3)
for i, col in enumerate(cols):
    col.markdown(f"<div style='font-size: 60px; text-align: center;'>{st.session_state.slots[i]}</div>", unsafe_allow_html=True)

if st.session_state.result:
    st.markdown("---")
    st.header(st.session_state.result)
    st.markdown("🗓️ Spil med igen næste mandag!")
