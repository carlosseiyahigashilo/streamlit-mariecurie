import streamlit as st
from multiapp import MultiApp
import home, presencasimulado

app = MultiApp()
st.markdown("""
    # Automação da Análise de Simulados

    Projetinho com objetivo de tentar otimizar o nosso trabalho!

""")
#st.image(r"C:\Users\carlo\PycharmProjects\pythonProject\venv\MarieCurie\logobranco.png")

# Colocar todas as subpáginas aqui
app.add_app("Home", home.app)
app.add_app("Presença Simulados", presencasimulado.app)
# app.add_app("Model", model_app)

# The main app
app.run()
