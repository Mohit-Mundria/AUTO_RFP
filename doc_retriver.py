from pypdf import PdfReader
from langchain_core.documents import Document
from dotenv import load_dotenv
import numpy as np

load_dotenv()
# This Function is used to load the data from the given folder name, and return a documents

def data_loader(uploaded_pdfs)->np.ndarray:
    # # here we extract the full path of the folder for windows
    # data_path=Path(path).resolve()
    # # here we list all the pdf files present in the folder
    # data_path=list(data_path.glob('**/*.pdf'))
    # print(f"The file paths for the documents: {data_path}")
    documents=[]
    # uploaded_files=[]
    # for i in uploaded_pdfs:
    #     if isinstance(i, bytes):
    #         uploaded_file = BytesIO(i)
    
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
    
