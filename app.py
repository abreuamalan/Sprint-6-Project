
import streamlit as st
import pandas as pd
import plotly.express as px

data = pd.read_csv('vehicles_us.csv')
print(data.head(5))

st.title('Project 6: Web Aplication Creation (Data Scientist)')

odo_button = st.button('Odometer Histogram')
p_o_button = st.button('Price per Odometer')
car_type_button = st.button('Car Type Histogram')

if odo_button:
    st.write('Odometer Histogram')
    fig = px.histogram(data, x='odometer', title='Odometer Histogram')
    st.plotly_chart(fig)


if p_o_button:
    st.write('Price per Odometer')
    fig_2 = px.scatter(data, x="odometer", y="price", title='Price per Odometer') 
    st.plotly_chart(fig_2)

if car_type_button:
    st.write('Car Type Histogram')
    fig_3 = px.histogram(data, x='type', title='SUV, Sedan and Truck are the most car types of this analysis' )
    st.plotly_chart(fig_3)