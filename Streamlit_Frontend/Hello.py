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

   We can live a healthy life with a balanced diet based on our height, weight, and age. Your diet can help you achieve and 
   maintain a healthy weight, lower your chance of developing chronic diseases (including cancer and heart disease), 
   and improve your general health when combined with physical activity. 
    """
)
