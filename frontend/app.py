import streamlit as st
import requests

st.title("🎙️ Voice-to-SQL Analytics Engine")
st.write("Speak or type your natural language data request to dynamically generate SQL queries.")

transcript_input = st.text_input("Enter Voice Transcript (e.g., 'Show me the total revenue'):")

if st.button("Generate SQL"):
    if transcript_input.strip():
        try:
            response = requests.post("http://127.0.0.1:8000/api/convert", json={"transcript": transcript_input})
            if response.status_code == 200:
                data = response.json()
                st.success("Query Converted Successfully!")
                st.code(data["generated_sql"], language="sql")
                st.metric(label="Confidence Score", value=f"{data['confidence_score'] * 100}%")
            else:
                st.error("Failed to fetch response from backend service.")
        except Exception as e:
            st.error(f"Connection error: {e}")
    else:
        st.warning("Please enter a valid transcript text.")