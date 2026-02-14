

## 🕵️ TurboRFP: Enterprise RFP & Security Questionnaire Automator (A Business To Business Problem Solver)

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
