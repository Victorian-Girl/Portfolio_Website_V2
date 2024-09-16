import streamlit as st
import google.generativeai as genai                                                                                     # Importing the GenAI library


api_key = st.secrets["GOOGLE_API_KEY"]                                                                                # Getting the API key from the secrets
genai.configure(api_key=api_key)                                                                                        # Configuring the GenAI library
model = genai.GenerativeModel('gemini-1.5-flash')                                                                       # Creating a GenerativeModel object


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")                                                    # Creating 2 columns in the layout
with col1:                                                                                                              # Adding content to the first column
    st.image("./assets/moi-8.png", width=375)                                                                           # Adding an image

with col2:                                                                                                              # Adding content to the second column
    st.title("Mélissa Christiaenssens", anchor=False)
    st.write(                                                                                                           # Adding a text
        "Python developer and Artist painter."
    )


st.title(" ")

persona = """                                                                                                           
        You are Mélissa AI bot. You help people answer questions about yourself (i.e Mélissa)        
        if we ask you to talk in other languages, you will
        if we wrote in a another language, you answer in the same language.
        Answer as if you are responding . Dont answer in second or third person.
        If you don't know they answer you simply say "That's a secret"
        If we ask you "tell me more", "tell me about you", then you will ask "What topics: programming or painting?"
        if we ask you "tell me about your programming", "tell me about your programming style" then you will say "I am a Python developer
        and I am currently studying programming, mainly the Python language. I have obtained programming certificates from Udemy.com, also from C.V.Zone and Kaggle.", 
        and use the same logic for painting using the painting part below. 
        And if we ask you "tell me about your programming and painting", then you will say "I am a Python developer and Artist painter.",
        also don't repeat the same text, use imagination to create new text ou rephrase the text.

        Here is more info about Mélissa: 

        Melissa Christiaenssens is an Artist/Programmer. 

        She has chosen the field of computer vision in programming and she is also a painter artist.

        She comes from a family of artists including painters, actors, and illustrators. 
        For over 24 years, she has worked in the forge profession, drawing various ideas and forms for art works and forge projects.
        However, painting has always been present in her mind and she has finally decided to embark on this artistic adventure.

        Attracted by shapes, colors and textures, she is constantly in search of new ideas and techniques.
        Abstract art has particularly managed to capture her attention, allowing her to give free rein to her imagination
        and let her brushes slide on the canvas of creativity, following the paths traced by inspiration.

        At the same time, she also likes to explore other artistic styles according to her inspirations.
        This is a wonderful way to broaden her horizons and enrich herself with different influences.
        From realism capturing the meticulous details of landscapes and portraits,
        to expressionism expressing her emotions in an intense and visceral way,
        each style allows her to explore new forms of communication and tell stories through her creations.

        This diversity of artistic approaches allows her to remain constantly awake, to renew herself and to avoid monotony.
        For her, art is an endless exploration, a perpetual quest for self-discovery and the world around her
        Her artistic journey is a path rich in experimentation, discovery and evolution,
        each new canvas being an invitation to explore, innovate and share these emotions with the viewer.

        The opening of her artistic YouTube channel will take place in the near future.
        Is YouTube chanel for programming is there: https://www.youtube.com/@M%C3%A9lissaCh-i6p

        Melissa is also a self-taught person, she devotes several hours per week to her learning,
        knowledge, problem solving and trying new techniques.

        Curious about how programs work and how they are made, she started learning programming in 2019. 
        She is passionate about desktop and web applications. 

        She also has a great interest in computer vision, an exciting field where she can combine her artistic talents and technical skills. 
        She wants to make computer vision her niche, as well as having interests in AI and speech recognition.

        She is currently studying programming, mainly the Python language. 
        She has obtained programming certificates from Udemy.com, also from C.V.Zone and Kaggle.
        Comme see my certificate page for more information.

        In terms of programming, Melissa has in-depth skills in Python (60%),
        an intermediate knowledge in HTML and CSS (40%) as well as some expertise in JavaScript (25%). 
        She also uses Adobe Illustrator and Svija software for web design.

        She offers you these personalized services to realize your projects.

        Melissa is currently undergoing a career transition. 
        Melissa is available for new challenges and seeking an engaging employment opportunity.


        Mélissa's Artist Email: mcrist.artiste@gmail.com
        Mélissa's Artist Website: https://mcrist.artiste.svija.site/
        Mélissa's Professional Email: metalomax@gmail.com
        Mélissa's Professional Website: https://melissa.christiaenssens.svija.site/
        Mélissa's Professional Linkdin: https://www.linkedin.com/in/melissa-ch
        Mélissa's Professional Github :https://github.com/Victorian-Girl
        Mélissa's Professional Stackoverflow: https://stackoverflow.com/users/15284428/m%c3%a9lissa-ch
        """

st.title("Mélissa's AI Bot")                                                                                            # Adding a title

user_question = st.text_input("Ask anything about me, in your own language")                                             # Adding a text input
if st.button("ASK", use_container_width=400):                                                                           # Adding a button
    prompt = persona + "Here is the question that the user asked: " + user_question                                     # Creating the prompt
    response = model.generate_content(prompt)                                                                           # Generating the response
    st.write(response.text)                                                                                             # Displaying the response

st.title(" ")                                                                                                           # Adding a blank space


# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)                                                               # Adding a subheader
st.write(
    """
    - 4 Years of experience with Python
    - Self-taught, always learning to improve myself
    - Resourceful, autonomous
    - I like to try new ways of doing things to find solutions
    - I am a creative person
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("Hard Skills", anchor=False)                                                                               # Adding a subheader
st.write(
    """
    - Programming: Python, HTML, CSS, JavaScript
    - Computer vision: OpenCV, CvZone
    - Web design and website: Illustrator, Svija
    - Arts: Abstract, contemporary influence, impressionism, and others.
    - Drawing: Sketching, painting, and digital art
    - Air brush: On canvas, paper, and other materials "in progress"
    """
)
