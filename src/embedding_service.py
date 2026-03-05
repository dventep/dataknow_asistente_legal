from langchain_openai import AzureOpenAIEmbeddings
import config

def get_embeddings():
    """
    Crea una instancia de AzureOpenAIEmbeddings utilizando la configuración proporcionada.
    Returns:
        AzureOpenAIEmbeddings: Instancia de AzureOpenAIEmbeddings configurada.
    """
    embeddings = AzureOpenAIEmbeddings(
        azure_deployment=config.EMBEDDING_DEPLOYMENT,
        openai_api_version="2024-02-01",
        azure_endpoint=config.OPENAI_ENDPOINT,
        api_key=config.OPENAI_KEY
    )
    return embeddings