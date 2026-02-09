from pypdf import PdfReader
from langchain_core.documents import Document
from dotenv import load_dotenv
import numpy as np

load_dotenv()
# This Function is used to load the data from the given folder name, and return a documents

def data_loader(uploaded_pdfs)->np.ndarray:
    documents=[]
    
    for uploaded_file in uploaded_pdfs:
        reader=PdfReader(uploaded_file)
        for i, page in enumerate(reader.pages):
                text = page.extract_text()
                
                if text.strip(): # Only add if there's actual text
                    doc = Document(
                        page_content=text,
                        metadata={
                            "source": uploaded_file,
                            "page": i + 1
                        }
                    )
                    documents.append(doc)
    print("The upload part of the project including pdf and RFP questions is complete_________________________________________")
    return documents
    
