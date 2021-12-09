import streamlit as st
import numpy as np
from PIL import Image
import io


st.title("Blood sample analysis")
uploaded_file = st.file_uploader("Upload a blood sample .png image", type=["png"])


if uploaded_file is not None:

    st.markdown("""### To show uploaded in streamlit""")
    st.image(uploaded_file)

    # st.markdown("""### To read file as bytes""")
    # bytes_data = uploaded_file.getvalue()
    # reshape necessary, but could only get shape with PIL, not from bytes directly

    st.markdown("""### To read file as an image & convert to numpy array""")
    # image = Image.open(io.BytesIO(bytes_data))
    image = Image.open(uploaded_file)
    st.image(image)
    st.write("Image shape: ", np.asarray(image).shape)
    st.write(np.asarray(image))
