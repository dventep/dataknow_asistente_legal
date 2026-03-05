# ⚖️ Legal AI Assistant

Asistente conversacional basado en IA para consultar precedentes judiciales utilizando **RAG (Retrieval Augmented Generation)**.

El sistema permite realizar preguntas en lenguaje natural sobre sentencias judiciales y obtener explicaciones claras y resumidas.

---

# Arquitectura

El sistema utiliza una arquitectura RAG combinando recuperación semántica y generación de texto.

![Arquitectura compacta](https://gist.githubusercontent.com/dventep/5186ffe60f3328d9d5dd265f1adc4ae7/raw/94ce33a116094d8a0587f76c2bc42362d605adbc/Compact.jpg)

---

# Tecnologías utilizadas

- Python
- Streamlit
- Azure OpenAI
- Azure AI Search
- Azure Blob Storage
- Pandas
- LangChain

---

# Estructura del proyecto

```
Resultados
│
├── requirements.txt
│
├── src
│ ├── .streamlit
│ │ ├── config.toml
│ ├── app.py
│ ├── retriever.py
│ ├── copilot.py
│ ├── rag_evaluator.py
│ ├── data_processor.py
│ ├── embedding_service.py
│ ├── search_indexer.py
│ ├── blob_loader.py
│ └── config.py
```

---

# Flujo del sistema

1. El usuario realiza una pregunta en la interfaz.
2. Se genera un embedding de la consulta.
3. Azure AI Search recupera documentos relevantes.
4. Se construye el contexto RAG.
5. Azure OpenAI genera la respuesta.
6. Se evalúa la confiabilidad de la respuesta.

---

# Instalación

Clonar el repositorio:
```
git clone https://github.com/dventep/dataknow_asistente_legal.git
```

Instalar dependencias:
```
pip install -r requirements.txt
```

Crear archivo `.env` con las variables necesarias.

---

# Preparación del índice de búsqueda

Antes de ejecutar la aplicación es necesario indexar los documentos jurídicos en Azure AI Search.

Este proceso:

- Lee el dataset de sentencias almacenado en Azure Blob Storage
- Genera embeddings utilizando Azure OpenAI
- Crea el índice vectorial en Azure AI Search

Ejecutar:
```
python src/index_data.py
```

Este proceso solo debe ejecutarse una vez o cuando se actualicen los datos.

---

# Ejecutar la aplicación

Una vez indexados los documentos, se puede iniciar la interfaz conversacional.
```
streamlit run src/app.py
```

La aplicación estará disponible en:
```
http://localhost:8501
```

---

# Variables de entorno

El proyecto utiliza variables de entorno para credenciales de Azure:

- AZURE_OPENAI_ENDPOINT
- AZURE_OPENAI_KEY
- AZURE_OPENAI_CHAT_DEPLOYMENT
- AZURE_OPENAI_EMBEDDING_DEPLOYMENT

- AZURE_SEARCH_ENDPOINT
- AZURE_SEARCH_KEY
- AZURE_SEARCH_INDEX

- AZURE_STORAGE_CONNECTION_STRING
- AZURE_STORAGE_CONTAINER
- AZURE_STORAGE_FILE

---

# Futuras mejoras

- Despliegue en Azure Container Apps.
- Autenticación de usuarios.
- Evaluación automática del RAG.
- Dashboard de métricas.

---

# Autor

David Venté Polo