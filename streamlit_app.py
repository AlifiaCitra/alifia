import streamlit as st
import time

st.set_page_config(page_title="Simulasi Lab Kimia Organik", page_icon="🧪", layout="centered")

st.title("🧪 Lab Maya: Uji Kualitatif Organik")
st.write("Silakan lakukan eksperimen mandiri untuk mengidentifikasi gugus fungsi sampel misterius.")
st.divider()

# 1. STEP 1: PILIH SAMPEL MISTERIUS
st.subheader("Langkah 1: Ambil Sampel")
sampel = st.selectbox("Pilih Sampel yang akan diuji:", ["-- Pilih Sampel --", "Sampel A", "Sampel B", "Sampel C"])

if sampel != "-- Pilih Sampel --":
    st.info(f"📋 **Status:** {sampel} telah dimasukkan ke dalam tabung reaksi (Cairan Bening).")
    
    st.divider()
    
    # 2. STEP 2: PILIH REAGEN / UJI
    st.subheader("Langkah 2: Tambahkan Reagen")
    reagen = st.selectbox("Pilih Reagen Uji:", ["-- Pilih Reagen --", "Reagen Tollens (AgNO3 + NH4OH)", "Larutan FeCl3 1%", "Larutan NaHCO3 5%"])
    
    if reagen != "-- Pilih Reagen --":
        st.info(f"🧪 **Status:** Menambahkan {reagen} ke dalam {sampel}...")
        
        st.divider()
        
        # 3. STEP 3: AKSI PEMANASAN (SANGAT COCOK UNTUK SIMULASI)
        st.subheader("Langkah 3: Perlakuan Kimia")
        butuh_panas = False
        
        # Uji Tollens butuh pemanasan, yang lain tidak wajib
        if "Tollens" in reagen:
            st.warning("⚠️ Reaksi ini memerlukan energi aktivasi (pemanasan).")
            butuh_panas = True
            panaskan = st.button("🔥 Nyalakan Bunsen / Panaskan Tabung")
        else:
            panaskan = st.button("🧪 Kocok Tabung Reaksi")

        # 4. LOGIKA HASIL EKSPERIMEN (SIMULASI PERUBAHAN)
        if panaskan:
            with st.spinner("Mengamati reaksi kimia... Mohon tunggu..."):
                time.sleep(2) # Efek menunggu reaksi lab selama 2 detik
            
            st.success("✨ Reaksi Selesai! Berikut hasil pengamatan laboratorium:")
            
            # Kolom Hasil Visual
            col_teks, col_warna = st.columns([2, 1])
            
            with col_teks:
                # PENENTUAN HASIL BERDASARKAN KOMBINASI SAMPEL & REAGEN
                if sampel == "Sampel A" and "Tollens" in reagen:
                    st.markdown("### 🪞 Hasil: Terbentuk Cermin Perak")
                    st.write("**Analisis:** Sampel teroksidasi dan mereduksi ion $Ag^+$ menjadi logam perak yang menempel di dinding tabung.")
                    st.markdown("**Kesimpulan:** Sampel A mengandung gugus **Aldehida**.")
                    warna_box = "🥈"
                    bg_color = "#D3D3D3" # Abu-abu perak
                
                elif sampel == "Sampel B" and "FeCl3" in reagen:
                    st.markdown("### 🟣 Hasil: Larutan Menjadi Ungu Pekat")
                    st.write("**Analisis:** Terbentuk senyawa kompleks antara ion $Fe^{3+}$ dengan senyawa fenolik.")
                    st.markdown("**Kesimpulan:** Sampel B mengandung gugus **Fenol**.")
                    warna_box = "🔮"
                    bg_color = "#8A2BE2" # Ungu
                    
                elif sampel == "Sampel C" and "NaHCO3" in reagen:
                    st.markdown("### 🫧 Hasil: Terbentuk Gelembung Gas Cepat")
                    st.write("**Analisis:** Terjadi reaksi asam-basa yang menghasilkan gas Karbondioksida ($CO_2$).")
                    st.markdown("**Kesimpulan:** Sampel C mengandung gugus **Asam Karboksilat**.")
                    warna_box = "🧼"
                    bg_color = "#E0FFFF" # Biru muda gelembung
                    
                else:
                    st.markdown("### ❌ Hasil: Tidak Ada Perubahan (Negatif)")
                    st.write("**Analisis:** Reagen tidak bereaksi dengan struktur
