import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

st.title('My First App-Pokemon')

@st.cache
def load_data():
    data = pd.read_csv('Pokemon.csv')
    return data

df = load_data()

st.subheader('basic-viz')

fig, ax = plt.subplots(figsize=[12,7])
sns.histplot(df['Attack'])
st.pyplot(fig)

st.subheader('callback')

selected_gen = st.selectbox('Select Generation', options=(1, 2, 3, 4, 5, 6), index=4)

fig1, ax1 = plt.subplots(figsize=[12,7])
sns.histplot(df[df['Generation']==selected_gen]['Attack'])
st.pyplot(fig1)

st.subheader('callback-pairplot')
selected_type = st.radio(label='Choose Type 1', options=df['Type 1'].unique())

fig2, ax2 = plt.subplots(figsize=[12,7])
sns.scatterplot(df[df['Type 1']==selected_type]['Attack'], df[df['Type 1']==selected_type]['Speed'])
st.pyplot(fig2)

st.write(df[df['Type 1']=='Flying'])

# st.image upload gambar
img = Image.open('dog.jpg')

st.header('Dog')
st.image(img, caption='Dog', width=400, use_column_width=None)

# st.columns menggunakan with notation
st.header('Column Partitioning')
col1, col2, col3 = st.columns(3)

with col1:
    st.write('Kolom Pertama')
    st.image(img)

with col2:
    st.write('kolom kedua')

with col3:
    st.write('kolom ketiga')
    st.image('https://cdn-2.tstatic.net/aceh/foto/bank/images/singa_20180328_155722.jpg')

# st.columns menggunakan variabel
st.header('Column using ratio Partitioning')
col1, col2 = st.columns([3, 1]) # 3 = jumlah kolom, 1 = ratio
data = np.random.randn(10, 1)

col1.subheader("A wide column with a chart")
col1.line_chart(data)

col2.subheader('A narrow column with data')
col2.write(data)

# Container menggunakan notasi with
with st.container():
  st.write("This is inside the container")

  # You can call any Streamlit command, including custom components:
  st.bar_chart(np.random.randn(50, 3))

st.write("This is outside the container")

# container menggunakan variable
st.subheader("container using variable")
cont = st.container()
cont.write('This is inside container')

st.write('This is outside container')

cont.write('This is inside container 2')

st.line_chart({"data": [1, 5, 2, 6, 2, 1]})

# EXPANDER
with st.expander("See explanation"):
  st.write("""
     The chart above shows some numbers I picked for you.
     I rolled actual dice for these, so they're *guaranteed* to
     be random.
  """)

  st.image("https://static.streamlit.io/examples/dice.jpg")