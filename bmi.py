# weight = float(input('enter weigth in kg:'))
# height = float(input('enter height in m:'))

# bmi = weight/(height**2)
# print(bmi)

import streamlit as st

weight = st.number_input('enter weigth in kg:')
height = st.number_input('enter height :')

unit= st.selectbox("Height unit: ", ["m","cm","feet"])

if unit == "cm":
   height= height/100
elif unit == "feet":
   height= height * 0.3048
else:
   height = height 

if st.button('calculate'):
   bmi = weight/(height**2)
   st.write(bmi)


