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
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #0F2548;
        border-radius: 8px;
        padding: 8px 16px;
        color: white;
        font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #0083B0 0%, #00B4DB 100%);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-header">📡 Pak Datacom Limited (PDL) - AI Enterprise Hub</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Unified AI Operations: NOC, Customer Support, HR Policies & Finance Procurement</p>', unsafe_allow_html=True)

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
tab1, tab2, tab3, tab4 = st.tabs([
    "📡 Technical NOC",
    "💬 Customer Support",
    "🏛️ HR Policy & SOPs",
    "💰 Finance & Procurement"
])

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
            ],
            key="noc_scene"
        )
    with col2:
        severity_level = st.selectbox("Select Priority Level:", ["Tier 1 - Minor Warning", "Tier 2 - Major Degradation", "Tier 3 - Critical Outage"], key="noc_sev")

    custom_notes = st.text_area("Additional Technical Parameters:", "Check signal-to-noise ratio and trigger automated backup link restoration.", key="noc_notes")

    if st.button("🚀 Run AI-NOC Diagnostic & Escalation Protocol", use_container_width=True):
        with st.spinner("AI-NOC Specialist analyzing telemetry..."):
            prompt = f"""
            You are Senior AI-NOC & Operations Specialist at Pak Datacom Limited (PDL).
            Analyze network incident:
            - Scenario: {incident_scenario}
            - Severity: {severity_level}
            - Notes: {custom_notes}
            
            Provide structured technical report covering:
            1. Root Cause Analysis (RCA).
            2. Immediate AI Compensation / Automated Mitigation Strategy.
            3. Tier-wise Fault Escalation Matrix with SLA targets.
            4. Field Team Dispatch instructions & GPS alert format.
            """
            try:
                response = llm.invoke(prompt)
                st.success("✅ AI-NOC Diagnostic Completed Successfully!")
                st.markdown("### 📋 Technical Incident Report")
                st.markdown(response.content)
            except Exception as e:
                st.error(f"Error: {e}")

# ------------------------------------------
# TAB 2: CUSTOMER SUPPORT & TICKETING
# ------------------------------------------
with tab2:
    st.subheader("💬 PDL 24/7 AI Customer Support & Ticketing Desk")
    
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        client_name = st.text_input("Client / Organization Name:", "National Bank of Pakistan")
    with col_c2:
        query_type = st.selectbox("Inquiry Category:", ["VSAT Connectivity & Latency", "Billing & Service Package Inquiry", "Fiber Link SLA Compliance", "Emergency Support Request"])

    client_query = st.text_area("Describe Customer Issue:", "Our branch office link is experiencing intermittent packet loss during peak hours.")

    if st.button("🚀 Generate Support Response & Auto-Ticket", use_container_width=True):
        with st.spinner("AI Customer Support Agent checking SLAs..."):
            support_prompt = f"""
            You are PDL AI Customer Experience & Ticketing Specialist.
            Process client inquiry:
            - Client: {client_name}
            - Category: {query_type}
            - Issue: {client_query}
            
            Provide professional response including:
            1. Empathetic acknowledgment & troubleshooting steps.
            2. PDL SLA commitment reference.
            3. Auto-generated Unique Incident Ticket ID (e.g., PDL-INC-2026-XXXX).
            4. Department routing details.
            """
            try:
                support_response = llm.invoke(support_prompt)
                st.success("✅ Support Response Generated & Ticket Logged!")
                st.markdown("### 🎫 Customer Response & Ticket Summary")
                st.markdown(support_response.content)
            except Exception as e:
                st.error(f"Error: {e}")

# ------------------------------------------
# TAB 3: HR POLICY & WORKPLACE SOPS
# ------------------------------------------
with tab3:
    st.subheader("🏛️ PDL HR Policy & Workplace Governance Assistant")
    
    hr_query_type = st.selectbox(
        "Select HR Inquiry Type:",
        [
            "Leave Policy Guidelines (Annual, Sick, Casual Leaves)",
            "Employee Code of Conduct & Workplace SOPs",
            "Medical Insurance & Staff Benefits",
            "Performance Appraisal & Promotion Criteria"
        ]
    )
    
    hr_details = st.text_area("Enter specific HR question or scenario:", "What is the standard procedure for applying for extended medical leave and what documents are required?")

    if st.button("🚀 Consult HR Policy Guidelines", use_container_width=True):
        with st.spinner("HR & Governance Specialist auditing policies..."):
            hr_prompt = f"""
            You are PDL HR & Workplace Governance Specialist.
            Address the following HR inquiry:
            - Category: {hr_query_type}
            - Details: {hr_details}
            
            Provide a clear, professional response based on corporate telecom HR policies, leave frameworks, and standard operating procedures.
            """
            try:
                hr_response = llm.invoke(hr_prompt)
                st.success("✅ HR Policy Guidelines Retrieved!")
                st.markdown("### 📄 HR Advisory Report")
                st.markdown(hr_response.content)
            except Exception as e:
                st.error(f"Error: {e}")

# ------------------------------------------
# TAB 4: FINANCE & SLA PROCUREMENT
# ------------------------------------------
with tab4:
    st.subheader("💰 PDL Corporate Finance & SLA Procurement Auditor")
    
    fin_query_type = st.selectbox(
        "Select Financial / Procurement Scope:",
        [
            "Vendor SLA Compliance & Penalty Clauses",
            "OpEx & CapEx Budget Optimization for Telecom Infrastructure",
            "Procurement Rules & Bidding Guidelines",
            "Corporate Billing & Revenue Assurance Auditing"
        ]
    )
    
    fin_details = st.text_area("Enter financial scenario or audit question:", "Evaluate procurement compliance and financial SLA penalties for delayed hardware delivery by a vendor.")

    if st.button("🚀 Run Financial & SLA Audit", use_container_width=True):
        with st.spinner("Finance & Procurement Strategist analyzing parameters..."):
            fin_prompt = f"""
            You are PDL Corporate Finance & SLA Procurement Auditor.
            Analyze the following financial scenario:
            - Scope: {fin_query_type}
            - Details: {fin_details}
            
            Provide an executive financial audit report covering cost implications, SLA compliance parameters, and optimization recommendations.
            """
            try:
                fin_response = llm.invoke(fin_prompt)
                st.success("✅ Financial & SLA Audit Completed!")
                st.markdown("### 📊 Financial Audit & Compliance Report")
                st.markdown(fin_response.content)
            except Exception as e:
                st.error(f"Error: {e}")
