import streamlit as st
import time

st.set_page_config(page_title="Organic Detective Game", page_icon="🕵️‍♂️", layout="centered")

# Menggunakan session_state agar skor dan nyawa tidak reset saat tombol diklik
if "nyawa" not in st.session_state:
    st.session_state.nyawa = 3
if "skor" not in st.session_state:
    st.session_state.skor = 0
if "kasus" not in st.session_state:
    st.session_state.kasus = 1

st.title("🕵️‍♂️ Organic Detective: Misteri Lab Kimia")
st.write("Gunakan keahlian uji kualitatif organikmu untuk menebak senyawa misterius di TKP!")
st.divider()

# TAMPILAN STATUS PEMAIN
col_hp, col_score = st.columns(2)
with col_hp:
    st.metric(label="❤️ Kesempatan (Nyawa)", value="⭐ " * st.session_state.nyawa if st.session_state.nyawa > 0 else "GAME OVER")
with col_score:
    st.metric(label="🏆 Skor Detektif", value=f"{st.session_state.skor} Poin")

st.divider()

if st.session_state.nyawa <= 0:
    st.error("💀 **Game Over!** Kamu terlalu banyak meledakkan tabung reaksi atau salah analisis. Silakan restart aplikasi untuk mencoba lagi.")
    if st.button("🔄 Ulangi Game"):
        st.session_state.nyawa = 3
        st.session_state.skor = 0
        st.session_state.kasus = 1
        st.rerun()
else:
    # CERITA KASUS
    if st.session_state.kasus == 1:
        st.subheader("📁 Kasus 1: Botol Tanpa Label di Pabrik Kosmetik")
        st.write("Detektif, ditemukan cairan jernih berbau menyengat. Kami curiga ini adalah *Formaldehida* (pengawet berbahaya) atau *Aseton* (pelarut). Tugasmu adalah memastikannya!")
        target_sampel = "Formaldehida"
    elif st.session_state.kasus == 2:
        st.subheader("📁 Kasus 2: Limbah Misterius di Sungai")
        st.write("Warga melaporkan air sungai berubah bau menyengat seperti karbol antiseptik. Ambil sampelnya dan uji apakah ini limbah *Fenol* beracun atau hanya alkohol biasa!")
        target_sampel = "Fenol"
    else:
        st.success("🎉 **Selamat!** Semua kasus di laboratorium telah terpecahkan. Kamu adalah Detektif Kimia Organik terbaik!")
        if st.button("🔄 Main Lagi"):
            st.session_state.nyawa = 3
            st.session_state.skor = 0
            st.session_state.kasus = 1
            st.rerun()
        st.stop()

    # MEJA KERJA DETEKTIF
    reagen = st.selectbox(
        "Pilih Reagen Uji dari Tas Detektifmu:",
        ["-- Ambil Reagen --", "Pereaksi Tollens", "Larutan FeCl3 (Besi Klorida)"]
    )
    suhu = st.radio("Atur Pemanasan Alat:", ["Tanpa Pemanasan (25°C)", "Panaskan Kuat (80°C)"], horizontal=True)

    if reagen != "-- Ambil Reagen --":
        if st.button("🧪 Analisis Campuran Zat"):
            with st.spinner("🕵️‍♂️ Melakukan uji laboratorium kualitatif..."):
                time.sleep(1.5)

            # LOGIKA KASUS 1 (Formaldehida)
            if st.session_state.kasus == 1:
                if reagen == "Pereaksi Tollens" and "80°C" in suhu:
                    st.success("🪞 **Luar Biasa!** Terbentuk cermin perak di dinding tabung! Cairan tersebut positif **Formaldehida (Aldehida)**!")
                    st.session_state.skor += 50
                    st.session_state.kasus = 2
                    st.balloons()
                    time.sleep(2)
                    st.rerun()
                else:
                    st.error("❌ **Analisis Gagal / Negatif.** Tidak ada perubahan visual yang berarti atau kondisi suhu salah. Nyawamu berkurang 1!")
                    st.session_state.nyawa -= 1
                    st.rerun()

            # LOGIKA KASUS 2 (Fenol)
            elif st.session_state.kasus == 2:
                if reagen == "Larutan FeCl3 (Besi Klorida)":
                    st.success("🟣 **Tepat Sekali!** Larutan seketika berubah menjadi ungu pekat khas kompleks besi-fenolat! Limbah tersebut positif **Fenol**!")
                    st.session_state.skor += 50
                    st.session_state.kasus = 3
                    st.balloons()
                    time.sleep(2)
                    st.rerun()
                else:
                    st.error("❌ **Salah Analisis!** Reagen tidak bereaksi atau tabung pecah karena pemanasan yang tidak perlu. Nyawamu berkurang 1!")
                    st.session_state.nyawa -= 1
                    st.rerun()
