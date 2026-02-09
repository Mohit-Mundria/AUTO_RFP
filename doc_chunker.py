from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
from typing import Any
import numpy as np
from dotenv import load_dotenv

load_dotenv()
# In this function we chunks the document in the fixed length to process properly.
def doc_chunker(documents:list[Any])->np.ndarray:
    splitter=RecursiveCharacterTextSplitter(
        chunk_size=512,
        chunk_overlap=130,
        separators=["\n\nSECTION", "\n\n", "\n"]
    )
    # here we take only the content of the pages
    texts=[page.page_content for page in documents]
    chunks=splitter.create_documents(texts)
    print(f"The size of chunks of the documents is: {len(chunks)}")
    print("The Chunking part is complete______________________________________________________________")
    return chunks

# def embedding(chunks:list[Any])->np.ndarray:
#     text=[chunk.page_content for chunk in chunks]
#     print("text afetr the embedding,: ", len(text))
#     embeddings=embedding_model.embed_documents(text)
#     print(f"Successfully create the embeddings of the chunks")
#     return embeddings

