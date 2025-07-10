import streamlit as st

length = {
    'millimeter': 0.001,
    'centimeter': 0.01,
    'meter': 1.0,
    'kilometer': 1000.0,
    'inch': 0.0254,
    'foot': 0.3048,
    'yard': 0.9144,
    'mile': 1609.34       
}

weight = {
    'milligram': 0.000001,
    'gram': 0.001,
    'kilogram': 1.0,
    'ounce': 0.0283495,
    'pound': 0.453592
}

length_units = list(length.keys())
weight_units = list(weight.keys())
temperature = ['celcius', 'kelvin', 'fahreinheit']

class ConvertProcess():
    def __init__(self):
        pass

    def length_conversion(self,get_length ,get_unit_length, get_choose_length):
        if get_unit_length == get_choose_length:
            st.subheader("Identical Values") 
        else:
            calcu_input = get_length * length[get_unit_length]
            convert = calcu_input / length[get_choose_length]
            st.subheader(f"{get_length} {get_unit_length} = {convert} {get_choose_length}") 
    
    def weight_conversion(self, get_weight, get_unit_weight, get_choose_weight):
        if get_unit_weight == get_choose_weight:
            st.subheader("Identical Values") 
        else:
            calcu_input = get_weight * weight[get_unit_weight]
            convert = calcu_input / weight[get_choose_weight]
            st.subheader(f"{get_weight} {get_unit_weight} = {convert} {get_choose_weight}") 

    def temperature_conversion(self, get_temperature, get_unit_temperature, get_choose_temperature):
        if get_unit_temperature == get_choose_temperature:
            st.subheader("Identical Values")
        match get_unit_temperature:
            case "celcius":
                if get_choose_temperature == "fahreinheit":
                    convert = ((get_temperature * 9)/5) + 32
                    st.subheader(f"{get_temperature} {get_unit_temperature} = {convert} {get_choose_temperature}")
                else:
                    convert = get_temperature + 273.15
                    st.subheader(f"{get_temperature} {get_unit_temperature} = {convert} {get_choose_temperature}")
            case "fahreinheit":
                if get_choose_temperature == "celcius":
                    convert = ((get_temperature * 5)/9) - 32
                    st.subheader(f"{get_temperature} {get_unit_temperature} = {convert} {get_choose_temperature}")
                else:
                    convert = (((get_temperature - 32) * 5) / 9) + 273.15
                    st.subheader(f"{get_temperature} {get_unit_temperature} = {convert} {get_choose_temperature}")
            case "kelvin":
                if get_choose_temperature == "celcius":
                    convert = get_temperature - 273.15
                    st.subheader(f"{get_temperature} {get_unit_temperature} = {convert} {get_choose_temperature}")
                else:
                    convert = (((get_temperature - 273.15) * 9) / 5) + 32
                    st.subheader(f"{get_temperature} {get_unit_temperature} = {convert} {get_choose_temperature}")


class Interface():
    def __init__(self):
        self.convertprocess = ConvertProcess()

    def web(self):
        st.title("Unit Converter")
        tabs = st.tabs(["Length", "Weight", "Temperature"])

        with tabs[0]:
            with st.form("length conversion"):
                enter_length = st.number_input("Enter the length to convert:")
                unit_length = st.selectbox("Unit to convert from", length_units)
                choose_length = st.selectbox("Unit to convert to", length_units)

                convert_length = st.form_submit_button("Convert")

                if convert_length:
                    self.convertprocess.length_conversion(enter_length, unit_length, choose_length)

        with tabs[1]:
            with st.form("weight conversion"):
                enter_weight = st.number_input("Enter the weight to convert:")
                unit_weight = st.selectbox("Unit to convert from", weight_units)
                choose_weight = st.selectbox("Unit to convert to", weight_units)

                convert_weight = st.form_submit_button("Convert")

                if convert_weight:
                    self.convertprocess.weight_conversion(enter_weight, unit_weight, choose_weight)

        with tabs[2]:
            with st.form("temperature conversion"):
                enter_temperature = st.number_input("Enter the temperature to convert:")
                unit_temperature = st.selectbox("Unit to convert from", temperature)
                choose_temperature = st.selectbox("Unit to convert to", temperature)
                
                convert_temperature = st.form_submit_button("Convert")

                if convert_temperature:
                    self.convertprocess.temperature_conversion(enter_temperature, unit_temperature, choose_temperature)

if __name__ == "__main__":
    interface = Interface()
    interface.web()