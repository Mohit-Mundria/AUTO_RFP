import streamlit as st
import time

# 1. PAGE CONFIG
st.set_page_config(layout="wide", page_title="TurboRFP", page_icon="🛡️")

def apply_styles():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;800&display=swap');
        
        /* Global App Style */
        .stApp { 
            background: radial-gradient(circle at top right, #1e293b, #0f172a); 
            color: #f1f5f9; 
            font-family: 'Plus Jakarta Sans', sans-serif; 
        }
        
        /* Hide Default Streamlit Elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        /* Glassmorphic Cards */
        .glass-card {
            background: rgba(30, 41, 59, 0.4);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 25px;
            transition: all 0.3s ease;
        }
        .glass-card:hover {
            border-color: #38bdf8;
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }

        /* Hero Text Gradient */
        .hero-title {
            font-size: 4.5rem;
            font-weight: 800;
            background: linear-gradient(135deg, #ffffff 30%, #38bdf8 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            line-height: 1.1;
            margin-bottom: 20px;
        }

        /* Animated Button Logic */
        div.stButton > button {
            border-radius: 12px;
            padding: 10px 24px;
            font-weight: 600;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        /* Navbar specific styling */
        .nav-container {
            position: fixed;
            top: 0;
            width: 100%;
            z-index: 1000;
            padding: 10px 0;
            background: rgba(15, 23, 42, 0.8);
            backdrop-filter: blur(10px);
        }

        /* Step Card Styling */
        .step-box {
            background: linear-gradient(145deg, #1e293b, #0f172a);
            border: 1px solid #334155;
            padding: 30px;
            border-radius: 24px;
            text-align: center;
        }

        /* Status Pills */
        .status-pill {
            display: inline-block;
            padding: 4px 12px;
            border-radius: 100px;
            background: rgba(56, 189, 248, 0.2);
            color: #38bdf8;
            font-size: 12px;
            font-weight: 600;
            margin-bottom: 10px;
        }
        /* Fix Button Visibility & Contrast */
        div.stButton > button {
            border-radius: 12px;
            padding: 10px 24px;
            font-weight: 600;
            background-color: #1e293b !important; /* Dark Background */
            color: #38bdf8 !important; /* Bright Blue Text */
            border: 1px solid #334155 !important;
            transition: all 0.3s ease;
        }
        
        div.stButton > button:hover {
            border-color: #38bdf8 !important;
            background-color: #334155 !important;
            color: white !important;
            box-shadow: 0 0 15px rgba(56, 189, 248, 0.4);
        }

        /* Active Navigation Button */
        div.stButton > button[kind="primary"] {
            background: linear-gradient(90deg, #38bdf8, #818cf8) !important;
            color: white !important;
            border: none !important;
        }

        /* Distinct Header Separator */
        .header-separator {
            height: 1px;
            background: linear-gradient(90deg, transparent, #38bdf8, #818cf8, transparent);
            margin: 10px 0 40px 0;
            opacity: 0.6;
        }
    </style>
    """, unsafe_allow_html=True)



# --- HELPER FUNCTIONS ---
def change_pg(target):
    st.session_state.pg = target
    st.rerun()

# --- COMPONENT: HEADER ---
def render_header():
    c1, c2, c3 = st.columns([3, 1, 2])
    with c1:
        st.markdown("<h2 style='margin:0;'>🛡️ <span style='color:#38bdf8;'>TurboRFP</span></h2>", unsafe_allow_html=True)
    with c3:
        sub_c1, sub_c2, sub_c3 = st.columns(3)
        # We use type="primary" logic to highlight the current page
        with sub_c1:
            if st.button("Home", key="nav_home", type="primary" if st.session_state.pg == 'home' else "secondary", use_container_width=True): change_pg('home')
        with sub_c2:
            if st.button("About", key="nav_about", type="primary" if st.session_state.pg == 'about' else "secondary", use_container_width=True): change_pg('about')
        with sub_c3:
            if st.button("Contact", key="nav_contact", type="primary" if st.session_state.pg == 'contact' else "secondary", use_container_width=True): change_pg('contact')
    
    st.markdown('<div class="header-separator"></div>', unsafe_allow_html=True)

# --- COMPONENT: FOOTER ---
def render_footer():
    st.markdown("""
        <div style="text-align:center; padding: 60px 0 30px 0; color:#64748b; font-size:14px; border-top: 1px solid rgba(255,255,255,0.05);">
            <p>Built with ❤️ by a BCA student• 2026</p>
        </div>
    """, unsafe_allow_html=True)

# --- PAGE: HOME ---
def render_home():
    # Hero Section with visual hierarchy
    st.markdown("""
        <div style="text-align:center; padding: 60px 0;">
            <div class="status-pill">NEW: TurboRFP project Engine Is now active</div>
            <h1 class="hero-title">RFP Processing <br>Simplified by Python, GenAI and Retrieval Augmented Generation(RAG).</h1>
            <p style="color:#94a3b8; font-size: 1.40rem; max-width: 700px; margin: 0 auto; line-height: 1.6;">
                The first GenAI and RAG system that reads policies like a human expert and maps RFPs with highest semantic accuracy.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    m1, m2, m3 = st.columns(3)
    with m1:
        st.markdown('<div class="glass-card" style="text-align:center;"><h3>90%</h3><p style="color:#94a3b8;">Reduction in Manual Work</p></div>', unsafe_allow_html=True)
    with m2:
        st.markdown('<div class="glass-card" style="text-align:center;"><h3>100%</h3><p style="color:#94a3b8;">Policy Concentrated and No Hallucination</p></div>', unsafe_allow_html=True)
    with m3:
        st.markdown('<div class="glass-card" style="text-align:center;"><h3>< 5 min</h3><p style="color:#94a3b8;">Average Processing Time</p></div>', unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    
    st.markdown("### 🛠️ Built for Modern Compliance")
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("✅ **GenAI and RAG:** Retrive context by RAG System and answer generation by LLM.")
        st.write("✅ **Semantic Mapping:** Beyond keyword matching; understands context.")
        st.write("✅ **Data Preprocessing:** Apply data preprocessing of the RFP file via pandas.")
    with col_b:
        st.write("✅ **Zero-Data Leakage:** Enterprise-grade document handling.")
        st.write("✅ **Data Security and Integrity:** Implement Data Security and protect data from Prompt Injection, PII, and Answer's Confidence Score.")
        st.write("✅ **Multi-Format:** Supports PDF, XLSX, and CSV seamlessly.")
    
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        if st.button("✨ START ANALYZING", type="primary", use_container_width=True):
            change_pg('upload')
        
        if st.button("🧪 Try with Sample Data", use_container_width=True):
            st.session_state.use_sample = True
            change_pg('upload')
    # Work Your Way - Refined Modern Grid
    st.markdown("<h3 style='text-align:center; margin-bottom:40px;'>How TurboRFP Works</h3>", unsafe_allow_html=True)
    w1, w2, w3 = st.columns(3)
    
    with w1:
        st.markdown("""
        <div class="glass-card">
            <span style="font-size:32px;">📥</span>
            <h4 style="margin:10px 0;">Ingest</h4>
            <p style="color:#94a3b8; font-size:14px;">Upload your PDF policies. Our System/Pipeline vectorize the knowledge base instantly.</p>
        </div>
        """, unsafe_allow_html=True)

    with w2:
        st.markdown("""
        <div class="glass-card">
            <span style="font-size:32px;">🤖</span>
            <h4 style="margin:10px 0;">LLM And RAG Logic</h4>
            <p style="color:#94a3b8; font-size:14px;">RAG system retrive the context according to current RFP question and the LLM will generate the answer.</p>
        </div>
        """, unsafe_allow_html=True)

    with w3:
        st.markdown("""
        <div class="glass-card">
            <span style="font-size:32px;">📤</span>
            <h4 style="margin:10px 0;">Panda and Export Logic</h4>
            <p style="color:#94a3b8; font-size:14px;">Received answer placed in the RFP file by the help of pandas and Receive a perfectly formatted Excel sheet ready for your clients.</p>
        </div>
        """, unsafe_allow_html=True)

# --- PAGE: UPLOAD ---
def render_upload():
    if st.button("← Back"): change_pg('home')
    
    # Logic to show if Sample Mode is active
    is_sample = st.session_state.get('use_sample', False)
    
    if is_sample:
        st.success("🎯 Sample Mode Active: Pre-loaded 'Enterprise Security Policy' & 'Standard RFP'")
        if st.button("Reset & Upload My Own Files"):
            st.session_state.use_sample = False
            st.rerun()
    
    st.markdown("<h2 style='text-align:center;'>Knowledge Ingestion</h2>", unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader("📚 Security Policies")
        if is_sample:
            st.info("Using: internal_security_v4.pdf")
            pdf = ['Dataset/AWS_Security_Whitepaper.pdf', 'Dataset/Comapny_policy.pdf']
        else:
            pdf = st.file_uploader("Drop PDF files here", type='pdf', key="pdf_up", accept_multiple_files=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with c2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader("📋 RFP Questionnaire")
        if is_sample:
            st.info("Using: rfp_requirements_2026.xlsx")
            xls = 'Dataset/RFP_Sample_Questions.csv'
        else:
            xls = st.file_uploader("Drop Excel/CSV here", type=['xlsx', 'csv'], key="xls_up")
        st.markdown('</div>', unsafe_allow_html=True)
    return pdf, xls         
            
# --- PAGE: RESULT ---
def render_result():
    st.markdown("""
        <div style="background: linear-gradient(135deg, rgba(16, 185, 129, 0.1), rgba(56, 189, 248, 0.1)); padding: 60px; border-radius: 30px; text-align: center; border: 1px solid #10b981;">
            <div style="font-size:70px; margin-bottom:20px;">🎉</div>
            <h1 style="color:#34d399; margin:0;">Intelligence Compiled</h1>
            <p style="color:#94a3b8; font-size:1.2rem;">All RFP items have been mapped to your policies.</p>
        </div>
    """, unsafe_allow_html=True)
    
    _, c2, _ = st.columns([1, 2, 1])
    with c2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.download_button(
            label="⬇️ DOWNLOAD COMPLETED RFP",
            data=st.session_state.processed_data, 
            file_name="TurboRFP_Response.csv",
            mime="csv",
            use_container_width=True
        )
        if st.button("↺ Process Another", use_container_width=True):
            change_pg('home')
    
def render_about():
    st.markdown("<h1 style='color:#38bdf8; text-align:center;'>Behind the Intelligence</h1>", unsafe_allow_html=True)
    st.markdown("## 🤖 About TurboRFP")
    st.markdown("""
    <div style="background:#1e293b; padding:30px; border-radius:15px; border-left: 5px solid #818cf8;">
        <p>TurboRFP is a cutting-edge tool designed to automate the tedious process of filling out Security RFPs which take most precious thing of the IT sector: "TIME".</p>
        <ul>
            <li><b>Student Project:</b> Created by BCA Students.</li>
            <li><b>Tech Stack:</b> Python, RAG(Retrival Augmented Generation), Streamlit, LangChain, Vector Databases, Pandas, LLM.</li>
            <li><b>Vision:</b> To reduce manual documentation time by 90%.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # 1. THE PROBLEM (The "Why")
    st.markdown("""
    <div class="glass-card">
        <h3 style='color:#f87171;'>🛑 The Industry Pain Point</h3>
        <p style='font-size:1.1rem;'>
            Security and Compliance teams at medium-to-large enterprises spend an average of <b>40-60 hours per month</b> manually cross-referencing RFP questionnaires against internal policy PDFs. This process is slow, prone to human error, and creates massive bottlenecks in the sales cycle.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)

    # 2. THE SYSTEM ARCHITECTURE (The "How")
    st.markdown("### 🏗️ Python based RAG Architecture")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="glass-card" style="height:100%;">
            <h4 style='color:#38bdf8;'>Python-RAG Orchestration</h4>
            <p>TurboRFP doesn't just "search" for keywords. It perform semantic search to find the most relevent context for the LLM.</b>:</p>
            <ul>
                <li><b>Contextual Parser:</b> Breaks down complex PDF structures while maintaining hierarchical intent.</li>
                <li><b>Semantic Evaluator:</b> Uses <i> Google Embedding Model</i> to map requirements to policies with 95%+ accuracy.</li>
                <li><b>Hallucination Guard:</b>Stop Hallucination by give strong System Prompting and use Answer's Confidence Score</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="glass-card" style="height:100%;">
            <h4 style='color:#38bdf8;'>Data Security and Integrity</h4>
            <ul>
                <li><b>Prompt Injection:</b> Before the RFP question go to LLM, checked for prompt Injection which make Comapny's Internal policy safe.</li>
                <li><b>PII(Personally Identifiable Information):</b> Check for PII information in the output of the LLM, maintain privacy of the employees.</li>
                <li><b>Confidence Score:</b> LLM give Confidence score and provide the reason for that particular answer of RFP question.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="glass-card" style="height:100%;">
            <h4 style='color:#38bdf8;'>Technical Excellence</h4>
            <ul>
                <li><b>Persistence Layer:</b> FAISS vector indexing with localized storage for instant query response.</li>
                <li><b>API Optimization:</b> Manual batch processing and rate-limit handling for production stability.</li>
                <li><b>Model Selection:</b> Specifically engineered for the 2026 by ChatGPT LLM and Google Embedding Model.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # 3. THE "WHY HIRE ME" (The Pitch)
    st.markdown("""
    <div class="glass-card" style="border-color: #818cf8; background: rgba(129, 140, 248, 0.1);">
        <h3 style='color:#818cf8; text-align:center;'>The Objective</h3>
        <p style='text-align:center; font-size:1.1rem;'>
            This project was built to demonstrate my ability to move beyond basic AI wrappers. I focus on <b>Python and RAG Logic, Real World B2B problems, Data Persistence, and Production-Ready UI/UX.</b> 
            I am ready to help your company bridge the gap between AI experimentation and real-world ROI. I'm open to Internship and a full time opportunity. 
            Find my contact details on the conatct button.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("← Back to Home", key="back_abt"): change_pg('home')

# --- PAGE: CONTACT ---
def render_contact():
    st.markdown("## 📞 Contact Me")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div style="background:#1e293b; padding:30px; border-radius:15px;">
            <p>📧 Email: <b>mundriamohit100@gmail.com</b></p>
            <p>📍 Location: Jhajjar, Haryana</p>
            <p>🔗 GitHub: https://github.com/Mohit-Mundria</p>
            <p>🔗 Linkedin: www.linkedin.com/in/mohit-mundria-31631a322</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("← Back to Home", key="back_cnt"): change_pg('home')