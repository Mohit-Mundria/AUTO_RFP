# 🕵️ NexusAI: Enterprise RFP & Security Questionnaire Automator (A Business To Business Problem Solver)
# 📌 The Problem: The "40-Hour" Compliance Bottleneck
Enterprise sales teams face a massive hurdle: Security RFPs. Companies must answer hundreds of complex technical questions (e.g., "How is data encrypted at rest in your DB?") by manually searching through 100+ page security policies, AWS/Azure whitepapers, and SOC2 reports.

* Manual Effort: Takes 3–5 days per RFP.
* Risk: High chance of human error/hallucination in answers.
* Scalability: Impossible to handle 10+ RFPs simultaneously without a massive team.

# 🚀 The Solution: NexusAI
NexusAI is an End-to-End RAG (Retrieval-Augmented Generation) Pipeline designed to automate the extraction and answering process. It transforms unstructured PDF policies into a searchable vector brain, providing grounded, high-confidence answers to CSV-based questionnaires in minutes.

# 🛠️ System Architecture & Logic Flow
The project is built using a Decoupled Architecture, separating the UI (Streamlit), the Orchestration (App Controller), and the Brain (RAG Engine).

# 1. In-Memory Data Ingestion (Engineering Effort)
* Most beginner projects rely on local folder paths. NexusAI uses Stream-based Processing.
  Logic: Files are handled as BytesIO streams. This ensures the app is cloud-ready and doesn't require a local file system (essential for Docker and Streamlit Cloud).
  Library: pypdf for lightweight, dependency-free PDF extraction.

# 2. The RAG Pipeline (The "Brain")
* Chunking Strategy: Uses RecursiveCharacterTextSplitter with an overlap of 200 tokens.
  Why? To preserve context across page breaks and ensure the embedding captures the full meaning of technical clauses.
* Vector Store: FAISS (Facebook AI Similarity Search).
  Logic: Converts text chunks into high-dimensional vectors. It uses Cosine Similarity to find the most relevant policy text for every RFP question.

* Embeddings: Google Generative AI Embeddings (models/embedding-001).

# 3. LLM Pipeline & Grounded Generation
* Model: Google Gemini 1.5 Flash (optimized for speed and long-context window).
* The "Zero-Hallucination" Prompt: The system uses a strict system prompt. If the answer is not found in the vector search results, the LLM is forced to state "Information not found" rather than guessing.
* Rate-Limit Handling: Custom logic built to handle the Gemini Free Tier constraints, including time.sleep intervals and error-retry logic to ensure the pipeline doesn't crash during long CSV processing.

# 🏗️ Technical Stack
Category       ->      Technology
Interface      ->      Streamlit (Multi-page Architecture)
Orchestration  ->      LangChain
LLM            ->      Google Gemini 1.5 Flash
Vector DB      ->      FAISS
Data Handling  ->      Pandas (Vectorized CSV processing)
Environment    ->      Docker (Containerized for portability)
Automation     ->      GitHub Actions (CI/CD Linting)

# 📈 Key Engineering Highlights
* Memory Optimization: Implemented a generator-based callback system to update the UI progress bar without blocking the main execution thread.
* Robust Error Handling: Added pd.to_numeric coercion to handle messy CSV inputs (headers, empty rows, or non-numeric IDs) without crashing the loop.
* Separation of Concerns: The project follows a strict directory structure:
* frontend_code/: Pure UI logic.
* core/: Pure RAG and LLM logic.
* app.py: Controller managing the data flow.


# Manual Setup
1. Clone the repo: git clone https://github.com/your-username/AUTO_RFP.git
2. Install dependencies: pip install -r requirements.txt
3. Set up your .env file with GOOGLE_API_KEY.
4. Run the app: streamlit run app.py

# 👨‍💻 Logic Deep Dive: Why This Works
Developer Note: The hardest part of this project wasn't the AI—it was the data flow. Transitioning from a local script that "looks at a folder" to a web app that "receives bytes" required a complete refactor of the ingestion logic. This ensures that the system is scalable and can be deployed on any server architecture without modification.

# 🛑 Troubleshooting & System Resilience
In a production environment, external APIs and data formats are the primary points of failure. NexusAI is designed with the following safety nets:

1. Gemini API Rate Limiting (Error 429)
Problem: The Google Gemini Free Tier is restricted to a limited number of Requests Per Minute (RPM). Solution: * The system implements a 2-second mandatory cooldown between queries to avoid hitting the 429 threshold.
Recruiter Note: If you encounter a "Resource Exhausted" error during large CSV processing, the system will pause. In a professional setting, this would be handled by a Celery task queue with exponential backoff, but for this MVP, it is managed via a synchronized sleep loop to ensure stability without cost.

2. PDF Parsing Failures
Problem: Some PDFs are "Scanned Images" (OCR required) rather than "Digital Text." Solution:
Currently, the system uses pypdf for fast, digital text extraction.
If text extraction returns 0 pages: Ensure the PDF is not password-protected or a raw image scan. For production-grade OCR, the roadmap includes integrating pdfplumber or pytesseract.

3. CSV Alignment Issues
Problem: The system expects the CSV to follow a specific structure (ID, Question, Response, Confidence). Solution:
I implemented Pandas Column Mapping logic using df.iloc. Even if the user provides extra columns, the system extracts only the top 4 relevant indices.
Constraint: If the second column (Index 1) does not contain the "Question text," the LLM will receive garbage data. Always ensure your CSV matches the provided template in the /samples folder.
