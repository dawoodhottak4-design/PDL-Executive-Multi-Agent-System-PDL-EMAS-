import streamlit as st
from langchain_groq import ChatGroq

# ==========================================
# 1. PAGE CONFIGURATION & STYLING
# ==========================================
st.set_page_config(
    page_title="PDL AI Enterprise Hub",
    page_icon="📡",
    layout="wide"
)

# Custom CSS for Professional Corporate UI
st.markdown("""
    <style>
    .main-header {
        font-size: 2.2rem;
        color: #00B4DB;
        font-weight: 800;
        margin-bottom: 5px;
    }
    .sub-header {
        font-size: 1rem;
        color: #8892B0;
        margin-bottom: 25px;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 15px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #0F2548;
        border-radius: 8px;
        padding: 10px 20px;
        color: white;
        font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #0083B0 0%, #00B4DB 100%);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-header">📡 Pak Datacom Limited (PDL) - AI Enterprise Hub</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Unified AI-NOC Telemetry & Customer Support Ticketing System (Powered by Groq API)</p>', unsafe_allow_html=True)

# ==========================================
# 2. API KEY SETUP
# ==========================================
groq_api_key = st.secrets.get("GROQ_API_KEY")

if not groq_api_key:
    groq_api_key = st.text_input("Enter Groq API Key:", type="password")
    if not groq_api_key:
        st.warning("Please configure GROQ_API_KEY in Streamlit Secrets or enter it above to proceed.")
        st.stop()

# Initialize Groq LLM
llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="openai/gpt-oss-120b",
    temperature=0.2
)

# ==========================================
# 3. MULTI-TAB INTERFACE SETUP
# ==========================================
tab1, tab2 = st.tabs([
    "📡 Technical NOC & Operations",
    "💬 Customer Support & Auto-Ticketing"
]
)

# ------------------------------------------
# TAB 1: TECHNICAL NOC & OPERATIONS
# ------------------------------------------
with tab1:
    st.subheader("🛠️ AI-NOC Telemetry & Fault Diagnostics")
    
    col1, col2 = st.columns(2)
    with col1:
        incident_scenario = st.selectbox(
            "Select Network Incident Scenario:",
            [
                "VSAT Rain Fade & Uplink Attenuation (Quetta Hub)",
                "Main Optical Fiber Link Cut (Lahore-Multan Segment)",
                "Commercial Grid Failure on Off-Grid Remote VSAT Tower #88"
            ]
        )
    with col2:
        severity_level = st.selectbox("Select Priority Level:", ["Tier 1 - Minor Warning", "Tier 2 - Major Degradation", "Tier 3 - Critical Outage"])

    custom_notes = st.text_area("Additional Technical Parameters (Optional):", "Check signal-to-noise ratio and trigger automated backup link restoration.")

    if st.button("🚀 Run AI-NOC Diagnostic & Escalation Protocol", use_container_width=True):
        with st.spinner("AI-NOC Specialist analyzing telemetry and generating protocol..."):
            
            prompt = f"""
            You are Senior AI-NOC & Operations Specialist at Pak Datacom Limited (PDL).
            Analyze the following network incident:
            - Scenario: {incident_scenario}
            - Severity: {severity_level}
            - Notes: {custom_notes}
            
            Provide a structured technical report covering:
            1. Root Cause Analysis (RCA).
            2. Immediate AI Compensation / Automated Mitigation Strategy.
            3. Tier-wise Fault Escalation Matrix with SLA targets.
            4. Field Team Dispatch instructions & GPS alert format.
            """
            
            try:
                response = llm.invoke(prompt)
                st.success("✅ AI-NOC Diagnostic Completed Successfully!")
                st.markdown("### 📋 Technical Incident Report & Escalation Plan")
                st.markdown(response.content)
            except Exception as e:
                st.error(f"Error executing AI model: {e}")

# ------------------------------------------
# TAB 2: CUSTOMER SUPPORT & AUTO-TICKETING
# ------------------------------------------
with tab2:
    st.subheader("💬 PDL 24/7 AI Customer Support & Ticketing Desk")
    
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        client_name = st.text_input("Client / Organization Name:", "National Bank of Pakistan / Corporate Client")
    with col_c2:
        query_type = st.selectbox("Inquiry / Issue Category:", ["VSAT Connectivity & Latency", "Billing & Service Package Inquiry", "Fiber Link SLA Compliance", "Emergency Support Request"])

    client_query = st.text_area("Describe Customer Issue or Request:", "Our branch office link is experiencing intermittent packet loss during peak hours. Please check status and provide resolution.")

    if st.button("🚀 Generate Support Response & Auto-Ticket", use_container_width=True):
        with st.spinner("AI Customer Support Agent checking SLAs and drafting response..."):
            
            support_prompt = f"""
            You are PDL AI Customer Experience & Ticketing Specialist.
            Process the following client inquiry:
            - Client: {client_name}
            - Category: {query_type}
            - Issue: {client_query}
            
            Provide a professional response including:
            1. Empathetic acknowledgment & immediate troubleshooting steps.
            2. PDL SLA commitment reference.
            3. Auto-generated Unique Incident Ticket ID (e.g., PDL-INC-2026-XXXX).
            4. Routing details to the respective technical or billing department.
            """
            
            try:
                support_response = llm.invoke(support_prompt)
                st.success("✅ Support Response Generated & Ticket Logged!")
                st.markdown("### 🎫 Customer Response & Ticket Summary")
                st.markdown(support_response.content)
            except Exception as e:
                st.error(f"Error generating support ticket: {e}")
