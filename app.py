import streamlit as st
import numpy as np
from PIL import Image
import io


st.title("Blood sample analysis")
uploaded_file = st.file_uploader("Upload a blood sample .png image")

st.image(uploaded_file)

if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    # st.write(bytes_data)


st.write(np.frombuffer(bytes_data, dtype=np.uint8))
# reshape necessary
