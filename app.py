import streamlit as st
import main

# App configs
st.set_page_config(
page_title="Bike Sharing Demand Prediction",
layout="centered",
initial_sidebar_state="expanded",
)

# Heading
st.markdown("<h1 style='text-align: center; background-color:deepskyblue'>🚴 Bike Rental Demand Prediction 🚴</h1>", 
            unsafe_allow_html=True)
# Sub heading
st.markdown("<h4 style='text-align: center'><i>∞∞∞ A Machine Learning based web app to predict bike rental demand ∞∞∞</i></h4>",
            unsafe_allow_html=True)
# Image
st.markdown("<h1 align='center'><img src='https://storage.googleapis.com/kaggle-competitions/kaggle/3948/media/bikes.png'></img></h1>", 
            unsafe_allow_html=True)


# SideBar
st.sidebar.title("Explore notebooks📖")
html = "<a href='https://www.google.com'></a>"
st.sidebar.write("➡️Check out [Part 1 - EDA](https://nbviewer.jupyter.org/github/SarthakRana/Bike-Sharing-Demand-Prediction/blob/main/Bike_Sharing_EDA_Part1.ipynb)")
st.sidebar.write("➡️Check out [Part 2 - Data Prep](https://nbviewer.jupyter.org/github/SarthakRana/Bike-Sharing-Demand-Prediction/blob/main/bike_sharing_data_preparation_Part2.ipynb)")
st.sidebar.write("➡️Check out [Part 3 - Modelling](https://nbviewer.jupyter.org/github/SarthakRana/Bike-Sharing-Demand-Prediction/blob/main/bike-demand-prediction-modelling-part3.ipynb)")

st.sidebar.title("Follow ❤️ me on :")
st.sidebar.write("➡️[Github](https://github.com/SarthakRana)")
st.sidebar.write("➡️[LinkedIn](https://www.linkedin.com/in/sarthakrana/)")
st.sidebar.write("➡️[Kaggle](https://www.kaggle.com/sarthak97)")



# About 
st.write("Bike sharing systems are a means of renting bicycles where the process of obtaining membership, rental, and bike return is automated via a network of kiosk locations throughout a city. Using these systems, people are able rent a bike from a one location and return it to a different place on an as-needed basis.")
st.write("This project is based on a Kaggle competition. Our task is to combine historical usage patterns with weather data in order to forecast bike rental demand in the Capital Bikeshare program in Washington, D.C.")
st.markdown("<i>For more details on this competition, [visit here](https://www.kaggle.com/c/bike-sharing-demand).</i>", unsafe_allow_html=True)

st.markdown("<br><h4><b> Please fill in the below details:</b></h4><br>", unsafe_allow_html=True)

# User input features
date = st.date_input("Enter date :")
time = st.time_input("Enter Time (HH24:MM):")
day = st.selectbox("What type of day is it?", ['Holiday', 'Working day', 'Weekend'])
weather = st.selectbox("What type of weather is it?", 
             ['Clear/Few clouds', 
              'Mist/Cloudy', 
              'Light Rain/Light Snow/Scattered clouds',
              'Heavy Rain/Snowfall/Foggy/Thunderstorm'])
temp = st.text_input("Enter temperature (in °C):")
humidity = st.text_input("Enter humidity (in %):")
windspeed = st.text_input("Enter windspeed (in km/h):")

if st.button("Predict Rentals"):
    if ((date=='') | (time=='') | (day=='') | (weather=='') | 
        (temp=='') | (humidity=='') | (windspeed=='')):
        st.error("Please fill all fields before proceeding.")
    else :
        prediction = main.process_data(date, time, day, weather, 
                                       temp, humidity, windspeed)    
        st.success("There will be an approx. demand of " + str(prediction) + " bikes for above conditions.")























