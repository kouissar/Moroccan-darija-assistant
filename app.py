import streamlit as st
from transformers import pipeline



st.set_page_config(page_title="Moroccan Darija Assistant App", page_icon="🇲🇦")

# Create a Streamlit app title
st.title("Darija Assistant App")
st.caption("This app uses Hugging Face's Transformers library to perform English to Moroccan Darija translation with transliteration option")

# Header Section 

    # st.write("I am a highly motivated professional with a passion for coding, music, and outdoor adventures. In my free time, I enjoy hiking and camping in the great outdoors, as well as playing and composing music. I am always looking for new challenges and ways to learn and grow, both personally and professionally. Whether I'm coding a new software application or exploring the wilderness, I am driven by my love of problem-solving and creation.")
    #sp.speak("Hi, I am Rafik. A Software Engineer From USA.I am passionate about coding, fishing, and music. What about you? ")

col1, col2 = st.columns(2)
model= col2.selectbox('Select a model', options=['Vrspi/EnglishToDarija', 'lachkarsalim/Helsinki-translation-en-moroccann_darija' ])
task= col1.selectbox('Select a task', options=['text2text-generation'])


#I'm glad I could help!  Is there anything else you'd like to know about pantry organization, or anything 
# else around the house? I can also help you find information on storage containers, pantry cabinet options, 
# or even healthy pantry staples to stock your new organized space.

# Input text and labels
prompt = st.text_area("Enter English text to translate to Moroccan Arabic (Darija):", "")


# create the pipeline
@st.cache_resource
def run_model(task, model, text):
    classifier  = pipeline(task, model=model)
    response = classifier(text)
    return response


# Perform classification when the user clicks the button
if st.button("Translate"):
    if not prompt:
        st.warning("Please enter a text to translate.")
    # elif not labels:
    #     st.warning("Please enter at least one label for classification.")
    else:
        # Perform zero-shot classification
        result = run_model(task, model, prompt)

        # Display the results in a table
        st.subheader("Translation Results:")

        # st.write(result)
        st.info(result[0]['generated_text'])

# Add clear button
st.write("---")

with st.container():
    st.subheader("Hi, I am Rafik :wave:")
    st.write("A Software Engineer From Maryland, USA")
    # Introduction and Instructions
    st.caption(
    '''Credit goes to pretrained models providers which can be found at huggingface hub using model tag.
    Checkout my blog for more about my work: https://techwithrafik.wordpress.com/.''')
    st.caption("If you are interested in contributing, checkout project github page: https://github.com/kouissar/Moroccan-darija-assistant")
