from langchain_community.document_loaders import PyMuPDFLoader
from dotenv import load_dotenv
from typing import Any, List
from pathlib import Path
import numpy as np

load_dotenv()

def data_loader(path:str)->np.ndarray:
    data_path=Path(path).resolve()
    
    data_path=list(data_path.glob('**/*.pdf'))
    print(f"The file paths for the documents: {data_path}")
    documents=[]
    
    
    for i in data_path:
        loader=PyMuPDFLoader(str(i))
        loaded=loader.load()
        documents.extend(loaded)
    
    
    print(f"The Documents are successfully loaded, the size of documents is {len(documents)}")
    return documents
    
    
# print(data_loader("Dataset"))