import streamlit as st
import os

st.set_page_config(page_title='PhotoMeBooth', page_icon=':camera:')

# Assuming your streamlit_app.py is in the 'pmb-overlay' directory.
# Update these paths to match where your image files are located.
LOGO_DARK = '/Users/chanceneihouse/MyuzoLabs/pmb-overlay/pmb-logo/Dark-Logo.png'  # Updated path
LOGO_LIGHT = '/Users/chanceneihouse/MyuzoLabs/pmb-overlay/pmb-logo/Light-Logo.png'  # Updated path
LOGO_JUST = '/Users/chanceneihouse/MyuzoLabs/pmb-overlay/pmb-logo/justlogo.png'  # Updated path

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
    if os.path.isfile(LOGO_LIGHT):
        st.image(LOGO_LIGHT, use_column_width=True)
    else:
        st.error('Light logo file not found.')
    
    st.title('Welcome to PhotoMeBooth')
    st.header('Create personalized photo overlays with AI!')
    st.write('These selected overlays will add a special touch to your event and make it more memorable.')

def create_overlay_page():
    if os.path.isfile(LOGO_DARK):
        st.image(LOGO_DARK, use_column_width=True)
    else:
        st.error('Dark logo file not found.')

    st.title('Create Your Overlay')
    description = st.text_area('Describe your overlay', 'e.g., "birthday party with balloons and confetti"')
    uploaded_file = st.file_uploader('Choose your base image', type=['png', 'jpg'])
    if uploaded_file:
        st.image(uploaded_file, caption='Your Base Image')
    st.button('Generate Preview')

def feedback_page():
    if os.path.isfile(LOGO_JUST):
        st.image(LOGO_JUST, use_column_width=True)
    else:
        st.error('Just logo file not found.')

    st.title('Provide Feedback')
    feedback = st.text_area('Your feedback')
    st.markdown('*We value your input and would love to hear what you have to say, whether it\'s a compliment, a suggestion, a question, or a concern.*')
    st.button('Submit Feedback')

if __name__ == '__main__':
    main()
