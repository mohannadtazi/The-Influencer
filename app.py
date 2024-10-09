import streamlit as st
from crew import crew 

st.set_page_config(page_title='The Influencer App', page_icon=':sunglasses:')
st.title('Welcome to The Influencer App')

st.write('This app generates posts for your socials.')

col1, col2= st.columns(2)
results = None
with col1:
    st.header('Step 1: Research')
    st.write('Tell us what you want to write about and how you want it to sound.')
    st.write('We will generate a research report for you.')
    topic = st.text_input('Enter your topic')
    style = st.text_input('Enter a style (e.g., inspirational, funny, serious)')
    length = st.selectbox('Select a length', ['short', 'medium', 'long'], index=0)
    platform = st.selectbox('Select a platform', ['LinkedIn', 'Facebook', 'Twitter'], index=0)

    if st.button('Generate Post'):
    # Validate inputs
        if not topic or not style:
            st.error("Please provide both a topic and a style.")
        else:
            try:
                results = crew.kickoff({"topic": topic, "style": style, "length": length, "platform": platform})
            except Exception as e:
                st.error(f"An error occurred: {e}")

with col2:
# Display the generated post
    if results:
        st.header('Here is your post:')
        st.markdown(results.raw)
    