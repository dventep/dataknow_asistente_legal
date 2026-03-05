from langchain_openai import AzureChatOpenAI
import config

def get_llm():
    """
    Crea una instancia de AzureChatOpenAI utilizando la configuración proporcionada.
    Returns:
        AzureChatOpenAI: Instancia de AzureChatOpenAI configurada.
    """
    return AzureChatOpenAI(
        azure_deployment=config.CHAT_DEPLOYMENT,
        openai_api_version="2024-02-01",
        azure_endpoint=config.OPENAI_ENDPOINT,
        api_key=config.OPENAI_KEY,
        temperature=0
    )