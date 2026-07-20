import streamlit as st
import sys
from pathlib import Path

# ==========================================================
# Add Project Root
# ==========================================================

ROOT_DIR = Path(__file__).resolve().parents[2]

if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from src.website_checker import check_website
from src.database import save_scan, create_database

# Create database if it doesn't exist
create_database()

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="CyberShield | Website Security",
    page_icon="🛡️",
    layout="wide"
)

# ==========================================================
# Header
# ==========================================================

st.title("🌐 Website Security Checker")
st.write("Analyze a website's security configuration and SSL information.")

st.markdown("---")

# ==========================================================
# User Input
# ==========================================================

url = st.text_input(
    "Enter Website URL",
    placeholder="https://github.com"
)

st.markdown("---")
if st.button("🔍 Analyze Website"):

    if not url.strip():
        st.warning("Please enter a website URL.")

    else:

        with st.spinner("Analyzing Website..."):
            result = check_website(url)

        st.subheader("🛠 Debug Result")
        st.json(result)

        if "error" in result:
            st.error(result["error"])

        else:

            save_scan(
                website=result.get("website", "Unknown"),
                ip_address=result.get("ip", "Unavailable"),
                security_score=result.get("score", 0),
                risk_level=result.get("risk", "Unknown"),
                https="Enabled" if result.get("https") else "Disabled",
                ssl_status=result.get("ssl_status", "Unknown")
            )

            col_logo, col_title = st.columns([1, 5])

            with col_logo:
                if result.get("favicon"):
                    st.image(result["favicon"], width=80)

            with col_title:
                st.success("✅ Analysis Completed Successfully")
                st.header(result.get("website", "Unknown Website"))

            st.markdown("---")

            c1, c2, c3 = st.columns(3)

            with c1:
                st.metric("🌍 IP Address", result.get("ip", "Unavailable"))
                st.metric("📡 Status Code", result.get("status", "N/A"))
                st.metric("⚡ Response Time", f"{result.get('response_time', 'N/A')} ms")

            with c2:
                st.metric("🏢 Server", result.get("server", "Unknown"))
                st.metric("🔒 HTTPS", "Enabled ✅" if result.get("https") else "Disabled ❌")
                st.metric("🔐 SSL Status", result.get("ssl_status", "Unavailable"))

            with c3:
                st.metric("📅 SSL Expiry", result.get("ssl_expiry", "Unavailable"))
                st.metric("🛡 Security Score", f"{result.get('score', 0)}/100")
                st.metric("🚦 Risk Level", result.get("risk", "Unknown"))

            st.markdown("---")
                        # ==========================================================
            # Security Headers
            # ==========================================================

            st.subheader("🛡 Security Headers")

            headers = result.get("headers", {})

            if headers:
                for header, present in headers.items():
                    if present:
                        st.success(f"✅ {header}")
                    else:
                        st.error(f"❌ {header}")
            else:
                st.warning("No Security Header Information Found.")

            st.markdown("---")

            # ==========================================================
            # Recommendations
            # ==========================================================

            st.subheader("💡 Security Recommendations")

            recommendations = []

            for header, present in headers.items():
                if not present:
                    recommendations.append(f"Add **{header}** header.")

            if not result.get("https"):
                recommendations.append("Enable HTTPS.")

            if result.get("ssl_status") != "Valid ✅":
                recommendations.append("Install or renew a valid SSL certificate.")

            if recommendations:
                for rec in recommendations:
                    st.warning(rec)
            else:
                st.success(
                    "🎉 Excellent! This website follows recommended security practices."
                )

            st.markdown("---")
            st.caption("🛡 CyberShield • Website Security Analyzer")
