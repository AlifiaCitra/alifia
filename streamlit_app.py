import streamlit as st
import time

# Konfigurasi Halaman Game
st.set_page_config(page_title="Unreal Chemist 2D", page_icon="⚗️", layout="centered")

st.title("⚗️ Unreal Chemist - Edisi Lab Maya")
st.write("Simulator lab kimia organik interaktif. Campurkan zat, atur suhu, dan lihat reaksinya!")
st.divider()

# 1. INPUT EKSPERIMEN
st.subheader("1. Siapkan Alat & Bahan")
sampel = st.radio(
    "Pilih Senyawa Organik (Sampel):",
    ["Kosong", "Formaldehida (Aldehida)", "Aseton (Keton)", "Fenol"],
    horizontal=True
)

reagen = st.selectbox(
    "Pilih Reagen Uji:",
    ["-- Pilih Reagen --", "Pereaksi Fehling (Biru)", "Pereaksi Tollens (Bening)", "Larutan FeCl3 (Kuning)"]
)

suhu = st.slider("Atur Suhu Pemanas Bunsen (°C):", min_value=25, max_value=100, value=25, step=5)

st.divider()

# 2. PROSES REAKSI GAME
if sampel != "Kosong" and reagen != "-- Pilih Reagen --":
    st.subheader("2. Jalankan Eksperimen")
    
    if st.button("🧪 TUANGKAN REAGEN & REAKSIKAN!", use_container_width=True):
        
        # Animasi Loading
        status = st.empty()
        bar = st.progress(0)
        for p in range(100):
            time.sleep(0.01)
            bar.progress(p + 1)
            if p < 50:
                status.text("💧 Meneteskan reagen ke tabung...")
            else:
                status.text("🔄 Mengguncang tabung reaksi...")
        status.text("✨ Reaksi Selesai!")
        
        # Logika Hasil Perubahan Warna
        warna_akhir = "#FFFFFF"  # Default Bening
        emoji = "💧"
        catatan = "Tidak ada perubahan visual yang teramati (Reaksi Negatif)."
        is_pos = False

        # Kondisi 1: Aldehida + Fehling
        if "Formaldehida" in sampel and "Fehling" in reagen:
            if suhu >= 60:
                warna_akhir = "#B22222" # Merah Bata
                emoji = "🔴"
                catatan = "Positif! Gugus Aldehida mereduksi ion Cu2+ menjadi endapan Cu2O merah bata."
                is_pos = True
            else:
                warna_akhir = "#0000FF" # Tetap Biru
                emoji = "🔵"
                catatan = "Negatif. Uji Fehling membutuhkan pemanasan (>60°C) untuk membentuk endapan."

        # Kondisi 2: Aldehida + Tollens
        elif "Formaldehida" in sampel and "Tollens" in reagen:
            if suhu >= 60:
                warna_akhir = "#D3D3D3" # Cermin Perak
                emoji = "🪞"
                catatan = "Positif! Terbentuk lapisan cermin perak mengkilap di dinding tabung."
                is_pos = True
            else:
                warna_akhir = "#F5F5F5"
                emoji = "⚪"
                catatan = "Reaksi berjalan lambat. Naikkan suhu Bunsen untuk memicu endapan cermin perak."

        # Kondisi 3: Fenol + FeCl3
        elif "Fenol" in sampel and "FeCl3" in reagen:
            warna_akhir = "#4B0082" # Ungu Pekat
            emoji = "🟣"
            catatan = "Positif! Ion Fe3+ langsung membentuk senyawa kompleks berwarna ungu pekat dengan Fenol."
            is_pos = True

        # Kondisi 4: Keton (Aseton) -> Selalu Negatif
        elif "Aseton" in sampel:
            warna_akhir = "#F0F2F6"
            emoji = "⚪"
            catatan = "Negatif. Senyawa Keton (Aseton) tidak dapat dioksidasi oleh reagen Tollens atau Fehling."

        # TAMPILAN GRAFIS VISUAL
        st.divider()
        col1, col2 = st.columns([1, 2])
        
        with col1:
            # Menggambar bentuk tabung reaksi otomatis warna dinamis
            st.markdown(f"""
            <div style="
                background: linear-gradient(to bottom, rgba(255,255,255,0.1) 20%, {warna_akhir} 100%);
                border: 4px solid #E0E0E0;
                border-bottom-left-radius: 40px;
                border-bottom-right-radius: 40px;
                width: 80px; height: 200px; margin: 0 auto;
                display: flex; align-items: flex-end; justify-content: center; padding-bottom: 20px;
            ">
                <h2 style="margin: 0;">{emoji}</h2>
            </div>
            <p style="text-align: center; font-size: 12px; font-weight: bold; margin-top: 5px;">Tabung Reaksi</p>
            """, unsafe_allow_html=True)
            
        with col2:
            if is_pos:
                st.success("### 🎉 Hasil Pengamatan: POSITIF")
            else:
                st.error("### 🧪 Hasil Pengamatan: NEGATIF")
            st.info(catatan)
            st.metric("Suhu Lab Saat Ini", f"{suhu} °C")

else:
    st.warning("💡 Silakan tentukan **Sampel** dan **Reagen** di atas terlebih dahulu untuk memulai simulasi!")
