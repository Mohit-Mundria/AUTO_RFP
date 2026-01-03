import streamlit as st  
import time
from typing import Any
 

def render_first_page():
    st.title("🕵️ NexusAI: Enterprise RFP Security Automator")
    st.markdown("---")

    # --- TOP LEVEL VALUE PROPOSITION ---
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("The Problem")
        st.write("""
        Security RFPs are a bottleneck for Sales and Compliance teams. They involve 
        thousands of repetitive questions that require manual cross-referencing of 
        internal policies and security whitepapers. 
        
        **NexusAI reduces this 40-hour manual process to 5 minutes.**
        """)
    
    with col2:
        st.info("**Key Technologies:**\n- LangChain\n- Google Gemini 1.5\n- FAISS Vector Store\n- pypdf (Stream Processing)")

    st.markdown("### 🏗️ System Architecture & Logic")
    
    # --- TABS FOR TECHNICAL DEPTH ---
    tab1, tab2, tab3 = st.tabs(["Data Engineering", "Retrieval Logic", "LLM Pipeline"])

    with tab1:
        st.write("#### 1. In-Memory Data Ingestion")
        st.write("""
        Unlike basic scripts that rely on local file paths, this system uses **BytesIO Stream Processing**. 
        This means user data never hits the server's hard drive, ensuring better security and 
        compatibility with cloud environments.
        """)
        st.code("""
# Core Logic: Extracting from memory buffers
reader = PdfReader(uploaded_file)
for page in reader.pages:
    text += page.extract_text()
        """, language="python")

    with tab2:
        st.write("#### 2. Vector Semantic Search (FAISS)")
        st.write("""
        We use **Recursive Character Text Splitting** to maintain context. These chunks are 
        converted into 768-dimensional vectors. When a question is asked, we use 
        **Similarity Search** to find the top 'K' most relevant policy snippets.
        """)
        

    with tab3:
        st.write("#### 3. Grounded Generation")
        st.write("""
        The LLM is strictly constrained. It is instructed to *only* answer using the provided 
        context. If the information isn't in the uploaded PDFs, it will flag it as 'Not Found' 
        rather than hallucinating.
        """)

    # --- STEP-BY-STEP USER GUIDE ---
    st.markdown("---")
    st.subheader("🛠️ How to use the Tool")
    
    col_a, col_b, col_c = st.columns(3)
    col_a.markdown("**1. Upload Knowledge**\nProvide company policy PDFs or AWS/Azure security whitepapers.")
    col_b.markdown("**2. Upload RFP**\nProvide the questionnaire in .CSV format (Column 2 must be the question).")
    col_c.markdown("**3. Process & Download**\nThe system will generate answers, confidence scores, and a reason for each.")

    # --- CALL TO ACTION ---
    st.sidebar.success("Ready? Switch to 'RFP Processor' in the sidebar to start.")   
    
    
def render_second_page()->list[Any]:
    st.title("🚀 RFP Processing Engine")
    # uploaded_pdfs = None
    # uploaded_csv = None
                
    st.subheader("Step 1: Upload Knowledge Base")
    uploaded_pdfs = st.file_uploader("Upload Security Policies/Whitepapers (PDF)", type="pdf", accept_multiple_files=True)
            
    st.success(f"{len(uploaded_pdfs)} PDFs uploaded. Please upload the Company's Policy files.....")
    st.divider()
        
    st.subheader("Step 2: Upload RFP Questions")
    uploaded_csv = st.file_uploader("Upload RFP Questionnaire (CSV)", type="csv")
    return [uploaded_pdfs, uploaded_csv]

        # if uploaded_csv:
        #     df = pd.read_csv(uploaded_csv)
                    
        #     if st.button("Generate Answers"):        
        #         df=df.iloc[:,[0,1,2,3]]
        #         df.columns=["id","Question","Response", 'Confidence']
        #         st.write("Preview of Input CSV:", df.iloc[0:15,])

        #         # 'coerce' turns non-numeric strings (like "Header" or empty cells) into NaN
        #         numeric_ids = pd.to_numeric(df.iloc[:, 0], errors='coerce')
        #         # Get the index where the ID is NOT null (meaning it is a valid int or float)
        #         question_index = df[numeric_ids.notnull()].index
        #         data=data_loader(uploaded_pdfs)
        #         chunks=doc_chunker(data)
        #         retriver=retiver_fun(chunks)
                
        #         for i,index in enumerate(question_index):
        #             question=df.loc[index,"Question"]
        #              # here we generate the llm response 
        #             response=llm_response(question,retriver)
        #              # here we extract the content of the response, which is a string now. We split the string and return a list of string
        #             response=response.content.split('\n')
        #             df.at[index,"Response"]=response[2]
        #             df.at[index,"Confidence"]=response[0]+' '+(response[1])
        #             time.sleep(2) 
                
                    
                    
def download_csv(dataset):                  
    # DOWNLOAD BUTTON
    st.success("Processing Complete!")
    csv = dataset.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Answered RFP",
        data=csv,
        file_name='Answered_RFP.csv',
        mime='text/csv',
            )