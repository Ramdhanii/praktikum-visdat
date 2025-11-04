import streamlit as st

# st.header("Ini header")
# st.subheader("Ini sub header")
# st.text("ini teks biasa tanpa format")
# st.markdown("**ini text bold** dan *ini text italic*")
# st.markdown("""
# - ini baris 1
# - ini menggunakan markdown multibaris
# 1. ini baris 2
# 2. ini menggunakan markdown multibaris
# * ini baris 3
# * ini menggunakan markdown multibaris
# """)
# st.caption("ini caption")
# st.title("Ini Judul")

st.header("Displaying Text Element")
st.title("Praktikum 1 - Visualisasi Data")
st.subheader("Text Element")
st.markdown("""
Kelompok 4 :
- Erina Nurul Hodijah - 0110112113
- Hanin Salwa Salsabila Hidayati Nurrohman - 0110122294
- Mohammad Ramdhani - 0110122083
""")

st.header("Displaying Latex")
st.latex(r''' \cos^2\theta = 1-2\sin^2\theta ''')
st.latex(r''' (a+b)^2 = a^2 + b^2 + 2ab ''')

st.header("Displaying Code")
st.subheader("Python Code")

code = '''
def hello():
    print("Hello, Streamlit")
'''

st.code(code, language='python')

st.subheader("Java Code")
st.code("""
    public class GFG {
        public static void main(String arg[]) {
            System.out.printIn("Hello World");
        }
    }
""", language='java')

st.subheader("Javascript Code")
st.code("""
<script>
try{
    adddlert("Welcome guest!); //kesalahan ketik (adddlert)
    sengaja dibuat untuk menimbulkan error
}
catc(err) {
    document.getElementById("demo").innerHTML = err.message; //menampilkan pesan error di element HTML dengan id 'demo'
}
</script>
""", language='javascript')
