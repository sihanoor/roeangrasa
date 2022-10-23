import streamlit as st

title = c2.text_input('Comments',key=blob+"title")
if st.button('Save Me', key=blob+"save"):
    st.write(title)
