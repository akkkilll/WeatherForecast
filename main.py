import streamlit as st
import plotly.express as px
from backend import getData

st.title("Weather Forecast")
st.text("designed using Streamlit")

place = st.text_input("Place:")
days = st.slider("Forecast days", min_value=1, max_value=5, 
                help="Select the number of days into which you would like to see the weather forecast.")

option = st.selectbox("Select data to view",("Temperature","Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

# x - dates, y - temparature   <--- array type objects

# dates = ["2022-25-10","2022-26-10","2022-27-10"]
# temperatures = [32, 30, 35]
if place:

    try:
        filtereddata = getData(place, days)

        if option == "Temperature":
            #Create a temperature plot
            temperatures = [dict["main"]["temp"] for dict in filtereddata]  #Stores all 8*ndays temperature values
            dates = [dict['dt_txt'] for dict in filtereddata]
            figure = px.line(x=dates, y=temperatures, labels = {"x":"Date", "y":"Temperatures (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                        "Rain": "images/rain.png", "Snow": "images/snow.png"}
            skyconditions = [dict["weather"][0]["main"] for dict in filtereddata]  #Stores all 8*ndays Sky conditions
            imagepaths = [images[condition] for condition in skyconditions]
            st.image(imagepaths, width=115)
    except KeyError:
        st.write("Invalid Place Input / Place not Found")