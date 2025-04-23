
import streamlit as st
import random
import base64
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

# Indlæs billede og konverter til base64
img_path = Path("pjerrot.png")
with open(img_path, "rb") as img_file:
    img_base64 = base64.b64encode(img_file.read()).decode()

# Brug HTML til at vise billeder side om side på mobil
if "choice" not in st.session_state:
    st.session_state.choice = None

image_row_html = """
<div style='display: flex; justify-content: center; gap: 10px; flex-wrap: wrap;'>
"""

for i in range(3):
    image_row_html += f"""
    <a href="?choice={i}" style="text-decoration: none;">
        <img src="data:image/png;base64,{img_base64}" style="width: 80px; height: auto; border: none;" />
    </a>
    """

image_row_html += "</div>"

st.markdown(image_row_html, unsafe_allow_html=True)

# Klik-registrering via query param
if "clicked_index" not in st.session_state:
    st.session_state.clicked_index = None

for i in range(3):
    if st.query_params.get("choice") == str(i):
        st.session_state.clicked_index = i
        st.session_state.choice = pick_result()

if st.session_state.choice:
    st.markdown("---")
    st.subheader(st.session_state.choice)
    if st.button("Prøv igen"):
        st.session_state.choice = None
        st.experimental_set_query_params()
