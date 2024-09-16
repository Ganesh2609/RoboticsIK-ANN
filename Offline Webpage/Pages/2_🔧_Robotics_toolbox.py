import streamlit as st
import os
from PIL import Image
import base64

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
st.markdown('<div class="right-column"><h2> ROBOTICS TOOLBOX - MANIPULATOR </h2></div>', unsafe_allow_html=True)    

pdf_name = 'roboticstoolbox_manipulator.pdf'
with open(pdf_name, "rb") as f:
    base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'''
    <div style="display: flex; justify-content: center; align-items: center; height: 100vh;">
        <embed src="data:application/pdf;base64,{base64_pdf}" width="80%" height="90%" type="application/pdf">
    </div>
    '''
    st.markdown(pdf_display, unsafe_allow_html=True)
