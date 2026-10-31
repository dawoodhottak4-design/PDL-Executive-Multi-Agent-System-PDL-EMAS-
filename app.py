import streamlit as st
from langchain_groq import ChatGroq

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="PDL AI-NOC Operations Hub",
    page_icon="📡",
    layout="wide"
)

st.title("📡 Pak Datacom Limited (PDL) - Technical NOC & Operations Module")
st.caption("Powered by Groq API (openai/gpt-oss-120b) | Zero Local Dependencies")

# ==========================================
# 2. API KEY SETUP
# ==========================================
groq_api_key = st.secrets.get("GROQ_API_KEY")

if not groq_api_key:
    groq_api_key = st.text_input("Enter Groq API Key:", type="password")
    if not groq_api_key:
        st.warning("Please configure GROQ_API_KEY in Streamlit Secrets or enter it above to proceed.")
        st.stop()

# Initialize Groq LLM directly for robust performance
llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="openai/gpt-oss-120b",
    temperature=0.2
)

# ==========================================
# 3. TECHNICAL NOC SIMULATION & DIAGNOSTICS UI
# ==========================================
st.subheader("🛠️ AI-NOC Telemetry & Fault Diagnostics")

incident_scenario = st.selectbox(
    "Select Network Incident Scenario:",
    [
        "VSAT Rain Fade & Uplink Attenuation (Quetta Hub)",
        "Main Optical Fiber Link Cut (Lahore-Multan Segment)",
        "Commercial Grid Failure on Off-Grid Remote VSAT Tower #88"
    ]
)

custom_notes = st.text_area("Additional Technical Parameters (Optional):", "Check signal-to-noise ratio and trigger automated backup link restoration.")

if st.button("🚀 Run AI-NOC Diagnostic & Escalation Protocol"):
    with st.spinner("AI-NOC Specialist analyzing telemetry and generating protocol..."):
        
        prompt = f"""
        You are Senior AI-NOC & Operations Specialist at Pak Datacom Limited (PDL).
        Analyze the following network incident scenario:
        Scenario: {incident_scenario}
        Additional Notes: {custom_notes}
        
        Provide a structured technical response covering:
        1. Root Cause Analysis (RCA) based on telecom telemetry.
        2. Immediate AI Compensation / Automated Mitigation Strategy.
        3. Tier 1 to Tier 3 Fault Escalation Matrix with SLA targets.
        4. Field Team Dispatch instructions (GPS / site coordinates alert format).
        """
        
        try:
            response = llm.invoke(prompt)
            st.success("✅ AI-NOC Diagnostic Completed Successfully!")
            st.markdown("### 📋 Technical Incident Report & Escalation Plan")
            st.markdown(response.content)
        except Exception as e:
            st.error(f"Error executing AI model: {e}")
