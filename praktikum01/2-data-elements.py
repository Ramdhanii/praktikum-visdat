import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as pit

st.title("Praktikum 1 - Visualisasi Data")
st.caption("Bagian 2: Data Elements")
st.markdown("""
Kelompok 4 :
- Erina Nurul Hodijah - 0110112113
- Hanin Salwa Salsabila Hidayati Nurrohman - 0110122294
- Mohammad Ramdhani - 0110122083
""")

st.subheader("DataFrame")
df = pd.DataFrame(
    np.random.randn(30, 10),
    columns=('col_no %d' % i for i in range (10))
)
st.dataframe(df)

st.subheader("Hightlight Minimum Value di DataFrame")

st.dataframe(df.style.highlight_min(axis=0))

st.subheader("Table Statis")

df = pd.DataFrame(
    np.random.randn(30, 10),
    columns=('col_no %d' % i for i in range (10))
)

st.table(df)

st.subheader("Metrics")

st.metric(label="Temprature", value="31 °C", delta="1.2 °C")
col1, col2, col3 = st.columns(3)

col1.metric("Curah Hujan", "100 cm", "10 cm")
col2.metric(label="Populasi", value="123 Miliar", delta ="1 Miliar", delta_color="inverse")
col3.metric(label="Pelanggan", value=100, delta=10, delta_color="off")

st.metric(label="Speed", value=None, delta=0)
st.metric("Trees", "91456", "-1132649")

df = pd.DataFrame(
    np.random.randn(30, 10),
    columns=('col_no %d' % i for i in range (10))
)
st.write('Here is our Data', df, 'Data is in dataframe format.\n', "\nWrite is Super function")

df = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['a', 'b']
)
chart = alt.Chart(df).mark_bar().encode(
x='a', y='b', tooltip=['a','b']
)
st.write(chart)

s = np.random.logistic(10, 5, size=5)
chart, ax = pit.subplot()
ax.hist(s, bins=15)

"chart", chart