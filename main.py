import streamlit as st

length = ['milimiter', 'centimeter', 'meter', 'kilometer', 'inch', 'foot', 'yard', 'mile']
weight = ['miligram', 'gram', 'kilogram', 'ounce', 'pound']
temperature = ['celcius', 'kelvin', 'fahreinheit']

st.title("Unit Converter")

tabs = st.tabs(["Length", "Weight", "Temperature"])

with tabs[0]:
    enter_length = st.number_input("Enter the length to convert:")
    unit_length = st.selectbox("Unit to convert from", length)
    choose_length = st.selectbox("Unit to convert to", length)
    convert_length = st.button("Convert", key="convert_length")

with tabs[1]:
    enter_weight = st.number_input("Enter the weight to convert:")
    unit_weight = st.selectbox("Unit to convert from", weight)
    choose_weight = st.selectbox("Unit to convert to", weight)
    convert_weight = st.button("Convert", key="convert_weight")

with tabs[2]:
    enter_temperature = st.number_input("Enter the temperature to convert:")
    unit_temperature = st.selectbox("Unit to convert from", temperature)
    choose_temperature = st.selectbox("Unit to convert to", temperature)
    convert_temperature = st.button("Convert", key="convert_temperature")