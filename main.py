import pandas as pd
import streamlit as st 
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import datetime
st.title('Analisis Data Bike Sharing Dataset Menggunakan Python')
df = pd.read_csv("hour.csv")
df['dteday'] = pd.to_datetime(df['dteday'])

tab1, tab2 = st.tabs(["Rental Sepeda", "Analisis Data"])
 
with tab1:
    st.header("Bike Sharing Dataset")
    st.subheader('Data')
    st.dataframe(df.describe())
    st.subheader('Penyewa Sepeda')
    col1, col2 = st.columns(2)
 
    with col1:
        st.header("Tanggal")
        date = st.date_input(label='Tanggal', value=df['dteday'].min().date())
        filtered_data = df[df['dteday'].dt.date==date]
        # Menampilkan total jumlah penyewa pada tanggal tertentu
        total_count = filtered_data['cnt'].sum()
        st.write(f'Jumlah penyewa sepeda pada tanggal {date}: {total_count}')
 
    with col2:
        st.header("Ketentuan Musim")
        st.write('1. Spring = 01/01/2011 - 20/03/2011, 21/12/2011 - 20/03/2012, dan 21/12/2012 - 31/12/2012')
        st.write('2. Summer = 21/03/2011 - 20/06/2011 dan 21/03/12 - 20/06/2012')
        st.write('3. Fall = 21/06/2011 - 22/09/2011 dan 21/06/2012 - 22/09/2012')
        st.write('4. Winter = 23/09/2011 - 20/12/2011 dan 23/09/2012 - 20/12/2012')
with tab2:
    st.header("Analisis Data")
    st.subheader('Outlier')
    plt.figure()
    sns.boxplot(x=df['cnt'])
    plt.title('Jumlah Penyewa Sepeda')
    st.pyplot(plt)  # Menampilkan plot di Streamlit
    # Menampilkan teks
    st.write('Terdapat outlier pada jumlah penyewa sepeda')
    st.subheader('Analisis Data')
    st.write('Setelah dilakukan penghapusan outlier, maka akan dilanjutkan analisis data')
    st.subheader('Perbedaan Jumlah Penyewa Terhadap Keempat Musim')
    musim = ('Spring', 'Summer', 'Fall', 'Winter')
    mean1 = (108.410609, 189.459440, 211.527687, 180.872195)
    fig, ax = plt.subplots()
    ax.plot(musim,mean1,marker='o', linewidth=2,color="#90CAF9")
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=15)
    st.pyplot(fig)
    st.write('Rata - rata penyewa sepeda tertinggi yaitu pada musim fall (musim gugur) dengan rata - rata ≈ 211 penyewa, dan tertinggi kedua adalah musim summer (musim panas) dengan rata - rata ≈ 189 penyewa. Berdasarkan hasil tersebut dapat disimpulkan bahwa rata - rata penyewa sepeda paling banyak pada pertengahan tahun.')
    st.subheader('Perbedaan Jumlah penyewa Terhadap Kondisi Cuaca')
    kondisi_cuaca = ('Cerah', 'Kabut', 'Hujan Ringan', 'Hujan Berat')
    mean2 = (185.314247, 162.626463, 106.050462, 74.333333)
    fig, ax = plt.subplots()
    ax.plot(kondisi_cuaca,mean2,marker='o', linewidth=2,color="#90CAF9")
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=15)
    st.pyplot(fig)
    st.write('Rata-rata penyewa sepeda tertinggi yaitu pada kondisi cuaca cerah dengan rata - rata ≈ 185 penyewa, dan tertinggi kedua kondisi berkabut dengan rata - rata ≈ 163 penyewa. Berdasarkan hasil tersebut dapat disimpulkan bahwa penyewa sepeda saat kondisi cuaca cerah lebih banyak daripada penyewa sepeda saat kondisi cuaca hujan.')
st.caption('Copyright (c) 2023')