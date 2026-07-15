import streamlit as st
import sys
from pathlib import Path

# ======================================================
# Add project root to Python path
# ======================================================

ROOT_DIR = Path(__file__).resolve().parents[2]

if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from src.password_checker import check_password

# ======================================================
# Page Configuration
# ======================================================

st.set_page_config(
    page_title="Password Analyzer",
    page_icon="🔐",
    layout="wide"
)

# ======================================================
# Title
# ======================================================

st.title("🔐 Password Strength Analyzer")

st.write("Analyze your password strength and receive security suggestions.")

st.markdown("---")

# ======================================================
# Input
# ======================================================

password = st.text_input(
    "Enter Password",
    type="password"
)

# ======================================================
# Analyze
# ======================================================

if st.button("Analyze Password"):

    if password.strip() == "":
        st.warning("Please enter a password.")

    else:

        score, strength, suggestions = check_password(password)

        st.subheader("Analysis Result")

        st.metric(
            "Security Score",
            f"{score}/5"
        )

        if score == 5:
            st.success(strength)

        elif score >= 3:
            st.warning(strength)

        else:
            st.error(strength)

        st.progress(score / 5)

        st.markdown("### Suggestions")

        if suggestions:

            for suggestion in suggestions:
                st.write("✅", suggestion)

        else:
            st.success("Excellent! Your password follows all recommended security practices.")