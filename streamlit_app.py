import streamlit as st
import time

# 1. Konfigurasi Halaman Game
st.set_page_config(page_title="Unreal Chemist 2D", page_icon="⚗️", layout="wide")

st.title("⚗️ Unreal Chemist - Edisi Visual Lab")
st.write("Visualisasikan eksperimen ujimu langsung dengan foto hasil laboratorium asli!")
st.divider()

# Buat layout 2 kolom besar: Kiri untuk kontrol/rak meja lab, Kanan untuk Rak Hasil Tabung
col_kontrol, col_canvas = st.columns([1, 1.2])

with col_kontrol:
    st.markdown("### 🎛️ Meja Kerja Laboratorium")
    
    # LANGKAH 1: PILIH SAMPEL CAIRAN MISTERIUS
    sampel = st.selectbox(
        "1. Tuangkan Sampel Organik ke Tabung Reaksi:",
        ["-- Pilih Sampel di Meja --", "Sampel Cairan A (Aldehida)", "Sampel Cairan B (Fenol)", "Sampel Cairan C (Keton)"]
    )
    
    # LANGKAH 2: PILIH REAGEN DARI RAK (Pake radio biar keliatan semua opsinya)
    st.markdown("**2. Pilih Botol Reagen Pengetes:**")
    reagen = st.radio(
        "Pilih salah satu reagen di bawah:",
        ["Belum Memilih", "Reagen Tollens (AgNO3 + Basa)", "Larutan FeCl3 (Besi Klorida)"],
        index=0
    )
    
    # LANGKAH 3: KONTROL PEMANAS (BUNSEN)
    st.markdown("**3. Pengaturan Suhu Kamar/Pemanas:**")
    suhu = st.select_slider(
        "Atur kondisi Bunsen:",
        options=["Suhu Kamar (25°C)", "Pemanasan Hangat (50°C)", "Pemanasan Kuat (80°C)"]
    )
    
    st.divider()
    
    # TOMBOL UTAMA UNTUK MENCAMPURKAN
    mulai_reaksi = st.button("🧪 CAMPURKAN & REAKSIKAN ZAT!", use_container_width=True)

# 2. SEKSI KANAN: CANVAS VISUAL GAME (Tempat tabung reaksi berada)
with col_canvas:
    st.markdown("### 🔬 Tampilan Tabung Reaksi")
    
    # Jika tombol belum diklik, tampilkan tabung reaksi kosong/bening biasa
    if not mulai_reaksi or sampel == "-- Pilih Sampel di Meja --" or reagen == "Belum Memilih":
        st.info("Silakan tentukan Sampel, Reagen, dan Suhu di sebelah kiri, lalu klik tombol **CAMPURKAN** untuk melihat perubahan kimia!")
        # Foto default tabung reaksi laboratorium bening/kosong
        st.image("https://images.unsplash.com/photo-1576086213369-97a306d36557?auto=format&fit=crop&q=80&w=400", caption="Tabung Reaksi Siap Digunakan", width=350)
        
    else:
        # JALANKAN ANIMASI PROSES GAME
        with st.spinner("⏳ Menuangkan reagen... Mengocok tabung..."):
            time.sleep(1.5) # Jeda animasi biar dramatis
            
        st.success("✨ Reaksi Selesai! Berikut perubahan visual zat:")
        
        # LOGIKA DIAGNOSIS GAME & MEMANGGIL FOTO ASLI NYATA
        # Kasus 1: Aldehida + Tollens + Panas Kuat -> Cermin Perak
        if "Aldehida" in sampel and "Tollens" in reagen:
            if "80°C" in suhu:
                st.markdown("#### 🔴 Hasil: POSITIF (Terbentuk Cermin Perak)")
                st.image("https://upload.wikimedia.org/wikipedia/commons/d/df/Tollens_test.jpg", caption="Foto Asli Hasil Uji Tollens Positif", width=400)
                st.info("💡 **Analisis:** Gugus Aldehida mereduksi kompleks perak menjadi logam perak mendidih yang menempel mengkilap di dinding tabung seperti cermin.")
            else:
                st.markdown("#### 🟡 Hasil: NEGATIF / BELUM SEMPURNA")
                st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Silver_nitrate_solution.jpg/640px-Silver_nitrate_solution.jpg", caption="Larutan Tetap Bening Kekuningan", width=400)
                st.warning("⚠️ **Petunjuk Game:** Reaksi Tollens membutuhkan **Pemanasan Kuat (80°C)** untuk memicu pengendapan perak. Coba naikkan suhu bunsenmu!")

        # Kasus 2: Fenol + FeCl3 -> Ungu Pekat (Bisa di semua suhu)
        elif "Fenol" in sampel and "FeCl3" in reagen:
            st.markdown("#### 🔴 Hasil: POSITIF (Terbentuk Kompleks Ungu)")
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Iron%28III%29_salicylate_complex.jpg/640px-Iron%28III%29_salicylate_complex.jpg", caption="Foto Asli Hasil Uji FeCl3 Positif", width=400)
            st.info("💡 **Analisis:** Ion Besi(III) langsung mengikat gugus hidroksil pada cincin fenol, menciptakan kompleks warna ungu gelap seketika.")

        # Kasus 3: Keton + Tollens atau FeCl3 -> Tetap Negatif/Bening
        elif "Keton" in sampel:
            st.markdown("#### ⚪ Hasil: NEGATIF (Tidak Ada Reaksi)")
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Silver_nitrate_solution.jpg/640px-Silver_nitrate_solution.jpg", caption="Larutan Tidak Berubah Warna", width=400)
            st.error("
