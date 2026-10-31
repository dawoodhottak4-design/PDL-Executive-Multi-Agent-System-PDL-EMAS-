import streamlit as st
from langchain_groq import ChatGroq

# ==========================================
# 1. PAGE CONFIGURATION & STYLING
# ==========================================
st.set_page_config(
    page_title="PDL AI Enterprise & Executive Hub",
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
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #0F2548;
        border-radius: 6px;
        padding: 6px 14px;
        color: white;
        font-weight: 600;
        font-size: 0.9rem;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #0083B0 0%, #00B4DB 100%);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-header">📡 Pak Datacom Limited (PDL) - AI Enterprise Hub</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Unified AI Operations: NOC, Customer Support, HR, Finance, Green Energy & Safe City Solutions</p>', unsafe_allow_html=True)

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
# 3. MULTI-TAB INTERFACE SETUP (6 MODULES)
# ==========================================
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📡 Technical NOC",
    "💬 Customer Support",
    "🏛️ HR & SOPs",
    "💰 Finance & SLA",
    "⚡ Green Energy / Solar",
    "🛡️ B2G Safe City"
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

    if st.button("🚀 Run AI-NOC Diagnostic Protocol", use_container_width=True, key="btn_noc"):
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
                with st.container(border=True):
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

    if st.button("🚀 Generate Support Response & Auto-Ticket", use_container_width=True, key="btn_cs"):
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
                with st.container(border=True):
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

    if st.button("🚀 Consult HR Policy Guidelines", use_container_width=True, key="btn_hr"):
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
                with st.container(border=True):
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

    if st.button("🚀 Run Financial & SLA Audit", use_container_width=True, key="btn_fin"):
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
                with st.container(border=True):
                    st.markdown("### 📊 Financial Audit & Compliance Report")
                    st.markdown(fin_response.content)
            except Exception as e:
                st.error(f"Error: {e}")

# ------------------------------------------
# TAB 5: GREEN ENERGY & SOLAR OPTIMIZATION (NEW)
# ------------------------------------------
with tab5:
    st.subheader("⚡ Green AI Energy & Remote Site Power Optimization")
    energy_scope = st.selectbox(
        "Select Green Energy Focus:",
        [
            "Hybrid Solar-Battery-Generator Integration for Remote VSAT Sites",
            "Diesel OpEx Reduction & Fuel Consumption Audit",
            "Remote Power Telemetry & Battery Health Forecasting",
            "Green Telecom Sustainability Roadmap for Balochistan Grid-Isolated Hubs"
        ]
    )
    energy_details = st.text_area("Enter site specific power parameters:", "Calculate potential monthly diesel savings and battery backup runtime for an off-grid VSAT repeater station operating under extreme weather.")

    if st.button("🚀 Run Green Energy Optimization Plan", use_container_width=True, key="btn_energy"):
        with st.spinner("Green Energy Specialist calculating power metrics..."):
            energy_prompt = f"""
            You are Green AI Energy & Site Power Specialist at Pak Datacom Limited (PDL).
            Analyze the following power optimization scenario:
            - Focus: {energy_scope}
            - Details: {energy_details}
            
            Provide an executive engineering report covering:
            1. Hybrid power system configuration (Solar capacity, lithium battery bank, diesel gen set).
            2. Estimated OpEx reduction and fuel cost savings model.
            3. Carbon footprint mitigation metrics.
            4. Implementation roadmap for remote off-grid telecom towers.
            """
            try:
                energy_response = llm.invoke(energy_prompt)
                st.success("✅ Green Energy Optimization Blueprint Generated!")
                with st.container(border=True):
                    st.markdown("### 🌿 Solar & Energy Efficiency Report")
                    st.markdown(energy_response.content)
            except Exception as e:
                st.error(f"Error: {e}")

# ------------------------------------------
# TAB 6: B2G SAFE CITY & CIVIC INTEGRATION (NEW)
# ------------------------------------------
with tab6:
    st.subheader("🛡️ B2G Safe City & Municipal AI Integration Hub")
    safe_city_scope = st.selectbox(
        "Select Safe City Project Scope:",
        [
            "Turnkey Command & Control Center VMS Integration",
            "AI-Powered Automatic Number Plate Recognition (ANPR) on Main Corridors",
            "Municipal Traffic Analytics & Emergency Corridor Management",
            "Public Safety Video Analytics & Threat Detection Framework"
        ]
    )
    safe_city_details = st.text_area("Enter municipal project requirements:", "Design an integrated architecture for high-definition surveillance feeds and ANPR monitoring along major urban transport arteries.")

    if st.button("🚀 Generate Safe City Solution Blueprint", use_container_width=True, key="btn_safecity"):
        with st.spinner("B2G Safe City Lead formulating integration strategy..."):
            safe_city_prompt = f"""
            You are B2G Safe City & Civic AI Integration Lead at Pak Datacom Limited (PDL).
            Design a technical solution proposal for:
            - Scope: {safe_city_scope}
            - Requirements: {safe_city_details}
            
            Provide a comprehensive executive proposal document covering:
            1. Core system architecture & optical fiber/wireless backhaul integration.
            2. Real-time video analytics and ANPR data processing workflow.
            3. Command center dashboard integration and emergency dispatch protocols.
            4. Scalability, security, and municipal compliance guidelines.
            """
            try:
                safe_city_response = llm.invoke(safe_city_prompt)
                st.success("✅ Safe City Solution Blueprint Generated Successfully!")
                with st.container(border=True):
                    st.markdown("### 🏛️ B2G Safe City Project Proposal & Architecture")
                    st.markdown(safe_city_response.content)
            except Exception as e:
                st.error(f"Error: {e}")
