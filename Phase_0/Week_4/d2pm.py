import streamlit as st
import numpy as np
from PIL import Image

st.set_page_config(
    page_title="Fadhil's cool App",
    page_icon="😩",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.google.com',
        'Report a bug': "https://www.github.com/4dhil",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

selected = st.sidebar('Pages: ', ['Data Visualization', 'Hypothesis testing'])

if selected == 'Data Visualization':
    with st.container():
        st.write("This is inside the container")

        # You can call any Streamlit command, including custom components:
        st.bar_chart(np.random.randn(50, 3))

        st.write("This is outside the container")

else:
    st.write('Demo page')