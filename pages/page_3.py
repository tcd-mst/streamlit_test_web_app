import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# データ分析関連
df = pd.read_csv("./data/平均気温.csv", index_col = "月")
# # 表形式で表示
# st.dataframe(df)
# 折れ線グラフ形式で表示
st.line_chart(df)
# 2021年値をの棒グラフとして表示
st.bar_chart(df["2021年"])

# matplotlib
fig, ax = plt.subplots()
ax.plot(df.index, df["2021年"])
ax.set_title("matplotlib draph")
st.pyplot(fig)