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
st.markdown('<div class="right-column"><h2> THEORY OF IRB - 140 INDUSTRIAL ROBOT </h2></div>', unsafe_allow_html=True)
st.write('')


# Part - 1
st.markdown('<div class="subhead"><h3> Introduction </h3></div>', unsafe_allow_html=True)
st.markdown('<div class="subcontent"><h3> The ABB IRB-140 robot is a compact industrial manipulator with 6 degrees of freedom (DOF). This robot has a capacity load of 6 Kg and a scope of 810 mm; it also has the possibility of backward dub. Some of the specialized works in which this robot was used are: </h3></div>', unsafe_allow_html=True)
st.markdown('<div class="subcontent"><h3> • The assisted robot system of measurement of 3-D shape for transparent glass created on. </h3></div>', unsafe_allow_html=True)
st.markdown('<div class="subcontent"><h3> • High precision drilling operations, taking advantage of the 6 DOF of ABB IRB-140 robot arm. </h3></div>', unsafe_allow_html=True)
st.markdown('<div class="subcontent"><h3> • Adaptive multimodal applications wherein this robot is provided with artificial vision and controlled by speech, through advanced algorithms of word recognition. </h3></div>', unsafe_allow_html=True)  
st.write('')
m1, m2, m3 = st.columns(3)
with m2:    
    st.image(Image.open('Images/img1.jpg'))
    st.image(Image.open('Images/img2.jpg').resize((239*2, 208*2)))
    
    
# Part - 2
st.markdown("<hr style='margin-left: 50px;'>", unsafe_allow_html=True)
st.markdown('<div class="subhead"><h3> General Terminology in Robotics </h3></div>', unsafe_allow_html=True)
st.markdown('<div class="subcontent"><h3> Workspace: The reachable workspace of a robot\'s end-effector is the manifold of reachable frames. </h3></div>', unsafe_allow_html=True)
m1, m2, m3 = st.columns(3)
with m2:    
    st.image(Image.open('Images/img3.jpg').resize((1000,1000)))
st.markdown('<div class="subcontent"><h3> Accuracy: Accuracy refers to a robot\'s ability to position its wrist end at a desired target point within the work volume, and it is defined in terms of spatial resolution. It depends on the technology and the control increments. </h3></div>', unsafe_allow_html=True)
st.markdown('<div class="subcontent"><h3> Repeatability: Repeatability is a statistical term associated with accuracy. If a robot joint moves by the same angle from a certain point a number of times, all with equal environmental conditions, the target is always missed by a large margin. If the same error is repeated, then we say that the repeatability is high and the accuracy is poor. </h3></div>', unsafe_allow_html=True)
st.markdown('<div class="subcontent"><h3> Safety: The ability to reduce the human-robot impact force and ensure human safety is a fundamental requirement for human-friendly robots. </h3></div>', unsafe_allow_html=True)

# Part - 3
st.markdown("<hr style='margin-left: 50px;'>", unsafe_allow_html=True)
st.markdown('<div class="subhead"><h3> Technical data of ABB IRB-140 Robot </h3></div>', unsafe_allow_html=True)
m1, m2, m3 = st.columns(3)
with m2:    
    st.image(Image.open('Images/img4.jpg').resize((317*2, 384*2)))
    
    
# Part - 4
st.markdown("<hr style='margin-left: 50px;'>", unsafe_allow_html=True)
st.markdown('<div class="subhead"><h3> Forward Kinematics </h3></div>', unsafe_allow_html=True)
st.markdown('<div class="subcontent"><h3> Forward kinematics (FK) mainly deals with constructing a Denavit-Hartenberg (D-H) transformation matrix with IRB-140\'s parameters obtained from a D-H parameter table shown below: </h3></div>', unsafe_allow_html=True)
m1, m2, m3 = st.columns(3)
with m2:    
    st.image(Image.open('Images/img5.jpg'))
    st.image(Image.open('Images/img6.jpg').resize((800,400)))
    
st.write('')
st.markdown('<div class="subcontent"><h3> For the simplicity of calculations and matrix product, it can be assumed that S2 = sin (θ2-90), C2 = cos (θ2-90). After achieving the D-H table, the individual transformation matrix for each link is achieved by substituting the link parameters into the general homogeneous transformation matrix. </h3></div>', unsafe_allow_html=True)
m1, m2, m3 = st.columns((3,10,2))
with m2:
    st.image(Image.open('Images/img7.jpg').resize((1000,1275)))


# Part - 5
st.markdown("<hr style='margin-left: 50px;'>", unsafe_allow_html=True)
st.markdown('<div class="subhead"><h3> Final Transformation matrix </h3></div>', unsafe_allow_html=True)
m1, m2, m3 = st.columns(3)
with m2:    
    st.image(Image.open('Images/img8.jpg'))
    
st.markdown('<div class="subcontent"><h3> The orientation and position of the end effector with reference to the base coordinate is obtained from the final matrix: </h3></div>', unsafe_allow_html=True)
m1, m2, m3 = st.columns(3)
with m2:    
    st.image(Image.open('Images/img9.jpg'))
    
st.markdown('<div class="subcontent"><h3> Here, </h3></div>', unsafe_allow_html=True)
m1, m2, m3 = st.columns((3,6,2))
with m2:    
    st.image(Image.open('Images/img10.jpg').resize((500,125)))
    st.image(Image.open('Images/img11.jpg').resize((500,410)))
    
st.markdown('<div class="subcontent"><h3> It is also possible to find the position of the Tool Centre Point (TCP) with respect to the robot base. According to the robot frame assignment, it is simply a transition along the z axis of frame {6} by d6 (distance from Joint 6 to the TCP). Therefore, the final position of the end effector with respect to the robot global reference frame can be expressed as: </h3></div>', unsafe_allow_html=True)
m1, m2, m3 = st.columns(3)
with m2:    
    st.image(Image.open('Images/img12.jpg'))


# Part - 6
st.markdown("<hr style='margin-left: 50px;'>", unsafe_allow_html=True)  
st.markdown('<div class="subhead"><h3> IRB-140 Kinematic Diagrams </h3></div>', unsafe_allow_html=True)
m1, m2, m3 = st.columns((3,8,2))
with m2:    
    st.image(Image.open('Images/img13.jpg'))
    st.image(Image.open('Images/img14.jpg'))
   
    
# Part - 7
st.markdown("<hr style='margin-left: 50px;'>", unsafe_allow_html=True)
st.markdown('<div class="subhead"><h3> Inverse kinematics </h3></div>', unsafe_allow_html=True)
st.markdown('<div class="subcontent"><h3> Inverse kinematics is used to calculate the joint angles required to achieve the desired position and orientation in the robot workspace. In general, there are two methods of solution, the analytical and geometrical approaches. Since three consecutive axes of the robot intersect at a common point, Piepers solution can be applied. Piepers approach works on the principle of separating the position solution for Ɵ1, Ɵ2 and Ɵ3 from the orientation solution to solve for Ɵ4, Ɵ5 and Ɵ6 [4]. Therefore, a geometrical approach is initially implemented to find the joint variables Ɵ1, Ɵ2 and Ɵ3 that define the end effector position in space, while an analytical solution is applied to calculate the angles Ɵ4, Ɵ5 and Ɵ6 which describe the end-effector orientation. </h3></div>', unsafe_allow_html=True)


# Part - 8
st.markdown("<hr style='margin-left: 50px;'>", unsafe_allow_html=True)  
st.markdown('<div class="subhead"><h3> Geometrical solution: </h3></div>', unsafe_allow_html=True)
m1, m2, m3 = st.columns((3,8,2))
with m2:    
    st.image(Image.open('Images/img18.jpg'))
    
st.markdown('<div class="subcontent"><h3> Therefore, the projection of the wrist components on x-y plane of frame {0} has the same components on frame {1} [5, 6]. In addition, since both link two and three are planar, the position vector in y direction changes with respect to θ1 only. Thus, two possible solutions for θ1 can be achieved by simply applying the arctangent function. </h3></div>', unsafe_allow_html=True)
m1, m2, m3 = st.columns(3)
with m2:    
    st.image(Image.open('Images/img19.jpg'))
    
st.markdown('<div class="subcontent"><h3> The solutions of θ2 and θ3 are obtained by considering the plane, shown in Figure 5, formed by the second and third planar links with respect to the robot global reference frame. </h3></div>', unsafe_allow_html=True)
m1, m2, m3 = st.columns((3,8,2))
with m2:    
    st.image(Image.open('Images/img20.jpg'))
    st.image(Image.open('Images/img21.jpg'))
    
st.markdown('<div class="subcontent"><h3> The negative sign in θ3 indicates that the rotation occurred in the opposite direction. Likewise, we can follow the same procedure to solve for θ2 using similar trigonometric relationships. </h3></div>', unsafe_allow_html=True)
m1, m2, m3 = st.columns((3,8,2))
with m2:    
    st.image(Image.open('Images/img22.jpg'))
    
st.markdown('<div class="subcontent"><h3> Again the rotation occurred in the opposite direction of the z axis as well as there are an initial rotation of 900 between axis 1 and axis 2. Therefore, the final value of θ2 equal to: </h3></div>', unsafe_allow_html=True)
m1, m2, m3 = st.columns((3,8,2))
with m2:    
    st.image(Image.open('Images/img23.jpg').resize((150, 30)))
    
    
# Part - 9
st.markdown("<hr style='margin-left: 50px;'>", unsafe_allow_html=True)  
st.markdown('<div class="subhead"><h3> Analytical solution </h3></div>', unsafe_allow_html=True)
st.markdown('<div class="subcontent"><h3> After solving the first inverse kinematic sub-problem which gives the required position of the end effector, the next step of the inverse kinematic solution will deal with the procedure of solving the orientation sub-problem to find the joint angles Ɵ4, Ɵ5 and Ɵ6. This can be done using Z-Y-X Eulers formula. As the orientation of the tool frame with respect to the robot base frame is described in term of Z-Y-X Eulers rotation, this means that each rotation will take place about an axis whose location depends on the previous rotation [3]. The Z-Y-X Eulers rotation is shown below in Figure. </h3></div>', unsafe_allow_html=True)
m1, m2, m3 = st.columns((3,8,2))
with m2:    
    st.image(Image.open('Images/img24.jpg'))
    st.image(Image.open('Images/img25.jpg'))
    
st.markdown('<div class="subcontent"><h3> However, it can be concluded that the last three intersected joints form a set of ZYZ Euler angles with respect to frame {3}. Therefore, these rotations can be expressed as: </h3></div>', unsafe_allow_html=True)
m1, m2, m3 = st.columns(3)
with m2:    
    st.image(Image.open('Images/img26.jpg'))
    st.image(Image.open('Images/img27.jpg'))
    
st.markdown('<div class="subcontent"><h3> It is possible now to use the ZYZ Eulers angles formula to obtain the solutions for Ɵ4, Ɵ5 and Ɵ6 where </h3></div>', unsafe_allow_html=True)
m1, m2, m3 = st.columns(3)
with m2:    
    st.image(Image.open('Images/img28.jpg'))
    
st.markdown('<div class="subcontent"><h3> For each of the eight solutions achieved from the geometric approach for Ɵ1, Ɵ2 and Ɵ3, there is another flipped solution of Ɵ4, Ɵ5 and Ɵ6 that can be obtained as: </h3></div>', unsafe_allow_html=True)
m1, m2, m3 = st.columns(3)
with m2:    
    st.image(Image.open('Images/img29.jpg'))
    
st.markdown('<div class="subcontent"><h3> Now, if β = 0 or 180, this means that the robot in a singular configuration where the joint axes 4 and 6 are parallel. This results in a similar motion of the last three intersection links of the robot manipulator. Alternatively: </h3></div>', unsafe_allow_html=True)
m1, m2, m3 = st.columns(3)
with m2:    
    st.image(Image.open('Images/img30.jpg'))
    st.image(Image.open('Images/img15.jpg'))
    st.image(Image.open('Images/img16.jpg'))


# Part 10
st.markdown("<hr style='margin-left: 50px;'>", unsafe_allow_html=True)  
st.markdown('<div class="subhead"><h3> Advanced methodology description </h3></div>', unsafe_allow_html=True)
st.write('')
st.markdown('<div class="subhead"><h3> Introduction </h3></div>', unsafe_allow_html=True)
st.markdown('<div class="subcontent"><h3> The study addresses the challenges in robot inverse kinematics (IK) due to limitations like manufacturing tolerances and setup errors that affect robot performance. Traditional IK methods are computationally intensive and complex, especially for robots with many degrees of freedom (DOF). The method proposes a machine learning (ML) sequential methodology for robot IK modeling to improve computational efficiency and accuracy. </h3></div>', unsafe_allow_html=True)
st.write('')
st.markdown('<div class="subhead"><h3> Methodology Structure </h3></div>', unsafe_allow_html=True)
st.markdown('<div class="subcontent"><h3> The methodology consists of three macro-steps: </h3></div>', unsafe_allow_html=True)
st.markdown('<div class="subcontent"><h3> 1) IK Boundary Definition and Pre-processing: Selection of the robot and dataset generation using forward kinematics (FK) equations derived from Denavit-Hartenberg (D-H) parameters. </h3></div>', unsafe_allow_html=True)
st.markdown('<div class="subcontent"><h3> 2) Network Architecture Definition: Selection of the artificial neural network (ANN) and defining hidden layers and neurons. The approach can be global (all joints simultaneously) or sequential (each joint calculated in sequence using previously obtained values). </h3></div>', unsafe_allow_html=True)
st.markdown('<div class="subcontent"><h3> 3) Model Validation: Validation of the IK model using the same trajectories employed in the initial FK validation, assessing performance in joint and Cartesian errors. </h3></div>', unsafe_allow_html=True)
st.write('')
st.markdown('<div class="subhead"><h3> Experimental Campaign and Results </h3></div>', unsafe_allow_html=True)
st.markdown('<div class="subcontent"><h3> 1) Simulation Validation: Conducted on an IRB140 articulated robot to demonstrate the methodology by drawing a given picture. </h3></div>', unsafe_allow_html=True)
st.markdown('<div class="subcontent"><h3> 2) •	Experimental Validation: Implemented on a 6 DOFs IRB-140 robot. The sequential method reduced mean squared error by 42.7-56.7% compared to the global method. </h3></div>', unsafe_allow_html=True)
st.write('')
st.markdown('<div class="subhead"><h3> Conclusion </h3></div>', unsafe_allow_html=True)
st.markdown('<div class="subcontent"><h3> The sequential ML methodology effectively improves the accuracy of IK modeling, reducing computational costs and errors compared to traditional methods and global ML approaches. This method shows promise for practical applications in robotic control and trajectory planning.     </h3></div>', unsafe_allow_html=True)