from gtts import gTTS
import streamlit as st
st.title("text to speech")
inputtext = st.text_area("English",height=200)
if st.button("submit"):
    speech=gTTS(inputtext)
    speech.save('example.mp3')
    st.audio('example.mp3')
