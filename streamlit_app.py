import streamlit as st


def initialize_chatbot():
    # Initialization code for the chatbot components and states
    st.write("Chatbot initialized on this page!")


# Get the current page parameter from the URL using st.query_params
query_params = st.query_params
current_page = query_params.get("page", "")

# Based on the current page, initialize the chatbot
if current_page == "about_me":
    initialize_chatbot()


# --- PAGE SETUP ---

project_1_page = st.Page(
    "Professional_Portfolio.py",
    title="Professional_Portfolio",
    icon=":material/computer:",
)
project_2_page = st.Page(
    "Artist_Portfolio.py",
    title="Artist_Portfolio",
    icon=":material/palette:",
)
project_3_page = st.Page(
    "Certificate.py",
    title="Certificate",
    icon=":material/license:",
)
about_page = st.Page(
    "about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)


# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page, project_3_page],
    }
)


# --- SHARED ON ALL PAGES ---
st.logo("assets/logo4.jpg")                                                                                            # 24 height, max width = 240 px or 10:1 ratio
st.sidebar.text("Made with ❤️ by Mélissa")


# --- RUN NAVIGATION ---
pg.run()
