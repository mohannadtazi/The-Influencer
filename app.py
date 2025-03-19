import streamlit as st
from crew import crew, crew_image
from txt_to_image import generate_image
import agent

st.set_page_config(page_title='The Influencer App', page_icon=':sunglasses:')
st.title('Welcome to The Influencer App')

st.write('This app generates posts for your socials.')

col1, col2= st.columns(2)
results = None
image_prompt = ''
with st.sidebar:
    st.write('## Settings')
    st.write('Select the model you want to use:')
    agent.model = st.selectbox('Model', ["llama3-8b-8192", "llama3-70b-8192","llama-3.1-8b-instant"], index=0)
    st.write('Select the creativity level:')
    agent.temperature = st.slider('Temperature', 0.0, 0.5, 1.0)

with col1:
    st.header('Step 1: Research')
    st.write('Tell us what you want to write about and how you want it to sound.')
    st.write('We will generate a relevant post for you.')
    topic = st.text_input('Enter your topic')
    style = st.text_input('Enter a style (e.g., inspirational, funny, serious)')
    length = st.selectbox('Select a length', ['short', 'medium', 'long'], index=0)
    platform = st.selectbox('Select a platform', ['LinkedIn', 'Facebook', 'Twitter'], index=0)
    isImage = st.checkbox('You want to generate Image')

    if st.button('Generate Post'):
    # Validate inputs
        if not topic or not style:
            st.error("Please provide both a topic and a style.")
        else:
            try:
                
                results = crew.kickoff({"topic": topic, "style": style, "length": length, "platform": platform})
                if isImage:
                    image_prompt = crew_image.kickoff({"topic": topic, "style": style, "platform": platform})
            except Exception as e:
                st.error(f"An error occurred: {e}")

with col2:
# Display the generated post
    if isImage:
        if results and image_prompt:
            st.header('Oups.. There is just 1 step. \nHere is the post:')
            st.markdown(results)
            st.header('Here is the image:')
            st.write(f"prompt: {image_prompt}:")
            image_bytes = generate_image(image_prompt)
            if isinstance(image_bytes, str):
                st.error(image_bytes)
            st.image(image_bytes, use_container_width=True)
    else:
      if results :
        st.header('Here is your post:')
        st.markdown(results)
    
    
