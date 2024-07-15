import streamlit as st
from PIL import Image

st.title("初めてのstreamlitアプリ")
st.caption("これはPythonVtuber サプーさんの動画を見て作成したテストWebアプリです")

# 画像
image = Image.open("./data/nyanko.png")
st.image(image, width=200)