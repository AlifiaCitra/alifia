import streamlit as st
import pandas as pd
import time

# 1. Konfigurasi Halaman
st.set_page_config(page_title="ChemQual - Lab & Katalog", page_icon="🧪", layout="wide")

# 2. Database Utama (Katalog & Foto)
data_uji = [
    {
        "Nama Uji": "Uji Tollens",
        "Gugus Fungsi": "Aldehida",
        "Reagen": "AgNO3 + NaOH + NH4OH (Reagen Tollens)",
        "Prosedur Singkat": "Tambahkan sampel ke reagen Tollens, lalu panaskan di penangas air.",
        "Hasil Positif": "Terbentuk lapisan perak mengkilap di dinding tabung reaksi.",
        "Warna/Visual": "🪞 Cermin Perak (Silver Mirror)",
        "Reaksi Kimia": "R-CHO + 2[Ag(NH3)2]+ + 3OH- --> R-COO- + 2Ag (s) + 4NH3 + 2H2O",
        "Link Foto": "https://upload.wikimedia.org/wikipedia/commons/d/df/Tollens_test.jpg"
    },
    {
        "Nama Uji": "Uji Fehling",
        "Gugus Fungsi": "Aldehida",
        "Reagen": "Fehling A + Fehling B",
        "Prosedur Singkat": "Campurkan Fehling A & B, tambahkan sampel, panaskan.",
        "Hasil Positif": "Warna biru tua berubah menjadi endapan merah bata.",
        "Warna/Visual": "🔴 Endapan Merah Bata",
        "Reaksi Kimia": "R-CHO + 2Cu2+ + 5OH- --> R-COO- + Cu2O (s) + 3H2O",
        "Link Foto": "https://upload.wikimedia.org/wikipedia/commons/b/b9/Fehling_test_positive_negative.jpg"
    },
    {
        "Nama Uji": "Uji Ferri Klorida",
        "Gugus Fungsi": "Fenol",
        "Reagen": "Larutan FeCl3 1%",
        "Prosedur Singkat": "Larutkan sampel, lalu teteskan beberapa tetes larutan FeCl3.",
        "Hasil Positif": "Terbentuk warna kompleks ungu, hijau, atau biru pekat.",
        "Warna/Visual": "🟣 Warna Ungu / Biru / Hijau Pekat",
        "Reaksi Kimia": "6Ar-OH + Fe3+ --> [Fe(OAr)6]3- + 6H+",
        "Link Foto": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Iron%28III%29_salicylate_complex.jpg/640px-Iron%28III%29_salicylate_complex.jpg"
    }
]

df = pd.DataFrame(data_uji)

# Header Aplikasi
st.title("🧪 ChemQual v2.0")
st.subheader("Katalog & Simulasi Uji Kualitatif Organik")
st.divider()

# 3. Pembagian Menu Navigasi (Menu 1: Katalog, Menu 2: Lab Virtual)
tab1, tab2 = st.tabs(["📚 Katalog & Panduan Foto", "🎮 Lab Maya (Simulasi)"])

with tab1:
    st.markdown("### Cari Berdasarkan Parameter")
    search_gugus = "Semua Gugus"
    search_name = ""
    
    col1, col2 = st.columns(2)
    with col1:
        search_gugus = st.selectbox("Pilih Gugus Fungsi:", ["Semua Gugus"] + list(df["Gugus Fungsi"].unique()))
    with col2:
        search_name = st.text_input("Atau ketik nama uji / reagen:")

    filtered_df = df.copy()
    if search_gugus != "Semua Gugus":
        filtered_df = filtered_df[filtered_df["Gugus Fungsi"] == search_gugus]
    if search_name:
        filtered_df = filtered_df[
            filtered_df["Nama Uji"].str.contains(search_name, case=False) | 
            filtered_df["Reagen"].str.contains(search_name, case=False)
        ]

    if filtered_df.empty:
        st.warning("Uji kualitatif tidak ditemukan.")
    else:
        for index, row in filtered_df.iterrows():
            with st.expander(f"🔹 {row['Nama Uji']} — Target: {row['Gugus Fungsi']}", expanded=True):
                c1, c2, c3 = st.columns([2, 1, 1.5]) 
                with c1:
                    st.markdown(f"**🔬 Reagen:** {row['Reagen']}")
                    st.markdown(f"**📝 Prosedur:** {row['Prosedur Singkat']}")
                    st.markdown(f"**⚗️ Persamaan Reaksi:** `{row['Reaksi Kimia']}`")
                with c2:
                    st.info(f"**💡 Hasil:**\n{row['Hasil Positif']}")
                    st.success(f"**👁️ Visual:**\n{row['Warna/Visual']}")
                with c3:
                    if row["Link Foto"]:
                        st.image(row["Link Foto"], caption=f"Hasil Positif {row['Nama Uji']}", use_container_width=True)
                    else:
                        st.write("📷 Foto belum tersedia")

with tab2:
    st.markdown("### Eksperimen Mandiri di Laboratorium Virtual")
    st.write("Campurkan sampel misterius dengan reagen untuk melihat perubahan fasa/warna secara langsung.")
    
    sampel = st.selectbox("1. Pilih Sampel:", ["-- Pilih Sampel --", "Sampel X", "Sampel Y"])
    reagen_pilih = st.selectbox("2. Pilih Reagen Kimia:", ["-- Pilih Reagen --", "Reagen Tollens", "Larutan FeCl3 1%"])
    
    if sampel != "-- Pilih Sampel --" and reagen_pilih != "-- Pilih Reagen --":
        if "Tollens" in reagen_pilih:
            aksi = st.button("🔥 Panaskan di Penangas Air")
        else:
            aksi = st.button("🧪 Guncang Tabung Reaksi")
            
        if aksi:
            with st.spinner("Reaksi sedang berlangsung..."):
                time.sleep(1.5)
            
            res_col1, res_col2 = st.columns([2, 1])
            with res_col1:
                if sampel == "Sampel X" and "Tollens" in reagen_pilih:
                    st.success("### 🎉 Hasil: Positif Cermin Perak!")
                    st.write("**Kesimpulan:** Sampel X positif mengandung gugus **Aldehida**.")
                    bg_color, emoji = "#D3D3D3", "🥈"
                elif sampel == "Sampel Y" and "FeCl3" in reagen_pilih:
                    st.success("### 🎉 Hasil: Positif Larutan Ungu Pekat!")
                    st.write("**Kesimpulan:** Sampel Y positif mengandung gugus **Fenol**.")
                    bg_color, emoji = "#8A2BE2", "🔮"
                else:
                    st.error("### ❌ Hasil: Negatif / Tetap Bening")
                    st.write("**Kesimpulan:** Reagen tidak cocok dengan gugus fungsi pada sampel ini.")
                    bg_color, emoji = "#F0F2F6", "💧"
            
            with res_col2:
                st.markdown(f"""
                <div style="text-align: center; background-color: {bg_color}; border: 3px solid #333; padding: 30px; border-radius: 0px 0px 40px 40px; width: 80px; margin: 0 auto;">
                    <h2 style="margin: 0;">{emoji}</h2>
                </div>
                """, unsafe_allow_html=True)
