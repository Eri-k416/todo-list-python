import streamlit as st
import csv
import os
import pandas as pd

# Fungsi untuk menampilkan tugas saat ini
def tampilkan_tugas_berjalan():

    with open(FILE_CSV, mode="r") as f:
        reader = csv.reader(f)
        data_tugas = list(filter(lambda x: x[2] == "False",list(reader)))

    ada_tugas = False
    
    for index, tugas in enumerate(data_tugas):
        if len(tugas) < 3: 
            continue
            
        nama_tugas = tugas[0]
        deadline = tugas[1]
        status = tugas[2]

        ada_tugas = True
        with st.container(border=True):
            col_teks, col_cek = st.columns([4, 1])
            
            with col_teks:
                st.markdown(f"**{nama_tugas}**")
                st.caption(f"Deadline: {deadline}")
            
            with col_cek:
                st.write("") 
                is_checked = st.checkbox("Selesai", key=f"tugas_{index}")
                
                if is_checked:
                    data_tugas[index][2] = "True"
                    with open(FILE_CSV, mode="w", newline="") as f_write:
                        writer = csv.writer(f_write)
                        writer.writerows(data_tugas)
                    
                    st.rerun()
    if not ada_tugas:
        st.markdown("<p style='text-align: center; color: gray; height: 50px;'>Tidak ada tugas yang belum diselesaikan.</p>", unsafe_allow_html=True)

# Fungsi untuk tampilkan tugas yang sudah selesai 
def tampilkan_tugas_selesai():
    with open(FILE_CSV, mode="r") as f:
        reader = csv.reader(f)
        data_tugas = list(filter(lambda x: x[2] == "True",list(reader)))

    ada_tugas = False
    
    for index, tugas in enumerate(data_tugas):
        if len(tugas) < 3: 
            continue
            
        nama_tugas = tugas[0]
        deadline = tugas[1]
        status = tugas[2]

        ada_tugas = True
        with st.container(border=True):
            col_teks, col_cek = st.columns([4, 1])
            
            with col_teks:
                st.markdown(f"**{nama_tugas}**")
                st.caption(f"Deadline: {deadline}")
            
            with col_cek:
                st.write("") 
                is_checked = st.checkbox("Selesai", key=f"tugas_{index}_selesai", value=True)
                
                if not is_checked:
                    data_tugas[index][2] = "False"
                    with open(FILE_CSV, mode="w", newline="") as f_write:
                        writer = csv.writer(f_write)
                        writer.writerows(data_tugas)
                    
                    st.rerun()
    if not ada_tugas:
        st.markdown("<p style='text-align: center; color: gray; height: 50px;'>Anda belum menyelesaikan tugas apapun.</p>", unsafe_allow_html=True)

    
                        
# Set variabel untuk nama file csv
FILE_CSV = "task-data.csv"

st.title("To-do app")
st.text("Aplikasi manajemen tugas ber-deadline",  text_alignment="center")

# Bagian untuk input
with st.container(border=True):
    st.header("Tambah tugas")
    
    nama_tugas = st.text_input("Nama tugas :")
    deadline = st.date_input("Tenggat tanggal tugas :")

    if st.button("Tambah Tugas ➕"):
        isFinished = False
        with open(FILE_CSV, mode="a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([nama_tugas, deadline, isFinished])
        st.success(f"Tugas \"{nama_tugas}\" sudah di tambahkan.")

# memanggil 2 function
with st.container(border=True):
    st.header("Daftar Tugas")
    tampilkan_tugas_berjalan()

with st.container(border=True):
    st.header("Tugas yang diselesaikan")
    tampilkan_tugas_selesai()

                    