import streamlit as st
import pandas as pd
import numpy as np
import graphviz as graphviz


st.title("Praktikum 2 - Visualisasi Data")
st.caption("Bagian 5: Graphviz")
st.markdown("""
Kelompok 4 :
- Erina Nurul Hodijah - 0110112113
- Hanin Salwa Salsabila Hidayati Nurrohman - 0110122294
- Mohammad Ramdhani - 0110122083
""")

st.graphviz_chart("""
    digraph {
        "Training Data" -> "ML Algorithm"
        "ML Algorithm" -> "Model"
        "Model" -> "Results Forecasting"
        "New Data" -> "Model"              
    }              
""")