# Pastikan nama variabelnya sama persis: search_gugus dan search_name
filtered_df = df.copy()

if search_gugus != "Semua Gugus":
    filtered_df = filtered_df[filtered_df["Gugus Fungsi"] == search_gugus]

# Menggunakan 'search_name' yang sudah didefinisikan di col2 tadi
if search_name:
    filtered_df = filtered_df[
        filtered_df["Nama Uji"].str.contains(search_name, case=False) | 
        filtered_df["Reagen"].str.contains(search_name, case=False)
    ]

# Menampilkan Hasil Filter dalam bentuk Card yang rapi
if filtered_df.empty:
    st.warning("Uji kualitatif tidak ditemukan. Coba kata kunci lain!")
else:
    for index, row in filtered_df.iterrows():
        with st.expander(f"🔹 {row['Nama Uji']} — Target: {row['Gugus Fungsi']}", expanded=True):
            c1, c2 = st.columns([2, 1])
            with c1:
                st.markdown(f"**🔬 Reagen:** {row['Reagen']}")
                st.markdown(f"**📝 Prosedur:** {row['Prosedur Singkat']}")
                st.markdown(f"**⚗️ Persamaan Reaksi:** `{row['Reaksi Kimia']}`")
            with c2:
                st.info(f"**💡 Hasil Positif:**\n{row['Hasil Positif']}")
                st.success(f"**👁️ Pengamatan Visual:**\n{row['Warna/Visual']}")
            
