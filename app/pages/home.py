import streamlit as st

from data.loader import load_data


def show():

    datasets = load_data()

    st.title("🎓 CampusPilotAI")

    st.caption("AI-Powered Smart College Management System")

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "👨‍🎓 Students",
            len(datasets["students"])
        )

    with col2:
        st.metric(
            "👨‍🏫 Faculty",
            len(datasets["faculty"])
        )

    with col3:
        st.metric(
            "🏢 Departments",
            len(datasets["departments"])
        )

    col4, col5, col6 = st.columns(3)

    with col4:
        st.metric(
            "📚 Books",
            len(datasets["books"])
        )

    with col5:
        st.metric(
            "📖 Subjects",
            len(datasets["subjects"])
        )

    with col6:
        st.metric(
            "🏫 Sections",
            len(datasets["sections"])
        )

    st.divider()

    st.subheader("📂 Loaded Datasets")

    for name, df in sorted(datasets.items()):

        st.write(
            f"✅ **{name}** — {len(df):,} records"
        )