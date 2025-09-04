import streamlit as st
import requests

st.set_page_config(page_title="AI YouTube Script Generator", layout="wide")

st.title("AI-Powered YouTube Script Generator")
st.subheader("")

st.write(
    """
    Enter a topic below to generate a ready-to-use YouTube Script .
    """
)

topic = st.text_input("Enter video topic:")
if st.button("Generate Script") and topic:
    response = requests.post(
        "http://localhost:8000/generate",
        json={"topic": topic}
    )

    if response.status_code == 200:
        script = response.json()["script"]
        st.text_area("Generated Script:", script, height=300)
    else:
        st.error("Something went wrong.")