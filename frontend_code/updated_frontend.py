import streamlit as st


# 1. MANDATORY: Page Config must be FIRST
st.set_page_config(layout="wide", page_title="NexusAI", page_icon="🛡️")

# --- CSS STYLING ---
def apply_styles():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
        .stApp { background-color: #0f172a; color: #f1f5f9; font-family: 'Inter', sans-serif; }
        header, footer {visibility: hidden;}
        div.stButton > button[kind="primary"] {
            background: linear-gradient(90deg, #38bdf8, #818cf8);
            color: white; border: none; font-weight: 800; padding: 15px 30px;
            border-radius: 8px; box-shadow: 0 0 15px rgba(56, 189, 248, 0.6);
        }
        .dl-container { border: 2px solid #34d399; background: rgba(16, 185, 129, 0.1); padding: 30px; border-radius: 15px; text-align: center; }
        .grad-txt { background: linear-gradient(90deg, #38bdf8, #818cf8); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 800; }
        .file-box { border: 2px dashed #475569; padding: 20px; border-radius: 10px; text-align: center; background: #1e293b; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION LOGIC ---
# if 'pg' not in st.session_state:
#     st.session_state.pg = 'home'
# if 'processed_data' not in st.session_state:
#     st.session_state.processed_data = None

def change_pg(target):
    st.session_state.pg = target
    st.rerun()

# --- PAGE FUNCTIONS ---

def render_navbar():
    col_brand, col_space, c1, c2, c3 = st.columns([3, 5, 1, 1, 1])
    with col_brand:
        st.markdown("<h3 style='margin:0;'>🛡️ NexusAI</h3>", unsafe_allow_html=True)
    with c1: 
        if st.button("Home"): change_pg('home')
    with c2: 
        if st.button("About"): change_pg('about')
    with c3: 
        if st.button("Contact"): change_pg('contact')
    st.markdown("---")

def render_firstpage():
    st.markdown("""
        <div style="text-align:center;">
            <p style="color:#818cf8; font-weight:bold; font-size:12px; letter-spacing:1px;">✨ PDF TOOL FOR HACKATHON</p>
            <h1 style="font-size:3.5rem;">Automate Security RFPs <br> <span class="grad-txt">With AI Speed</span></h1>
        </div>
    """, unsafe_allow_html=True)
    
    _, b2, _ = st.columns([1, 1, 1])
    with b2:
        st.markdown("<div style='text-align:center;'><h3>Analyze RFP</h3></div>", unsafe_allow_html=True)
        if st.button("🚀 SMART ANALYSIS", type="primary", use_container_width=True):
            change_pg('upload')

def render_secondpage():
    if st.button("← Back"): change_pg('home')
    
    st.markdown("<h2 style='text-align:center;'>Upload Files</h2>", unsafe_allow_html=True)
    col_u1, col_u2 = st.columns(2)

    with col_u1:
        st.markdown('<div class="file-box">📂 <b>Policy PDF</b></div>', unsafe_allow_html=True)
        pdf_file = st.file_uploader("Upload PDF", type='pdf', key="pdf_up", accept_multiple_files=True)
        
    with col_u2:
        st.markdown('<div class="file-box">📊 <b>RFP Excel</b></div>', unsafe_allow_html=True)
        xls_file = st.file_uploader("Upload Excel/CSV", type=['xlsx', 'csv'], key="xls_up")

    # This function returns values to the controller
    return pdf_file, xls_file

def render_thirdpage():
    if st.button("← Start Over"):
        st.session_state.processed_data = None
        change_pg('upload')
        
    st.markdown("""
        <div class="dl-container">
            <div style="font-size:50px;">✅</div>
            <div style="color:#34d399; font-weight:bold; font-size:24px;">ANALYSIS COMPLETE</div>
            <p>Your RFP has been mapped successfully.</p>
        </div>
    """, unsafe_allow_html=True)

    if st.session_state.processed_data is not None:
        _, d2, _ = st.columns([1, 1, 1])
        with d2:
            st.markdown("<br>", unsafe_allow_html=True)
            # Example download logic using session state data
            st.download_button(
                label="⬇️ DOWNLOAD REPORT",
                data=st.session_state.processed_data,
                file_name="Final_RFP_Output.csv",
                mime="text/csv",
                type="primary",
                use_container_width=True
            )







# from time import sleep
# # from app import file_processing

# def change_pg(target):
#     st.session_state.pg= target
        
        
        
# def render_firstpage():
#     # --- Basic Config ---
#     # Page ka title aur icon set kar rahe hain
#     st.set_page_config(layout="wide", page_title="NexusAI", page_icon="🛡️")

#     # --- CSS JAADU (Styling) ---
#     # Yahan humne thoda hardcode CSS likha hai taaki look professional aye
#     # Aur buttons ko highlight karne ke liye 'primary' class ko override kiya hai
#     st.markdown("""
#     <style>
#         /* Font import kar lete hain */
#         @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');

#         /* Main Background - Dark Cyberpunk theme */
#         .stApp {
#             background-color: #0f172a;
#             background-image: radial-gradient(circle at 50% 0%, #1e293b 0%, #0f172a 70%);
#             color: #f1f5f9;
#             font-family: 'Inter', sans-serif;
#         }

#         /* Upar ka default header gayab */
#         header, footer {visibility: hidden;}

#         /* === NAVBAR STYLE === */
#         /* Buttons ko simple text link jaisa banaya */
#         div.stButton > button {
#             background: transparent;
#             border: none;
#             color: #94a3b8;
#             font-weight: 600;
#         }
#         div.stButton > button:hover {
#             color: #fff;
#             background: rgba(255,255,255,0.05);
#         }

#         /* === IMPORTANT BUTTONS HIGHLIGHT (Neon Glow) === */
#         /* Jo bhi button type="primary" hoga, wo glow karega */
#         div.stButton > button[kind="primary"] {
#             background: linear-gradient(90deg, #38bdf8, #818cf8);
#             color: white;
#             border: none;
#             font-weight: 800;
#             padding: 15px 30px;
#             border-radius: 8px;
#             box-shadow: 0 0 15px rgba(56, 189, 248, 0.6); /* Ye hai wo glow */
#             transition: 0.3s;
#         }
#         div.stButton > button[kind="primary"]:hover {
#             transform: scale(1.02);
#             box-shadow: 0 0 25px rgba(56, 189, 248, 0.9);
#         }

#         /* === DOWNLOAD BOX SPECIAL STYLE === */
#         .dl-container {
#             border: 2px solid #34d399; /* Green Border */
#             background: rgba(16, 185, 129, 0.1);
#             padding: 30px;
#             border-radius: 15px;
#             text-align: center;
#             margin-top: 20px;
#             animation: fadeIn 1s;
#         }
#         .dl-title {
#             color: #34d399;
#             font-weight: bold;
#             font-size: 20px;
#             margin-bottom: 10px;
#         }

#         /* Text Gradients */
#         .grad-txt {
#             background: linear-gradient(90deg, #38bdf8, #818cf8);
#             -webkit-background-clip: text;
#             -webkit-text-fill-color: transparent;
#         }
        
#         /* Upload Boxes styling */
#         .file-box {
#             border: 2px dashed #475569;
#             padding: 20px;
#             border-radius: 10px;
#             text-align: center;
#             background: #1e293b;
#         }

#     </style>
#     """, unsafe_allow_html=True)

#     # --- NAVIGATION LOGIC (Session State) ---
#     # Simple logic rakha hai taaki code complex na lage
#     if 'pg' not in st.session_state:
#         st.session_state.pg = 'home'

#     # def change_pg(target):
#     #     st.session_state.pg = target

#     # --- NAVBAR (Always Top) ---
#     # Layout ke liye columns use kiye
#     col_brand, col_space, c1, c2, c3 = st.columns([3, 5, 1, 1, 1])

#     with col_brand:
#         # Logo area
#         st.markdown("<h3 style='margin:0; padding:0; cursor:pointer;'>🛡️ NexusAI</h3>", unsafe_allow_html=True)

#     # Navbar ke buttons
#     with c1:
#         if st.button("Home"): change_pg('home')
#     with c2:
#         if st.button("About"): render_aboutpage()
#     with c3:
#         if st.button("Contact"): render_contactpage()

#     st.markdown("---") # Line separator


#     # ==============================
#     #      PAGE 1: HOME SECTION
#     # ==============================
#     if st.session_state.pg == 'home':
        
#         st.markdown("<br>", unsafe_allow_html=True)
        
#         # Hero Text Section
#         # HTML use kiya taaki control rahe looks pe
#         st.markdown("""
#             <div style="text-align:center;">
#                 <p style="color:#818cf8; font-weight:bold; font-size:12px; letter-spacing:1px;">✨ PDF TOOL FOR HACKATHON</p>
#                 <h1 style="font-size:3.5rem; line-height:1.2;">
#                     Automate Security RFPs <br> 
#                     <span class="grad-txt">With AI Speed</span>
#                 </h1>
#                 <p style="color:#94a3b8; font-size:1.1rem;">Upload documents, get excel report. Simple.</p>
#             </div>
#         """, unsafe_allow_html=True)

#         st.markdown("<br>", unsafe_allow_html=True)

#         # === BIG HIGHLIGHTED BUTTON ===
#         # Isko center karne ke liye columns ka jugaad
#         b1, b2, b3 = st.columns([1, 1, 1])
#         with b2:
#             # Fake card look text
#             st.markdown("""
#                 <div style="text-align:center; margin-bottom:10px;">
#                     <span style="font-size:30px;">📄</span>
#                     <h3 style="margin:0;">Analyze RFP</h3>
#                 </div>
#             """, unsafe_allow_html=True)
            
#             # # ASLI BUTTON (Type='primary' matlab Highlighted wala style)
#             # if st.button("🚀 SMART ANALYSIS", type="primary", use_container_width=True):
#             #     change_pg('upload') # Page change logic
#             #     st.rerun()

#         # Step Process Section (Images)
#         st.markdown("<br><br><br>", unsafe_allow_html=True)
#         st.markdown("<h3 style='text-align:center;'>Work Your Way</h3>", unsafe_allow_html=True)
#         st.markdown("<p style='text-align:center; color:#666; font-size:12px; margin-top:-15px;'>3 Step Process</p>", unsafe_allow_html=True)
        
#         # 3 Images row mein
#         img_a, img_b, img_c = st.columns(3)
        
#         with img_a:
#             st.image("https://placehold.co/300x200/1e293b/38bdf8?text=1.+Upload", use_column_width=True)
#             st.caption("1. Upload PDF & Excel")
#         with img_b:
#             st.image("https://placehold.co/300x200/1e293b/818cf8?text=2.+Process", use_column_width=True)
#             st.caption("2. AI Extraction")
#         with img_c:
#             st.image("https://placehold.co/300x200/1e293b/34d399?text=3.+Result", use_column_width=True)
#             st.caption("3. Download Report")
        
#         # Footer styling
#         st.markdown("<br><br><hr style='opacity:0.2'>", unsafe_allow_html=True)
#         st.markdown("<div style='text-align:center; font-size:12px; color:#555;'>© 2026 NexusAI Project.</div>", unsafe_allow_html=True)


#     # ==============================
#     #      PAGE 2: UPLOAD SECTION
#     # ==============================
#     # elif st.session_state.pg == 'upload':
# def render_secondpage():
#     # Back button normal style
#     if st.button("← Back"):
#         change_pg('home')
#         # st.rerun()
    
#     st.markdown("<h2 style='text-align:center;'>Upload Files</h2>", unsafe_allow_html=True)
#     st.markdown("<br>", unsafe_allow_html=True)

#     # Layout for uploaders
#     col_u1, col_u2 = st.columns(2)

#     # Box 1: PDF
#     with col_u1:
#         st.markdown('<div class="file-box">📂 <b>Policy PDF</b></div>', unsafe_allow_html=True)
#         pdf_file = st.file_uploader(" ", type='pdf', accept_multiple_files=True)
#         if pdf_file: st.success("Loaded!")
        
#     # Box 2: Excel
#     with col_u2:
#         st.markdown('<div class="file-box">📊 <b>RFP Excel</b></div>', unsafe_allow_html=True)
#         xls_file = st.file_uploader(" ", type=['xlsx', 'csv'])
#         if xls_file: st.success("Loaded!")

#     st.markdown("<br><br>", unsafe_allow_html=True)
    
#     return pdf_file, xls_file
#     # st.inf("⚠️ Please upload both files to start.")


#     # ==============================
#     #      PAGE 3: RESULT SECTION
#     # ==============================
#     # elif st.session_state.pg == 'result':
# def render_thirdpage(csv_file):
        
#     if st.button("← Start Over"):
#         change_pg('upload')
#         st.rerun()
        
#     st.markdown("<br>", unsafe_allow_html=True)

#     # === DOWNLOAD BOX (SPECIAL REQUEST) ===
#     # Isko 'dl-container' class di hai CSS mein (Green Border wala)
#     st.markdown("""
#         <div class="dl-container">
#                 <div style="font-size:50px;">✅</div>
#                 <div class="dl-title">ANALYSIS COMPLETE</div>
#                 <p style="color:#ccc;">Your RFP has been mapped successfully.</p>
#         </div>
#     """, unsafe_allow_html=True)

#         # Download Button ko container ke niche, lekin Highlighted
#         # Hum columns use kar rahe taaki button box ki width match na kare, thoda chhota rahe
#     d1, d2, d3 = st.columns([1, 1, 1])
#     with d2:
#         st.markdown("<br>", unsafe_allow_html=True)
            
#         # Dummy csv data create kar rahe
#         # csv_data = "Question,Answer,Confidence\nIs data encrypted?,Yes AES-256,High"
            
#         # Ye button bhi primary hai (Glowing Blue/Purple)
#         csv = csv_file.to_csv(index=False).encode("utf-8")
#         st.download_button(
#             label="⬇️ DOWNLOAD REPORT",
#             data=csv,
#             file_name="Final_RFP_Output.csv",
#             mime="text/csv",
#             type="primary", 
#             use_container_width=True
#         )

#     # ==============================
#     #      EXTRAS: ABOUT & CONTACT
#     # ==============================
#     # if st.session_state.pg == 'about':
def render_aboutpage():
    st.markdown("<div class='dl-container'><h2>About Us</h2><p>We automate boring stuff.</p></div>", unsafe_allow_html=True)
    if st.button("Back Home"): change_pg('home'); st.rerun()

    # elif st.session_state.pg == 'contact':
def render_contactpage():
    st.markdown("<div class='dl-container'><h2>Contact</h2><p>Email: dev@nexus.ai</p></div>", unsafe_allow_html=True)
    if st.button("Back Home"): change_pg('home'); st.rerun()
        
        
        
