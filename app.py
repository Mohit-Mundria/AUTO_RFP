from doc_retriver import data_loader
from doc_chunker import doc_chunker
from llm_response import retiver_fun, llm_response
import pandas as pd
from typing import Any
from pathlib import Path



"""In the following function, we load the csv file which hold the company's question by the help of pandas.
   Then create the resonse by the help 'llm_response' function. Then take the response and rewrite that response to the original 
   file which hold all the questions of Company"""
   
def load_question(path:str, chunks:list[Any])->list[Any]:
    file_path=Path(path).resolve()
    path=file_path.glob('*.csv')
    for file in path:
        df=pd.read_csv(str(file))
        print("sucessfully load the questions file/////////////////////")
    
        df=df.iloc[:,[0,1,2,3]]
        df.columns=["id","Question","Response", 'Confidence']
        
        # question_index=df[df.iloc[:,0].apply(lambda x: str(x).strip().isdigit())].index
        # 'coerce' turns non-numeric strings (like "Header" or empty cells) into NaN
        numeric_ids = pd.to_numeric(df.iloc[:, 0], errors='coerce')
        # Get the index where the ID is NOT null (meaning it is a valid int or float)
        question_index = df[numeric_ids.notnull()].index
        
        retriver=retiver_fun(chunks)
        print("sucessfully retrive function run ///////////////////")
        
        for index in question_index:
            question=df.loc[index,"Question"]
            # here we generate the llm response 
            response=llm_response(question,retriver)
            # here we extract the content of the response, which is a string now. We split the string and return a list of string
            response=response.content.split('\n')
            df.at[index,"Response"]=response[2]
            df.at[index,"Confidence"]=response[0]+' '+(response[1])
            # output_file=file_path/f"processed_file"
            print(f"RESPONSE FOR QUESTION AT INDEX: {index} of RESPONSE COLUMN: \n {response}\n\n")
            df.to_csv(file, index=False)
            print(f"sucessfully made changes to the file, path of file{file}")
        
    return "SUCESSFULLY WRITE ALL THE ANSWERS/RESPONSE ALONG WITH THE CONFIDENCE SCORE IN THE COMAPNY'S FILE"   
    
data=data_loader("dataset")
chunks=doc_chunker(data)
print("Sucessfully do the chunks/////////////////")

question=load_question('Dataset',chunks)
