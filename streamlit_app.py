import base64

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
        "Projects": [project_1_page, project_2_page],
        "Certificates": [project_3_page],
    }
)

# --- SHARED ON ALL PAGES ---
image_path = "assets/website1.png"                                                                                      # path to the image
image2_path = "assets/linkedin.png"
image3_path = "assets/git.png"
image4_path = "assets/stackoverflow.png"
image5_path = "assets/youtube.png"

st.sidebar.markdown(                                                                                                    # Adding a markdown content to the sidebar panel
    """
    <h2>Professional Website:
    <a href="https://melissa.christiaenssens.svija.site/">
        <img src="data:image/png;base64,{}" alt="Logo" style="width:40px;">
    </a></h2>
    """.format(base64.b64encode(open(image_path, "rb").read()).decode()), unsafe_allow_html=True
)

st.sidebar.markdown(
    """
    <h2>Artist Website:
    <a href="https://mcrist.artiste.svija.site/">
        <img src="data:image/png;base64,{}" alt="Logo" style="width:40px;">
    </a></h2>
    """.format(base64.b64encode(open(image_path, "rb").read()).decode()), unsafe_allow_html=True
)

st.sidebar.markdown(
    """
    <h2>LinkedIn:
    <a href="https://www.linkedin.com/in/melissa-ch">
        <img src="data:image/png;base64,{}" alt="Logo" style="width:30px;">
    </a></h2>
    """.format(base64.b64encode(open(image2_path, "rb").read()).decode()), unsafe_allow_html=True
)

st.sidebar.markdown(
    """
    <h2>GitHub:
    <a href="https://github.com/Victorian-Girl">
        <img src="data:image/png;base64,{}" alt="Logo" style="width:30px;">
    </a></h2>
    """.format(base64.b64encode(open(image3_path, "rb").read()).decode()), unsafe_allow_html=True
)

st.sidebar.markdown(
    """
    <h2>Stackoverflow:
    <a href="https://stackoverflow.com/users/15284428/m%c3%a9lissa-ch">
        <img src="data:image/png;base64,{}" alt="Logo" style="width:30px;">
    </a></h2>
    """.format(base64.b64encode(open(image4_path, "rb").read()).decode()), unsafe_allow_html=True
)

st.sidebar.markdown(
    """
    <h2>YouTube:
    <a href="https://www.youtube.com/@M%C3%A9lissaCh-i6p">
        <img src="data:image/png;base64,{}" alt="Logo" style="width:30px;">
    </a></h2>
    """.format(base64.b64encode(open(image5_path, "rb").read()).decode()), unsafe_allow_html=True
)


# --- LOGO and FOOTER ---
st.logo("assets/logo4.jpg")                                                                                             # 24 height, max width = 240 px or 10:1 ratio


st.write(" ")
st.sidebar.write('<div style="position: fixed; bottom: 10px; width: 95%;">Made with ❤️ by Mélissa</div>',               # Adding a footer
                 unsafe_allow_html=True)

# --- RUN NAVIGATION ---
pg.run()
