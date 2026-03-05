from azure.storage.blob import BlobServiceClient
import pandas as pd
import io
import config

def load_excel():
    """
    Carga el archivo Excel desde Azure Blob Storage y lo convierte en un DataFrame de pandas.
    Returns:
        DataFrame: DataFrame con los datos del archivo Excel.
    """
    blob_service = BlobServiceClient.from_connection_string(
        config.STORAGE_CONNECTION
    )
    blob_client = blob_service.get_blob_client(
        config.STORAGE_CONTAINER,
        config.STORAGE_FILE
    )
    data = blob_client.download_blob().readall()
    data_df = pd.read_excel(io.BytesIO(data))
    return data_df