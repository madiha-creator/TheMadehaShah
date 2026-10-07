from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Madii | Madeha Shah",
    page_icon="💖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Make the website fill the whole browser window
st.markdown(
    """
    <style>
    #MainMenu, header, footer {visibility: hidden;}
    [data-testid="stToolbar"], [data-testid="stDecoration"] {display: none;}
    .block-container {padding: 0 !important; max-width: 100% !important;}
    iframe {width: 100%; height: 100vh; border: 0; display: block;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = (Path(__file__).parent / "index.html").read_text(encoding="utf-8")
components.html(html, height=900, scrolling=True)
