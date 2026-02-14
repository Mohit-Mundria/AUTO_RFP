from doc_retriver import data_loader
from doc_chunker import doc_chunker
from llm_response import retiver_fun, llm_response
import time
import streamlit as st
import pandas as pd
from typing import Any
from securities import injection_detection
from frontend_code.frontend import apply_styles, render_header, render_footer, render_about, render_contact, render_home, render_result, render_upload, change_pg

def file_processing(uploaded_pdf,uploaded_csv):
    df = pd.read_csv(uploaded_csv)      
    df=df.iloc[:,[0,1,2,3]]
    df.columns=["id","Question","Response", 'Confidence']
    st.write("Preview of Input CSV:", df.iloc[0:20,])

    # 'coerce' turns non-numeric strings (like "Header" or empty cells) into NaN
    numeric_ids = pd.to_numeric(df.iloc[:, 0], errors='coerce')
    # Get the index where the ID is NOT null (meaning it is a valid int or float)
    question_index = df[numeric_ids.notnull()].index
    
    # print(f"the pdf file type is {type(uploaded_pdf)} and size is {len(uploaded_pdf)}")
    update_terminal("Sucessfully done the data preprocessing part of the RFP ques's Excel File_____________")
    
    data=data_loader(uploaded_pdf)
    update_terminal("Data Loading part is completed sucessfully..............")
    
    chunks=doc_chunker(data)
    update_terminal("Starting of Chunking of the text.............. ")

    retriver=retiver_fun(chunks)
    update_terminal("Starting generating the answers of the RFP questions___________________") 
    
    
    
             
    for i,index in enumerate(question_index):
        question=df.loc[index,"Question"]
        
        # Here we detect the prompt injection from each question. And then give to LLM.
        if injection_detection(question):
            update_terminal(f"In the current question the system detect the Prompt Injection********************************* The question: {question}")
            continue
        else:
            # here we generate the llm response 
            response=llm_response(question,retriver)
            # here we extract the content of the response, which is a string now. We split the string and return a list of string
            response=response.content.split('\n')
            df.at[index,"Response"]=response[2]
            df.at[index,"Confidence"]=response[0]+' '+(response[1])
            update_terminal(f"Generating Answers of the RFP questions.........Question no. {i+1}")
            time.sleep(10) 
                    
    return df



if 'pg' not in st.session_state:
    st.session_state.pg = 'home'
if 'processed_data' not in st.session_state:
    st.session_state.processed_data = None
apply_styles()
render_header()
if st.session_state.pg == 'home':
    render_home()
    render_footer()
elif st.session_state.pg == 'upload':
    pdf, csv = render_upload()
    
    if pdf and csv:
        if st.button("⚡ GENERATE REPORT", type="primary", use_container_width=True):
            st.markdown("### 👨‍💻 System Terminal")
            terminal_placeholder = st.empty()
            logs = []
            
            def update_terminal(text):
                logs.append(f"<div class='log-line'><span class='success-text'>➜</span> {text}</div>")
                terminal_placeholder.markdown(f"<div class='terminal-box'>{''.join(logs)}<span class='info-text'>_</span></div>", unsafe_allow_html=True)
            documents=file_processing(pdf, csv)
            st.session_state.processed_data = documents.to_csv(index=False).encode('utf-8')
            change_pg('result')
            render_footer()
            
    else:
        st.info("Please upload both files to enable report generation.")

elif st.session_state.pg == 'result':
    render_result()
    render_footer()

elif st.session_state.pg == 'about':
    render_about()
    render_footer()
    if st.button("Back"): 
        change_pg('home')
        render_footer()

elif st.session_state.pg == 'contact':
    render_contact()
    if st.button("Back"): 
        change_pg('home')
        render_footer()
    






# NOTEE: THE FOLLOWING CODE WAS CREATED TO RUN THE SCRIPT LOCALLY. HERE I MANUALLY CALL ALL THE FUNCTION AND IN RETURN IT MODIFY THE ACTUAL CSV FILE OF QUESTIONS.




            # """In the following function, we load the csv file which hold the company's question by the help of pandas.
#    Then create the resonse by the help 'llm_response' function. Then take the response and rewrite that response to the original 
#    file which hold all the questions of Company"""
   
# def load_question(path:str, chunks:list[Any])->list[Any]:
#     file_path=Path(path).resolve()
#     path=file_path.glob('*.csv')
#     for file in path:
#         df=pd.read_csv(str(file))
#         print("sucessfully load the questions file/////////////////////")
    
#         df=df.iloc[:,[0,1,2,3]]
#         df.columns=["id","Question","Response", 'Confidence']
        
#         # question_index=df[df.iloc[:,0].apply(lambda x: str(x).strip().isdigit())].index
#         # 'coerce' turns non-numeric strings (like "Header" or empty cells) into NaN
#         numeric_ids = pd.to_numeric(df.iloc[:, 0], errors='coerce')
#         # Get the index where the ID is NOT null (meaning it is a valid int or float)
#         question_index = df[numeric_ids.notnull()].index
        
#         retriver=retiver_fun(chunks)
#         print("sucessfully retrive function run ///////////////////")
        
#         for index in question_index:
#             question=df.loc[index,"Question"]
#             # here we generate the llm response 
#             response=llm_response(question,retriver)
#             # here we extract the content of the response, which is a string now. We split the string and return a list of string
#             response=response.content.split('\n')
#             df.at[index,"Response"]=response[2]
#             df.at[index,"Confidence"]=response[0]+' '+(response[1])
#             # output_file=file_path/f"processed_file"
#             print(f"RESPONSE FOR QUESTION AT INDEX: {index} of RESPONSE COLUMN: \n {response}\n\n")
#             df.to_csv(file, index=False)
#             print(f"sucessfully made changes to the file, path of file{file}")
        
#     return "SUCESSFULLY WRITE ALL THE ANSWERS/RESPONSE ALONG WITH THE CONFIDENCE SCORE IN THE COMAPNY'S FILE"   
    
# data=data_loader("dataset")
# chunks=doc_chunker(data)
# print("Sucessfully do the chunks/////////////////")

# question=load_question('Dataset',chunks)
