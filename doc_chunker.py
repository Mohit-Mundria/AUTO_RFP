from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from typing import Any
import numpy as np
from dotenv import load_dotenv

load_dotenv()

# In this function we chunks the document in the fixed length to process properly.
def doc_chunker(documents:list[Any])->np.ndarray:
    splitter=RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=["\n\nSECTION", "\n\n", "\n"]
    )
    # here we take only the content of the pages
    texts=[page.page_content for page in documents]
    chunks=splitter.create_documents(texts)
    print(f"The size of chunks of the documents is: {len(chunks)}")
    print("documents are: ", len(documents))
    print("text is: ",len(texts))
    print("Chunks are: ",len(chunks))
    return chunks

# def embedding(chunks:list[Any], model_name:str="models/text-embedding-004")->np.ndarray:
#     model=GoogleGenerativeAIEmbeddings(model=model_name)
#     text=[chunk.page_content for chunk in chunks]
#     print("text afetr the embedding,: ", len(text))
#     embeddings=model.embed_documents(text)
#     print(f"Successfully create the embeddings of the chunks")
#     return embeddings

