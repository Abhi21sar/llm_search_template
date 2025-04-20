
import streamlit as st
import requests



st.title("LLM-based RAG Search")

query = st.text_input("Enter your query:")

if st.button("Search"):
    st.write("Sending query to Flask backend...")

    try:
        response = requests.post("http://localhost:5001/query", json={"query": query})

        if response.status_code == 200:
            # Display the generated answer
            answer = response.json().get('answer', "No answer received.")
            st.markdown("**Answer:**")
            st.write(answer)
        else:
            st.error(f"Error from backend: {response.status_code} - {response.text}")

    except Exception as e:
        st.error(f"Failed to connect to Flask backend. Exception: {e}")