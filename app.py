import streamlit as st
from transformers import pipeline



st.set_page_config(page_title="Moroccan Darija Assistant App", page_icon="🇲🇦")
"""
This module contains the main Streamlit application for the Moroccan Darija Assistant.

The app provides a user-friendly interface for translating English text into Moroccan Darija
using pre-trained models from Hugging Face. Users can select different translation models and
tasks, enter their text, and receive the translated output.
"""

import streamlit as st
from transformers import pipeline

# Create a Streamlit app title
st.title("Darija Assistant App")
st.caption("This app uses Hugging Face's Transformers library to perform English to Moroccan Darija translation with transliteration option")

# Header Section

# Split the app into two columns for model and task selection
col1, col2 = st.columns(2)
model = col2.selectbox('Select a model', options=['Vrspi/EnglishToDarija', 'lachkarsalim/Helsinki-translation-en-moroccann_darija'])
task = col1.selectbox('Select a task', options=['text2text-generation'])

# Input text and labels
prompt = st.text_area("Enter English text to translate to Moroccan Arabic (Darija):", "")

# Function to run the translation model
@st.cache_resource
def translate_text(text, task, model):
    """
    Translates the given text from English to Moroccan Darija using the selected task and model.

    Args:
        text (str): The English text to be translated.
        task (str): The task to be performed (e.g., 'text2text-generation').
        model (str): The pre-trained model to be used for translation.

    Returns:
        str: The translated text in Moroccan Darija.
    """
    translator = pipeline(task, model=model)
    response = translator(text)
    return response[0]['generated_text']

# Perform translation when the user clicks the button
if st.button("Translate"):
    if not prompt:
        st.warning("Please enter a text to translate.")
    else:
        # Perform translation
        result = translate_text(prompt, task, model)

        # Display the results
        st.subheader("Translation Results:")
        st.info(result)

# Add clear button
st.write("---")

with st.container():
    st.subheader("Hi, I am Rafik :wave:")
    st.write("A Software Engineer From Maryland, USA")
    # Introduction and Instructions
    st.caption(
        """
        Credit goes to pretrained models providers which can be found at huggingface hub using model tag.
        Checkout my blog for more about my work: https://techwithrafik.wordpress.com/.
        """
    )
    st.caption("If you are interested in contributing, checkout project github page: https://github.com/kouissar/Moroccan-darija-assistant")
