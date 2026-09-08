import streamlit as st

st.set_page_config(page_title="SentenciaClara", page_icon="⚖️", layout="centered")

st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>⚖️ SentenciaClara</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #4B5563;'>Tu sentencia judicial en español cotidiano · Pontificia Universidad Javeriana</p>", unsafe_allow_html=True)

st.warning("⚠️ **Aviso Legal:** Esta herramienta es un ejercicio académico. No constituye asesoría legal ni sustituye la consulta con un abogado.")

st.markdown("### 📝 Pega tu sentencia o elige un ejemplo:")

col1, col2, col3 = st.columns(3)
ejemplo = ""
if col1.button("🩺 Ejemplo Salud EPS"):
    ejemplo = "PRIMERO: TUTELAR el derecho a la salud de Pedro Gómez. SEGUNDO: ORDENAR a EPS SANITAS que en 48 horas autorice la cirugía y garantice el tratamiento integral. TERCERO: Prevenir sobre sanciones por desacato."
if col2.button("🏠 Ejemplo Arriendo"):
    ejemplo = "PRIMERO: DECLARAR IMPROCEDENTE la acción de tutela instaurada contra Carlos Restrepo por no satisfacer el principio de subsidiariedad al contar con la jurisdicción ordinaria civil."
if col3.button("📦 Medicina Entregada"):
    ejemplo = "PRIMERO: DECLARAR la carencia actual de objeto por hecho superado dentro de la tutela contra EPS SURA, toda vez que el medicamento fue suministrado durante el trámite."

sentencia_input = st.text_area("Texto de la sentencia (Resuelve):", value=ejemplo, height=130)

def traducir(texto):
    t = texto.lower()
    if "hecho superado" in t or "carencia" in t:
        return ("⚪ Carencia de Objeto (Hecho Superado)", "El caso está CERRADO porque la entidad ya cumplió lo pedido antes de la sentencia.", ["No hay órdenes pendientes inmediatas."], ["1. Guarda una copia de este fallo.", "2. Si vuelven a suspenderte el servicio, podrás acudir nuevamente al juez."])
    elif "improcedente" in t or "subsidiariedad" in t:
        return ("🟡 Tutela Improcedente (Vía Incorrecta)", "El juez no revisó el fondo porque la tutela no es para este tipo de conflictos; debes ir a la justicia ordinaria.", ["No se dieron órdenes contra el demandado en tutela."], ["1. Tienes 3 DÍAS HÁBILES para impugnar (apelar) si crees que hubo error.", "2. Acude a un consultorio jurídico para presentar la demanda ante un juez civil."])
    elif "tutelar" in t or "conceder" in t:
        return ("🟢 ¡Amparo Concedido! (Ganaste)", "El juez protegió tus derechos y le dio una orden obligatoria a la entidad demandada.", ["La entidad debe cumplir lo ordenado.", "Plazo: 48 horas hábiles desde la notificación.", "Garantía de tratamiento integral sin trabas."], ["1. Lleva copia de este fallo a la entidad hoy mismo.", "2. Si en 48 horas hábiles no cumplen, solicita un Incidente de Desacato en el juzgado."])
    elif "negar" in t:
        return ("🔴 Tutela Negada", "El juez consideró que no se probó la vulneración a los derechos fundamentales en este momento.", ["No se emitieron órdenes a favor del accionante."], ["1. ¡URGENTE! Tienes exactamente 3 DÍAS HÁBILES desde la notificación para impugnar.", "2. Si no impugnas, el caso va a la Corte Constitucional para eventual revisión."])
    else:
        return ("📄 Decisión Judicial", "Revisa las órdenes y plazos de tu documento.", ["Verificar fecha de notificación oficial."], ["1. Exige el cumplimiento en el plazo fijado.", "2. Recuerda el plazo de 3 días para impugnar si no estás conforme."])

if st.button("✨ Traducir a Lenguaje Ciudadano", type="primary", use_container_width=True):
    if sentencia_input.strip():
        tipo, res, ordenes, ruta = traducir(sentencia_input)
        st.subheader(tipo)
        st.success(res)
        st.markdown("#### 📋 ¿Qué ordenó el juez y en qué plazo?")
        for o in ordenes:
            st.markdown(f"- ✅ {o}")
        st.markdown("#### 🚶 Tu Ruta de Acción Inmediata:")
        for r in ruta:
            st.info(r)
        st.caption("📚 *Fundamentado en el Decreto 2591 de 1991 y la Sentencia T-262 de 2022.*")
