def build_documents(df):
    """
    Construye una lista de documentos a partir del DataFrame.
    Cada documento es un diccionario con el contenido formateado y metadatos.
    Args:
        df (pd.DataFrame): DataFrame con los datos de las sentencias.
    Returns:
        list: Lista de documentos formateados.
    """
    docs = []
    for _, row in df.iterrows():
        subject = str(row["Tema - subtema"])
        if subject == "nan":
            subject = "No especificado"

        content = f"""
        Descripción del caso:
        {row['sintesis']}

        Decisión del tribunal:
        {row['resuelve']}

        Tema jurídico:
        {subject}

        Providencia:
        {row['Providencia']}
        """.strip()
        docs.append({
            "id": str(row["#"]),
            "content": content,
            "providencia": str(row["Providencia"]),
            "tema": subject
        })
    return docs