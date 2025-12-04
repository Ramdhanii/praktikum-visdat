import streamlit as st
import pandas as pd
import numpy as np


st.title("Praktikum 2 - Visualisasi Data")
st.caption("Bagian 6: Column")
st.markdown("""
Kelompok 4 :
- Erina Nurul Hodijah - 0110112113
- Hanin Salwa Salsabila Hidayati Nurrohman - 0110122294
- Mohammad Ramdhani - 0110122083
""")

col1, col2 = st.columns(2)
col1.write("Ini adalah kolom pertama")
col1.image("../../praktikum01/assets/katak.jpeg", caption="Gambar 1")
col2.write("Ini adalah kolom kedua")