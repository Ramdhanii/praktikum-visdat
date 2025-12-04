import streamlit as st
import pandas as pd
import numpy as np


st.title("Praktikum 2 - Visualisasi Data")
st.caption("Bagian 2: Line Chart")
st.markdown("""
Kelompok 4 :
- Erina Nurul Hodijah - 0110112113
- Hanin Salwa Salsabila Hidayati Nurrohman - 0110122294
- Mohammad Ramdhani - 0110122083
""")

df = pd.DataFrame(
    np.random.randn(40, 4),
    columns=["c1", "c2", "c3", "c4"]
)

st.line_chart(df)