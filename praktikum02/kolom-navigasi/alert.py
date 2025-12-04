import streamlit as st

st.title("Praktikum 2 - Visualisasi Data")
st.caption("Bagian 2: Alert")
st.markdown("""
Kelompok 4 :
- Erina Nurul Hodijah - 0110112113
- Hanin Salwa Salsabila Hidayati Nurrohman - 0110122294
- Mohammad Ramdhani - 0110122083
""")

# Menampilkan berbagai jenis notifikasi atau alert
st.success("Data berhasil dimuat!")
st.warning("Peringatan! Data tidak lengkap.")
st.info("Silakan periksa kembali input Anda.")
st.error("Terjadi kesalahan saat memproses data.")
st.exception("Ini adalah contoh exception (pengecualian).")