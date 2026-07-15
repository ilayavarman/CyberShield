import streamlit as st

# ==========================================================
# Load CSS
# ==========================================================

def load_css():
    with open("static/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="CyberShield",
    page_icon="🛡️",
    layout="wide"
)

# Load Custom CSS
load_css()

# ==========================================================
# Header
# ==========================================================

st.title("🛡️ CyberShield")

st.subheader("AI-Powered Network Security Toolkit")

st.markdown("---")

st.write("Welcome to CyberShield!")

# ==========================================================
# Dashboard
# ==========================================================

col1, col2 = st.columns(2)

with col1:
    st.info("🔐 Password Strength Analyzer")

with col2:
    st.info("🌐 Website Security Checker")

col3, col4 = st.columns(2)

with col3:
    st.info("🔒 File Encryption & Decryption")

with col4:
    st.info("📄 PDF Security Reports")

st.markdown("---")

st.success("✅ Project Initialized Successfully")