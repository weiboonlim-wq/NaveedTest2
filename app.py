import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(layout="wide", page_title="LogiRoute Pro V2")

# V2 - Loading Logic identical to V1
path = os.path.join(os.getcwd(), 'static', 'index.html')

if os.path.exists(path):
    with open(path, 'r', encoding='utf-8') as f:
        html_string = f.read()
    
    components.html(html_string, height=1200, scrolling=True)
else:
    st.error("static/index.html not found!")
