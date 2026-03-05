from langchain_openai import AzureChatOpenAI
from llm_factory import get_llm
import config

def build_llm():
    """
    Crea una instancia de AzureChatOpenAI utilizando la configuración proporcionada.
    Returns:
        AzureChatOpenAI: Instancia de AzureChatOpenAI configurada.
    """
    llm = get_llm()
    return llm

def generate_answer(question, context, history_text=""):
    """
    Genera una respuesta a una pregunta utilizando el modelo de lenguaje y el contexto proporcionados.
    Args:        
        question (str): Pregunta a responder.
        context (str): Contexto relevante para la pregunta.
    Returns:
        str: Respuesta generada.
    """
    llm = build_llm()
    prompt = f"""
    Eres un asistente legal que explica sentencias judiciales.

    Reglas de respuesta:

    1. Responde en máximo 3 frases.
    2. Usa lenguaje sencillo.
    3. Resume la decisión principal del tribunal.
    4. No incluyas detalles extensos.

    Si el usuario pide palabras como:
    "detallar", "explicar", "profundizar", "más información"
    Entonces puedes dar una explicación más completa.

    Ten en cuenta el historial de la conversación.
    Historial:
    {history_text}

    Contexto:
    {context}

    Pregunta:
    {question}
    """
    response = llm.invoke(prompt)
    return response.content