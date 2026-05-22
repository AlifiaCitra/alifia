import streamlit as st
import pandas as pd

st.set_page_config(page_title="ChemQual - Katalog Organik", page_icon="🧪", layout="wide")

# 1. TAMBAHKAN KOLOM "Link Foto" PADA DATABASE
# Ganti URL di bawah dengan link foto asli hasil ujimu nanti
data_uji = [
    {
        "Nama Uji": "Uji Tollens",
        "Gugus Fungsi": "Aldehida",
        "Reagen": "AgNO3 + NaOH + NH4OH (Reagen Tollens)",
        "Prosedur Singkat": "Tambahkan sampel ke reagen Tollens, lalu panaskan di penangas air.",
        "Hasil Positif": "Terbentuk lapisan perak mengkilap di dinding tabung reaksi.",
        "Warna/Visual": "🪞 Cermin Perak (Silver Mirror)",
        "Reaksi Kimia": "R-CHO + 2[Ag(NH3)2]+ + 3OH- --> R-COO- + 2Ag (s) + 4NH3 + 2H2O",
        "Link Foto": "https://upload.wikimedia.org/wikipedia/commons/d/df/Tollens_test.jpg" # <-- Contoh link foto dari Wikipedia
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
    }
]

df = pd.DataFrame(data_uji)

st.title("🧪 ChemQual v1.0")
st.subheader("Katalog Uji Kualitatif Senyawa Organik")
st.divider()

tab1, tab2 = st.tabs(["🔍 Pencarian & Filter", "📚 Semua Daftar Uji"])

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
                # Kita bagi halaman menjadi 3 kolom agar ada space buat foto di sebelah kanan
                c1, c2, c3 = st.columns([2, 1, 1.5]) 
                
                with c1:
                    st.markdown(f"**🔬 Reagen:** {row['Reagen']}")
                    st.markdown(f"**📝 Prosedur:** {row['Prosedur Singkat']}")
                    st.markdown(f"**⚗️ Persamaan Reaksi:** `{row['Reaksi Kimia']}`")
                
                with c2:
                    st.info(f"**💡 Hasil:**\n{row['Hasil Positif']}")
                    st.success(f"**👁️ Visual:**\n{row['Warna/Visual']}")
                
                # 2. SEKSI UNTUK MENAMPILKAN FOTO
                with c3:
                    if row["Link Foto"]:
                        st.image(
                            row["Link Foto"], 
                            caption=f"Hasil Positif {row['Nama Uji']}", 
                            use_container_width=True
                        )
                    else:
                        st.write("📷 Foto belum tersedia")

with tab2:
    st.dataframe(df[["Nama Uji", "Gugus Fungsi", "Reagen", "Warna/Visual"]], hide_index=True, use_container_width=True)
