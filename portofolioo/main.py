import streamlit as st
import requests
from PIL import Image
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Portofolio", page_icon="🐍", layout="wide")

# Function untuk memuat animasi via URL
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None 
    return r.json()

# Function untuk menambahkan CSS lokal
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Ambil file CSS
local_css("style/style.css")

# Load animasi Lottie untuk profile
lottie_contact = load_lottieurl("https://lottie.host/3c5f4cdd-9d97-4519-8706-96f3e716db03/lHWZQ62bi7.json")
lottie_profile = load_lottieurl("https://lottie.host/53ad62ae-42f5-446a-83c4-4d99346656b0/minpMzTtts.json")
lottie_projek = load_lottieurl("https://lottie.host/67145e6e-8789-40b9-b5a8-7378e94ce8f2/GbrA7JH57R.json")
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_2 = Image.open("images/x.png")
img_1 = Image.open("images/y.png")

# Bagian profil di sidebar
with st.sidebar:
    st.subheader("Profil Saya")
    st_lottie(lottie_profile, height=200, loop=True, key="profile")
    st.write("Halo semua, perkenalkan saya Yosia Christian :wave:")
    st.write("Saya sekolah di SMK Taruna Bhakti, kelas 11.")
    st.write("[Selengkapnya >](https://github.com/YosiaCT)")

with st.container():
    st.subheader("Apa yang saya kerjakan?")
    st.write("##")
    st.write(""" 
             Saat ini saya sudah melakukan beberapa projek seperti :
             - Membuat Kalkulator menggunakan Python
             - Membuat Simple Text Editor menggunakan Python
             - Mengolah data menggunakan Python dengan ekstensi Jupyter Notebook
             """)

    col1, col2 = st.columns([1, 1])  # Lebar kolom pertama 3 kali lipat dari kolom kedua

    with col1:
        # Teks akan berada di kolom pertama
        st.write("")

    with col2:
        # Animasi akan berada di kolom kedua
        st.empty()  # Slot kosong di bagian atas
        st_lottie(lottie_coding, height=300, key="coding")


# Daftar Projek
with st.container():
    st.header("Daftar Projek")
    st.write("##")
    

    
    # Konten projek 1
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_1)
    with text_column:
        st.subheader("Kalkulator Python")
        st.write("""
                 Membuat kalkulator menggunakan ekstensi tkinter
                 """)
        st.write("[Source Code >](https://github.com/YosiaCT/kalkulator_python)")
        
    

    # Konten projek 2
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_2)
    with text_column:
        st.subheader("Simple Text Editor")
        st.write("""
                Membuat Simple text editor menggunakan ekstensi tkinter
                """)
        st.write("[Source Code >](https://github.com/YosiaCT/simple_text_editor)")
        st_lottie(lottie_projek, height=300, key="projek")
        

# Kontak
with st.container():
    st.header("Hubungi Saya")
    st.write("##")
    st.write("""
             Jika tertarik dengan apa yang saya bisa, silahkan hubungi melalui :\n
             Email : yosiachristian@gmail.com \n
             Whatsapp : 0895-1239-4140
             """)
    st_lottie(lottie_contact, height=300, key="contact")
    
