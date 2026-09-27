import streamlit as st

from database.connection import check_connection
from database.repositories.subjects import SubjectRepository
from database.repositories.topics import TopicRepository
from database.repositories.users import UserRepository


st.set_page_config(
    page_title="Adaptive AI Mock Test Engine",
    page_icon="🎓",
    layout="wide",
)


def main() -> None:
    st.title("🎓 Adaptive AI Mock Test Engine")
    st.caption("Phase 1 — Neon database foundation")

    with st.sidebar:
        st.header("System Status")

        if check_connection():
            st.success("Neon database connected")
        else:
            st.error("Neon database connection failed")
            st.info("Check DATABASE_URL in .env or Streamlit secrets.")

    if not check_connection():
        st.stop()

    st.subheader("Database verification")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Users", UserRepository().count())

    with col2:
        st.metric("Subjects", SubjectRepository().count())

    with col3:
        st.metric("Topics", TopicRepository().count())

    st.divider()

    st.markdown(
        '''
        ### Phase 1 is intentionally small

        The application is **not** calling Gemini, Groq, or R2 yet.

        We first establish:

        `Streamlit → Repository Layer → Neon PostgreSQL`

        After this is verified, we add storage and AI services without
        changing the database contract.
        '''
    )


if __name__ == "__main__":
    main()
