from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import json

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


o=json.load(open('浙江省人民政府-住房搜索结果.json','r',encoding='utf-8').read())
st.dataframe(o)
