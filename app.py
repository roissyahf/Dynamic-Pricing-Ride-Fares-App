import streamlit as st
import pickle
import pandas as pd

st.set_page_config(page_title="Dynamic Pricing Ride Fares", page_icon=":car:")

# load the model
model = pickle.load(open('catboost_tuning.pkl', 'rb'))

# add title
st.title('Dynamic Pricing on Cost of the Rides')
st.write('Dynamically adjust prices in response to changing factors')

# create 2 columns
col1, col2 = st.columns(2)
with col1:
    # add form for input one column with selection
    vehicle_type = st.selectbox(
            "What is your preferred vehicle type?",
            ("Premium", "Economy"),
            index=None,
            placeholder="Select vehicle type...")
    #st.write("You selected:", vehicle_type)

with col2:
    # add form for input number of riders
    number_of_riders = st.number_input("Insert number of riders", placeholder="Type number of riders...",
                                       min_value=15, max_value=120, value=None, step=1)
    #st.write("The number of riders:", number_of_riders)

# create more 2 columns
col3, col4 = st.columns(2)

with col3:
    # add form for input number of drivers
    number_of_drivers = st.number_input("Insert number of drivers", placeholder="Type number of drivers...",
                                        min_value=5, max_value=95, value=None, step=1)
    #st.write("The number of drivers:", number_of_drivers)

with col4:
    # add form for input expected ride duration in minutes
    expected_ride_duration = st.number_input("Insert expected ride duration", placeholder="Type expected ride duration...",
                                             min_value=8, max_value=200, value=None, step=1)
    #st.write("The expected ride duration:", expected_ride_duration)

# store input in pandas dataframe
user_input = pd.DataFrame([[vehicle_type, number_of_riders, number_of_drivers, expected_ride_duration]],
                        columns=['Vehicle_Type_encoded', 'Number_of_Riders', 'Number_of_Drivers', 'Expected_Ride_Duration'])

# process categorical features
def encode_vehicle_type(vehicle_type):
    return vehicle_type.apply(lambda x: 1 if x=='Premium' else 0)

user_input['Vehicle_Type_encoded'] = encode_vehicle_type(user_input['Vehicle_Type_encoded'])

# show the result
if st.button("Predict", type="primary"):
    # make prediction
    predicted_cost = model.predict(user_input)

    # show the result
    st.success(f"Predicted cost of the rides is: ${round(predicted_cost[0],3)}")

