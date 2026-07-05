import streamlit as st

# ============================================================================
# 1. CONFIGURACION DEL ENTORNO
# ============================================================================
st.set_page_config(
    page_title="Tutor de Elite",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# 2. GESTION DE ESTADOS DE SESION (PERSISTENCIA DE DATOS)
# ============================================================================
if "fase" not in st.session_state:
    st.session_state.fase = 1
if "tema_actual" not in st.session_state:
    st.session_state.tema_actual = ""

# ============================================================================
# 3. BARRA LATERAL (CONTROL DE MENUS Y PROGRESO)
# ============================================================================
with st.sidebar:
    st.header("Tutor de Elite IA")
    st.write("---")
    
    disciplina = st.selectbox(
        "Disciplina Cientifica:",
        ["Medicina Veterinaria y Zootecnia", "Biologia Celular y Molecular"]
    )
    
    if disciplina == "Medicina Veterinaria y Zootecnia":
        opciones = ["Fisiologia Renal: Insuficiencia Renal Aguda"]
    else:
        opciones = ["Biologia Celular: Mitosis y Cancer Canino"]
        
    tema = st.selectbox("Modulo Clinico:", opciones)
    
    # Si el alumno cambia de tema, se reinicia el progreso a la Fase 1
    if tema != st.session_state.tema_actual:
        st.session_state.fase = 1
        st.session_state.tema_actual = tema
        
    st.write("---")
    st.write(f"**Progreso del Alumno:** Fase {st.session_state.fase} de 3")
    
    if st.button("Reiniciar Modulo"):
        st.session_state.fase = 1
        st.rerun()

# ============================================================================
# 4. CUERPO PRINCIPAL DE LA PLATAFORMA
# ============================================================================
st.title("Ecosistema de Aprendizaje Estructurado")
st.subheader(f"Modulo Actual: {tema}")
st.write("---")

# ============================================================================
# 5. RUTA: MEDICINA VETERINARIA - FISIOLOGIA RENAL
# ============================================================================
if "Fisiologia Renal" in tema:
    
    # --- FASE 1 ---
    if st.session_state.fase >= 1:
        st.info("**Fase 1: El Filtro de Agua de la Vida (Concepto Intuitivo)**")
        st.write("Imagina que los rinones de un perro son como el sistema de filtracion de una piscina. Si la bomba funciona bien, el agua se mantiene limpia. Si una sustancia toxica arroja arena al motor, el filtro se tapa de golpe. Las toxinas se acumulan en la sangre e intoxican al animal en horas. Esto es una Insuficiencia Renal Aguda.")
        
        if st.session_state.fase == 1:
            st.write("---")
            st.write("**RETO COGNITIVO 1:** Si la bomba se queda sin presion por deshidratacion, ¿cual es la consecuencia?")
            r1_renal = st.radio(
                "Selecciona una opcion:",
                ["A) Las toxinas se eliminan mas rapido.", "B) El organismo acumula desechos toxicos en sangre por falta de filtrado.", "C) El rinon genera mas nefronas de inmediato."],
                key="radio_renal_1"
            )
            if st.button("Validar Fase 1", key="btn_renal_1"):
                if "B)" in r1_renal:
                    st.session_state.fase = 2
                    st.rerun()
                else:
                    st.error("Respuesta incorrecta. Analiza la falta de presion en el filtro.")

    # --- FASE 2 ---
    if st.session_state.fase >= 2:
        st.write("---")
        st.warning("**Fase 2: Fisiopatologia de la Tasa de Filtracion Glomerular (Rigor Tecnico)**")
        st.write("La Insuficiencia Renal Aguda se caracteriza por una caida abrupta de la Tasa de Filtracion Glomerular (TFG), desencadenando Azotemia. A nivel epitelial ocurre una Necrosis Tubular Aguda (NTA), donde el filtrado celular sufre una fuga retrograda (back-leak), colapsando la presion hidrostatica dentro de la capsula de Bowman.")
        
        if st.session_state.fase == 2:
            st.write("---")
            st.write("**RETO COGNITIVO 2:** ¿Por que la Necrosis Tubular Aguda colapsa la filtracion?")
            r2_renal = st.radio(
                "Selecciona una opcion:",
                ["A) Por una reabsorcion retrograda anomala (back-leak) del filtrado hacia el intersticio.", "B) Por aumento de la presion oncotica.", "C) Por aceleracion mitotica."],
                key="radio_renal_2"
            )
            if st.button("Validar Fase 2", key="btn_renal_2"):
                if "A)" in r2_renal:
                    st.session_state.fase = 3
                    st.rerun()
                else:
                    st.error("Respuesta incorrecta. Revisa el concepto de back-leak.")

    # --- FASE 3 ---
    if st.session_state.fase >= 3:
        st.write("---")
        st.success("**Fase 3: Caso Clinico de Aplicacion Real (Solucion Tangible)**")
        st.write("**Paciente:** Canino, Golden Retriever, 4 anos. Creatinina en 5.8 mg/dL y oliguria tras ingresar etilenglicol. **Plan de Accion:** Fluidoterapia intravenosa inmediata con soluciones cristaloides isotonicas para restablecer la perfusion glomerular y monitoreo de diuresis horaria.")
        st.balloons()

# ============================================================================
# 6. RUTA: BIOLOGIA CELULAR Y MOLECULAR
# ============================================================================
elif "Biologia Celular" in tema:
    
    # --- FASE 1 ---
    if st.session_state.fase >= 1:
        st.info("**Fase 1: La Fotocopiadora Biologica Descompuesta (Concepto Intuitivo)**")
        st.write("Imagina que la division celular (mitosis) es como una fotocopiadora industrial que duplica planos. Si la maquina funciona bien, saca una copia y se apaga. Si el boton de encendido se queda trabado, saca millones de copias sin control, gastando el papel y los recursos. Eso es el cancer: celulas que olvidaron como dejar de fotocopiarse.")
        
        if st.session_state.fase == 1:
            st.write("---")
            st.write("**RETO COGNITIVO 1:** Bajo esta analogia, ¿que es un tumor maligno?")
            r1_bio = st.radio(
                "Selecciona una opcion:",
                ["A) Una celula que trabaja mas rapido para sanar.", "B) Una masa de copias celulares descontroladas que saturan el tejido sano.", "C) Un virus que detiene la produccion de copias."],
                key="radio_bio_1"
            )
            if st.button("Validar Fase 1", key="btn_bio_1"):
                if "B)" in r1_bio:
                    st.session_state.fase = 2
                    st.rerun()
                else:
                    st.error("Respuesta incorrecta. Piensa en las copias acumuladas.")

    # --- FASE 2 ---
    if st.session_state.fase >= 2:
        st.write("---")
        st.warning("**Fase 2: Control del Ciclo Celular y Complejos Ciclina-CDK (Rigor Tecnico)**")
        st.write("La replicacion descontrolada se debe a mutaciones en los genes que regulan los puntos de control (checkpoints) del ciclo celular, especificamente la transicion G1 a S. Las celulas neoplasicas presentan sobreexpresion de Ciclinas y Cinasas dependientes (CDK), evadiendo la Apoptosis regulada por el gen p53.")
        
        if st.session_state.fase == 2:
            st.write("---")
            st.write("**RETO COGNITIVO 2:** ¿Que alteracion molecular promueve el desarrollo de este cancer?")
            r2_bio = st.radio(
                "Selecciona una opcion:",
                ["A) La activacion exacerbada de la apoptosis.", "B) La perdida de control en los checkpoints por desregulacion de complejos Ciclina-CDK.", "C) El aumento de la presion osmotica."],
                key="radio
