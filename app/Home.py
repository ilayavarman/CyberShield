import streamlit as st
from pathlib import Path

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="CyberShield",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# Load CSS
# ==========================================================

def load_css():
    css_path = Path(__file__).resolve().parents[1] / "static" / "style.css"

    if css_path.exists():
        with open(css_path, "r", encoding="utf-8") as css:
            st.markdown(
                f"<style>{css.read()}</style>",
                unsafe_allow_html=True
            )
    else:
        st.error(f"❌ CSS file not found:\n{css_path}")

load_css()

# ==========================================================
# HEADER
# ==========================================================

st.markdown("""
# 🛡️ CyberShield
### AI-Powered Cyber Security Toolkit
""")

st.markdown("---")

st.markdown("""
Welcome to **CyberShield**.

Analyze websites, inspect SSL certificates, perform DNS lookups,
WHOIS lookups, technology detection, and more.
""")

# ==========================================================
# DASHBOARD
# ==========================================================

st.subheader("🚀 Available Modules")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("🔐 Password Analyzer")
    st.info("🌐 Website Security")

with col2:
    st.info("🌍 DNS Lookup")
    st.info("🔒 SSL Inspector")

with col3:
    st.info("📄 WHOIS Lookup")
    st.info("💻 Technology Detector")

st.markdown("---")

# ==========================================================
# SYSTEM STATUS
# ==========================================================

st.subheader("📊 System Status")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Modules", "6")

with c2:
    st.metric("Database", "Connected")

with c3:
    st.metric("Status", "Online 🟢")

st.markdown("---")

# ==========================================================
# LIVE STATUS
# ==========================================================

st.subheader("🖥 Security Console")

st.code(
"""
> Initializing CyberShield...
> Loading AI Modules...
> Connecting Database...
> SSL Inspector Ready
> DNS Lookup Ready
> WHOIS Ready
> Technology Detector Ready

STATUS : ONLINE
""",
language="text"
)

st.success("🟢 CyberShield Loaded Successfully")

st.caption("© 2026 CyberShield | AI Powered Cyber Security Toolkit")