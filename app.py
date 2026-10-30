import streamlit as st
from crewai import Agent, Crew, Process, Task
from langchain_groq import ChatGroq

# ==========================================
# 1. PAGE CONFIGURATION & STYLING
# ==========================================
st.set_page_config(
    page_title="PDL AI-Exec Council & Support Hub",
    page_icon="📡",
    layout="wide"
)

st.title("📡 Pak Datacom Limited (PDL) - Unified AI Executive & Operations Hub")
st.caption("Powered by CrewAI & Groq (openai/gpt-oss-120b)")

# ==========================================
# 2. API KEY & MODEL CONFIGURATION
# ==========================================
groq_api_key = st.secrets.get("GROQ_API_KEY")

if not groq_api_key:
    groq_api_key = st.text_input("Enter Groq API Key:", type="password")
    if not groq_api_key:
        st.warning("Please configure GROQ_API_KEY in Streamlit Secrets or enter it above to proceed.")
        st.stop()

# Initialize Groq LLM with requested model
llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="openai/gpt-oss-120b",
    temperature=0.2
)

# ==========================================
# 3. DEFINE ALL SPECIALIZED AGENTS (ZERO DEPENDENCY CONFLICT)
# ==========================================

ceo_agent = Agent(
    role="PDL Chief AI Transformation Officer",
    goal="Synthesize cross-departmental operations, customer support metrics, and NOC escalation strategies.",
    backstory="You are an executive strategist at Pak Datacom Limited overseeing unified digital operations and corporate compliance.",
    verbose=True,
    allow_delegation=True,
    llm=llm
)

customer_support_agent = Agent(
    role="PDL AI Customer Experience & Ticketing Specialist",
    goal="Handle client inquiries, troubleshoot link queries, draft SLA responses, and auto-generate e-tickets.",
    backstory="You manage customer communications, SLA query resolutions, and ticket routing for PDL's corporate and government clients.",
    verbose=True,
    llm=llm
)

noc_monitoring_agent = Agent(
    role="PDL AI-NOC Telemetry & Network Health Monitor",
    goal="Analyze satellite attenuation, VSAT rain fade, fiber link degradation, and predict network faults.",
    backstory="You are an automated network monitoring expert that reads link telemetry and flags predictive faults before outages occur.",
    verbose=True,
    llm=llm
)

escalation_agent = Agent(
    role="PDL Incident Escalation & SLA Compliance Officer",
    goal="Execute Tier 1 to Tier 3 fault escalation protocols, assign field teams with GPS alerts, and track SLA restoration deadlines.",
    backstory="You enforce SLA restoration compliance. When network faults occur, you trigger automated team alerts and management escalations.",
    verbose=True,
    llm=llm
)

hr_agent = Agent(
    role="PDL HR & Workplace Governance Specialist",
    goal="Audit HR leave policies, employee SOPs, and organizational compliance guidelines.",
    backstory="You manage internal workforce policies and standard operating procedures.",
    verbose=True,
    llm=llm
)

finance_agent = Agent(
    role="PDL Corporate Finance & SLA Procurement Auditor",
    goal="Audit procurement rules, financial SLAs, OpEx models, and cost optimization strategies.",
    backstory="You manage operational budget audits, vendor SLAs, and telecom financial planning.",
    verbose=True,
    llm=llm
)

energy_agent = Agent(
    role="Green AI Energy & Site Power Specialist",
    goal="Optimize hybrid power systems (Solar/Battery/Generator) for remote VSAT towers to cut fuel OpEx.",
    backstory="You optimize off-grid power infrastructure and reduce diesel generator consumption.",
    verbose=True,
    llm=llm
)

safe_city_agent = Agent(
    role="B2G Safe City & Civic AI Integration Lead",
    goal="Design turnkey civic safety, VMS integration, and municipal traffic AI solutions.",
    backstory="You specialize in regional public sector AI projects and Video Management System (VMS) integration.",
    verbose=True,
    llm=llm
)

# ==========================================
# 4. UI MULTI-TAB NAVIGATION
# ==========================================
tab1, tab2, tab3 = st.tabs([
    "💬 Customer Support & Auto-Ticketing",
    "📡 Live NOC Monitoring & Fault Escalation",
    "🏛️ Executive Council & Policy Audit"
])

# ------------------------------------------
# TAB 1: CUSTOMER SUPPORT CHATBOT & TICKETING
# ------------------------------------------
with tab1:
    st.subheader("💬 PDL 24/7 AI Customer Support Portal")
    client_name = st.text_input("Client Organization Name:", "National Bank / Enterprise Client")
    client_query = st.text_area("Describe your issue or query:", "Our satellite VSAT link at Quetta branch is experiencing high latency and packet loss during heavy rain.")
    
    if st.button("Submit Customer Query"):
        with st.spinner("AI Customer Support Agent is analyzing query & checking SLAs..."):
            task_cs = Task(
                description=f"Analyze query from {client_name}: '{client_query}'. Check PDL SLAs, provide troubleshooting steps, and generate an automated ticket summary.",
                expected_output="Professional customer response with troubleshooting guide and auto-generated Incident Ticket ID.",
                agent=customer_support_agent
            )
            cs_crew = Crew(agents=[customer_support_agent], tasks=[task_cs], process=Process.sequential)
            res_cs = cs_crew.kickoff()
            
            st.success("✅ Support Response Generated & Ticket Created!")
            st.markdown(res_cs)

# ------------------------------------------
# TAB 2: NOC MONITORING & FAULT ESCALATION
# ------------------------------------------
with tab2:
    st.subheader("📡 AI-NOC Telemetry & Automated Fault Escalation")
    st.info("Simulate live network incident to trigger Tier 1-3 Escalation Workflow:")
    
    incident_type = st.selectbox(
        "Select Network Incident Scenario:",
        [
            "VSAT Rain Fade & Uplink Degradation (Quetta Hub)",
            "Main Optical Fiber Link Cut (Lahore-Multan Segment)",
            "Commercial Grid Failure on Off-Grid Remote VSAT Tower #88"
        ]
    )
    
    if st.button("🚀 Trigger AI-NOC Incident Workflow"):
        with st.spinner("NOC Monitoring & Escalation Agents collaborating..."):
            task_mon = Task(
                description=f"Analyze network telemetry for incident: '{incident_type}'. Identify root cause and immediate AI compensation strategy.",
                expected_output="Technical telemetry diagnosis report.",
                agent=noc_monitoring_agent
            )
            
            task_esc = Task(
                description=f"Formulate Tier 1 to Tier 3 Escalation Matrix for '{incident_type}'. Specify field team alert triggers, GPS dispatch details, and SLA restoration deadlines.",
                expected_output="Detailed Fault Escalation Protocol and SLA Target Timeline.",
                agent=escalation_agent
            )
            
            noc_crew = Crew(
                agents=[noc_monitoring_agent, escalation_agent],
                tasks=[task_mon, task_esc],
                process=Process.sequential
            )
            res_noc = noc_crew.kickoff()
            
            st.success("✅ Incident Diagnostic & Escalation Matrix Executed!")
            st.markdown(res_noc)

# ------------------------------------------
# TAB 3: EXECUTIVE COUNCIL & DEPARTMENTAL AUDIT
# ------------------------------------------
with tab3:
    st.subheader("🏛️ Enterprise Multi-Agent Policy & Strategy Audit")
    
    audit_category = st.selectbox(
        "Select Audit Scope:",
        [
            "HR Leave Policy & Workplace SOP Verification",
            "Finance, Procurement & Vendor SLA Audit",
            "Green AI Energy OpEx Savings Plan",
            "Full Cross-Departmental Digital Transformation Blueprint"
        ]
    )
    
    audit_instructions = st.text_area("Audit Focus Details:", "Analyze PDL standard operating procedures, HR policy guidelines, and financial SLA margins.")
    
    if st.button("Run Multi-Agent Executive Audit"):
        with st.spinner("Executive Council Agents compiling master report..."):
            task_hr = Task(
                description=f"Audit HR policies and SOPs regarding: {audit_instructions}.",
                expected_output="HR Policy Summary Report.",
                agent=hr_agent
            )
            task_fin = Task(
                description=f"Audit financial SLAs and OpEx models for: {audit_instructions}.",
                expected_output="Financial SLA Audit Report.",
                agent=finance_agent
            )
            task_ceo = Task(
                description=f"Synthesize HR, Finance, and Technical inputs into a Master Strategy Document for: {audit_category}.",
                expected_output="Executive Master Audit Report addressed to PDL Board.",
                agent=ceo_agent
            )
            
            exec_crew = Crew(
                agents=[ceo_agent, hr_agent, finance_agent],
                tasks=[task_hr, task_fin, task_ceo],
                process=Process.sequential
            )
            res_exec = exec_crew.kickoff()
            
            st.success("✅ Executive Audit Completed!")
            st.markdown(res_exec)
