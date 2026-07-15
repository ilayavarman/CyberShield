import streamlit as st
import sys
from pathlib import Path

# ==========================================================
# Add Project Root
# ==========================================================

ROOT_DIR = Path(__file__).resolve().parents[2]

if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from src.whois_lookup import whois_lookup

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="CyberShield | WHOIS Lookup",
    page_icon="🌍",
    layout="wide"
)

# ==========================================================
# Header
# ==========================================================

st.title("🌍 WHOIS Lookup")
st.write("Retrieve public registration information for a domain.")

st.markdown("---")

# ==========================================================
# User Input
# ==========================================================

domain = st.text_input(
    "Enter Domain",
    placeholder="github.com"
)

# ==========================================================
# Lookup Button
# ==========================================================

if st.button("🔍 Lookup WHOIS"):

    if domain.strip() == "":
        st.warning("Please enter a domain.")
    else:

        with st.spinner("Fetching WHOIS information..."):

            result = whois_lookup(domain)

        if "error" in result:

            st.error(result["error"])

        else:

            st.success("✅ WHOIS Information Retrieved Successfully")

            st.markdown("---")

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "🌐 Domain",
                    result["domain"]
                )

                st.metric(
                    "🏢 Registrar",
                    result["registrar"]
                )

                st.metric(
                    "📅 Creation Date",
                    result["creation_date"]
                )

                st.metric(
                    "📅 Expiry Date",
                    result["expiry_date"]
                )

                st.metric(
                    "🟢 Domain Age",
                    result["domain_age"]
                )

            with col2:

                st.metric(
                    "🌍 Country",
                    result["country"]
                )

                st.metric(
                    "🏛 Organization",
                    result["organization"]
                )

                st.write("📧 **Abuse Email**")
                st.code(str(result["abuse_email"]))

                st.write("📄 **Status**")
                st.code(str(result["status"]))

            st.markdown("---")

            st.subheader("🖥 Name Servers")

            if result["name_servers"]:

                for ns in result["name_servers"]:

                    st.code(ns)

            else:

                st.info("No Name Servers Found.")

            st.markdown("---")

            st.subheader("📘 About WHOIS")

            st.info(
                """
WHOIS provides publicly available registration information about a domain.

CyberShield displays:

• 🌐 Domain Name
• 🏢 Registrar
• 📅 Creation Date
• 📅 Expiry Date
• 🟢 Domain Age
• 🌍 Country
• 🏛 Organization
• 📧 Abuse Email
• 🖥 Name Servers
• 📄 Domain Status
"""
            )

            st.markdown("---")

            st.caption("🛡 CyberShield | WHOIS Lookup v1.0")