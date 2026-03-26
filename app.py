import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(layout="wide", page_title="LogiRoute Pro V2", initial_sidebar_state="collapsed")

# Simple Read and Render
path = os.path.join(os.getcwd(), 'static', 'index.html')
if os.path.exists(path):
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    # High height and wide width to prevent cut-off in Codespaces
    components.html(html, height=2000, scrolling=True)
else:
    st.error("static/index.html not found!")
