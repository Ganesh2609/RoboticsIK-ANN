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
st.markdown('<div class="right-column"><h2> QUESTIONS AND ANSWERS </h2></div>', unsafe_allow_html=True)
st.write('')


# Part - 1
st.markdown('<div class="subhead"><h3> Theory Questions </h3></div>', unsafe_allow_html=True)
st.write('')
st.write('')

st.markdown('<div class="subcontent" style="font-weight: bold;"><h3> 1. What is the Degrees of Freedom (DOF) for the IRB-140 robot? </h3></div>', unsafe_allow_html=True)
st.markdown('<div class="subcontent"><h3> Answer: The IRB-140 robot has 6 degrees of freedom. </h3></div>', unsafe_allow_html=True)
st.write('')
st.write('')

st.markdown('<div class="subcontent"><h3> 2. What is the significance of Denavit-Hartenberg (DH) parameters in robotic kinematics? </h3></div>', unsafe_allow_html=True)
st.markdown('<div class="subcontent"><h3> Answer: Denavit-Hartenberg parameters provide a standardized way to represent the relative positions and orientations of links and joints in a robot. This standardization simplifies the kinematic equations and helps in systematically deriving the forward and inverse kinematics of the robot. </h3></div>', unsafe_allow_html=True)
st.write('')
st.write('')

st.markdown('<div class="subcontent"><h3> 3. What is forward kinematics, and why is it important? </h3></div>', unsafe_allow_html=True)
st.markdown('<div class="subcontent"><h3> Answer: Forward kinematics involves calculating the position and orientation of the robot\'s end-effector based on the given joint angles. It is important because it allows us to determine the pose of the robot\'s end-effector, which is crucial for tasks like positioning, path planning, and simulation. </h3></div>', unsafe_allow_html=True)
st.write('')
st.write('')

st.markdown('<div class="subcontent"><h3> 4. Explain the difference between forward and inverse kinematics. </h3></div>', unsafe_allow_html=True)
st.markdown('<div class="subcontent"><h3> Answer: Forward kinematics calculates the end-effector\'s pose (position and orientation) from given joint angles. Inverse kinematics, on the other hand, determines the joint angles required to achieve a desired end-effector pose. Forward kinematics is generally straightforward, while inverse kinematics can be more complex and may have multiple or no solutions. </h3></div>', unsafe_allow_html=True)
st.write('')
st.write('')

st.markdown('<div class="subcontent"><h3> 5. What are some common applications of the ABB IRB-140 robot in industry? </h3></div>', unsafe_allow_html=True)
st.markdown('<div class="subcontent"><h3> Answer: The ABB IRB-140 robot is commonly used in applications such as material handling, machine tending, assembly, welding, and packaging. Its precision and versatility make it suitable for a wide range of industrial tasks. </h3></div>', unsafe_allow_html=True)
st.write('')
st.write('')


# Part - 2
st.markdown("<hr style='margin-left: 50px;'>", unsafe_allow_html=True)  
st.markdown('<div class="subhead"><h3> Programming Questions </h3></div>', unsafe_allow_html=True)
st.write('')
st.write('')

st.markdown('<div class="subcontent"><h3> 1. Write a Python script to create a model of the IRB-140 robot using the Robotics Toolbox and print its DH parameters. </h3></div>', unsafe_allow_html=True)
m1, m2, m3 = st.columns((3,6,2))
with m2:    
    st.image(Image.open('Images/img31.jpg'))
st.markdown('<div class="subcontent"><h3> Answer: The script loads the built-in IRB 140 model from the Robotics Toolbox and prints its DH parameters. </h3></div>', unsafe_allow_html=True)
st.write('')
st.write('')

st.markdown('<div class="subcontent"><h3> 2. Write a Python function to calculate the forward kinematics of the IRB-140 given a set of joint angles. </h3></div>', unsafe_allow_html=True)
m1, m2, m3 = st.columns((3,6,2))
with m2:    
    st.image(Image.open('Images/img32.jpg'))
st.markdown('<div class="subcontent"><h3> Answer: The function forward_kinematics takes a list of joint angles, computes the forward kinematics using the IRB 140 model, and returns the end-effector pose. </h3></div>', unsafe_allow_html=True)
st.write('')
st.write('')

st.markdown('<div class="subcontent"><h3> 3. Write a Python function to solve the inverse kinematics for a given target pose of the IRB-140. </h3></div>', unsafe_allow_html=True)
m1, m2, m3 = st.columns((3,6,2))
with m2:    
    st.image(Image.open('Images/img33.jpg'))
st.markdown('<div class="subcontent"><h3> Answer: The function inverse_kinematics takes a target pose, computes the inverse kinematics using the IRB 140 model, and returns the joint angles required to achieve the target pose. </h3></div>', unsafe_allow_html=True)
st.write('')
st.write('')

st.markdown('<div class="subcontent"><h3> 4. How would you verify the correctness of the forward and inverse kinematics functions? </h3></div>', unsafe_allow_html=True)
st.markdown('<div class="subcontent"><h3> Answer: To verify the correctness: </h3></div>', unsafe_allow_html=True)
st.markdown('<div class="subcontent"><h3> &nbsp &nbsp &nbsp &nbsp 1. Select a set of joint angles. </h3></div>', unsafe_allow_html=True)
st.markdown('<div class="subcontent"><h3> &nbsp &nbsp &nbsp &nbsp 2. Compute the end-effector pose using the forward kinematics function. </h3></div>', unsafe_allow_html=True)
st.markdown('<div class="subcontent"><h3> &nbsp &nbsp &nbsp &nbsp 3. Use the computed end-effector pose as the target pose for the inverse kinematics function. </h3></div>', unsafe_allow_html=True) 
st.markdown('<div class="subcontent"><h3> &nbsp &nbsp &nbsp &nbsp 4. Compare the joint angles returned by the inverse kinematics function with the original joint angles. </h3></div>', unsafe_allow_html=True) 
st.markdown('<div class="subcontent"><h3> &nbsp &nbsp &nbsp &nbsp 5. The results should match closely, considering numerical tolerances. </h3></div>', unsafe_allow_html=True) 
st.write('')
st.write('')
