from azure.search.documents import SearchClient
from azure.search.documents.models import VectorizedQuery
from azure.core.credentials import AzureKeyCredential
from embedding_service import get_embeddings
import config

def expand_query(query):
    q = query.lower()
    if "piar" in q:
        query += " educación inclusiva plan individual de ajustes razonables"
    return query

def search(query):

    client = SearchClient(
        endpoint=config.SEARCH_ENDPOINT,
        index_name=config.SEARCH_INDEX,
        credential=AzureKeyCredential(config.SEARCH_KEY)
    )
    query = expand_query(query)

    embeddings = get_embeddings()
    vector = embeddings.embed_query(query)
    vector_query = VectorizedQuery(
        vector=vector,
        k_nearest_neighbors=4,
        fields="embedding"
    )

    results = client.search(
        search_text=query,
        vector_queries=[vector_query],
        top=4
    )
    docs = []
    for result in results:
        docs.append({
            "content": result["content"],
            "providencia": result["providencia"],
            "tema": result["tema"]
        })
    return docs