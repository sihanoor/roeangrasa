"""Main module for the streamlit app"""
import os

import streamlit as st
import requests
import streamlit.components.v1 as components

from utils.sidebar import sidebar_caption

# Config the whole app
st.set_page_config(
    page_title="Roeang Rasa",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("💬 Roeang Rasa")
#twitter
class Tweet(object):
    def __init__(self, s, embed_str=False):
        if not embed_str:
            # Use Twitter's oEmbed API
            # https://dev.twitter.com/web/embedded-tweets
            api = "https://publish.twitter.com/oembed?url={}".format(s)
            response = requests.get(api)
            self.text = response.json()["html"]
        else:
            self.text = s

    def _repr_html_(self):
        return self.text

    def component(self):
        return components.html(self.text,height=800)
   
st.markdown('Kamu bisa mengikuti #tantanganbahagia yang akan dibagikan setiap hari. Kamu bisa alirkan apa yang kamu rasakan setelah menyelesaikan #tantanganbahagia hari ini, tuliskan di halaman berbagi rasa ya!')
t = Tweet("https://twitter.com/roeangrasa_mu").component()     

            

    


    
