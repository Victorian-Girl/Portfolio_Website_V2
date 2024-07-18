import streamlit as st


def initialize_chatbot():
    # Initialization code for the chatbot components and states
    st.write("Chatbot initialized on this page!")


def render_chatbot_ask_button():
    # Inject JavaScript to handle the Enter key press event
    st.markdown(
        """
        <script>
            document.addEventListener('keypress', function(e){
                if(e.key === 'Enter'){
                    var askButton = document.querySelector("button[data-testid=stCheckbox]");
                    if(askButton){
                        askButton.click();
                    }
                }
            });
        </script>
        """,
        unsafe_allow_html=True
    )

    if st.button("Ask", key="ask_button"):
        initialize_chatbot()
