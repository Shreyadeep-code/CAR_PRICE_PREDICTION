import streamlit as st
from config.companies import companies
import requests
fuel_types=['Petrol','Diesel','LPG']
app_url=""
st.markdown(
    "<h1 style='text-align: center; '>Cars Hub</h1>",
    unsafe_allow_html=True
)
st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSmxk9NAl0NP0-7ITK8Cq-qkyvse6-zOWe4WL8_LmWh0j6agrdXx5RvbK4&s=10" width="800">
    </div>
    """,
    unsafe_allow_html=True
)
company=st.selectbox('Select the car company',companies)
name=st.text_input('Car name')

col1,col2=st.columns(2)
with col1:
    year=st.number_input('Year',min_value=1900,step=1)
with col2:
    kms_driven=st.number_input('Klometers driven ',min_value=0,step=1)

fuel_type=st.selectbox('Select Fuel Type',fuel_types)

button=st.button('Price')

if button:
    payload={
        "company": company,
        "name": name,
        "year": year,
        "kms_driven": kms_driven,
        "fuel_type": fuel_type
    }
    try:
        response=requests.post(app_url,json=payload,timeout=10)
        response.raise_for_status()
        result=response.json()
        prediction_price=result.get("Price")
        st.success(f'Car Price is ₹{float(prediction_price):,.2f}')
    except requests.exceptions.RequestException as e:
        st.error(f'Error in requesting  {e}')
