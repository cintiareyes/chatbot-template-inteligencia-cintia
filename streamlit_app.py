import streamlit as st
from openai import OpenAI

# Show title and description.
st.title("Inteligencia Artificial con IDESIE Bussiness School")
st.write (
    "Es una aplicacion para resumir y responder tus dudas de los videos de clases grabadas. " 
     "Te enseñamos como funciona AGREGAR PARENTESIS Y ENTRE ELLOS COLOCAR LINK DEL TUTORIAL. "
)

st.button ('Empieza aquí')

# Ask user for their OpenAI API key via `st.text_input`.
# Alternatively, you can store the API key in `./.streamlit/secrets.toml` and access it
# via `st.secrets`, see https://docs.streamlit.io/develop/concepts/connections/secrets-management
openai_api_key = st.text_input("OpenAI API Key PREGUNTA AQUI", type="password")
