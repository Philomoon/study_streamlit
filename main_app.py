import streamlit as st
from PIL import Image

st.title("サプーアプリ")
st.caption("これはサプーの動画用テストアプリです")

# 画像
image = Image.open("./data/はつね1.jpeg")
st.image(image,width=200)