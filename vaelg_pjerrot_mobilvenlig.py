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

# Brug HTML til at gøre billeder klikbare i en mobilvenlig størrelse
cols = st.columns(3)
if "choice" not in st.session_state:
    st.session_state.choice = None

for i, col in enumerate(cols):
    with col:
        button_html = f"""
        <form action="" method="post">
            <input type="hidden" name="choice" value="{i}">
            <button type="submit" style="border: none; background: none; padding: 0;">
                <img src='data:image/png;base64,{img_base64}' style='max-width: 80px; height: auto;'>
            </button>
        </form>
        """
        st.markdown(button_html, unsafe_allow_html=True)

# Brug formdata (hack) til at registrere klik
# Men Streamlit tillader ikke almindelige POSTs – vi simulerer klik internt
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
