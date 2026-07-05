import streamlit as streamlit

# ============================================================================
# 1. CONFIGURACIÓN DE ARQUITECTURA DE MARCA Y UI (ENTORNO PREMIUM)
# ============================================================================
streamlit.set_page_config(
    page_title="Tutor de Élite - Ecosistema de Aprendizaje Modular",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS de alta gama para mantener el look corporativo premium
streamlit.markdown("""
    <style>
    .main-title { font-size: 2.6rem; font-weight: 800; color: #FFFFFF; margin-bottom: 0.3rem; }
    .sub-title { font-size: 1.1rem; color: #A3AED0; margin-bottom: 1.8rem; }
    .phase-box { padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1.2rem; line-height: 1.6; }
    .fase1 { background-color: #0B1437; border-left: 5px solid #00E5FF; }
    .fase2 { background-color: #111C44; border-left: 5px solid #4318FF; }
    .fase3 { background-color: #1B254B; border-left: 5px solid #01B574; }
    .titulo-fase { font-size: 1.4rem; font-weight: 700; color: #FFFFFF; margin-bottom: 0.8rem; }
    .badges { background-color: #243B80; color: #00E5FF; padding: 0.2rem 0.6rem; border-radius: 0.3rem; font-size: 0.8rem; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# ============================================================================
# 2. CONTROL DE FLUJO PEDAGÓGICO (ESTADOS DE SESIÓN)
# ============================================================================
# Inicializamos el control de qué fases están desbloqueadas para el alumno
if "fase2_desbloqueada" not in streamlit.session_state:
    streamlit.session_state.fase2_desbloqueada = False
if "fase3_desbloqueada" not in streamlit.session_state:
    streamlit.session_state.fase3_desbloqueada = False

# ============================================================================
# 3. BARRA LATERAL: CONTROL DE NAVEGACIÓN CURADA (MODELO COMERCIAL SAAS)
# ============================================================================
with streamlit.sidebar:
    streamlit.markdown("### 🧠 Tutor de Élite IA")
    streamlit.markdown("---")
    streamlit.markdown("#### 🎯 Ruta de Aprendizaje")
    
    disciplina = streamlit.selectbox(
        "Disciplina Científica:",
        ["Medicina Veterinaria y Zootecnia", "Estadística Aplicada y Modelación"]
    )
    
    tema = streamlit.selectbox(
        "Selecciona el Módulo Clínico:",
        ["Fisiología Renal: Insuficiencia Renal Aguda (IRA)", "Biología Celular: Mitosis y Cáncer Canino"]
    )
    
    streamlit.markdown("---")
    streamlit.markdown("#### 📊 Progreso del Estudiante")
    # Indicadores visuales automáticos basados en el avance del alumno
    streamlit.checkbox("Fase 1: Concepto Intuitivo", value=True, disabled=True)
    streamlit.checkbox("Fase 2: Rigor Técnico Formal", value=streamlit.session_state.fase2_desbloqueada, disabled=True)
    streamlit.checkbox("Fase 3: Solución Práctica", value=streamlit.session_state.fase3_desbloqueada, disabled=True)
    
    # Botón para reiniciar el módulo actual
    if streamlit.button("🔄 Reiniciar Desafío Clínico"):
        streamlit.session_state.fase2_desbloqueada = False
        streamlit.session_state.fase3_desbloqueada = False
        streamlit.rerun()

    streamlit.markdown("---")
    streamlit.markdown("<p style='font-size:0.8rem; color:#A3AED0;'>Método Modular v16.0 - Sin Dependencia de API<br>© 2026 Ecosistema de Aprendizaje S.A.</p>", unsafe_allow_html=True)

# ============================================================================
# 4. ENCABEZADO DE LA PLATAFORMA
# ============================================================================
streamlit.markdown("<div class='main-title'>🧠 Ecosistema de Aprendizaje Estructurado</div>", unsafe_allow_html=True)
streamlit.markdown(f"<div class='sub-title'>Plataforma Interactiva Orientada a Soluciones Tangibles // <b>Tema: {tema}</b></div>", unsafe_allow_html=True)

# ============================================================================
# 5. CONTENIDO MODULAR: ENFOQUE EN EL ANDAMIAJE DEL OMNIPROMPT
# ============================================================================

# ----------------------------------------------------------------------------
# FASE 1: CONCEPTOS INTUITIVOS Y CLAROS (Siempre Abierta)
# ----------------------------------------------------------------------------
streamlit.markdown(
    """
    <div class='phase-box fase1'>
        <div class='titulo-fase'>💧 Fase 1: El Filtro de Agua de la Vida (Concepto Intuitivo)</div>
        <p>Imagina que los riñones de un perro son como el <b>sistema de filtración de una piscina olímpica</b>. Si la bomba de agua funciona bien, la basura se va y el agua se mantiene cristalina. Pero ¿qué pasa si una sustancia tóxica (como el anticongelante de carros o una infección grave) avienta arena dentro del motor de la bomba?</p>
        <p>El filtro se tapa de golpe. La basura (toxinas urémicas) empieza a acumularse en el agua de la piscina (la sangre), intoxicando a todo el cuerpo del animal en cuestión de horas. Esto es una <b>Insuficiencia Renal Aguda</b>: un fallo repentino del sistema de filtrado corporal.</p>
    </div>
    """, 
    unsafe_allow_html=True
)

# Reto interactivo para obligar a la demanda cognitiva (Mayéutica)
with streamlit.expander("📝 RETO COGNITIVO 1: Demuestra tu intuición para desbloquear la Fase 2"):
    streamlit.markdown("**Pregunta:** Si la 'bomba de filtración' renal falla repentinamente debido a deshidratación severa (falta de presión de agua), ¿cuál sería la consecuencia inmediata en el organismo del paciente?")
    
    r1 = streamlit.radio(
        "Selecciona la respuesta correcta analizando la analogía:",
        [
            "A) Las toxinas se eliminan más rápido por el sudor.",
            "B) El organismo acumula desechos metabólicos tóxicos en la sangre al no haber suficiente presión para filtrar.",
            "C) El riñón genera más nefronas automáticamente para compensar el flujo."
        ],
        key="radio_fase1"
    )
    
    if streamlit.button("Validar Respuesta de Fase 1"):
        if "B)" in r1:
            streamlit.success("🎉 ¡Excelente deducción clínica! Has comprendido el impacto sistémico del fallo. La Fase 2 ha sido desbloqueada.")
            streamlit.session_state.fase2_desbloqueada = True
            streamlit.rerun()
        else:
            streamlit.error("❌ Respuesta incorrecta. Piensa en la analogía de la piscina tapada: ¿Qué le pasa al agua si el filtro no tiene presión?")

# ----------------------------------------------------------------------------
# FASE 2: PUENTE DE RIGOR TÉCNICO FORMAL (Condicionada)
# ----------------------------------------------------------------------------
if streamlit.session_state.fase2_desbloqueada:
    streamlit.markdown(
        """
        <div class='phase-box fase2'>
            <div class='titulo-fase'>🔬 Fase 2: Fisiopatología de la Tasa de Filtración Glomerular (Rigor Técnico)</div>
            <p>Pasando al nivel académico formal, la Insuficiencia Renal Aguda (IRA) se caracteriza por una disminución abrupta de la <b>Tasa de Filtración Glomerular (TFG)</b>. Esto genera una retención de compuestos nitrogenados no proteicos en sangre, cuadro clínico conocido como <b>Azotemia</b>.</p>
            <p>A nivel celular, el daño ocurre principalmente en el epitelio tubular debido a procesos isquémicos o nefrotóxicos, desencadenando una <b>Necrosis Tubular Aguda (NTA)</b>. Al perderse la integridad de las células epiteliales tubulares, el filtrado glomerular se 'fuga' de regreso al intersticio renal (back-leak), lo que colapsa la presión hidrostática dentro de la cápsula de Bowman e impide por completo la formación de orina (Anuria u Oliguria).</p>
            <p><b>Marcadores bioquímicos clave en laboratorio:</b> Elevación de Creatinina sérica, Nitrógeno Ureico en Sangre (BUN) e Hiperpotasemia (acumulación crítica de Potasio K+).</p>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    with streamlit.expander("🧪 RETO COGNITIVO 2: Evalúa el rigor técnico para desbloquear la Fase Clínica 3"):
        streamlit.markdown("**Pregunta:** Desde el punto de vista fisiopatológico formal, ¿por qué la Necrosis Tubular Aguda colapsa la filtración renal?")
        
        r2 = streamlit.radio(
            "Selecciona el argumento científico exacto:",
            [
                "A) Porque las células tubulares mueren y causan una reabsorción retrógrada anómala (back-leak) del filtrado hacia el intersticio.",
                "B) Porque aumenta drásticamente la presión oncótica celular.",
                "C) Porque acelera la mitosis en las células del glomérulo de forma descontrolada."
            ],
            key="radio_fase2"
        )
        
        if streamlit.button("Validar Respuesta de Fase 2"):
            if "A)" in r2:
                streamlit.success("🚀 ¡Rigor impecable! Has dominado el concepto anatomofisiológico. La Fase de Solución Tangible está disponible.")
                streamlit.session_state.fase3_desbloqueada = True
                streamlit.rerun()
            else:
                streamlit.error("❌ Análisis incorrecto. Recuerda el concepto de 'fuga retrógrada' o 'back-leak' mencionado en el texto técnico.")

# ----------------------------------------------------------------------------
# FASE 3: SOLUCIONES TANGIBLES Y CASOS CLÍNICOS (Condicionada)
# ----------------------------------------------------------------------------
if streamlit.session_state.fase3_desbloqueada:
    streamlit.markdown(
        """
        <div class='phase-box fase3'>
            <div class='titulo-fase'>💼 Fase 3: Caso Clínico de Aplicación Real (Solución Tangible)</div>
            <p><b>Paciente:</b> Canino, Golden Retriever, Macho, 4 años. Llega a la clínica con vómitos, letargia severa y deshidratación estimada del 10%. Los dueños mencionan que accidentalmente lamió líquido del piso del cochera (sospecha de etilenglicol / anticongelante).</p>
            <p><b>Resultados de Laboratorio:</b></p>
            <ul>
                <li>Creatinina sérica: 5.8 mg/dL (Normal: 0.5 - 1.8 mg/dL) ➔ <b>Azotemia Severa</b></li>
                <li>Potasio (K+): 6.5 mEq/L (Riesgo de paro cardíaco) ➔ <b>Hiperpotasemia</b></li>
                <li>Volumen urinario: 0.2 mL/kg/h en las últimas 6 horas ➔ <b>Oliguria Crítica</b></li>
            </ul>
            <p><b>Protocolo de Intervención Tangible:</b> Fluidoterapia intravenosa agresiva inmediata con solución cristaloide isotónica para restaurar la perfusión renal, monitoreo estricto de la producción de orina mediante sonda Foley, y manejo farmacológico para proteger el miocardio de los efectos del potasio elevado.</p>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    streamlit.balloons()
    streamlit.info("🏆 **Módulo Concluido con Éxito:** Has completado el andamiaje progresivo del Protocolo Modular. Este alumno está listo para aplicar este conocimiento en un entorno veterinario real.")

streamlit.markdown(f"""
    <div class='phase-box'>
        <strong>Enfoque de Configuración Actual:</strong> Operando bajo la <strong>{fase_actual}</strong> para la disciplina de <strong>{disciplina}</strong>.
    </div>
""", unsafe_allow_html=True)

# ============================================================================
# 5. INYECCIÓN DEL OMNIPROMPT MAESTRO V15.0
# ============================================================================
OMNIPROMPT_MAESTRO = f"""
Actúas como un Tutor de Élite en la disciplina: {disciplina}. Tu objetivo es guian un aprendizaje de alta demanda cognitiva mediante el "Protocolo Modular de Alto Rendimiento", aplicando la filosofía Kaizen (mejora continua) y transformando el conocimiento en soluciones tangibles.

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
# 6. GESTIÓN DE SESIÓN PERSISTENTE (NOMECLATURA NATIVA REPARADA)
# ============================================================================
# Ajustado a la nomenclatura directa exigida por el SDK de Google
MODEL_ENGINE = "gemini-1.5-pro" 

if "chat" not in streamlit.session_state:
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
            error_msg = str(e)
            if "429" in error_msg or "quota" in error_msg.lower():
                streamlit.error("⚠️ Límite de consultas alcanzado para esta API Key. Por favor, introduce una nueva clave API válida en la barra lateral izquierda.")
            else:
                streamlit.error(f"Error de procesamiento en la simulación interactiva: {e}")
