import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(layout="wide", page_title="LogiRoute Pro V2")

# Read the HTML file from static/index.html
html_path = os.path.join(os.getcwd(), 'static', 'index.html')

if os.path.exists(html_path):
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Use components.html to render the entire V2 logic
    # Set height large enough to avoid double scrollbars if possible, or use 100vh
    components.html(html_content, height=1000, scrolling=True)
else:
    st.error("Error: static/index.html not found!")

