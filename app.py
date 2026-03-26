import streamlit as st
import streamlit.components.v1 as components
import os

# Version 2 - Mirroring the reliable loading logic of Version 1
st.set_page_config(layout="wide", page_title="LogiRoute Pro V2")

# Read the HTML file
path_to_html = os.path.join(os.getcwd(), 'static', 'index.html')

if os.path.exists(path_to_html):
    with open(path_to_html, 'r', encoding='utf-8') as f:
        html_data = f.read()
    
    # Render with standard Streamlit component
    components.html(html_data, height=1500, scrolling=True)
else:
    st.error("Error: index.html not found in static folder!")
