import streamlit as st
from PIL import Image

# Basic configuration
st.set_page_config(page_title='IRB 140 - Group 3', page_icon=':mechanical_arm:', layout='wide')

# Function to import CSS file
def load_css(file_name):
    with open(file_name) as f:
        return f.read()

# Import the CSS file
st.markdown(f"<style>{load_css('theory.css')}</style>", unsafe_allow_html=True)

st.markdown("<div class='main_header'> IRB 140 - INDUSTRIAL ROBOT [BATCH - A : GROUP - 3] </div>", unsafe_allow_html=True)

st.write('')
st.write('')
st.write('')
st.write('')
st.markdown('<div class="right-column"><h2> SIMULATION OF IRB - 140 </h2></div>', unsafe_allow_html=True)
st.write('')
st.write('')

m1, m2, m3, m4 = st.columns((2, 5, 5, 1))
with m2:
    st.image(Image.open('Images/img34.jpg'))
with m3:
    st.image(Image.open('Images/img35.jpg'))

st.write('')
st.write('')

# Create a function to display a styled button and redirect to the URL
def button_redirect(url, label):
    button_html = f'<a href="{url}" target="_blank" style="padding: 10px 20px; background-color: #008CBA; color: white; border: none; border-radius: 5px; cursor: pointer; text-decoration: none;">{label}</a>'
    st.markdown(button_html, unsafe_allow_html=True)

# Call the function with the YouTube URL and button label
button_redirect('simulation/web-3dmodel-threejs/index.html', 'Launch Robot Simulation')
