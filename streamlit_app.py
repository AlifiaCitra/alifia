import streamlit as st
import time

# Konfigurasi Halaman Game
st.set_page_config(page_title="Unreal Chemist - Streamlit Edition", page_icon="⚗️", layout="centered")

st.title("⚗️ Unreal Chemist (Streamlit Edition)")
st.write("Selamat datang di simulator lab kimia organik interaktif! Campurkan zat, atur suhu, dan lihat reaksinya.")
st.divider()

# LANGKAH 1: MENUANGKAN ISI TABUNG REAKSI UTAMA (SAMPEL)
st.subheader("1. Isi Tabung Reaksi Utama (Sampel)")
sampel = st.radio(
    "Pilih Senyawa Organik:",
    ["Kosong", "Formaldehida (Aldehida)", "Aseton (Keton)", "Fenol"],
    horizontal=True
)

# LANGKAH 2: MEMILIH REAGEN DARI RAK LAB
st.subheader("2. Pilih Reagen dari Rak")
reagen = st.selectbox(
    "Pilih zat yang ingin ditambahkan:",
    ["-- Pilih Reagen --", "Pereaksi Fehling (Biru)", "Pereaksi Tollens (Bening)", "Larutan FeCl3 (Kuning Muda)"]
)

# LANGKAH 3: KONTROL SUHU (SLIDER BUNSEN)
st.subheader("3. Kontrol Suhu Laboratorium")
suhu = st.slider("Atur Suhu Pemanas (°C):", min_value=25, max_value=100, value=25, step=5)
if suhu > 60:
    st.warning("🔥 Bunsen menyala: Kondisi pemanasan terpenuhi.")
else:
    st.info("❄️ Suhu Kamar: Tanpa pemanasan.")

st.divider()

# LANGKAH 4: TOMBOL AKSI REAKSI (MAIN GAME)
if sampel != "Kosong" and reagen != "-- Pilih Reagen --":
    st.subheader("4. Jalankan Eksperimen")
    
    if st.button("🧪 TUANGKAN REAGEN & REAKSIKAN!"):
        
        # Animasi Loading seperti menuang cairan
        status_text = st.empty()
        progress_bar = st.progress(0)
        
        for percent_complete in range(100):
            time.sleep(0.02)  # Efek animasi berjalan cepat
            progress_bar.progress(percent_complete + 1)
            if percent_complete < 40:
                status_text.text("💧 Meneteskan reagen ke dalam tabung...")
            elif percent_complete < 80:
                status_text.text("🔄 Mengguncang tabung reaksi...")
            else:
                status_text.text("⚡ Menunggu kesetimbangan reaksi...")
                
        status_text.text("✨ Reaksi Selesai!")
        st.divider()
        
        # LOGIKA KIMIA SIMULASI (Penentuan Perubahan Warna & Hasil)
        warna_akhir = "#FFFFFF"  # Default Bening
        emoji_tabung = "💧"
        catatan_kimia = ""
        nama_reaksi = "Tidak ada reaksi yang terjadi (Negatif)."
        sukses = False

        # Kondisi 1: Formaldehida + Fehling + Panas -> Merah Bata
        if "Formaldehida" in sampel and "Fehling" in reagen:
            if suhu >= 60:
                warna_akhir = "#B22222"  # Merah Bata (Firebrick)
                emoji_tabung = "🔴"
                nama_reaksi = "Uji Fehling Positif (Reduksi Kupri)"
                catatan_kimia = "Gugus Aldehida mereduksi ion $Cu^{2+}$ (biru) menjadi endapan $Cu_2O$ yang berwarna merah bata."
                sukses = True
            else:
                warna_akhir = "#0000FF"  # Tetap Biru kalau kurang panas
                emoji_tabung = "🔵"
                nama_reaksi = "Reaksi Tertunda (Kurang Panas)"
                catatan_kimia = "Uji Fehling memerlukan suhu tinggi (>60°C) untuk melewati energi aktivasi pengendapan merah bata."

        # Kondisi 2: Formaldehida + Tollens + Panas -> Cermin Perak
        elif "Formaldehida" in sampel and "Tollens" in reagen:
            if suhu >= 60:
                warna_akhir = "#D3D3D3"  # Abu-abu Perak
                emoji_tabung = "🪞"
                nama_reaksi = "Uji Tollens Positif (Cermin Perak)"
                catatan_kimia = "Aldehida dioksidasi menjadi asam karboksilat, sementara kompleks $[Ag(NH_3)_2]^+$ direduksi menjadi logam perak mendidih."
                sukses = True
            else:
                warna_akhir = "#F5F5F5"
                nama_reaksi = "Reaksi Lambat"
                catatan_kimia = "Cermin perak tidak terbentuk sempurna pada suhu kamar. Naikkan suhu bunsen!"

        # Kondisi 3: Fenol + FeCl3 -> Ungu Pekat (Suhu Kamar)
        elif "Fenol" in sampel and "FeCl3" in reagen:
            warna_akhir = "#4B0082"  # Ungu Pekat (Indigo)
            emoji_tabung = "🟣"
            nama_reaksi = "Pembentukan Kompleks Besi(III) Fenolat"
            catatan_kimia = "Ion $Fe^{3+}$ langsung berikatan dengan gugus hidroksil pada cincin benzena Fenol, menghasilkan warna ungu pekat seketika tanpa perlu pemanasan."
            sukses = True

        # Kondisi 4: Aseton + Semua Reagen -> Negatif (Keton tidak mudah dioksidasi)
        elif "Aseton" in sampel:
            warna_akhir = "#F0F2F6"  # Tetap Bening / Warna asal reagen
            emoji_tabung = "⚪"
            nama_reaksi = "Uji Negatif (Keton)"
            catatan_kimia = "Aseton adalah keton. Keton tidak memiliki atom hidrogen yang terikat pada karbon karbonil, sehingga tidak bisa dioksidasi oleh reagen lemah seperti Fehling atau Tollens."

        # TAMPILKAN GRAFIS SIMULATOR NYATA
        col_visual, col_deskripsi = st.columns([1, 2])
        
        with col_visual:
            st.markdown("<h4 style='text-align: center;'>Tabung Reaksi 3D</h4>", unsafe_allow_html=True)
            # Desain tabung reaksi interaktif menggunakan HTML CSS yang warnanya berubah dinamis
            st.markdown(f"""
            <div style="
                background: linear-gradient(to bottom, rgba(255,255,255,0.2) 30%, {warna_akhir} 100%);
                border: 4px solid #E0E0E0;
                border-bottom-left-radius: 50px;
                border-bottom-right-radius: 50px;
                width: 90px;
                height: 220px;
                margin: 0 auto;
                box-shadow: 0px 10px 20px rgba(0,0,0,0.2);
                display: flex;
                align-items: flex-end;
                justify-content: center;
                padding-bottom: 20px;
            ">
                <h1 style="font-size: 40px; margin: 0;">{emoji_tabung}</h1>
            </div>
            """, unsafe_allow_html=True)
            
        with col_deskripsi:
            if sukses:
                st.success(f"### 🎉 {nama_reaksi}")
            else:
                st.error(f"### 🧪 {nama_reaksi}")
                
            st.markdown(f"**Persamaan & Analisis Mekanisme:**")
            st.info(catatan_kimia)
            st.metric(label="Suhu Akhir Reaksi", value=f"{suhu} °C")

else:
    st.warning("💡 Silakan pilih **Sampel** dan **Reagen** terlebih dahulu di atas untuk memulai simulasi lab!")
