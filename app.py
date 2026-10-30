import streamlit as st
from crewai import Agent, Crew, Process, Task
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun

# ==========================================
# 1. PAGE CONFIGURATION & STYLING
# ==========================================
st.set_page_config(
    page_title="PDL AI Executive Council | Multi-Agent System",
    page_icon="📡",
    layout="wide"
)

st.title("📡 Pak Datacom Limited (PDL) - Enterprise AI Consulting System")
st.caption("Powered by CrewAI, Groq (openai/gpt-oss-120b), & DDG Search Tool")

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

# Initialize Online Policy & SOP Search Tool
search_tool = DuckDuckGoSearchRun()

# ==========================================
# 3. DEFINE DEPARTMENTAL AGENTS WITH SEARCH
# ==========================================

# 1. Chief AI Transformation Officer (CEO Coordinator)
ceo_agent = Agent(
    role="PDL Chief AI Transformation Officer",
    goal="Synthesize cross-departmental insights to align HR, Finance, and Operations with modern AI governance.",
    backstory="You are an executive strategist at Pak Datacom Limited skilled in enterprise policy alignment, digital transformation, and organizational SOPs.",
    verbose=True,
    allow_delegation=True,
    llm=llm,
    tools=[search_tool]
)

# 2. HR & Policy Compliance Lead
hr_agent = Agent(
    role="PDL HR & Governance Specialist",
    goal="Retrieve and audit HR leave policies, employee benefits, code of conduct, and workplace SOPs.",
    backstory="You are an expert HR Lead for telecom enterprises. You use online search tools to verify policy compliance, leave frameworks, and standard operating procedures.",
    verbose=True,
    llm=llm,
    tools=[search_tool]
)

# 3. Finance & Procurement Auditor
finance_agent = Agent(
    role="PDL Finance & SLA Procurement Strategist",
    goal="Analyze financial compliance, procurement SLAs, OpEx models, and company financial guidelines.",
    backstory="You specialize in corporate finance, auditing operational SLAs, vendor contracts, and cost optimization frameworks for telecom organizations.",
    verbose=True,
    llm=llm,
    tools=[search_tool]
)

# 4. Technical NOC & Operations Lead
noc_agent = Agent(
    role="Senior AI-NOC & Operations Specialist",
    goal="Manage technical SLAs, network uptime policies, incident management SOPs, and telemetry workflows.",
    backstory="You oversee VSAT satellite telemetry, optical fiber links, and technical escalation procedures according to strict SLA guidelines.",
    verbose=True,
    llm=llm,
    tools=[search_tool]
)

# ==========================================
# 4. USER INTERACTION INTERFACE
# ==========================================
st.subheader("📋 Query Departmental Policies, SOPs, or Strategy")

query_type = st.selectbox(
    "Select Department / Inquiry Category:",
    [
        "HR & Leave Policy / Workplace SOP Inquiry",
        "Finance, Procurement & Vendor SLA Verification",
        "Technical NOC SLA & Emergency Escalation SOPs",
        "Full Departmental Operational Alignment Audit"
    ]
)

user_query = st.text_area(
    "Enter specific policy question or scenario (e.g., 'What is the standard SLA for link restoration?' or 'Check leave policy guidelines'):",
    "Analyze PDL HR leave policy guidelines and standard technical NOC SLA turnaround times."
)

if st.button("🚀 Execute Multi-Agent Policy Consultation"):
    with st.spinner("Agents searching online documents and compiling response..."):
        
        # ==========================================
        # 5. DEFINE CONSULTING TASKS
        # ==========================================
        task_hr = Task(
            description=f"Search online for PDL/telecom standard HR policies, leave structures, and employee SOPs regarding: {user_query}.",
            expected_output="Clear summary of HR policy guidelines, leave categories, and standard operating procedures.",
            agent=hr_agent
        )

        task_finance = Task(
            description=f"Evaluate procurement rules, financial guidelines, and SLA compliance parameters related to: {user_query}.",
            expected_output="Financial audit report including cost implications and SLA parameters.",
            agent=finance_agent
        )

        task_noc = Task(
            description=f"Review technical SLA requirements, restoration protocols, and NOC escalation SOPs for: {user_query}.",
            expected_output="Technical operational breakdown and SLA response timeline.",
            agent=noc_agent
        )

        task_summary = Task(
            description=f"Compile all departmental search findings (HR, Finance, NOC) into an Executive Report answering: {user_query}.",
            expected_output="A structured Executive Summary Document formatted clearly for management review.",
            agent=ceo_agent
        )

        # ==========================================
        # 6. EXECUTE CREW PROCESS
        # ==========================================
        pdl_crew = Crew(
            agents=[ceo_agent, hr_agent, finance_agent, noc_agent],
            tasks=[task_hr, task_finance, task_noc, task_summary],
            process=Process.sequential,
            verbose=True
        )

        result = pdl_crew.kickoff()

        st.success("✅ Multi-Agent Consultation Completed Successfully!")
        st.markdown("### 📄 Policy & Executive Audit Report")
        st.markdown(result)
