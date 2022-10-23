import streamlit as st

title = st.text_input('Comments', "title")
if st.button('Save Me', "save"):
    st.write(title)
