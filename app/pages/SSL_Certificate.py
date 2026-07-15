import streamlit as st
import sys
from pathlib import Path

# ==========================================================
# Add Project Root
# ==========================================================

ROOT_DIR = Path(__file__).resolve().parents[2]

if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from src.ssl_checker import check_ssl

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="CyberShield | SSL Certificate Inspector",
    page_icon="🔒",
    layout="wide"
)

# ==========================================================
# Header
# ==========================================================

st.title("🔒 SSL Certificate Inspector")
st.write("Inspect SSL/TLS certificate details of any website.")

st.markdown("---")

# ==========================================================
# User Input
# ==========================================================

domain = st.text_input(
    "Enter Website",
    placeholder="github.com"
)

# ==========================================================
# Analyze Button
# ==========================================================

if st.button("🔍 Inspect Certificate"):

    if domain.strip() == "":

        st.warning("Please enter a website.")

    else:

        with st.spinner("Fetching SSL Certificate..."):

            result = check_ssl(domain)

        if "error" in result:

            st.error(result["error"])

        else:

            st.success("✅ SSL Certificate Retrieved Successfully")

            st.markdown("---")

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "🌐 Website",
                    result["website"]
                )

                st.metric(
                    "🔒 SSL Status",
                    result["status"]
                )

                st.metric(
                    "🔐 TLS Port",
                    result["port"]
                )

            with col2:

                st.metric(
                    "🏢 Issuer",
                    result["issuer"]
                )

                st.metric(
                    "📄 Common Name",
                    result["common_name"]
                )

                st.metric(
                    "📜 Certificate Version",
                    result["version"]
                )

            with col3:

                st.metric(
                    "📅 Valid From",
                    result["valid_from"]
                )

                st.metric(
                    "📅 Expiry Date",
                    result["valid_until"]
                )

                st.metric(
                    "⏳ Days Remaining",
                    result["days_remaining"]
                )

            st.markdown("---")
            # ==========================================================
# Certificate Summary
# ==========================================================

            st.subheader("🛡 Certificate Summary")

            days = result["days_remaining"]

            if result["status"] != "Valid ✅":

                st.error(
                    "❌ SSL Certificate is invalid or could not be verified."
                )

            elif days > 365:

                st.success(
                    f"🟢 Excellent! The SSL certificate is valid and expires in {days} days."
                )

            elif days > 180:

                st.success(
                    f"✅ SSL certificate is healthy. {days} days remaining."
                )

            elif days > 90:

                st.info(
                    f"ℹ️ SSL certificate is valid. {days} days remaining before expiry."
                )

            elif days > 30:

                st.warning(
                    f"⚠️ SSL certificate expires in {days} days. Plan the renewal."
                )

            elif days > 7:

                st.error(
                    f"🚨 SSL certificate expires in only {days} days. Renew it soon."
                )

            elif days > 0:

                st.error(
                    f"❌ Critical! SSL certificate expires in {days} days."
                )

            else:

                st.error(
                    "❌ SSL certificate has expired."
                )

            st.markdown("---")

# ==========================================================
# Certificate Information
# ==========================================================

            st.subheader("📘 About SSL Certificate")

            st.info(
                """
🔒 **SSL (Secure Sockets Layer)** protects data exchanged between your browser and the website.

CyberShield checks:

- 🌐 Website Name
- 🔒 SSL Certificate Status
- 🏢 Certificate Issuer
- 📄 Common Name (CN)
- 📅 Certificate Validity
- ⏳ Remaining Days
- 🔐 TLS Port
- 📜 Certificate Version

A valid SSL certificate helps ensure encrypted communication and improves user trust.
                """
            )

            st.markdown("---")

# ==========================================================
# Security Recommendation
# ==========================================================

            st.subheader("💡 Security Recommendation")

            if days > 180:

                st.success(
                    "✅ This website has a healthy SSL certificate. No immediate action is required."
                )

            elif days > 30:

                st.warning(
                    "⚠️ The SSL certificate is valid but should be monitored for renewal."
                )

            else:

                st.error(
                    "🚨 Renew the SSL certificate immediately to avoid service interruption."
                )

            st.markdown("---")

            st.caption("🛡 CyberShield | SSL Certificate Inspector v1.0")