import streamlit as st
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
product_A_sales = [10,20,15,25,30,45,40,50,60,55,65,70]
product_B_sales = [5,10,8,15,18,20,22,30,25,35,40,45]

st.title("Visualisasi Penjualan Produk")
st.sidebar.header("Pengaturan Grafik")
option = st.sidebar.selectbox("Pilih Tipe Visualisasi", ("Single Line Plot", "Multiple & Customizations", "Jenis Garis untuk Menunjukkan Tren", "Subplot"))

st.caption("Praktikum 3 - Matplotlib Line Chart")
st.markdown("""
Kelompok 4 :
- Erina Nurul Hodijah - 0110112113
- Hanin Salwa Salsabila Hidayati Nurrohman - 0110122294
- Mohammad Ramdhani - 0110122083
""")

#Single line plot
def line_plot():
    fig,ax = plt.subplots()
    ax.plot(months, product_A_sales, label="product A")
    ax.set_title('Penjualan Produk A per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Penjualan')
    st.pyplot(fig)


#Multiple line plot & Customizations
def customize_line_plot():
    fig,ax = plt.subplots()
    ax.plot(months, product_A_sales, label="product A", color="blue", linestyle='--', marker='o')
    ax.plot(months, product_B_sales, label="product B", color="red", linestyle='-', marker='x')

    ax.set_title('Penjualan Produk per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Penjualan')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

product_C_sales=[18,22,25,28,32,38,42,45,48,52,56,60]
product_D_sales=[7,9,11,13,16,18,20,23,25,28,30,33]
def tren_line_plot():
    fig,axs = plt.subplots()
    axs.plot(months, product_C_sales, label="product C", color="green", linestyle=':')
    axs.plot(months, product_D_sales, label="product D", color="purple", linestyle='-.')
    
    axs.set_title('Tren Penjualan Produk per Bulan')
    axs.set_xlabel('Bulan')
    axs.set_ylabel('Jumlah Penjualan')
    axs.legend()
    axs.grid(True)
    st.pyplot(fig)

def subplots():
    fig, axs = plt.subplots(2, 1, figsize=(10,8))

    axs[0].plot(months, product_C_sales, label='Product C', color='green', marker = 'd')
    axs[0].set_title('Penjualan Produk C per Bulan')
    axs[0].set_xlabel('Bulan')
    axs[0].set_ylabel('Jumlah Penjualan')
    axs[0].legend()
    axs[0].grid(True)


    axs[1].plot(months, product_D_sales, label='Product D', color='purple', marker = 's')
    axs[1].set_title('Penjualan Produk D per Bulan')
    axs[1].set_xlabel('Bulan')
    axs[1].set_ylabel('Jumlah Penjualan')
    axs[1].legend()
    axs[1].grid(True)

    plt.tight_layout()
    st.pyplot(fig)

if option == "Single Line Plot" :
    line_plot()
elif option == "Multiple & Customizations" :
    customize_line_plot()
elif option == "Jenis Garis untuk Menunjukkan Tren" :
    tren_line_plot()
elif option == "Subplot" :
    subplots()