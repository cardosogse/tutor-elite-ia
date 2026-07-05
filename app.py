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
        st.info("**Fase 1: La Fotocopiadora Biologica Descompuesta (Concepto Intuitivo)**")
        st.write("Imagina que la division celular (mitosis) es como una fotocopiadora industrial que duplica planos. Si la maquina funciona bien, saca una copia y se apaga. Si el boton de encendido se queda trabado, saca millones de copias sin control, gastando el papel y los recursos. Eso es el cancer: celulas que olvidaron como dejar de fotocopiarse.")
        
        if st.session_state.fase == 1:
            st.write("---")
            st.write("**RETO COGNITIVO 1:** Bajo esta analogia, ¿que es un tumor maligno?")
            r1_b = st.radio(
                "Selecciona una opcion:",
                ["A) Una celula que trabaja mas rapido para sanar.", "B) Una masa de copias celulares descontroladas que saturan el tejido sano.", "C) Un virus que detiene la produccion de copias."],
                key="r1_bio"
            )
            if st.button("Validar Fase 1"):
                if "B)" in r1_b:
                    st.session_state.st_fase = 2 # fallback analogo interno
                    st.session_state.fase = 2
                    st.rerun()
                else:
                    st.error("Respuesta incorrecta. Piensa en las copias acumuladas.")

    # CONTENIDO FASE 2
    if st.session_state.fase >= 2:
        st.write("---")
        st.warning("**Fase 2: Control del Ciclo Celular y Complejos Ciclina-CDK (Rigor Tecnico)**")
        st.write("La replicacion descontrolada se debe a mutaciones en los genes que regulan los puntos de control (checkpoints) del ciclo celular, especificamente la transicion G1 a S. Las celulas neoplasicas presentan sobreexpresion de Ciclinas y Cinasas dependientes (CDK), evadiendo la Apoptosis regulada por el gen p53.")
        
        if st.session_state.fase == 2:
            st.write("---")
            st.write("**RETO COGNITIVO 2:** ¿Que alteracion molecular promueve el desarrollo de este cancer?")
            r2_b = st.radio(
                "Selecciona una opcion:",
                ["A) La activacion exacerbada de la apoptosis.", "B) La perdida de control en los checkpoints por desregulacion de complejos Ciclina-CDK.", "C) El aumento de la presion osmotica."],
                key="r2_bio"
            )
            if st.button("Validar Fase 2"):
                if "B)" in r2_b:
                    st.session_state.fase = 3
                    st.rerun()
                else:
                    st.error("Respuesta incorrecta. Analiza el papel de las Ciclinas y CDK.")

    # CONTENIDO FASE 3
    if st.session_state.fase >= 3:
        st.write("---")
        st.success("**Fase 3: Aplicacion Diagnostica: Citologia de Mastocitoma (Solucion Tangible)**")
        st.write("**Caso Clinico:** Canino, Boxer, Hembra, 6 anos. Masa cutanea de crecimiento acelerado. La biopsia por aspiracion muestra celulas redondas con alta relacion nucleo-citoplasma y multiples figuras mitoticas atipicas. Diagnostico: Mastocitoma Grado II. Tratamiento: Reseccion quirurgica.")
        st.balloons()
        )
        if streamlit.button("Validar Fase 1", key="btn_r1"):
            if "B)" in r1:
                streamlit.success("Excelente! Fase 2 desbloqueada.")
                streamlit.session_state.fase2_desbloqueada = True
                streamlit.rerun()
            else:
                streamlit.error("Incorrecto. Analiza la falta de filtracion.")

    # FASE 2
    if streamlit.session_state.fase2_desbloqueada:
        streamlit.markdown("""
            <div class='phase-box fase2'>
                <div class='titulo-fase'>[Fase 2] Fisiopatologia de la Tasa de Filtracion Glomerular (Rigor Tecnico)</div>
                <p>La Insuficiencia Renal Aguda se caracteriza por una caida abrupta de la <b>Tasa de Filtracion Glomerular (TFG)</b>, desencadenando <b>Azotemia</b>. A nivel epitelial, ocurre una <b>Necrosis Tubular Aguda (NTA)</b>, donde el filtrado celular sufre una fuga retrograda (back-leak), colapsando la presion hidrostatica glomerular.</p>
            </div>
        """, unsafe_allow_html=True)
        
        with streamlit.expander("RETO COGNITIVO 2: Evalua el rigor tecnico para desbloquear la Fase 3"):
            r2 = streamlit.radio(
                "¿Por que la Necrosis Tubular Aguda colapsa la filtracion renal?",
                ["A) Por una reabsorcion retrograda anomala (back-leak) del filtrado hacia el intersticio.", "B) Por aumento drastico de la presion oncotica celular.", "C) Por aceleracion mitotica."],
                key="renal_r2"
            )
            if streamlit.button("Validar Fase 2", key="btn_r2"):
                if "A)" in r2:
                    streamlit.success("Rigor impecable! Fase 3 desbloqueada.")
                    streamlit.session_state.fase3_desbloqueada = True
                    streamlit.rerun()
                else:
                    streamlit.error("Incorrecto. Revisa el concepto de back-leak.")

    # FASE 3
    if streamlit.session_state.fase3_desbloqueada:
        streamlit.markdown("""
            <div class='phase-box fase3'>
                <div class='titulo-fase'>[Fase 3] Caso Clinico de Aplicacion Real (Solucion Tangible)</div>
                <p><b>Paciente:</b> Canino, Golden Retriever, 4 anos. Creatinina en 5.8 mg/dL y oliguria tras ingerir etilenglicol. <b>Plan de Accion:</b> Fluidoterapia intravenosa inmediata con soluciones cristaloides isotonicas para restablecer la perfusion glomerular y monitoreo de diuresis horaria.</p>
            </div>
        """, unsafe_allow_html=True)
        streamlit.balloons()

# ----------------------------------------------------------------------------
# CASO 2: BIOLOGÍA CELULAR Y MITOSIS
# ----------------------------------------------------------------------------
elif "Biologia Celular" in tema:
    # FASE 1
    streamlit.markdown("""
        <div class='phase-box fase1'>
            <div class='titulo-fase'>[Fase 1] La Fotocopiadora Biologica Descompuesta (Concepto Intuitivo)</div>
            <p>Imagina que la division celular (mitosis) es como una <b>fotocopiadora industrial</b> que duplica los planos de un edificio. Si la fotocopiadora funciona bien, saca una copia identica y se apaga. Pero ¿que pasa si el boton de encendido se queda trabado y la maquina empieza a sacar millones de copias sin control, gastando todo el papel y la luz de la oficina?</p>
            <p>Eso es un <b>tumor o cancer canino</b>: celulas rebeldes que olvidaron como dejar de fotocopiarse a si mismas, acumulandose y robando la energia y nutrientes de los tejidos sanos del perro.</p>
        </div>
    """, unsafe_allow_html=True)

    with streamlit.expander("RETO COGNITIVO 1: Demuestra tu intuicion para desbloquear la Fase 2"):
        r1_bio = streamlit.radio(
            "Bajo esta analogia, ¿que es un tumor maligno a nivel tisular?",
            ["A) Una celula que decidio trabajar mas rapido para sanar un tejido.", "B) Una masa de copias celulares descontroladas que saturan y destruyen el espacio de las celulas sanas.", "C) Un virus que detiene la produccion de copias."],
            key="bio_r1"
        )
        if streamlit.button("Validar Fase 1", key="btn_bio1"):
            if "B)" in r1_bio:
                streamlit.success("Excelente analogia comprendida! El puente al rigor tecnico formal de la mitosis esta abierto.")
                streamlit.session_state.fase2_desbloqueada = True
                streamlit.rerun()
            else:
                streamlit.error("Incorrecto. Piensa en la fotocopiadora atascada llenando la oficina de papel inservible.")

    # FASE 2
    if streamlit.session_state.fase2_desbloqueada:
        streamlit.markdown("""
            <div class='phase-box fase2'>
                <div class='titulo-fase'>[Fase 2] Control del Ciclo Celular y Complejos Ciclina-CDK (Rigor Tecnico)</div>
                <p>En la oncologia molecular veterinaria, la replicacion descontrolada se debe a mutaciones en los genes que regulan los <b>puntos de control (checkpoints)</b> del ciclo celular, especificamente la transicion de la fase <b>G1 a S</b>. Las celulas neoplasicas presentan una sobreexpresion de las proteinas llamadas <b>Ciclinas</b> y sus cinasas dependientes (CDK).</p>
                <p>Al alterarse esta maquinaria enzimatica, la celula evade la senal de detencion celular y entra en una <b>mitosis perpetua</b>, evadiendo los mecanismos de muerte celular programada o <b>Apoptosis</b> guiados normalmente por el gen supresor tumoral p53.</p>
            </div>
        """, unsafe_allow_html=True)
        
        with streamlit.expander("RETO COGNITIVO 2: Evalua el rigor tecnico para desbloquear la Fase 3"):
            r2_bio = streamlit.radio(
                "¿Que alteracion bioquimica molecular promueve el desarrollo del cancer celular canino?",
                ["A) La activacion exacerbada de los mecanismos de apoptosis celular.", "B) La perdida de control en los checkpoints (G1 a S) por desregulacion de complejos Ciclina-CDK.", "C) El aumento de la presion osmotica mitocondrial."],
                key="bio_r2"
            )
            if streamlit.button("Validar Fase 2", key="btn_bio2"):
                if "B)" in r2_bio:
                    streamlit.success("Brillante analisis bioanalitico! Has desbloqueado la fase de solucion diagnostica real.")
                    streamlit.session_state.fase3_desbloqueada = True
                    streamlit.rerun()
                else:
                    streamlit.error("Incorrecto. Analiza el papel de los checkpoints celulares.")

    # FASE 3
    if streamlit.session_state.fase3_desbloqueada:
        streamlit.markdown("""
            <div class='phase-box fase3'>
                <div class='titulo-fase'>[Fase 3] Aplicacion Diagnostica: Citologia de Mastocitoma Canino (Solucion Tangible)</div>
                <p><b>Caso Clinico:</b> Paciente Canino, Boxer, Hembra, 6 anos. Presenta una masa cutanea de consistencia firme en la region costal izquierda de crecimiento acelerado en el ultimo mes.</p>
                <p><b>Diagnostico por Solucion Tangible:</b> Se realiza una Biopsia por Aspiracion con Aguja Delgada (BAAD). Al microscopio se observa una poblacion homogenea de celulas redondas con alta <b>relacion nucleo-citoplasma</b>, multiples figuras mitoticas atipicas (celulas dividiendose aberrantemente) y granulacion metacromatica intensa. Diagnostico definitivo: <b>Mastocitoma Grado II</b>. El tratamiento requiere reseccion quirurgica con margenes limpios e histopatologia inmediata.</p>
            </div>
        """, unsafe_allow_html=True)
        streamlit.balloons()
        )
        if streamlit.button("Validar Fase 1", key="btn_r1"):
            if "B)" in r1:
                streamlit.success("🎉 ¡Excelente! Fase 2 desbloqueada.")
                streamlit.session_state.fase2_desbloqueada = True
                streamlit.rerun()
            else:
                streamlit.error("❌ Incorrecto. Analiza la falta de filtración.")

    # FASE 2
    if streamlit.session_state.fase2_desbloqueada:
        streamlit.markdown("""
            <div class='phase-box fase2'>
                <div class='titulo-fase'>[Fase 2] Fisiopatología de la Tasa de Filtración Glomerular (Rigor Técnico)</div>
                <p>La Insuficiencia Renal Aguda se caracteriza por una caída abrupta de la <b>Tasa de Filtración Glomerular (TFG)</b>, desencadenando <b>Azotemia</b>. A nivel epitelial, ocurre una <b>Necrosis Tubular Aguda (NTA)</b>, donde el filtrado celular sufre una fuga retrógrada (back-leak), colapsando la presión hidrostática glomerular.</p>
            </div>
        """, unsafe_allow_html=True)
        
        with streamlit.expander("🧪 RETO COGNITIVO 2: Evalúa el rigor técnico para desbloquear la Fase 3"):
            r2 = streamlit.radio(
                "¿Por qué la Necrosis Tubular Aguda colapsa la filtración renal?",
                ["A) Por una reabsorción retrógrada anómala (back-leak) del filtrado hacia el intersticio.", "B) Por aumento drástico de la presión oncótica celular.", "C) Por aceleración mitótica."],
                key="renal_r2"
            )
            if streamlit.button("Validar Fase 2", key="btn_r2"):
                if "A)" in r2:
                    streamlit.success("🚀 ¡Rigor impecable! Fase 3 desbloqueada.")
                    streamlit.session_state.fase3_desbloqueada = True
                    streamlit.rerun()
                else:
                    streamlit.error("❌ Incorrecto. Revisa el concepto de back-leak.")

    # FASE 3
    if streamlit.session_state.fase3_desbloqueada:
        streamlit.markdown("""
            <div class='phase-box fase3'>
                <div class='titulo-fase'>[Fase 3] Caso Clínico de Aplicación Real (Solución Tangible)</div>
                <p><b>Paciente:</b> Canino, Golden Retriever, 4 años. Creatinina en 5.8 mg/dL y oliguria tras ingerir etilenglicol. <b>Plan de Acción:</b> Fluidoterapia intravenosa inmediata con soluciones cristaloides isotónicas para restablecer la perfusión glomerular y monitoreo de diuresis horaria.</p>
            </div>
        """, unsafe_allow_html=True)
        streamlit.balloons()

# ----------------------------------------------------------------------------
# CASO 2: BIOLOGÍA CELULAR Y MITOSIS
# ----------------------------------------------------------------------------
elif "Biología Celular" in tema:
    # FASE 1
    streamlit.markdown("""
        <div class='phase-box fase1'>
            <div class='titulo-fase'>[Fase 1] La Fotocopiadora Biológica Descompuesta (Concepto Intuitivo)</div>
            <p>Imagina que la división celular (mitosis) es como una <b>fotocopiadora industrial</b> que duplica los planos de un edificio. Si la fotocopiadora funciona bien, saca una copia idéntica y se apaga. Pero ¿qué pasa si el botón de encendido se queda trabado y la máquina empieza a sacar millones de copias sin control, gastando todo el papel y la luz de la oficina?</p>
            <p>Eso es un <b>tumor o cáncer canino</b>: células rebeldes que olvidaron cómo dejar de fotocopiarse a sí mismas, acumulándose y robando la energía y nutrientes de los tejidos sanos del perro.</p>
        </div>
    """, unsafe_allow_html=True)

    with streamlit.expander("📝 RETO COGNITIVO 1: Demuestra tu intuición para desbloquear la Fase 2"):
        r1_bio = streamlit.radio(
            "Bajo esta analogía, ¿qué es un tumor maligno a nivel tisular?",
            ["A) Una célula que decidió trabajar más rápido para sanar un tejido.", "B) Una masa de copias celulares descontroladas que saturan y destruyen el espacio de las células sanas.", "C) Un virus que detiene la producción de copias."],
            key="bio_r1"
        )
        if streamlit.button("Validar Fase 1", key="btn_bio1"):
            if "B)" in r1_bio:
                streamlit.success("🎉 ¡Excelente analogía comprendida! El puente al rigor técnico formal de la mitosis está abierto.")
                streamlit.session_state.fase2_desbloqueada = True
                streamlit.rerun()
            else:
                streamlit.error("❌ Incorrecto. Piensa en la fotocopiadora atascada llenando la oficina de papel inservible.")

    # FASE 2
    if streamlit.session_state.fase2_desbloqueada:
        streamlit.markdown("""
            <div class='phase-box fase2
        )
        if streamlit.button("Validar Fase 1", key="btn_r1"):
            if "B)" in r1:
                streamlit.success("🎉 ¡Excelente! Fase 2 desbloqueada.")
                streamlit.session_state.fase2_desbloqueada = True
                streamlit.rerun()
            else:
                streamlit.error("❌ Incorrecto. Analiza la falta de filtración.")

    # FASE 2
    if streamlit.session_state.fase2_desbloqueada:
        streamlit.markdown("""
            <div class='phase-box fase2'>
                <div class='titulo-fase'>🔬 Fase 2: Fisiopatología de la Tasa de Filtración Glomerular (Rigor Técnico)</div>
                <p>La Insuficiencia Renal Aguda se caracteriza por una caída abrupta de la <b>Tasa de Filtración Glomerular (TFG)</b>, desencadenando <b>Azotemia</b>. A nivel epitelial, ocurre una <b>Necrosis Tubular Aguda (NTA)</b>, donde el filtrado celular sufre una fuga retrógrada (back-leak), colapsando la presión hidrostática glomerular.</p>
            </div>
        """, unsafe_allow_html=True)
        
        with streamlit.expander("🧪 RETO COGNITIVO 2: Evalúa el rigor técnico para desbloquear la Fase 3"):
            r2 = streamlit.radio(
                "¿Por qué la Necrosis Tubular Aguda colapsa la filtración renal?",
                ["A) Por una reabsorción retrógrada anómala (back-leak) del filtrado hacia el intersticio.", "B) Por aumento drástico de la presión oncótica celular.", "C) Por aceleración mitótica."],
                key="renal_r2"
            )
            if streamlit.button("Validar Fase 2", key="btn_r2"):
                if "A)" in r2:
                    streamlit.success("🚀 ¡Rigor impecable! Fase 3 desbloqueada.")
                    streamlit.session_state.fase3_desbloqueada = True
                    streamlit.rerun()
                else:
                    streamlit.error("❌ Incorrecto. Revisa el concepto de back-leak.")

    # FASE 3
    if streamlit.session_state.fase3_desbloqueada:
        streamlit.markdown("""
            <div class='phase-box fase3'>
        )
        if streamlit.button("Validar Fase 1", key="btn_r1"):
            if "B)" in r1:
                streamlit.success("🎉 ¡Excelente! Fase 2 desbloqueada.")
                streamlit.session_state.fase2_desbloqueada = True
                streamlit.rerun()
            else:
                streamlit.error("❌ Incorrecto. Analiza la falta de filtración.")

    # FASE 2
    if streamlit.session_state.fase2_desbloqueada:
        streamlit.markdown("""
            <div class='phase-box fase2'>
                <div class='titulo-fase'>🔬 Fase 2: Fisiopatología de la Tasa de Filtración Glomerular (Rigor Técnico)</div>
                <p>La Insuficiencia Renal Aguda se caracteriza por una caída abrupta de la <b>Tasa de Filtración Glomerular (TFG)</b>, desencadenando <b>Azotemia</b>. A nivel epitelial, ocurre una <b>Necrosis Tubular Aguda (NTA)</b>, donde el filtrado celular sufre una fuga retrógrada (back-leak), colapsando la presión hidrostática glomerular.</p>
            </div>
        """, unsafe_allow_html=True)
        
        with streamlit.expander("🧪 RETO COGNITIVO 2: Evalúa el rigor técnico para desbloquear la Fase 3"):
            r2 = streamlit.radio(
                "¿Por qué la Necrosis Tubular Aguda colapsa la filtración renal?",
                ["A) Por una reabsorción retrógrada anómala (back-leak) del filtrado hacia el intersticio.", "B) Por aumento drástico de la presión oncótica celular.", "C) Por aceleración mitótica."],
                key="renal_r2"
            )
            if streamlit.button("Validar Fase 2", key="btn_r2"):
                if "A)" in r2:
                    streamlit.success("🚀 ¡Rigor impecable! Fase 3 desbloqueada.")
                    streamlit.session_state.fase3_desbloqueada = True
                    streamlit.rerun()
                else:
                    streamlit.error("❌ Incorrecto. Revisa el concepto de back-leak.")

    # FASE 3
    if streamlit.session_state.fase3_desbloqueada:
        streamlit.markdown("""
            <div class='phase-box fase3'>
                <div class='titulo-fase'>💼 Fase 3: Caso Clínico de Aplicación Real (Solución Tangible)</div>
                <p><b>Paciente:</b> Canino, Golden Retriever, 4 años. Creatinina en 5.8 mg/dL y oliguria tras ingerir etilenglicol. <b>Plan de Acción:</b> Fluidoterapia intravenosa inmediata con soluciones cristaloides isotónicas para restablecer la perfusión glomerular y monitoreo de diuresis horaria.</p>
            </div>
        """, unsafe_allow_html=True)
        streamlit.balloons()

# ----------------------------------------------------------------------------
# CASO 2: BIOLOGÍA CELULAR Y MITOSIS
# ----------------------------------------------------------------------------
elif "Biología Celular" in tema:
    # FASE 1
    streamlit.markdown("""
        <div class='phase-box fase1'>
            <div class='titulo-fase'>🧬 Fase 1: La Fotocopiadora Biológica Descompuesta (Concepto Intuitivo)</div>
            <p>Imagina que la división celular (mitosis) es como una <b>fotocopiadora industrial</b> que duplica los planos de un edificio. Si la fotocopiadora funciona bien, saca una copia idéntica y se apaga. Pero ¿qué pasa si el botón de encendido se queda trabado y la máquina empieza a sacar millones de copias sin control, gastando todo el papel y la luz de la oficina?</p>
            <p>Eso es un <b>tumor o cáncer canino</b>: células rebeldes que olvidaron cómo dejar de fotocopiarse a sí mismas, acumulándose y robando la energía y nutrientes de los tejidos sanos del perro.</p>
        </div>
    """, unsafe_allow_html=True)

    with streamlit.expander("📝 RETO COGNITIVO 1: Demuestra tu intuición para desbloquear la Fase 2"):
        r1_bio = streamlit.radio(
            "Bajo esta analogía, ¿qué es un tumor maligno a nivel tisular?",
            ["A) Una célula que decidió trabajar más rápido para sanar un tejido.", "B) Una masa de copias celulares descontroladas que saturan y destruyen el espacio de las células sanas.", "C) Un virus que detiene la producción de copias."],
            key="bio_r1"
        )
        if streamlit.button("Validar Fase 1", key="btn_bio1"):
            if "B)" in r1_bio:
                streamlit.success("🎉 ¡Excelente analogía comprendida! El puente al rigor técnico formal de la mitosis está abierto.")
                streamlit.session_state.fase2_desbloqueada = True
                streamlit.rerun()
            else:
                streamlit.error("❌ Incorrecto. Piensa en la fotocopiadora atascada llenando la oficina de papel inservible.")

    # FASE 2
    if streamlit.session_state.fase2_desbloqueada:
        streamlit.markdown("""
            <div class='phase-box fase2'>
                <div class='titulo-fase'>🔬 Fase 2: Control del Ciclo Celular y Complejos Ciclina-CDK (Rigor Técnico)</div>
                <p>En la oncología molecular veterinaria, la replicación descontrolada se debe a mutaciones en los genes que regulan los <b>puntos de control (checkpoints)</b> del ciclo celular, específicamente la transición de la fase <b>G1 a S</b>. Las células neoplásicas presentan una sobreexpresión de las proteínas llamadas <b>Ciclinas</b> y sus cinasas dependientes (CDK).</p>
                <p>Al alterarse esta maquinaria enzimática, la célula evade la señal de detención celular y entra en una <b>mitosis perpetua</b>, evadiendo los mecanismos de muerte celular programada o <b>Apoptosis</b> guiados normalmente por el gen supresor tumoral p53.</p>
            </div>
        """, unsafe_allow_html=True)
        
        with streamlit.expander("🧪 RETO COGNITIVO 2: Evalúa el rigor técnico para desbloquear la Fase 3"):
            r2_bio = streamlit.radio(
                "¿Qué alteración bioquímica molecular promueve el desarrollo del cáncer celular canino?",
                ["A) La activación exacerbada de los mecanismos de apoptosis celular.", "B) La pérdida de control en los checkpoints (G1 a S) por desregulación de complejos Ciclina-CDK.", "C) El aumento de la presión osmótica mitocondrial."],
                key="bio_r2"
            )
            if streamlit.button("Validar Fase 2", key="btn_bio2"):
                if "B)" in r2_bio:
                    streamlit.success("🚀 ¡Brillante análisis bioanalítico! Has desbloqueado la fase de solución diagnóstica real.")
                    streamlit.session_state.fase3_desbloqueada = True
                    streamlit.rerun()
                else:
                    streamlit.error("❌ Incorrecto. Si la apoptosis se activa, la célula tumoral moriría o la presión osmótica no es el factor central. Relee con atención el texto molecular.")

    # FASE 3
    if streamlit.session_state.fase3_desbloqueada:
        streamlit.markdown("""
            <div class='phase-box fase3'>
                <div class='titulo-fase'>💼 Fase 3: Aplicación Diagnóstica: Citología de Mastocitoma Canino (Solución Tangible)</div>
                <p><b>Caso Clínico:</b> Paciente Canino, Bóxer, Hembra, 6 años. Presenta una masa cutánea de consistencia firme en la región costal izquierda de crecimiento acelerado en el último mes.</p>
                <p><b>Diagnóstico por Solución Tangible:</b> Se realiza una Biopsia por Aspiración con Aguja Delgada (BAAD). Al microscopio se observa una población homogénea de células redondas con alta <b>relación núcleo-citoplasma</b>, múltiples figuras mitóticas atípicas (células dividiéndose aberrantemente) y granulación metacromática intensa. Diagnóstico definitivo: <b>Mastocitoma Grado II</b>. El tratamiento requiere resección quirúrgica con márgenes limpios e histopatología inmediata.</p>
            </div>
        """, unsafe_allow_html=True)
        streamlit.balloons()
        )
        if streamlit.button("Validar Fase 1", key="btn_r1"):
            if "B)" in r1:
                streamlit.success("🎉 ¡Excelente! Fase 2 desbloqueada.")
                streamlit.session_state.fase2_desbloqueada = True
                streamlit.rerun()
            else:
                streamlit.error("❌ Incorrecto. Analiza la falta de filtración.")

    # FASE 2
    if streamlit.session_state.fase2_desbloqueada:
        streamlit.markdown("""
            <div class='phase-box fase2'>
                <div class='titulo-fase'>🔬 Fase 2: Fisiopatología de la Tasa de Filtración Glomerular (Rigor Técnico)</div>
                <p>La Insuficiencia Renal Aguda se caracteriza por una caída abrupta de la <b>Tasa de Filtración Glomerular (TFG)</b>, desencadenando <b>Azotemia</b>. A nivel epitelial, ocurre una <b>Necrosis Tubular Aguda (NTA)</b>, donde el filtrado celular sufre una fuga retrógrada (back-leak), colapsando la presión hidrostática glomerular.</p>
            </div>
        """, unsafe_allow_html=True)
        
        with streamlit.expander("🧪 RETO COGNITIVO 2: Evalúa el rigor técnico para desbloquear la Fase 3"):
            r2 = streamlit.radio(
                "¿Por qué la Necrosis Tubular Aguda colapsa la filtración renal?",
                ["A) Por una reabsorción retrógrada anómala (back-leak) del filtrado hacia el intersticio.", "B) Por aumento drástico de la presión oncótica celular.", "C) Por aceleración mitótica."],
                key="renal_r2"
            )
            if streamlit.button("Validar Fase 2", key="btn_r2"):
                if "A)" in r2:
                    streamlit.success("🚀 ¡Rigor impecable! Fase 3 desbloqueada.")
                    streamlit.session_state.fase3_desbloqueada = True
                    streamlit.rerun()
                else:
                    streamlit.error("❌ Incorrecto. Revisa el concepto de back-leak.")

    # FASE 3
    if streamlit.session_state.fase3_desbloqueada:
        streamlit.markdown("""
            <div class='phase-box fase3'>
                <div class='titulo-fase'>💼 Fase 3: Caso Clínico de Aplicación Real (Solución Tangible)</div>
                <p><b>Paciente:</b> Canino, Golden Retriever, 4 años. Creatinina en 5.8 mg/dL y oliguria tras ingerir etilenglicol. <b>Plan de Acción:</b> Fluidoterapia intravenosa inmediata con soluciones cristaloides isotónicas para restablecer la perfusión glomerular y monitoreo de diuresis horaria.</p>
            </div>
        """, unsafe_allow_html=True)
        streamlit.balloons()

# ----------------------------------------------------------------------------
# CASO 2: BIOLOGÍA CELULAR Y MITOSIS (EL TEMA DE TU CAPTURA DE PANTALLA)
# ----------------------------------------------------------------------------
elif "Biología Celular" in tema:
    # FASE 1
    streamlit.markdown("""
        <div class='phase-box fase1'>
            <div class='titulo-fase'>🧬 Fase 1: La Fotocopiadora Biológica Descompuesta (Concepto Intuitivo)</div>
            <p>Imagina que la división celular (mitosis) es como una <b>fotocopiadora industrial</b> que duplica los planos de un edificio. Si la fotocopiadora funciona bien, saca una copia idéntica y se apaga. Pero ¿qué pasa si el botón de encendido se queda trabado y la máquina empieza a sacar millones de copias sin control, gastando todo el papel y la luz de la oficina?</p>
            <p>Eso es un <b>tumor o cáncer canino</b>: células rebeldes que olvidaron cómo dejar de fotocopiarse a sí mismas, acumulándose y robando la energía y nutrientes de los tejidos sanos del perro.</p>
        </div>
    """, unsafe_allow_html=True)

    with streamlit.expander("📝 RETO COGNITIVO 1: Demuestra tu intuición para desbloquear la Fase 2"):
        r1_bio = streamlit.radio(
            "Bajo esta analogía, ¿qué es un tumor maligno a nivel tisular?",
            ["A) Una célula que decidió trabajar más rápido para sanar un tejido.", "B) Una masa de copias celulares descontroladas que saturan y destruyen el espacio de las células sanas.", "C) Un virus que detiene la producción de copias."],
            key="bio_r1"
        )
        if streamlit.button("Validar Fase 1", key="btn_bio1"):
            if "B)" in r1_bio:
                streamlit.success("🎉 ¡Excelente analogía comprendida! El puente al rigor técnico formal de la mitosis está abierto.")
                streamlit.session_state.fase2_desbloqueada = True
                streamlit.rerun()
            else:
                streamlit.error("❌ Incorrecto. Piensa en la fotocopiadora atascada llenando la oficina de papel inservible.")

    # FASE 2
    if streamlit.session_state.fase2_desbloqueada:
        streamlit.markdown("""
            <div class='phase-box fase2'>
                <div class='titulo-fase'>🔬 Fase 2: Control del Ciclo Celular y Complejos Ciclina-CDK (Rigor Técnico)</div>
                <p>En la oncología molecular veterinaria, la replicación descontrolada se debe a mutaciones en los genes que regulan los <b>puntos de control (checkpoints)</b> del ciclo celular, específicamente la transición de la fase <b>G1 a S</b>. Las células neoplásicas presentan una sobreexpresión de las proteínas llamadas <b>Ciclinas</b> y sus cinasas dependientes (CDK).</p>
                <p>Al alterarse esta maquinaria enzimática, la célula evade la señal de detención celular y entra en una <b>mitosis perpetua</b>, evadiendo los mecanismos de muerte celular programada o <b>Apoptosis</b> guiados normalmente por el gen supresor tumoral p53.</p>
            </div>
        """, unsafe_allow_html=True)
        
        with streamlit.expander("🧪 RETO COGNITIVO 2: Evalúa el rigor técnico para desbloquear la Fase 3"):
            r2_bio = streamlit.radio(
                "¿Qué alteración bioquímica molecular promueve el desarrollo del cáncer celular canino?",
                ["A) La activación exacerbada de los mecanismos de apoptosis celular.", "B) La pérdida de control en los checkpoints (G1 a S) por desregulación de complejos Ciclina-CDK.", "C) El aumento de la presión osmótica mitocondrial."],
                key="bio_r2"
            )
            if streamlit.button("Validar Fase 2", key="btn_bio2"):
                if "A)" in r2_bio:
                    streamlit.error("❌ Incorrecto. Si la apoptosis se activa, la célula tumoral moriría. Relee con atención el texto molecular.")
                elif "B)" in r2_bio:
                    streamlit.success("🚀 ¡Brillante análisis bioanalítico! Has desbloqueado la fase de solución diagnóstica real.")
                    streamlit.session_state.fase3_desbloqueada = True
                    streamlit.rerun()

    # FASE 3
    if streamlit.session_state.fase3_desbloqueada:
        streamlit.markdown("""
            <div class='phase-box fase3'>
                <div class='titulo-fase'>💼 Fase 3: Aplicación Diagnóstica: Citología de Mastocitoma Canino (Solución Tangible)</div>
                <p><b>Caso Clínico:</b> Paciente Canino, Bóxer, Hembra, 6 años. Presenta una masa cutánea de consistencia firme en la región costal izquierda de crecimiento acelerado en el último mes.</p>
                <p><b>Diagnóstico por Solución Tangible:</b> Se realiza una Biopsia por Aspiración con Aguja Delgada (BAAD). Al microscopio se observa una población homogénea de células redondas con alta <b>relación núcleo-citoplasma</b>, múltiples figuras mitóticas atípicas (células dividiéndose aberrantemente) y granulación metacromática intensa. Diagnóstico definitivo: <b>Mastocitoma Grado II</b>. El tratamiento requiere resección quirúrgica con márgenes limpios e histopatología inmediata.</p>
            </div>
        """, unsafe_allow_html=True)
        streamlit.balloons()
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
