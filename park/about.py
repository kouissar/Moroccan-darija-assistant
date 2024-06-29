import streamlit as st
import requests
from streamlit_lottie import st_lottie
import pyttsx3 as sp
"""
This module contains the Streamlit app for the "About Me" section.

It provides information about the developer, including their background, expertise, and contact details.
The app also includes a contact form for users to get in touch with the developer.
"""

from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title="About Me", page_icon=":tada:", layout="wide"
)

def load_lottieurl(url):
    """
    Load a Lottie animation from the given URL.

    Args:
        url (str): The URL of the Lottie animation file.

    Returns:
        dict: The JSON data representing the Lottie animation, or None if the URL is invalid.
    """
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    """
    Apply a local CSS file to the Streamlit app.

    Args:
        file_name (str): The path to the CSS file.
    """
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load a Lottie animation
lottie_coding = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_8kut1rsr.json")

# Header Section
with st.container():
    st.subheader("Hi, I am Rafik :wave:")
    st.title("A Software Engineer From Maryland, USA")
    st.write("I am a highly motivated professional with a passion for coding, music, and outdoor adventures. In my free time, I enjoy hiking and camping in the great outdoors, as well as playing and composing music. I am always looking for new challenges and ways to learn and grow, both personally and professionally. Whether I'm coding a new software application or exploring the wilderness, I am driven by my love of problem-solving and creation.")

with st.container():
    st.write("---")
    left_col, right_col = st.columns(2)
    with left_col:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            I am currently a Solutions Architect at CareFirst BCBS where I have been involved in various technology projects including test and QA automation, DevOps and infrastructure automation, performance engineering and APM, machine learning and NLP using Python, as well as working with open source technologies.
            
            [Visit my Linkedin Profile](https://www.linkedin.com/in/rkouissar/)

            My areas of expertise include test and QA automation, which involves the creation and execution of automated tests to ensure the quality of software applications. I have also worked on projects related to DevOps and infrastructure automation, which focus on the deployment and management of software applications and the provisioning and configuration of infrastructure resources. Additionally, I have experience in performance engineering and APM, where I have optimized the performance of software applications by identifying and addressing bottlenecks and implementing tools for monitoring and measuring performance. I have also utilized my skills in Python and machine learning to build and implement models and algorithms for data processing and analysis, such as natural language processing. In my work, I have also had the opportunity to utilize and contribute to open source technologies.
            """
        )
# with st.container():


# ---- PROJECTS ----
# with st.container():
#     st.write("---")
#     st.header("My Projects")
#     st.write("##")
#     image_column, text_column = st.columns((1, 2))
#     with image_column:
#         st.image(img_lottie_animation)
#     with text_column:
#         st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
#         st.write(
#             """
#             Learn how to use Lottie Files in Streamlit!
#             Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do it!
#             In this tutorial, I'll show you exactly how to do it
#             """
#         )
#         st.markdown("[Watch Video...](https://youtu.be/TXSOitGoINE)")
# with st.container():
#     image_column, text_column = st.columns((1, 2))
#     with image_column:
#         st.image(img_contact_form)
#     with text_column:
#         st.subheader("How To Add A Contact Form To Your Streamlit App")
# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documentation: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/kouissar@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with right_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with left_column:
        st_lottie(
            lottie_coding,
            speed=1,
            reverse=False,
            loop=True,
            quality="low",
            height="None",
            width="None",
            key="None",
        )
