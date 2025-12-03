# weight = float(input('enter weigth in kg:'))
# height = float(input('enter height in m:'))

# bmi = weight/(height**2)
# print(bmi)

import streamlit as st

weight = st.number_input('enter weigth in kg:')
height = st.number_input('enter height in m:')

if st.button('calculate'):
   bmi = weight/(height**2)
   st.write(bmi)


