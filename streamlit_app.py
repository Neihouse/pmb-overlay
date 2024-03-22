import streamlit as st
import os
from PIL import Image
# Assuming 'reflex' is a library that provides enhanced UI components for Streamlit
from reflex import ui

# Page configuration
st.set_page_config(page_title='PhotoMeBooth', page_icon=':camera:')

# Logo paths
LOGO_DARK = '/Users/chanceneihouse/MyuzoLabs/pmb-overlay/pmb-logo/Dark-Logo.png'
LOGO_LIGHT = '/Users/chanceneihouse/MyuzoLabs/pmb-overlay/pmb-logo/Light-Logo.png'
LOGO_JUST = '/Users/chanceneihouse/MyuzoLabs/pmb-overlay/pmb-logo/justlogo.png'

# Helper function to load and display logos
def load_logo(logo_path):
    if os.path.isfile(logo_path):
        return Image.open(logo_path)
    else:
        st.error(f'Logo file not found at {logo_path}')
        return None

# Main function
def main():
    st.sidebar.title("Navigation")
    # Utilizing Reflex for enhanced navigation
    page = ui.tab_bar(
        tabs=["Home", "Create New Overlay", "Provide Feedback"],
        help_text="Select a page to navigate to..."
    )

    if page == "Home":
        home_screen()
    elif page == "Create New Overlay":
        create_overlay_page()
    elif page == "Provide Feedback":
        feedback_page()

def home_screen():
    logo = load_logo(LOGO_LIGHT)
    if logo:
        st.image(logo, use_column_width=True)
    
    st.title('Welcome to PhotoMeBooth')
    st.header('Create personalized photo overlays with AI!')
    st.write('Select "Create New Overlay" from the navigation to start customizing your photo overlays.')

def create_overlay_page():
    logo = load_logo(LOGO_DARK)
    if logo:
        st.image(logo, use_column_width=True)

    st.title('Create Your Overlay')
    description = st.text_area('Describe your overlay', 'e.g., "birthday party with balloons and confetti"')
    
    uploaded_file = st.file_uploader('Choose your base image', type=['png', 'jpg'])
    if uploaded_file:
        st.image(uploaded_file, caption='Your Base Image', use_column_width=True)
    
    if st.button('Generate Preview'):
        with st.spinner('Generating your overlay...'):
            # Placeholder for overlay generation process
            st.success('Here is your preview! (placeholder)')

def feedback_page():
    logo = load_logo(LOGO_JUST)
    if logo:
        st.image(logo, use_column_width=True)

    st.title('Provide Feedback')
    feedback = st.text_area('Your feedback')
    # Assuming Reflex provides an enhanced button component
    if ui.button('Submit Feedback', style='primary'):
        st.success('Thank you for your feedback!')

if __name__ == '__main__':
    main()