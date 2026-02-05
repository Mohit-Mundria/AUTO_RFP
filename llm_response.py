from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from typing import Any
from dotenv import load_dotenv
import os
load_dotenv()

# Here we load all the required models of Google Gemini
# model=OpenAI(model='openai/gpt-oss-120b', temperature=0.5)
model=ChatOpenAI(
    base_url="https://api.groq.com/openai/v1",
    model="openai/gpt-oss-120b"
)
embedding_model=GoogleGenerativeAIEmbeddings(model='models/text-embedding-004',transport="rest")
# model=ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite',temperature=0.6)
db_path="faiss.index"

# In the following function we perform embedding, and then store that in the Vector Database and then create a retriver object
def retiver_fun(embedding:list[Any]):
    db_path="faiss.index"
    if os.path.exists(db_path):
        vector_db=FAISS.load_local(db_path,embedding_model,allow_dangerous_deserialization=True)
        print("sucessfully load the vector database which alreday present")
    else:
        print("Vector store is not present, creating vectorDatabase............")
        vector_db=FAISS.from_documents(embedding,embedding_model)
        vector_db.save_local(db_path)
        print("save fresh new data vector.......at given location.............")
    retriver=vector_db.as_retriever(search_type='similarity', search_kwargs={'k':8})
    return retriver



# In the following function, we take the query and then the retriver retrive the relevent context for the llm to generate a accurate response
def llm_response(query:str,retriver):
    # here the retriver retrive the context and combine them in a single string
    context=retriver.invoke(query)
    content='\n\n'.join(page.page_content for page in context)
    
    prompt = PromptTemplate(template="""You are the NexusAI Security Compliance Officer. Your goal is to answer RFP (Request for Proposal)"
    "questions accurately using ONLY the provided context from our internal security policies and AWS whitepapers."
    "\n\n"
    "STRICT RULES FOR YOUR RESPONSE:"
    "1. USE ONLY THE CONTEXT PROVIDED: Do not use outside knowledge. If the context does not contain the answer, "
    "state: 'Information not found in current policy documentation.'"
    "2. BE FACTUAL AND CONCISE: Use professional, technical language. Avoid fluff or 'marketing speak'."
    "3. CITE THE SECTION: If the context mentions a section number (e.g., Section 4.2), include it in your answer."
    "4. NO HALLUCINATION: If the question asks for a specific number (like RTO/RPO) and it's not in the context, "
    "5. Length Awareness: THE LENGTH OF THE RESPONSE SHOULD BE UNDER 4 SENTENCES ONLY. MAXIMUM RESPONSE LENGHT IS 5 SENTENCES",
    "6. SCORING CRITERIA:
        - 90-100: Answer is explicitly stated in the context.
        - 70-89: Answer is strongly implied or split across sections.
        - 50-69: Answer is partially present but requires minor inference.
        - Below 50: Context is vague or only tangentially related.
        STRICT OUTPUT FORMAT:
        Confidence Score: [0-100]
        Reason for Score: [One brief sentence]
        Answer: [Your 1-5 sentence response]
    "do not guess."
    "\n\n"
    "CONTEXT FROM POLICY DOCUMENTS:"
    "\n{context},
    The Question/Query is: {question}
    """,
    input_variables=['context', 'question'])
    # here we made our final prompt with the given query and the retrived context
    final_prompt=prompt.invoke({'context':content, 'question':query})
    
    response=model.invoke(final_prompt)
    
    return response
    
    
    

    