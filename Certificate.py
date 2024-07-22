import streamlit as st


col1, col2 = st.columns(2)                                                                                              # Creating 2 columns in the layout

with col1:                                                                                                              # Adding content to the first column
    st.subheader("Hi :wave:")                                                                                           # Adding a subheader
    st.title("My certificate's")                                                                                        # Adding a title

with col2:                                                                                                              # Adding content to the second column
    st.image("./assets/moi-8.png")                                                                                      # Adding an image

st.title(" ")

col1, col2, col3 = st.columns(3)                                                                                        # Creating 3 columns in the layout

with col1:                                                                                                              # Adding content to the first column
    st.image("certificate/CV_Game.JPG")                                                                                 # Adding an image
    st.image("certificate/CV_Web.jpg")
    st.image("certificate/Kaggle_Python.png")

with col2:                                                                                                              # Adding content to the second column
    st.image("certificate/Kaggle_C-V.png")                                                                              # Adding an image
    st.image("certificate/Kaggle_Intro_ML.png")
    st.image("certificate/Kaggle_Intermediate_ML.png")

with col3:                                                                                                              # Adding content to the third column
    st.image("certificate/Udemy_dev_Python.jpg")                                                                        # Adding an image
    st.image("certificate/Udemy_IA_2024.jpg")

st.subheader(" ")                                                                                                       # Adding a subheader
st.write("CONTACT")                                                                                                     # Adding a text
st.title("For any inquiries, email at:")                                                                                # Adding a title
st.subheader("Professional:  metalomax@gmail.com")                                                                      # Adding a subheader
