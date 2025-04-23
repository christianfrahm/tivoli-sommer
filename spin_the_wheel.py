import streamlit as st
import random
from pathlib import Path

st.set_page_config(page_title="Vælg en Pjerrot", page_icon="🤡")
st.title("🤡 Vælg en Pjerrot og vind!")

# Præmier og deres sandsynligheder
options = [
    ("💸 Tillykke! Du har vundet en turbillet!", 0.1),
    ("🍺 Du har vundet en valgfri drikkevare!", 0.2),
    ("❌ Desværre, du tabte. Prøv igen!", 0.7)
]

def pick_result():
    outcomes, probabilities = zip(*options)
    return random.choices(outcomes, probabilities)[0]

# Vis tre klikbare billeder
cols = st.columns(3)
img_path = Path("pjerrot.png")

if "choice" not in st.session_state:
    st.session_state.choice = None

for i, col in enumerate(cols):
    if col.button(f"Vælg Pjerrot #{i+1}"):
        st.session_state.choice = pick_result()

    col.image(img_path, use_column_width=True)

if st.session_state.choice:
    st.markdown("---")
    st.subheader(st.session_state.choice)
    if st.button("Prøv igen"):
        st.session_state.choice = None
