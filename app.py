import streamlit as st
import streamlit.components.v1 as components
import os
import base64

st.set_page_config(layout="wide", page_title="LogiRoute Pro V2")

def get_html_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode('utf-8')

path = os.path.join(os.getcwd(), 'static', 'index.html')

if os.path.exists(path):
    # Method: Data URI for the iframe. This is often faster for large HTML blobs
    # as it doesn't require Streamlit to process the string as much.
    html_b64 = get_html_base64(path)
    
    st.markdown(f'<iframe src="data:text/html;base64,{html_b64}" style="width:100%; height:100vh; border:none;"></iframe>', unsafe_allow_html=True)
else:
    st.error("static/index.html not found!")
