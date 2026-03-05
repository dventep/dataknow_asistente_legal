import streamlit as st
from retriever import search
from copilot import generate_answer
from rag_evaluator import evaluate

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "last_context_docs" not in st.session_state:
    st.session_state.last_context_docs = None
    
st.set_page_config(
    page_title="Asistente Legal IA",
    page_icon="⚖️",
    layout="centered"
)

# -----------------------------
# Encabezado
# -----------------------------

st.title("⚖️ Asistente Legal Inteligente")

if st.button("🔄 Nueva conversación"):
    st.session_state.chat_history = []
    st.session_state.last_context_docs = None
    st.rerun()

st.markdown("""
Bienvenido/a. Estamos aquí para ayudarte a **entender decisiones judiciales de forma clara y sencilla**.

Puedes hacernos preguntas sobre:

- Demandas relacionadas con **redes sociales**.
- Casos de **acoso escolar**  .
- Situaciones relacionadas con **educación y PIAR**.
- Decisiones de la **Corte Constitucional**.

Nuestro objetivo es explicarte los casos **en un lenguaje fácil de entender**, incluso si no tienes conocimientos jurídicos.
""")

st.info("Escribe tu pregunta en el cuadro de abajo y te ayudaremos a encontrar la información relevante.")

# -----------------------------
# Ejemplos de preguntas
# -----------------------------

with st.expander("Ejemplos de preguntas que puedes hacer"):

    st.write("""
    - ¿Cuál fue la sentencia del caso de acoso escolar?  
    - ¿Existen casos relacionados con PIAR?  
    - ¿Qué decisiones ha tomado la Corte sobre redes sociales?  
    - Explique el caso de acoso escolar de forma sencilla.  
    - ¿Cuáles son tres demandas importantes relacionadas con educación?
    """)

# -----------------------------
# Entrada del usuario
# -----------------------------

question = st.chat_input(
    "Escribe tu pregunta"
)

# -----------------------------
# Procesamiento
# -----------------------------

if question:
    follow_up_words = ["anterior", "anteriores", "esas", "esos", "estos", "aquellos", "mencionados", "que dijiste","que mencionaste", "de esos casos", "de esas demandas", "explica más", "detalla", "profundiza"]
    q = question.lower()
    use_previous_context = any(word in q for word in follow_up_words)
    
    st.session_state.chat_history.append({
        "role": "user",
        "content": question
    })

    history_text = ""
    for msg in st.session_state.chat_history[-4:]:
        history_text += f"{msg['role']}: {msg['content']}\n"        

    with st.spinner("🔎 Analizando jurisprudencia y precedentes..."):
        if use_previous_context and st.session_state.last_context_docs:
            context_docs = st.session_state.last_context_docs
        else:
            context_docs = search(question)
            st.session_state.last_context_docs = context_docs

        context = "\n\n".join([doc["content"] for doc in context_docs])
        answer = generate_answer(question, context, history_text)
        evaluation = evaluate(question, answer, context)
    st.divider()

    st.session_state.chat_history.append({
        "role": "assistant",
        "content": answer
    })

    # -----------------------------
    # Respuesta
    # -----------------------------

    with st.chat_message("assistant"):
        st.write(answer)

    # -----------------------------
    # Evaluación del sistema
    # -----------------------------

    st.subheader("- Confiabilidad de la respuesta")
    st.write(evaluation)

    # -----------------------------
    # Mensaje de apoyo
    # -----------------------------

    st.info("""
    ℹ️ Esta explicación se genera automáticamente a partir de precedentes judiciales.

    Aunque intentamos ofrecer información clara y útil, esta herramienta **no reemplaza la asesoría de un abogado profesional**.
    """)

    # -----------------------------
    # Continuar la conversación
    # -----------------------------

    st.markdown("""
    💬 Si quieres profundizar más, puedes hacer otra pregunta relacionada con este tema.
    Estoy aquí para ayudarte.
    """)