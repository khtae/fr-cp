import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to our Food Redommendation System")

st.sidebar.success("Select a recommendation app.")

st.markdown(
    """
   Our system offers personalized suggestions tailored to your dietary preferences and health objectives. 
   It provides detailed nutritional information for each recommended food item, enabling you to make informed decisions about your diet.
    """
)
