import streamlit as st

captions = list(range(300,1200,100))
blob_items = [f"https://dummyimage.com/400x{w}/d4c9d4/3740bd.jpg&text=IMG_{w}" for w in captions]

for blob in blob_items:
    c1,mid,c2 = st.columns([2,1,3])
    c1.image(blob)
    title = c2.text_input('Comments',key=blob+"title")
    if c2.button('Save Me', key=blob+"save"):
        c1.write(title)
