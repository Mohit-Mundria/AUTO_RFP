from doc_retriver import data_loader
from doc_chunker import doc_chunker
from llm_response import retiver_fun, llm_response
import pandas as pd
from typing import Any
from pathlib import Path



def load_question(path:str)->list[Any]:
    file_path=Path(path).resolve()
    path=file_path.glob('*.csv')
    for file in path:
        file=pd.read_csv(str(file))
        print("sucessfully load the questions file.......................")
    
    
    file=file.iloc[:,[0,1,2,3]]
    file.columns=["id","Question","Response", 'Confidence']
    
    question_index=file[file.iloc[:,0].apply(lambda x: str(x).strip().isdigit())].index
    
    
    retriver=retiver_fun(chunks)
    print("sucessfully retrive function run ///////////////////")
    print(f"sucessfully call the both functions")
    
    for index in question_index:
        question=file.loc[index,"Question"]
        response=llm_response(question,retriver)
        response=response.content.split('\n')
        file.loc[index,"Response"]=response[2]
        file.loc[index,"Confidence"]=response[0]+response[1]
        output_file=file_path/f"processed_file"
        file.to_csv(output_file, index=False)
        print("sucessfully made changes to the file, path of file{output_file}")
        break
        
    return "Sucessssssssss"   
    
data=data_loader("dataset")
chunks=doc_chunker(data)
print("sucessfully do the chunks//////////")
# retiver=retiver_fun(chunks)
# print(f"sucessfully call the both functions")

question=load_question('Dataset')
