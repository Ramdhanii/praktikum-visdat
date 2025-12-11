import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

suhu = [20, 22, 24, 26, 28, 30, 32, 34, 36]
penjualan = [50, 60, 70, 90, 100, 110, 130, 150, 180]

penjualan_weekdays = [50, 60, 70, 80, 90, 100, 110, 120, 130]
penjualan_weekends = [60, 70, 80, 100, 110, 120, 140, 160, 200]

data = {
    'Suhu': [20, 22, 24, 26, 28, 30, 32, 34, 36],
    'Penjualan_Cokelat': [50, 60, 70, 80, 90, 100, 110, 120, 130],
    'Penjualan_Vanila': [60, 70, 80, 90, 100, 110, 130, 140, 150],
    'Penjualan_Stroberi': [40, 50, 60, 70, 80, 90, 100, 110, 120],
    'Kelembapan': [60, 65, 70, 75, 80, 85, 90, 95, 100]
}

df = pd.DataFrame(data)

st.title('Visualisasi Scatter Plot Penjualan Es Krim')
st.sidebar.header('Pengaturan Visualiasi')

option = st.sidebar.selectbox(
    'Pilih contoh scatter plot',
    (
        'Basic Scatter Plot',
        'Kustomisasi Scatter Plot',
        'Multiple Scatter Plot',
        'Analisis Scatter Plot'
    )
)
st.title("Scatter Plot")
st.caption("Praktikum 5 - Matplotlib Scatter Plot")
st.markdown("""
Kelompok 4 :
- Erina Nurul Hodijah - 0110112113
- Hanin Salwa Salsabila Hidayati Nurrohman - 0110122294
- Mohammad Ramdhani - 0110122083
""")

#Basic scatter plot
def basic_scatter():
    st.subheader('1. Basic Scatter Plot')
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan)
    ax.set_title('Hubungan Penjualan Es Krim dengan Suhu')
    ax.set_xlabel('Suhu (°C)')
    ax.set_ylabel('Penjualan Es Krim')
    st.pyplot(fig)

# Kustomisasi scatter plot
def custom_scatter():
    st.subheader('2. Kustomisasi Scatter Plot')
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan, color='orange', s=100, edgecolor='black', alpha=0.7)
    ax.set_title('Hubungan Penjualan Es Krim dengan Suhu')
    ax.set_xlabel('Suhu (°C)')
    ax.set_ylabel('Penjualan Es Krim')
    ax.grid(True)
    st.pyplot(fig)

# Multiple scatter plot
def multiple_scatter():
    st.subheader('3. Multiple Scatter Plot')
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan_weekdays, color='green', label='Hari Kerja', s=80)
    ax.scatter(suhu, penjualan_weekends, color='purple', label='Akhir Pekan', s=80)
    ax.set_title('Hubungan Penjualan Es Krim dengan Suhu')
    ax.set_xlabel('Suhu (°C)')
    ax.set_ylabel('Penjualan Es Krim')
    ax.legend()
    st.pyplot(fig)

# Analisis dengan Scatter Plot
def scatter_3_variabel():
    st.subheader('4. Analisis dengan Scatter Plot')
    #opsi jenis eskrim
    jenis_eskrim = st.selectbox("Pilih Jenis Es Krim:", ['Cokelat', 'Vanila', 'Stroberi'])

    # logika untuk opsi jenis eskrim berdasarkan pilihan
    if jenis_eskrim == "Cokelat":
        penjualan = df['Penjualan_Cokelat']
    elif jenis_eskrim == "Vanila":
        penjualan = df['Penjualan_Vanila']
    else:
        penjualan = df['Penjualan_Stroberi']

    st.subheader("Data Penjualan dan Suhu")
    st.dataframe(df)

    # scatter Plot
    fig, ax = plt.subplots()
    scatter = ax.scatter(df['Suhu'], penjualan, c=df['Kelembapan'], s=100,
                        cmap='coolwarm', alpha=0.7)

    ax.set_title(f"Hubungan Penjualan Es Krim Jenis {jenis_eskrim} vs Suhu dan Kelembapan")
    ax.set_xlabel("Suhu (°C)")
    ax.set_ylabel(f"Penjualan Es Krim {jenis_eskrim}")
    plt.colorbar(scatter, label="Kelembapan (%)")

    # Tampilkan scatter plot di Streamlit
    st.pyplot(fig)

    # Ringkasan hubungan
    st.subheader("Analisis Hubungan")
    st.write(f"Grafik menunjukkan hubungan antara suhu, kelembapan, dan penjualan es krim jenis **{jenis_eskrim}**.")
    
if option == "Basic Scatter Plot" :
    basic_scatter()
elif option == "Kustomisasi Scatter Plot" :
    custom_scatter()
elif option == "Multiple Scatter Plot" :
    multiple_scatter()
elif option == "Analisis Scatter Plot" :
    scatter_3_variabel()