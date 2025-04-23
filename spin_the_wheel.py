
import streamlit as st
import random

st.set_page_config(page_title="Spin the Wheel", page_icon="🍀")
st.title("🍀 Spin the Wheel!")

# Resultater og deres sandsynligheder
options = [
    ("Du tabte... Prøv igen!", 0.7),
    ("🍺 Tillykke! Du har vundet en valgfri drikkevare!", 0.2),
    ("🚌 Du har vundet en turbillet!", 0.1)
]

def spin_wheel():
    outcomes, probabilities = zip(*options)
    result = random.choices(outcomes, probabilities)[0]
    return result

if st.button("Spin hjulet 🌁"):
    result = spin_wheel()
    st.subheader(result)
else:
    st.write("Klik på knappen for at spinne hjulet!")
