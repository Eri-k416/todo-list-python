import streamlit as st
import csv
import os
import pandas as pd

FILE_CSV = "task-data.csv"

st.title("To-do app")
st.text("Aplikasi manajemen tugas ber-deadline",  text_alignment="center")

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

with st.container(border=True):
    st.header("Tugas yang belum selesai")
    if os.path.exists(FILE_CSV):
        with open(FILE_CSV) as f:
            data = list(csv.reader(f))
            for task in data:
                with st.container(border=True):
                    with st.container():
                        st.subheader(task[0])
                        st.text(task[1])
                    isFinished = st.checkbox("")