import streamlit as st

# Título y autor de la app
st.title("Mi primera app")
st.markdown("Esta app fue elaborada por Juan Sebastian Herrera Gomez.")

# Pregunta al usuario su nombre
nombre_usuario = st.text_input("Por favor, ingresa tu nombre:")

# Imprime un mensaje de bienvenida
if nombre_usuario:
    st.write(f"{nombre_usuario}, te doy la bienvenida a mi primera app.")
