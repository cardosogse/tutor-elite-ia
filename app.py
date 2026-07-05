import streamlit as st

# 1. CONFIGURACION DEL ENTORNO
st.set_page_config(
    page_title="Tutor de Elite",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. GESTION DE ESTADOS DE SESION
if "fase" not in st.session_state:
    st.session_state.fase = 1
if "tema_actual" not in st.session_state:
    st.session_state.tema_actual = ""

# 3. CONTROL LATERAL (MENUS)
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
    
    if tema != st.session_state.tema_actual:
        st.session_state.fase = 1
        st.session_state.tema_actual = tema
        
    st.write("---")
    st.write(f"Progreso Actual: Fase {st.session_state.fase} de 3")
    
    if st.button("Reiniciar Modulo"):
        st.session_state.fase = 1
        st.rerun()

# 4. ENCABEZADO PRINCIPAL
st.title("Ecosistema de Aprendizaje Estructurado")
st.subheader(f"Modulo: {tema}")
st.write("---")

# 5. LOGICA DE DESPLIEGUE DE CONTENIDO
if "Fisiologia Renal" in tema:
    
    if st.session_state.fase >= 1:
        st.info("**Fase 1: El Filtro de Agua de la Vida (Concepto Intuitivo)**")
        st.write("Imagina que los rinones de un perro son como el sistema de filtracion de una piscina. Si la bomba funciona bien, el agua se mantiene limpia. Si una sustancia toxica arroja arena al motor, el filtro se tapa de golpe. Las toxinas se acumulan en la sangre e intoxican al animal en horas. Esto es una Insuficiencia Renal Aguda.")
        
        if st.session_state.fase == 1:
            st.write("---")
            st.write("**RETO COGNITIVO 1:** Si la bomba se queda sin presion por deshidratacion, ¿cual es la consecuencia?")
            r1_renal = st.radio(
                "Selecciona una opcion:",
                ["A) Las toxinas se eliminan mas rapido.", "B) El organismo acumula desechos toxicos en sangre por falta de filtrado.", "C) El rinon genera mas nefronas de inmediato."],
                key="key_r1_renal"
            )
            if st.button("Validar Fase 1", key="btn_f1_renal"):
                if "B)" in r1_renal:
                    st.session_state.fase = 2
                    st.rerun()
                else:
                    st.error("Respuesta incorrecta. Analiza la falta de presion en el filtro.")

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
                key="key_r2_renal"
            )
            if st.button("Validar Fase 2", key="btn_f2_renal"):
                if "A)" in r2_renal:
                    st.session_state.fase = 3
                    st.rerun()
                else:
                    st.error("Respuesta incorrecta. Revisa el concepto de back-leak.")

    if st.session_state.fase >= 3:
        st.write("---")
        st.success("**Fase 3: Caso Clinico de Aplicacion Real (Solucion Tangible)**")
        st.write("**Paciente:** Canino, Golden Retriever, 4 anos. Creatinina en 5.8 mg/dL y oliguria tras ingresar etilenglicol. **Plan de Accion:** Fluidoterapia intravenosa inmediata con soluciones cristaloides isotonicas para restablecer la perfusion glomerular y monitoreo de diuresis horaria.")
        st.balloons()

elif "Biologia Celular" in tema:
    
    if st.session_state.fase >= 1:
        st.info("**Fase 1: La Fotocopiadora Biologica Descompuesta (Concepto Intuitivo)**")
        st.write("Imagina que la division celular (mitosis) es como una fotocopiadora industrial que duplica planos. Si la maquina funciona bien, saca una copia y se apaga. Si el boton de encendido se queda trabado, saca millones de copias sin control, gastando el papel y los recursos. Eso es el cancer: celulas que olvidaron como dejar de fotocopiarse.")
        
        if st.session_state.fase == 1:
            st.write("---")
            st.write("**RETO COGNITIVO 1:** Bajo esta analogia, ¿que es un tumor maligno?")
            r1_bio = st.radio(
                "Selecciona una opcion:",
                ["A) Una celula que trabaja mas rapido para sanar.", "B) Una masa de copias celulares descontroladas que saturan el tejido sano.", "C) Un virus que detiene la producción de copias."],
                key="key_r1_bio"
            )
            if st.button("Validar Fase 1", key="btn_f1_bio"):
                if "B)" in r1_bio:
                    st.session_state.fase = 2
                    st.rerun()
                else:
                    st.error("Respuesta incorrecta. Piensa en las copias acumuladas.")

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
                key="key_r2_bio"
            )
            if st.button("Validar Fase 2", key="btn_f2_bio"):
                if "B)" in r2_bio:
                    st.session_state.fase = 3
                    st.rerun()
                else:
                    st.error("Respuesta incorrecta. Analiza el papel de las Ciclinas y CDK.")

    if st.session_state.fase >= 3:
        st.write("---")
        st.success("**Fase 3: Aplicacion Diagnostica: Citologia de Mastocitoma (Solucion Tangible)**")
        st.write("**Caso Clinico:** Canino, Boxer, Hembra, 6 anos. Masa cutanea de crecimiento acelerado. La biopsia por aspiracion muestra celulas redondas con alta relacion nucleo-citoplasma y multiples figuras mitoticas atipicas. Diagnostico: Mastocitoma Grado II. Tratamiento: Reseccion quirurgica.")
        st.balloons()
