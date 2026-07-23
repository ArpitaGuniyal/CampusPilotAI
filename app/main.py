import streamlit as st

from pages import (
    home,
    student,
    faculty,
    library,
    chatbot,
    about
)

st.set_page_config(
    page_title="CampusPilotAI",
    page_icon="🎓",
    layout="wide"
)

st.sidebar.title("🎓 CampusPilotAI")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Student",
        "Faculty",
        "Library",
        "AI Assistant",
        "About"
    ]
)

st.sidebar.divider()

st.sidebar.caption("CampusPilotAI v1.0")

st.sidebar.caption("Built with ❤️ using Streamlit")

if page == "Home":
    home.show()

elif page == "Student":
    student.show()

elif page == "Faculty":
    faculty.show()

elif page == "Library":
    library.show()

elif page == "AI Assistant":
    chatbot.show()

elif page == "About":
    about.show()