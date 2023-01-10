import streamlit as st

st.title("Weather Forecast")
st.text("designed using Streamlit")

place = st.text_input("Place:")
days = st.slider("Forecast days", min_value=1, max_value=5, 
                help="Select the number of days into which you would like to see the weather forecast.")

option = st.selectbox("Select data to view",("Temperature","Sky"))
st.subheader(f"{option} for the next {days} days in {place}")