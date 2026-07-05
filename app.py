import streamlit as streamlit
import google.generativeai as genai

# ============================================================================
# 1. CONFIGURACIÓN DE ARQUITECTURA DE MARCA Y UI (ENTORNO PREMIUM)
# ============================================================================
streamlit.set_page_config(
    page_title="Tutor de Élite IA - Ecosistema de Alto Rendimiento",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos personalizados para una experiencia visual de alta gama (Modo Oscuro/Premium)
streamlit.markdown("""
    <style>
    .main-title { font-size: 2.6rem; font-weight: 800; color: #FFFFFF; margin-bottom: 0.5rem; }
    .sub-title { font-size: 1.2rem; color: #A3AED0; margin-bottom: 2rem; }
    .phase-box { padding: 1rem; border-radius: 0.5rem; background-color: #111C44; border-left: 5px solid #4318FF; margin-bottom: 1rem; }
    </style>
""", unsafe_allow_html=True)

# ============================================================================
# 2. BARRA LATERAL: CONTROL DE ACCESO Y MONETIZACIÓN (CAPITALIZACIÓN SAAS)
# ============================================================================
with streamlit.sidebar:
    streamlit.markdown("### 🧠 Tutor de Élite IA")
    streamlit.markdown("---")
    streamlit.markdown("#### 🔐 Autenticación del Ecosistema")
    
    # Doble vía de acceso: API Key del usuario (SaaS B2C) o Secrets del Servidor (SaaS B2B)
    user_api_key = streamlit.text_input(
        "Introduce tu Gemini API Key Corporativa/Estudiante:",
        type="password",
        help="Para comercializar la app, los usuarios introducen su propia llave protegiendo tus costos de infraestructura."
    )
    
    streamlit.markdown("---")
    streamlit.markdown("#### 🛠️ Configuración del Motor")
    temperatura = streamlit.slider("Nivel de Creatividad (Kaizen):", min_value=0.0, max_value=1.0, value=0.3, step=0.1)
    
    # Botón de reset imperativo para limpiar la memoria de la sesión
    reset_session = streamlit.button("🔄 Reiniciar Ciclo de Alto Rendimiento")
    
    streamlit.markdown("---")
    streamlit.markdown("<p style='font-size:0.8rem; color:#A3AED0;'>Método de Simulación Interactiva v15.0<br>© 2026 Ecosistema de Aprendizaje de Alto Rendimiento</p>", unsafe_allow_html=True)

# ============================================================================
# 3. CAPA DE SEGURIDAD Y VALIDACIÓN DE CREDENCIALES API
# ============================================================================
API_KEY = None
if user_api_key:
    API_KEY = user_api_key
elif "GOOGLE_API_KEY" in streamlit.secrets:
    API_KEY = streamlit.secrets["GOOGLE_API_KEY"]

if not API_KEY:
    streamlit.warning("🔑 Conexión Protegida: Introduce tu API Key en la barra lateral izquierda para inicializar el backend.")
    streamlit.info("💡 Nota de producción: La arquitectura acepta llaves dinámicas por usuario para facilitar el modelo de negocio Freemium.")
    streamlit.stop()

try:
    genai.configure(api_key=API_KEY)
except Exception as e:
    streamlit.error(f"Error crítico de inicialización en el SDK de Google: {e}")
    streamlit.stop()

# ============================================================================
# 4. INTERFAZ PRINCIPAL DE CONDUCCIÓN COGNITIVA
# ============================================================================
streamlit.markdown("<div class='main-title'>🧠 Ecosistema de Aprendizaje de Alto Rendimiento</div>", unsafe_allow_html=True)
streamlit.markdown("<div class='sub-title'>Plataforma de Simulación Interactiva Orientada a Soluciones Tangibles (Engine: Gemini 2.0 Flash)</div>", unsafe_allow_html=True)

# Selectores dinámicos que alteran el comportamiento del Omniprompt Maestro en tiempo real
col_disp, col_fase = streamlit.columns([1, 1])

with col_disp:
    disciplina = streamlit.selectbox(
        "🎯 Selecciona la Disciplina Científica:",
        [
            "Medicina Veterinaria y Zootecnia", 
            "Biología Celular y Molecular", 
            "Anatomía Comparada Animal", 
            "Fisiología Veterinaria", 
            "Estadística Aplicada y Modelación Bioestadística"
        ]
    )

with col_fase:
    fase_actual = streamlit.select_slider(
        "📈 Fase Actual del Protocolo Modular:",
        options=[
            "Fase 1: Conceptos Intuitivos y Claros", 
            "Fase 2: Puente de Rigor Técnico Formal", 
            "Fase 3: Soluciones Tangibles y Casos Clínicos/Prácticos"
        ]
    )

# Cuadro informativo dinámico según la fase seleccionada
streamlit.markdown(f"""
    <div class='phase-box'>
        <strong>Enfoque de Configuración Actual:</strong> Operando bajo la <strong>{fase_actual}</strong> para la disciplina de <strong>{disciplina}</strong>. El modelo ajustará su andamiaje cognitivo automáticamente.
    </div>
""", unsafe_allow_html=True)

# ============================================================================
# 5. INYECCIÓN DEL OMNIPROMPT MAESTRO V15.0 (BACKEND OCULTO)
# ============================================================================
OMNIPROMPT_MAESTRO = f"""
Actúas como un Tutor de Élite en la disciplina: {disciplina}. Tu objetivo es guiar un aprendizaje de alta demanda cognitiva mediante el "Protocolo Modular de Alto Rendimiento", aplicando la filosofía Kaizen (mejora continua) y transformando el conocimiento en soluciones tangibles.

Estás operando específicamente bajo los lineamientos de la: {fase_actual}.

INSTRUCCIONES DE ANDAMIAJE PROGRESIVO OBLIGATORIAS:
1. Las explicaciones deben comenzar con conceptos intuitivos, analogías cotidianas limpias y esquemas claros para enganchar al alumno.
2. Inmediatamente después, construye el puente hacia el rigor técnico formal, utilizando la nomenclatura exacta, los términos médicos/biológicos precisos y el estado del arte que exige la disciplina.
3. Evita a toda costa dos extremos: el simplismo infantil o condescendiente, y el elitismo técnico confuso o inaccesible sin pedagogía.
4. Diseña cada respuesta para que el conocimiento se oriente a una solución tangible (un caso clínico, un diseño experimental, un modelo estadístico, etc.).

REGLAS DE INTERACCIÓN:
- Responde siempre con estructura académica profesional (puntos clave, negritas, bloques de código si aplica).
- Promueve que el usuario responda con un alto nivel de análisis estimulando la mayéutica.
"""

# ============================================================================
# 6. GESTIÓN DE ESTADOS DE SESIÓN Y MEMORIA PERSISTENTE (ENGINE GEMINI 2.0)
# ============================================================================
# Empleamos la infraestructura oficial de última generación de Google AI Studio
MODEL_ENGINE = "models/gemini-2.0-flash" 

if "chat" not in streamlit.session_state or reset_session:
    streamlit.session_state.messages = []
    streamlit.session_state.disciplina_actual = disciplina
    streamlit.session_state.fase_actual = fase_actual
    
    configuracion_generacion = genai.GenerationConfig(temperature=temperatura)
    
    model = genai.GenerativeModel(
        model_name=MODEL_ENGINE,
        system_instruction=OMNIPROMPT_MAESTRO,
        generation_config=configuracion_generacion
    )
    streamlit.session_state.chat = model.start_chat(history=[])

# Reinicio adaptativo automático si cambian los componentes visuales superiores
if (streamlit.session_state.disciplina_actual != disciplina) or (streamlit.session_state.fase_actual != fase_actual):
    streamlit.session_state.messages = []
    streamlit.session_state.disciplina_actual = disciplina
    streamlit.session_state.fase_actual = fase_actual
    
    configuracion_generacion = genai.GenerationConfig(temperature=temperatura)
    model = genai.GenerativeModel(
        model_name=MODEL_ENGINE,
        system_instruction=OMNIPROMPT_MAESTRO,
        generation_config=configuracion_generacion
    )
    streamlit.session_state.chat = model.start_chat(history=[])
    streamlit.rerun()

# ============================================================================
# 7. RENDERIZADO DEL FLUJO DE CONVERSACIÓN (UI/UX CHAT)
# ============================================================================
for message in streamlit.session_state.messages:
    with streamlit.chat_message(message["role"]):
        streamlit.markdown(message["content"])

# ============================================================================
# 8. CAPA DE PROCESAMIENTO ACTIVO Y LLAMADOS A LA API
# ============================================================================
if user_input := streamlit.chat_input(f"Escribe tu comando o respuesta para {disciplina}..."):
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
            streamlit.error(f"Error de procesamiento en la simulación interactiva: {e}")
