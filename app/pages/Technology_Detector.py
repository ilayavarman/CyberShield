import streamlit as st
import sys
from pathlib import Path

# ==========================================================
# Add Project Root
# ==========================================================

ROOT_DIR = Path(__file__).resolve().parents[2]

if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from src.technology_detector import detect_technology

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="CyberShield | Technology Detector",
    page_icon="🛠",
    layout="wide"
)

st.title("🛠 Technology Detector")

st.write("Detect technologies used by any website.")

st.markdown("---")

url = st.text_input(
    "Enter Website URL",
    placeholder="https://github.com"
)

if st.button("🔍 Detect Technology"):

    if url.strip() == "":
        st.warning("Please enter a website URL.")

    else:

        with st.spinner("Analyzing Website..."):

            result = detect_technology(url)

        if "error" in result:

            st.error(result["error"])

        else:

            st.success("✅ Technology Detection Completed Successfully")

            st.markdown("---")

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "🌐 Website",
                    result["url"]
                )

                st.metric(
                    "📡 Status Code",
                    result["status"]
                )

                st.metric(
                    "⚡ Response Time",
                    f'{result["response_time"]} ms'
                )

            with col2:

                st.metric(
                    "🖥 Server",
                    result["server"]
                )

                st.metric(
                    "☁ CDN",
                    result["cdn"]
                )

            with col3:

                st.metric(
                    "⚛ Frontend",
                    ", ".join(result["frontend"]) if result["frontend"] else "Unknown"
                )

                st.metric(
                    "🖥 Backend",
                    ", ".join(result["backend"]) if result["backend"] else "Unknown"
                )

            st.markdown("---")

            st.subheader("🌍 CMS")

            if result["cms"]:

                for cms in result["cms"]:
                    st.success(cms)

            else:

                st.info("No CMS Detected")

            st.markdown("---")

            st.subheader("🛡 Security Headers")

            for header, present in result["security"].items():

                if present:

                    st.success(f"✅ {header}")

                else:

                    st.error(f"❌ {header}")

            st.markdown("---")

            st.subheader("📘 About Technology Detection")

            st.info(
                """
CyberShield detects publicly observable technologies used by a website.

It checks:

• 🖥 Web Server
• ☁ CDN
• ⚛ Frontend Frameworks
• 🖥 Backend Technologies
• 🌍 CMS
• 🛡 Security Headers
• ⚡ Response Time

Some technologies cannot be detected reliably because many websites intentionally hide implementation details.
"""
            )

            st.markdown("---")

            st.caption("🛡 CyberShield | Technology Detector v1.0")