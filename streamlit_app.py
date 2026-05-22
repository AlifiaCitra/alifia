import streamlit as st

st.title("🎈 alifia's app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.title("Haii")
st.title("_SEMANGATT_ YAA :blue[SAYANG] :sunglasses:")

**2. app.py**
    Ini adalah jantung aplikasimu. Buka file ini di teks editor (seperti VS Code atau Notepad) lalu *copy-paste* kode awal ini:

    ```python
    import streamlit as st
    import pandas as pd

    # Konfigurasi Halaman
    st.set_page_config(page_title="Katalog Uji Organik", page_icon="🧪")

    # Data Katalog (Bisa kamu tambah sendiri nanti)
    data = {
        "Nama Uji": ["Uji Baeyer", "Uji Tollens", "Uji Fehling", "Uji Ferri Klorida"],
        "Gugus Fungsi Target": ["Alkena / Alkuna", "Aldehida", "Aldehida", "Fenol"],
        "Reagen": ["KMnO4 dingin", "AgNO3 + NH4OH", "CuSO4 + basa + tartrat", "FeCl3 1%"],
        "Hasil Positif (Pengamatan)": ["Warna ungu hilang, endapan coklat", "Terbentuk cermin perak", "Endapan merah bata (Cu2O)", "Warna kompleks ungu/hijau"]
    }

    df = pd.DataFrame(data)

    # Tampilan Judul
    st.title("🧪 Katalog Uji Kualitatif Senyawa Organik")
    st.write("Aplikasi web interaktif untuk panduan identifikasi gugus fungsi senyawa organik di laboratorium.")

    st.divider()

    # Fitur Interaktif: Filter Data
    st.subheader("Cari Uji Berdasarkan Gugus Fungsi")
    gugus_pilihan = st.selectbox("Pilih target gugus fungsi:", ["Semua"] + list(df["Gugus Fungsi Target"].unique()))

    if gugus_pilihan == "Semua":
        st.dataframe(df, hide_index=True, use_container_width=True)
    else:
        hasil_filter = df[df["Gugus Fungsi Target"] == gugus_pilihan]
        st.table(hasil_filter)
