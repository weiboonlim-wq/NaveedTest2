import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(layout="wide", page_title="LogiRoute Pro V2")

# Normal reliable loading
path = os.path.join(os.getcwd(), 'static', 'index.html')

if os.path.exists(path):
    with open(path, 'r', encoding='utf-8') as f:
        html_data = f.read()
    components.html(html_data, height=1200, scrolling=True)
else:
    st.error("static/index.html not found!")
