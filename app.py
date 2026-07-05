import streamlit as streamlit
import google.generativeai as genai

# 1. Configuración estética de la página web
streamlit.set_page_config(page_title="Tutor de Élite IA", page_icon="🧠", layout="centered")
streamlit.title("🧠 Ecosistema de Aprendizaje de Alto Rendimiento")
streamlit.subheader("Método de Simulación Interactiva para Ciencias Biológicas")

# 2. Conexión protegida con la API de Google (Oculta en el backend)
try:
    API_KEY = streamlit.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=API_KEY)
except Exception:
    streamlit.error("Falta configurar la llave de seguridad en el backend de la nube.")
    streamlit.stop()

# 3. Tu Omniprompt Maestro Versión 15.0 queda oculto en el servidor
OMNIPROMPT_MAESTRO = """
Actúas como un Tutor de Élite en la disciplina proporcionada por el usuario. Tu objetivo es guiar un aprendizaje de alta demanda cognitiva mediante el "Protocolo Modular de Alto Rendimiento", aplicando la filosofía Kaizen (mejora continua) y transformando el conocimiento en soluciones tangibles. Las explicaciones deben seguir un andamiaje progresivo: comenzar con conceptos intuitivos y claros para construir el puente hacia el rigor técnico formal y la nomenclatura exacta que exige la disciplina. Evita el simplismo infantil y el elitismo técnico confuso.

[Filtros de control e instrucciones de las Fases 1, 2 y 3 del Omniprompt...]
"""

# 4. Inicializar el motor de IA con las instrucciones ocultas
if "chat" not in streamlit.session_state:
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction=OMNIPROMPT_MAESTRO
    )
    streamlit.session_state.chat = model.start_chat(history=[])
    streamlit.session_state.messages = []

# 5. Dibujar el historial de mensajes en la pantalla del cliente
for message in streamlit.session_state.messages:
    with streamlit.chat_message(message["role"]):
        streamlit.markdown(message["content"])

# 6. Caja de interacción del usuario
if user_input := streamlit.chat_input("Escribe aquí tu comando (ej. Hola, o Fase 1: [Temas])..."):
    streamlit.session_state.messages.append({"role": "user", "content": user_input})
    with streamlit.chat_message("user"):
        streamlit.markdown(user_input)
    
    with streamlit.chat_message("assistant"):
        response_placeholder = streamlit.empty()
        response = streamlit.session_state.chat.send_message(user_input)
        response_placeholder.markdown(response.text)
        
    streamlit.session_state.messages.append({"role": "assistant", "content": response.text})

