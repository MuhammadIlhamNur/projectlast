import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pickle

def load_data_raw():
    data = pd.read_csv('https://github.com/MuhammadIlhamNur/DM_C2/blob/main/Data_Cleaning.csv')
    return data

def main():

    def load_data(url):
        return pd.read_csv(url)

    params = st.experimental_get_query_params()
    page = params.get("page", "home")

    st.sidebar.title("Navigasi")
    pages = {
        "Beranda": "home",
        "Analisis Data Eksploratif (EDA)": "eda",
        "Model Kepuasan Penumpang": "satisfaction_modeling"
    }
    selection = st.sidebar.radio("Pergi ke", list(pages.keys()))

    if selection == "Beranda":
        page = "home"
    elif selection == "Analisis Data Eksploratif (EDA)":
        page = "eda"
    elif selection == "Model Kepuasan Penumpang":
        page = "satisfaction_modeling"

    if page == "home":
        st.title('Analisis Kepuasan Penumpang Maskapai - Halaman Beranda')

        st.title('Analisis Kepuasan Penumpang Maskapai')

        st.header('Tujuan Bisnis')
        st.markdown("""
        - Meningkatkan kepuasan penumpang untuk meningkatkan loyalitas dan citra maskapai.
        - Mengidentifikasi area yang perlu perbaikan untuk meningkatkan kualitas layanan.
        - Memahami faktor-faktor yang mempengaruhi kepuasan penumpang.
        - Meningkatkan pangsa pasar dan reputasi maskapai.
        """)

        st.header('Evaluasi Situasi')
        st.subheader('Persaingan')
        st.write('Bagaimana performa maskapai dibandingkan dengan maskapai lain di industri?')
        st.subheader('Kekuatan dan Kelemahan')
        st.write('Apa saja aspek yang menjadi kekuatan dan kelemahan maskapai dalam hal kepuasan penumpang?')
        st.subheader('Peluang')
        st.write('Apa saja peluang yang bisa dimanfaatkan untuk meningkatkan kepuasan penumpang?')
        st.subheader('Ancaman')
        st.write('Apa saja ancaman yang bisa mengganggu kepuasan penumpang?')

        st.header('Tujuan Data Mining')
        st.markdown("""
        - Mengidentifikasi pola dan tren dalam umpan balik dan data penumpang.
        - Memprediksi tingkat kepuasan penumpang berdasarkan berbagai faktor.
        - Membangun model untuk merekomendasikan perbaikan layanan.
        """)

        st.header('Rencana Proyek')
        st.markdown("""
        - Rencana Awal: Memahami tujuan bisnis dan kebutuhan pengguna.
        - Identifikasi sumber data dan kumpulkan umpan balik pelanggan.
        """)

    elif page == "eda":
        st.title('Analisis Data Eksploratif (EDA) untuk Kepuasan Penumpang Maskapai')

        # Load data
        data = load_data_raw()

        # Tampilkan info dataset
        st.subheader('Informasi Dataset')
        st.write(data.info())

        # Tampilkan statistik deskriptif
        st.subheader('Statistik Deskriptif')
        st.write(data.describe())

        # Visualisasi Data
        st.subheader('Visualisasi Data')

        # Heatmap Korelasi
        numeric_cols = data.select_dtypes(include=['float64', 'int64'])
        st.subheader('Korelasi antar Fitur')
        plt.figure(figsize=(10, 6))
        sns.heatmap(numeric_cols.corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths=2)
        st.pyplot(plt)

    elif page == "satisfaction_modeling":
        st.title('Model Kepuasan Penumpang')

        st.title('Data Kepuasan Penumpang Maskapai')
        st.write('Berikut adalah beberapa baris pertama dari dataset kepuasan penumpang maskapai:')
        st.write(load_data_raw().head())

        # Statistik Deskriptif
        st.write('Statistik Deskriptif:')
        st.write(load_data_raw().describe())

        # Input nilai fitur untuk prediksi kepuasan
        st.title('Prediksi Kepuasan Penumpang')
        st.write('Selamat datang di Prediksi Kepuasan Penumpang.')

        Jarak_Penerbangan = st.text_input('Jarak Penerbangan')
        Layanan_Wifi_Penerbangan = st.text_input('Layanan Wifi Penerbangan')
        Kemudahan_Pemesanan_Online = st.text_input('Kemudahan Pemesanan Online')
        Check_in_Online = st.text_input('Check-in Online')
        Kenyamanan_Kursi = st.text_input('Kenyamanan Kursi')

        if st.button('Prediksi Kepuasan Penumpang'):
            # Periksa apakah semua nilai input diisi
            if all([Jarak_Penerbangan, Layanan_Wifi_Penerbangan, Kemudahan_Pemesanan_Online, Check_in_Online, Kenyamanan_Kursi]):
                # Contoh model prediksi kepuasan
                # Untuk tujuan demonstrasi, mari kita buat model prediksi kepuasan yang sederhana berdasarkan kondisi tertentu
                if int(Jarak_Penerbangan) > 500 and int(Check_in_Online) > 3:
                    hasil_prediksi_kepuasan = "Puas"
                else:
                    hasil_prediksi_kepuasan = "Tidak Puas"

                # Tampilkan hasil prediksi
                st.write(f'Prediksi Kepuasan Penumpang: {hasil_prediksi_kepuasan}')
            else:
                st.error("Harap isi semua nilai input sebelum melakukan prediksi.")

if __name__ == "__main__":
    main()
