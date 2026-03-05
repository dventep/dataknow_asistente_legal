from langchain_openai import AzureChatOpenAI
from llm_factory import get_llm
import config

def evaluate(question, answer, context):
    """
    Evalúa si la respuesta está basada en el contexto utilizando un modelo de lenguaje.
    Args:
        question (str): Pregunta a evaluar.
        answer (str): Respuesta a evaluar.
        context (str): Contexto relevante para la pregunta y respuesta.
    Returns:
        str: Resultado de la evaluación.
    """
    llm = get_llm()
    prompt = f"""
    Evalúa si la respuesta está basada en el contexto.

    Pregunta:
    {question}

    Respuesta:
    {answer}

    Contexto:
    {context}

    Devuelve:

    SCORE (0-1)
    JUSTIFICACION
    """
    result = llm.invoke(prompt)
    return result.content