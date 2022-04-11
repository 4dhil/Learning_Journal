import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

st.title('My First App')

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

if st.button('Say Hello'):
    st.write('Clicked!')
else:
    st.write('not clicked yet!')

st.header('This is checkbox')
if st.checkbox('Show Data'):
    st.write('Checked')

st.header('This is radio button')
st.radio('Select one: ', ('Comedy','Romance', 'Documentary'), 1)