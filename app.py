import streamlit as streamlit
import google.generativeai as genai

# 1. Configuración estética y de marca (Ecosistema de Alto Rendimiento)
streamlit.set_page_config(page_title="Tutor de Élite IA", page_icon="🧠", layout="wide")

# Barra lateral para el control de accesos e ingresos de capitalización
with streamlit.sidebar:
    streamlit.image("https://cdn-icons-png.flaticon.com/512/3449/3449614.png", width=80)
    streamlit.title("Control de Acceso SaaS")
    streamlit.subheader("Credenciales del Ecosistema")
    
    # Permitir al usuario usar su propia llave (vía de capitalización B2C sin costo de servidor para ti)
    user_key = streamlit.text_input("Introduce tu Gemini API Key de estudiante:", type="password")
    streamlit.markdown("---")
    streamlit.markdown("**Método de Simulación Interactiva** v15.0\n*Filosofía Kaizen aplicada a Ciencias Biológicas y Veterinarias.*")

# 2. Conexión Protegida con la API de Google
API_KEY = None
if user_key:
    API_KEY = user_key
elif "GOOGLE_API_KEY" in streamlit.secrets:
    API_KEY = streamlit.secrets["GOOGLE_API_KEY"]

if not API_KEY:
    streamlit.warning("🔑 Para iniciar tu sesión de alto rendimiento, introduce tu API Key en la barra lateral izquierda.")
    streamlit.info("💡 Si eres administrador, configura la variable GOOGLE_API_KEY en los Secrets del servidor.")
    streamlit.stop()

try:
    genai.configure(api_key=API_KEY)
except Exception as e:
    streamlit.error(f"Error al autenticar la llave de seguridad: {e}")
    streamlit.stop()

# 3. Interfaz Principal del Ecosistema
streamlit.title("🧠 Ecosistema de Aprendizaje de Alto Rendimiento")
streamlit.subheader("Método de Simulación Interactiva para Ciencias Biológicas y Veterinarias")

# Selección dinámica de la Disciplina y Fase para moldear el Omniprompt
col1, col2 = streamlit.columns([1, 2])
with col1:
    disciplina = streamlit.selectbox(
        "Selecciona la disciplina de estudio:",
        ["Medicina Veterinaria y Zootecnia", "Biología Celular", "Anatomía Comparada", "Fisiología Animal", "Estadística Aplicada"]
    )
with col2:
    fase_actual = streamlit.select_slider(
        "Fase del Protocolo Modular:",
        options=["Fase 1: Conceptos Intuitivos", "Fase 2: Puente de Rigor Técnico", "Fase 3: Soluciones Tangibles y Casos"]
    )

# 4. Tu Omniprompt Maestro Inyectado Dinámicamente
OMNIPROMPT_MAESTRO = f"""
Actúas como un Tutor de Élite en la disciplina: {disciplina}. Tu objetivo es guiar un aprendizaje de alta demanda cognitiva mediante el "Protocolo Modular de Alto Rendimiento", aplicando la filosofía Kaizen (mejora continua) y transformando el conocimiento en soluciones tangibles.

Estás actualmente operando bajo el enfoque específico de la: {fase_actual}.

Las explicaciones deben seguir un andamiaje progresivo: comenzar con conceptos intuitivos y claros para construir el puente hacia el rigor técnico formal y la nomenclatura exacta que exige la disciplina. Evita el simplismo infantil y el elitismo técnico confuso.

[Filtros de control e instrucciones detalladas de las Fases 1, 2 y 3 del Omniprompt...]
"""

# 5. Inicializar el motor de IA con el identificador de modelo oficial corregido
if "chat" not in streamlit.session_state or streamlit.sidebar.button("Reiniciar Tutoría (Limpiar Caché)"):
    model = genai.GenerativeModel(
        model_name="models/gemini-1.5-flash", 
        system_instruction=OMNIPROMPT_MAESTRO
    )
    streamlit.session_state.chat = model.start_chat(history=[])
    streamlit.session_state.messages = []
    streamlit.session_state.disciplina_actual = disciplina

# Si el usuario cambia de carrera o materia, reiniciamos el chat con sus nuevas instrucciones de sistema
if streamlit.session_state.disciplina_actual != disciplina:
    model = genai.GenerativeModel(
        model_name="models/gemini-1.5-flash",
        system_instruction=OMNIPROMPT_MAESTRO
    )
    streamlit.session_state.chat = model.start_chat(history=[])
    streamlit.session_state.messages = []
    streamlit.session_state.disciplina_actual = disciplina
    streamlit.rerun()

# 6. Dibujar el historial de conversación en la pantalla del cliente
for message in streamlit.session_state.messages:
    with streamlit.chat_message(message["role"]):
        streamlit.markdown(message["content"])

# 7. Caja de interacción activa del estudiante
if user_input := streamlit.chat_input(f"Escribe aquí tu comando o duda sobre {disciplina}..."):
    streamlit.session_state.messages.append({"role": "user", "content": user_input})
    with streamlit.chat_message("user"):
        streamlit.markdown(user_input)
    
    with streamlit.chat_message("assistant"):
        response_placeholder = streamlit.empty()
        try:
            response = streamlit.session_state.chat.send_message(user_input)
            response_placeholder.markdown(response.text)
            streamlit.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            streamlit.error(f"Ocurrió un error en la simulación: {e}")

