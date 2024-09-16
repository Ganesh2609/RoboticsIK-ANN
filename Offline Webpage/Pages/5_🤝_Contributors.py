import streamlit as st
import os
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
st.markdown('<div class="right-column"><h2> CONTRIBUTORS </h2></div>', unsafe_allow_html=True)
st.write('')
st.write('')
st.markdown('<div class="subcontent2"><h3> 1) Ganesh Sundhar S [CB.EN.U4AIE22017] &nbsp &nbsp &nbsp - Inverse kinematics using ANN and simulation along with its integration in website </h3></div>', unsafe_allow_html=True)
st.markdown('<div class="subcontent2"><h3> 2) Hari Krishnan N [CB.EN.U4AIE22020] &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp - Inverse kinematics using ANN and simulation along with its integration in website </h3></div>', unsafe_allow_html=True)
st.markdown('<div class="subcontent2"><h3> 3) Pranav [CB.EN.U4AIE22016] &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp - Wesbsite development using python libraries streamlit and PIL (major)</h3></div>', unsafe_allow_html=True)
st.markdown('<div class="subcontent2"><h3> 4) Siri Reddy [CB.EN.U4AIE22019] &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp - Preparing website content along with robotics toolbox maipulator page </h3></div>', unsafe_allow_html=True)