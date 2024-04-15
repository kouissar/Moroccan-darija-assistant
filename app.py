import streamlit as st
from transformers import pipeline




st.set_page_config(page_title="Moroccan Darija Assistant App", page_icon="🇲🇦")

# Create a Streamlit app title
st.title("Darija Assistant App")
col1, col2 = st.columns(2)
model= col2.selectbox('Select a model', options=['Vrspi/EnglishToDarija', 'lachkarsalim/Helsinki-translation-en-moroccann_darija' ])
task= col1.selectbox('Select a task', options=['text2text-generation'])

# Introduction and Instructions
st.write(
    "This app uses Hugging Face's Transformers library to perform English to Moroccan Darija translation with transliteration option."
)
#I'm glad I could help!  Is there anything else you'd like to know about pantry organization, or anything 
# else around the house? I can also help you find information on storage containers, pantry cabinet options, 
# or even healthy pantry staples to stock your new organized space.

# Input text and labels
text = st.text_area("Enter English text to translate to Moroccan Arabic (Darija):", "")



# create the pipeline
classifier  = pipeline(task, model=model)



# Perform classification when the user clicks the button
if st.button("Translate"):
    if not text:
        st.warning("Please enter a text to translate.")
    # elif not labels:
    #     st.warning("Please enter at least one label for classification.")
    else:
        # Perform zero-shot classification
        result = classifier(text)

        # Display the results in a table
        st.subheader("Translation Results:")

        # st.write(result)
        st.write(result[0]['generated_text'])
