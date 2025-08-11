import streamlit as st

    st.title("My First Streamlit App")
    x = st.slider("Select a value", 0, 100)
    st.write(f"You selected: {x}")
