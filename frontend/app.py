import streamlit as st
import requests

st.set_page_config(page_title="Contract Copilot", page_icon="⚖️", theme="dark")

st.title("Contract Intelligence Copilot")
uploaded = st.file_uploader("Upload a contract (PDF)", type=["pdf"])
if uploaded:
    with st.spinner("Analyzing..."):
        r = requests.post("http://localhost:8000/analyze", files={"file": uploaded})
        for seg in r.json()["results"]:
            st.markdown(seg)