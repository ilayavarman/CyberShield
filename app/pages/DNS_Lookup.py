import streamlit as st
import sys
from pathlib import Path

# ==========================================================
# Add Project Root
# ==========================================================

ROOT_DIR = Path(__file__).resolve().parents[2]

if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from src.dns_lookup import dns_lookup

# ==========================================================
# Page Config
# ==========================================================

st.set_page_config(
    page_title="CyberShield | DNS Lookup",
    page_icon="🌐",
    layout="wide"
)

st.title("🌐 DNS Lookup")
st.write("Find DNS records for any domain.")

st.markdown("---")

domain = st.text_input(
    "Enter Domain",
    placeholder="github.com"
)

if st.button("🔍 Lookup DNS"):

    if domain.strip() == "":
        st.warning("Please enter a domain.")

    else:

        with st.spinner("Looking up DNS Records..."):

            result = dns_lookup(domain)

        if "Error" in result:

            st.error(result["Error"])

        else:

            st.success("DNS Lookup Completed Successfully")

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "🌍 IP Address",
                    result["IP Address"]
                )

                st.subheader("📌 A Record")

                if result["A Record"]:
                    for item in result["A Record"]:
                        st.code(item)
                else:
                    st.info("Not Found")

                st.subheader("📌 AAAA Record")

                if result["AAAA Record"]:
                    for item in result["AAAA Record"]:
                        st.code(item)
                else:
                    st.info("Not Found")

            with col2:

                st.subheader("📨 MX Record")

                if result["MX Record"]:
                    for item in result["MX Record"]:
                        st.code(item)
                else:
                    st.info("Not Found")

                st.subheader("🖥 NS Record")

                if result["NS Record"]:
                    for item in result["NS Record"]:
                        st.code(item)
                else:
                    st.info("Not Found")

                st.subheader("📄 TXT Record")

                if result["TXT Record"]:
                    for item in result["TXT Record"]:
                        st.code(item)
                else:
                    st.info("Not Found")