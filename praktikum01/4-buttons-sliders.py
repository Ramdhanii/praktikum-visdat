import streamlit as st
import time

st.title("Praktikum 1 - Visualisasi Data")
st.caption("Bagian 4: Button dan Sliders")
st.markdown("""
Kelompok 4 :
- Erina Nurul Hodijah - 0110112113
- Hanin Salwa Salsabila Hidayati Nurrohman - 0110122294
- Mohammad Ramdhani - 0110122083
""")

button = st.button('Click Here')   # Menampilkan button
if button:
    st.write('You Have Clicked Button')   # Ditampilkan jika button di klik
else:
    st.write('You Have not clicked the button')   # Ditampilkan jika button di klik

gender = st.radio(
    "Select your Gender",  # Label teks di atas radio button
    ('Male', 'Female', 'Others')  # Opsi yang akan muncul di radio button
)

# Mengecek pilihan pengguna, dan menampilkan teks berbeda berdasarkan hasilnya
if gender == 'Male':
    st.write('You have selected Male.')  # Ditampilkan jika pengguna memilih Male
elif gender == 'Female':
    st.write('You have selected Female.')  # Ditampilkan jika pengguna memilih Female
else:
    st.write('You have selected Others.')  # Ditampilkan jika pengguna memilih Others



st.write('Select your Hobbies:')  # Menampilkan instruksi ke pengguna

# Membuat tiga checkbox (bisa dicentang lebih dari satu)
# Masing-masing checkbox akan mengembalikan nilai True (jika dicentang) atau False (jika tidak)
check_1 = st.checkbox('Books')
check_2 = st.checkbox('Movies')
check_3 = st.checkbox('Sports')

# Mengecek kondisi masing-masing checkbox dan menampilkan pesan jika dipilih
if check_1:
    st.write('You selected Books.')
if check_2:
    st.write('You selected Movies.')
if check_3:
    st.write('You selected Sports.')

hobby = st.selectbox(
    'Choose your hobby:',  # Label teks yang ditampilkan di atas dropdown
    ('Books', 'Movies', 'Sports')  # Pilihan yang tersedia dalam dropdown
)

# Menampilkan hasil pilihan pengguna
st.write('Your selected hobby is:', hobby)

# Membuat elemen multi select dengan pilihan default
hobbies = st.multiselect(
    'What are your Hobbies',  # Label pertanyaan
    ['Reading', 'Cooking', 'Watching Movies/TV Series', 'Playing', 'Drawing', 'Hiking'],  # Pilihan yang tersedia
    ['Reading', 'Playing']  # Nilai default yang sudah terpilih
)

# Menampilkan judul pada aplikasi
st.title("Download Button")

# Membuat tombol download
down_btn = st.download_button(
    label="Download Image",              # Teks yang muncul di tombol
    data=open(r"C:\Python Visdat\assets\kucing.jpeg", "rb"),  # File yang akan diunduh (dibuka dalam mode 'rb' = read binary)
    file_name="tiger.jpg",               # Nama file hasil unduhan
    mime="image/jpg"                     # Tipe MIME file
)

# Membuat progress bar awal dengan nilai 0
download = st.progress(0)

# Menjalankan perulangan untuk memperbarui prog ress bar dari 0 sampai 99
for percentage in range(100):
    time.sleep(0.1)  # Menunda proses selama 0.1 detik agar terlihat efek progresnya
    download.progress(percentage + 1)  # Memperbarui nilai progress bar

# Menampilkan teks setelah proses selesai
st.write('Download Complete')

# Membuat spinner (indikator proses sedang berlangsung)
with st.spinner('Loading...'):
    time.sleep(5)  # Menunggu selama 5 detik untuk mensimulasikan proses

# Menampilkan teks setelah spinner selesai
st.write('Hello Data Scientists')