import streamlit as st
st.set_page_config page_title='PhotoMeBooth', page_icon=':camera:rgb'

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Create New Overlay", "Provide Feedback"])

    if page == "Home":
        home_screen()
    elif page == "Create New Overlay":
        create_overlay_page()
    elif page == "Provide Feedback":
        feedback_page()

def home_screen():
    st.image('file.png', use_column_width=True)
    st.title('Welcome to PhotoMeBooth')
    st.header('Create personalized photo overlays with AI!')
    st.write('These selected overlays will add a special touch to your event and make it more memorable.')

def create_overlay_page():
    st.title('Create Your Overlay')
    description = st.text_area('Describe your overlay', '"e.g.,"birthday party with balloons and confetti"')
    uploaded_file = st.file_uploader('Choose your base image', type=['png', 'jpg'])
    if uploaded_file:
        st.image(uploaded_file, caption='Your Base Image')
    st.button('Generate Preview')

def feedback_page():
    st.title('Provide Feedback')
    feedback = st.text_area('Your feedback')
    st.markdown('*We value your input and would love to hear what you have to say, whether it's a compliment, a suggestion, a question, or a concern.'}
    st.button('Submit Feedback')

if __name__ == '__main__':
    main()
    