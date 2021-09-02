import streamlit as st
import numpy as np 
import pandas as pd 
import sklearn


st.text("Text : This is Soheil Tehranipour")

st.write("Write : This is Soheil Tehranipour")

st.markdown("# This is Heading")

st.title("This is Title")

st.latex(r'''
...     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
...     \sum_{k=0}^{n-1} ar^k =
...     a \left(\frac{1-r^{n}}{1-r}\right)
...     ''')

#-------------------------------------------------
df = pd.read_csv("1.csv")
st.dataframe(df)
# st.table(df)

#-------------------------------------------------
from PIL import Image
photo = Image.open("juve.jpg")
st.image(photo)

#-------------------------------------------------
st.error("Error Message")

st.warning("Warning")

st.success("Success")

#-------------------------------------------------
st.button('Click here')

st.checkbox("Check1")
st.checkbox("Check2")
st.checkbox("Check3")
st.checkbox("Check4")

st.radio("RADIO",[1,2,3,4,5,6])

st.slider("Slide me",10,100)

st.file_uploader("Upload:.......")

st.color_picker("COLOR")