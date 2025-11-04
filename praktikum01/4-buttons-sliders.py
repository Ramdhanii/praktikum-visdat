import streamlit as st

st.title("Praktikum 1 - Visualisasi Data")
st.caption("Bagian 4: Button dan Sliders")
st.markdown("""
Kelompok 4 :
- Erina Nurul Hodijah - 0110112113
- Hanin Salwa Salsabila Hidayati Nurrohman - 0110122294
- Mohammad Ramdhani - 0110122083
""")

button = st.button('Click Here')
if button:
    st.write('You Have Clicked Button')
else:
    st.write('You Have not clicked the button')

gender = 