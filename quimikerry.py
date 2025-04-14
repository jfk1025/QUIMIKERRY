import streamlit as st
import random

def mostrar_juegos():
    st.subheader("🧪 Juego: ¿Cuál es el Elemento?")
    elementos = [
        {"nombre": "Hidrógeno", "simbolo": "H"},
        {"nombre": "Oxígeno", "simbolo": "O"},
        {"nombre": "Carbono", "simbolo": "C"},
        {"nombre": "Nitrógeno", "simbolo": "N"}
    ]
    eleccion = random.choice(elementos)
    opciones = random.sample([e["nombre"] for e in elementos], 4)

    st.markdown(f"¿Qué elemento tiene el símbolo **{eleccion['simbolo']}**?")
    respuesta = st.radio("Selecciona la respuesta:", opciones)

    if st.button("Verificar"):
        if respuesta == eleccion["nombre"]:
            st.success("¡Correcto!")
        else:
            st.error(f"Incorrecto. Era {eleccion['nombre']}.")
