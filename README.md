

## 🕵️ TurboRFP: Enterprise RFP & Security Questionnaire Automator (A Business To Business Problem Solver)
# Live Demo of the Project: 
http://13.53.125.103/
# Running Project on Treminal Video:
https://youtu.be/srC5kR8GF-0?si=w9Dq9bfZb0DSY9mn

## 📌 The Problem: The "40-Hour" Compliance Bottleneck
Enterprise sales teams face a massive hurdle: Security RFPs. Companies must answer hundreds of complex technical questions (e.g., "How is data encrypted at rest in your DB?") by manually searching through 100+ page security policies, AWS/Azure whitepapers, and SOC2 reports.

* Manual Effort: Takes 3–5 days per RFP.
* Risk: High chance of human error/hallucination in answers.
* Scalability: Impossible to handle 10+ RFPs simultaneously without a massive team.

## 🚀 The Solution: TurboRFP
TurboRFP is an End-to-End RAG (Retrieval-Augmented Generation) Pipeline designed to automate the extraction and answering process. It transforms unstructured PDF policies into a searchable vector brain, providing grounded, high-confidence answers to CSV-based questionnaires in minutes.

**Automate your Security Questionnaires and RFPs with the power of Generative AI.**  
NexusAI is an advanced RAG (Retrieval-Augmented Generation) application designed to drastically reduce the time spent on answering Request for Information (RFI) and Request for Proposal (RFP) documents. By leveraging your internal knowledge base, it provides accurate, context-aware, and secure responses.

---

## 🏗️ Architecture

The system follows a modern RAG architecture, utilizing a hybrid cloud approach for scalability and security.

```mermaid
graph TD
    User[User (Security Officer)] -->|Uploads PDF & CSV| FE[Streamlit Frontend]
    FE -->|PDF| Ingest[Document Ingestion]
    FE -->|CSV| Proc[Question Processor]
    
    subgraph "Data Pipeline"
        Ingest -->|Chunking| Chunker[Doc Chunker]
        Chunker -->|Embed| EmbModel[Google Gemini Embeddings]
        EmbModel -->|Store/Retrieve| VectorDB[(FAISS Vector DB)]
        VectorDB <-->|Sync| S3[AWS S3 Bucket]
    end
    
    subgraph "Inference Engine"
        Proc -->|Query| RAG[RAG Chain]
        RAG -->|Retrieve Context| VectorDB
        RAG -->|Redact PII| Presidio[Microsoft Presidio]
        Presidio -->|Context + Query| LLM[Groq (Llama3/Mixtral)]
        LLM -->|Answer| Response[Generated Response]
    end
    
    Response -->|Update CSV| FE
    FE -->|Download| User
```

---
🔄 The S3-to-EC2 Data Lifecycle
1. The system ensures that the "Knowledge Brain" (FAISS Index) is persistent, scalable, and decoupled from the compute instance.
2. Ingestion & Embedding: When a document is uploaded, the RAG engine chunks the data and generates high-dimensional embeddings using the Gemini Embedding model.
3. Local Indexing: A temporary FAISS index is built in the EC2 instance's RAM and saved to the local disk.
   S3 Synchronization (s3_vectorDB.py): * Upload: Upon completion of indexing, the system triggers an automated sync, pushing the FAISS .index and metadata files to an Amazon S3 Bucket.
   Download: On service startup (systemd), the instance checks S3 for an existing index. If found, it pulls the latest vector state to the local environment, ensuring zero-knowledge loss during redeployments.
4. Query Execution: User queries are embedded and compared against the local FAISS index for sub-second retrieval, minimizing S3 latency during the inference phase.

🛠 Deployment Specifications
1. Compute: AWS EC2 (t3.medium recommended) running Ubuntu 24.04.
2. Process Management: Managed via systemd with a custom service unit for 99.9% uptime.
3. Object Storage: Amazon S3 for persistent vector store and document backups.
4. Infrastructure-as-Code: Bash-automated deployment via run_ec2.sh for one-click environment setup.

## Updates Required For Deployment over AWS
1. The Google Gemini Embedding Models have a limited usages quota only which do not satisfy the project Requirements. So I decide to change the Embedding model to BERT open source Model.
   CHANGES: 
   Remove: from langchain_google_genai import GoogleGenerativeAIEmbeddings
   Add: from langchain_huggingface import HuggingFaceEmbeddings
        model_name = "sentence-transformers/all-MiniLM-L6-v2"
        Force the model to run on the CPU (AWS Free Tier has no GPU)
        model_kwargs = {'device': 'cpu'}
        encode_kwargs = {'normalize_embeddings': True}
        return HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )
   Remove: The time.sleep() from the llm_response file, as we do not require this anymore.
   Remove: Comment Out the body of "analyze_pii_data" function in the Securities.py file. As I am using the AWS free tier account, I do not have enough resource to install the required library so comment out the             imports:
           from presidio_analyzer import AnalyzerEngine
           from presidio_anonymizer import AnonymizerEngine
   Remove: You can remove the unnecessary library from the requirements.txt
   # NOTE: 
   I am very beginner to AWS so I take help of  Gemini To deploy my Website On AWS. Also I use AI for the better UI/UX design as my main goal and efforts were to make the system/pipeline run without any error and    solve a real world problem.
   
## 🛠️ Tech Stack

This project is built using a robust selection of modern AI and web technologies:

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Frontend** | ![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white) | Interactive web interface for easy file uploads and result visualization. |
| **LLM Inference** | ![Groq](https://img.shields.io/badge/-Groq-f55036?style=flat-square) | Ultra-fast inference using open-source models (openai/gpt-oss-120b) via Groq API. |
| **Embeddings** | ![Gemini](https://img.shields.io/badge/-Google%20Gemini-4285F4?style=flat-square&logo=google&logoColor=white) | High-performance embedding generation with `models/gemini-embedding-001`. |
| **Orchestration** | ![LangChain](https://img.shields.io/badge/-LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white) | Manages the prompt engineering, retrieval chains, and LLM auditing. |
| **Vector DB** | ![FAISS](https://img.shields.io/badge/-FAISS-005A9C?style=flat-square) | Efficient similarity search for retrieving relevant documentation. |
| **Cloud Storage** | ![AWS S3](https://img.shields.io/badge/-AWS%20S3-569A31?style=flat-square&logo=amazon-s3&logoColor=white) | Persistent storage for the Vector Database to allow serverless-like scaling. |
| **Security** | ![Presidio](https://img.shields.io/badge/-Microsoft%20Presidio-0078D4?style=flat-square&logo=microsoft&logoColor=white) | Automated detection and redaction of PII (Personally Identifiable Information), Prompt Injection, LLM Auditing via confidence score|
| **Compute** | ![AWS EC2](https://img.shields.io/badge/-AWS%20EC2-FF9900?style=flat-square&logo=amazon-ec2&logoColor=white) | Hosted on scalable AWS EC2 instances for reliable availability. |

---

## ✨ Key Features

- **📄 Document Parsing**: Robustly handles PDF knowledge bases and Excel/CSV questionnaires.
- **🔍 Smart Retrieval**: Uses FAISS and Google Gemini embeddings to find the exact policy or technical spec needed.
- **🛡️ PII Protection**: Integrated PII analyzer prevents sensitive data leakage in prompts using Microsoft Presidio.
- **⚡ Blazing Fast Generation**: Powered by Groq's LPU inference engine for near-instant answers.
- **☁️ Cloud Persistent State**: Automatically syncs vector indexes to AWS S3, so knowledge is never lost between restarts.
- **💉 Prompt Injection Defense**: Basic heuristics to detect and block malicious prompt injection attempts in incoming questions.
- **📊 Confidence Scoring**: Every answer comes with a confidence score and reasoning, ensuring trutworthiness.

---

## Data Security and Integrity 
1. Prompt Injection: Implement the method that check for promot injection in every question of the RFP csv file before sending to the LLM.
2. Personally Identifiable Information(PII): Implement the method that preserve/hide the personal data of the employee and company like email, address, IP address, name etc using a python library named Microsoft Presidio.
3. Confidence Score: While generating the answer of the RFP questions, the LLM will also generate the confidence score ranging from 0 to 100 and a reason for generating that particular answer by giving the exact location of the context in policies.

## 📩 Contact
I am currently looking for roles in AI Engineering and Data Science. If you are looking for a developer who understands the intersection of AI Research and Production Stability, let's connect.

**Author:** [Mohit Mundria]  
**Email:** [mundriamohit100@gmail.com]  
**LinkedIn:** [www.linkedin.com/in/mohit-mundria-31631a322]

---
*Built with ❤️ for efficiency and security.*
