from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from embedding_service import get_embeddings
import config

def get_search_client():
    """
    Crea una instancia de SearchClient utilizando la configuración proporcionada.
    Returns:
        SearchClient: Instancia de SearchClient configurada.
    """
    return SearchClient(
        endpoint=config.SEARCH_ENDPOINT,
        index_name=config.SEARCH_INDEX,
        credential=AzureKeyCredential(config.SEARCH_KEY)
    )

def upload_documents(docs):
    """
    Sube una lista de documentos al índice de Azure Search.
    Args:
        docs (list): Lista de documentos a subir.
    Returns:
        None
    """
    client = get_search_client()

    embedding = get_embeddings()
    embedding_docs = []
    for i, doc in enumerate(docs):
        vector = embedding.embed_query(doc["content"])
        doc["embedding"] = vector
        embedding_docs.append(doc)
        
        if i % 20 == 0:
            print(f"Procesados {i} documentos")

    client.upload_documents(embedding_docs)
    print("Documentos indexados correctamente")