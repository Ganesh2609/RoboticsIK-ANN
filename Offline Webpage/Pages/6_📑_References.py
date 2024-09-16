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
st.markdown('<div class="right-column"><h2> REFERENCES </h2></div>', unsafe_allow_html=True)
st.write('')
st.write('')

st.markdown('<div class="subcontent"><h3> 1) Blender - <a href="https://www.blender.org/download/releases/4-0/" target="_blank"> Click here to access blender </a></h3></div>', unsafe_allow_html=True)
st.markdown('<div class="subcontent"><h3> 2) Literature - <a href="https://www.mdpi.com/2076-3417/12/19/9417#:~:text=2.-,Methodology%20Structure,a%20sequential%20set%20of%20ANNs" target="_blank"> Click here to access the literature </a></h3></div>', unsafe_allow_html=True)
st.markdown('<div class="subcontent"><h3> 3) Simulation integration - <a href="https://youtu.be/lGokKxJ8D2c" target="_blank"> Click here to access simulation integration </a></h3></div>', unsafe_allow_html=True)
st.markdown('<div class="subcontent"><h3> 4) Coppeliasim     - <a href="https://www.coppeliarobotics.com/" target="_blank"> Click here to access Coppeliasim </a></h3></div>', unsafe_allow_html=True)

