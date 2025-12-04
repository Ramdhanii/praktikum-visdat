import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.title("Bar Chart")
st.caption("Praktikum 4 - Matplotlib Bar Chart")
st.markdown("""
Kelompok 4 :
- Erina Nurul Hodijah - 0110112113
- Hanin Salwa Salsabila Hidayati Nurrohman - 0110122294
- Mohammad Ramdhani - 0110122083
""")

data={
    'Jurusan' : ['Ilmu Komputer', 'Sistem Informasi', 'Teknik Informatika', 'Data Science'],
    'Jumlah Mahasiswa' : [120, 150, 100, 80]
}

df=pd.DataFrame(data)

st.title('Bar Chart - Jumlah Mahasiswa per Jurusan')
st.bar_chart(df.set_index('Jurusan'))

st.title('Basic Bar Chart Menggunakan Matplotlib')
fig, ax = plt.subplots()
ax.bar(data['Jurusan'], data['Jumlah Mahasiswa'], color='skyblue')
ax.set_title('Jumlah Mahasiswa per Jurusan')
ax.set_xlabel('Jurusan')
ax.set_ylabel('Jumlah Mahasiswa')

st.pyplot(fig)

st.title("Kustomisasi Basic Bar Chart")  # Judul untuk grafik pertama

fig, ax = plt.subplots()  # Membuat figure dan axes Matplotlib
colors = ['blue', 'green', 'orange', 'purple']  # Warna untuk tiap batang

bars = ax.bar(data['Jurusan'], data['Jumlah Mahasiswa'], color=colors)  # Membuat bar chart
ax.set_title('Jumlah Mahasiswa per Jurusan')  # Judul chart
ax.set_xlabel('Jurusan')  # Label sumbu X
ax.set_ylabel('Jumlah Mahasiswa')  # Label sumbu Y

for bar in bars:  # Loop setiap batang
    ax.text(
        bar.get_x() + bar.get_width() / 2,  # Posisi teks di tengah batang
        bar.get_height() + 5,               # Posisi teks sedikit di atas batang
        str(bar.get_height()),              # Menampilkan nilai (tinggi batang)
        ha='center'                         # Teks rata tengah
    )

st.pyplot(fig)  # Menampilkan grafik di Streamlit

st.title("Multiple Basic Bar Chart")  # Judul grafik kedua

data_2023 = [120, 150, 100, 80]  # Data tahun 2023
data_2024 = [140, 160, 110, 98]  # Data tahun 2024

x = range(len(data['Jurusan']))  # Menghasilkan index 0,1,2,3 untuk posisi X
width = 0.4  # Lebar batang

fig, ax = plt.subplots()  # Membuat figure baru
ax.bar(x, data_2023, width=width, label='2023', color='skyblue')  # Bar 2023
ax.bar([p + width for p in x], data_2024, width=width, label='2024', color='orange')  # Bar 2024 di sebelah kanan

ax.set_title('Jumlah Mahasiswa per Jurusan (2023 vs 2024)')  # Judul chart
ax.set_xlabel('Jurusan')  # Label sumbu X
ax.set_ylabel('Jumlah Mahasiswa')  # Label sumbu Y

ax.set_xticks([p + width / 2 for p in x])  # Posisi label X di tengah dua bar
ax.set_xticklabels(data['Jurusan'])  # Nama jurusan pada sumbu X

ax.legend()  # Menampilkan legenda

st.pyplot(fig)  # Menampilkan grafik kedua di Streamlit

data = {
    'Tahun': ['2019', '2020', '2021', '2022', '2023'],
    'Ilmu Komputer': [100, 110, 120, 130, 140],
    'Sistem Informasi': [120, 125, 135, 145, 160],
    'Teknik Informatika': [90, 95, 100, 108, 110],
    'Data Science': [70, 75, 80, 85, 90]
}

df = pd.DataFrame(data)

st.title("Visualisasi Tren Jumlah Mahasiswa Memilih Jurusan Komputer (5 Tahun Terakhir)")

filter_tahun = st.multiselect("Pilih Tahun:", df['Tahun'], default=df['Tahun'])

jurusan_list = ['Ilmu Komputer', 'Sistem Informasi', 'Teknik Informatika', 'Data Science']
filter_jurusan = st.multiselect("Pilih Jurusan:", jurusan_list, default=jurusan_list)

filtered_data = df[df['Tahun'].isin(filter_tahun)][['Tahun'] + filter_jurusan]

st.subheader("Data Jumlah Mahasiswa")
st.dataframe(filtered_data)

st.subheader("Bar Chart dengan Filter")
fig, ax = plt.subplots(figsize=(10, 6))

x = range(len(filtered_data['Tahun']))
width = 0.2

for i, jur in enumerate(filter_jurusan):
    ax.bar([p + i * width for p in x], filtered_data[jur], width=width, label=jur)

ax.set_title("Jumlah Mahasiswa per Jurusan (Berdasarkan Filter)")
ax.set_xlabel("Tahun")
ax.set_ylabel("Jumlah Mahasiswa")
ax.set_xticks([p + width * len(filter_jurusan) / 2 - width / 2 for p in x])
ax.set_xticklabels(filtered_data['Tahun'])
ax.legend()

st.pyplot(fig)
