from pypdf import PdfReader
from langchain_core.documents import Document
from dotenv import load_dotenv
from typing import Any, List
from pathlib import Path
import numpy as np
from langchain_community.document_loaders import UnstructuredFileIOLoader

load_dotenv()
# This Function is used to load the data from the given folder name, and return a documents

def data_loader(uploaded_pdfs)->np.ndarray:
    # # here we extract the full path of the folder for windows
    # data_path=Path(path).resolve()
    # # here we list all the pdf files present in the folder
    # data_path=list(data_path.glob('**/*.pdf'))
    # print(f"The file paths for the documents: {data_path}")
    documents=[]
    
    for uploaded_file in uploaded_pdfs:
        reader=PdfReader(uploaded_file)
        for i, page in enumerate(reader.pages):
                text = page.extract_text()
                
                if text.strip(): # Only add if there's actual text
                    doc = Document(
                        page_content=text,
                        metadata={
                            "source": uploaded_file.name,
                            "page": i + 1
                        }
                    )
                    documents.append(doc)
    return documents
    
