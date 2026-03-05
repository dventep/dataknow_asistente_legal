"""
Archivo principal para cargar datos, procesarlos y subirlos al índice de búsqueda.

Este script realiza las siguientes tareas:
1. Carga el archivo Excel desde Azure Blob Storage utilizando la función `load_excel`.
2. Construye una lista de documentos a partir del DataFrame utilizando la función `build_documents`.
3. Sube los documentos al índice de Azure Search utilizando la función `upload_documents`.

Cada documento contiene el contenido formateado y metadatos relevantes para las sentencias judiciales.
"""
from blob_loader import load_excel
from data_processor import build_documents
from search_indexer import upload_documents

print("Cargando Excel desde Azure Blob Storage...")

data_df = load_excel()
print(f"Registros encontrados: {len(data_df)}")
docs = build_documents(data_df)
upload_documents(docs)

print("Indexación completada.")