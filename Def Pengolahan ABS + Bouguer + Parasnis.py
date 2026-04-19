import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def hitung_parasnis_abs(nama_file, sheet_name='Sheet2', simpan_csv=False, plot_grafik=False):
    """
    Fungsi untuk mengolah data gayaberat menggunakan metode Parasnis dan ABS.
    
    Parameter:
    - nama_file (str): Path file Excel yang akan dibaca.
    - sheet_name (str): Nama sheet di dalam file Excel.
    - simpan_csv (bool): Jika True, akan menyimpan hasil ke CSV.
    - plot_grafik (bool): Jika True, akan menampilkan visualisasi grafik.
    
    Return:
    - df_clean (DataFrame): Dataframe hasil perhitungan.
    - rho_estimasi (float): Nilai densitas estimasi dari regresi Parasnis.
    """
    
    # 1. Baca Data File 
    try:
        df = pd.read_excel(nama_file, sheet_name=sheet_name)
    except FileNotFoundError:
        print(f"Error: File {nama_file} tidak ditemukan.")
        return None, None

    # Bersihkan data
    df_clean = df.dropna(subset=['FAA', 'Z']).copy()
    df_clean['Z'] = pd.to_numeric(df_clean['Z'], errors='coerce')
    df_clean['FAA'] = pd.to_numeric(df_clean['FAA'], errors='coerce')
    df_clean = df_clean.dropna(subset=['FAA', 'Z'])

    # 2. METODE Parasnis
    df_clean['Sumbu_X'] = 0.04193 * df_clean['Z']
    df_clean['Sumbu_Y'] = df_clean['FAA']

    # Regresi Linear untuk Parasnis
    slope, intercept, r_value, _, _ = linregress(df_clean['Sumbu_X'], df_clean['Sumbu_Y'])
    rho_estimasi = slope 

    # 3. ABS (Anomali Bouguer Sederhana)
    df_clean['Koreksi_Bouguer'] = 0.04193 * rho_estimasi * df_clean['Z']
    df_clean['ABS_mGal'] = df_clean['FAA'] - df_clean['Koreksi_Bouguer']

    # Opsi Simpan ke CSV
    if simpan_csv:
        nama_output = 'Hasil_Parasnis_dan_ABS.csv'
        df_clean[['Titik', 'Z', 'FAA', 'Koreksi_Bouguer', 'ABS_mGal']].to_csv(nama_output, index=False)
        print(f"Data perhitungan telah disimpan di '{nama_output}'")

    # Opsi Visualisasi Grafik
    if plot_grafik:
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

        # GRAFIK 1: Plot Parasnis
        ax1.scatter(df_clean['Sumbu_X'], df_clean['Sumbu_Y'], color='blue', alpha=0.6, label='Data Observasi')
        garis_regresi = intercept + slope * df_clean['Sumbu_X']
        ax1.plot(df_clean['Sumbu_X'], garis_regresi, color='red', linewidth=2, label=f'Regresi ($\\rho$ = {rho_estimasi:.3f} g/cm³)')
        
        ax1.set_title('Grafik Metode Parasnis', fontsize=12)
        ax1.set_xlabel('0.04193 × Elevasi (Z)', fontsize=10)
        ax1.set_ylabel('Free Air Anomaly / FAA (mGal)', fontsize=10)
        ax1.legend()
        ax1.grid(True, linestyle='--', alpha=0.7)

        # GRAFIK 2: Profil ABS
        ax2.plot(df_clean['Titik'], df_clean['ABS_mGal'], marker='o', color='green', markersize=3, linewidth=1)
        ax2.set_title('Profil Anomali Bouguer Sederhana (ABS)', fontsize=12)
        ax2.set_xlabel('Titik (Stasiun)', fontsize=10)
        ax2.set_ylabel('ABS (mGal)', fontsize=10)
        ax2.tick_params(axis='x', rotation=90, labelsize=7)
        ax2.xaxis.set_major_locator(plt.MaxNLocator(20)) 
        ax2.grid(True, linestyle='--', alpha=0.7)

        plt.tight_layout()
        plt.show()

    # Kembalikan nilai ke pemanggil fungsi
    return df_clean, rho_estimasi

# Blok ini hanya dieksekusi jika file ini dijalankan langsung (bukan di-import)
if __name__ == "__main__":
    file_path = r'C:\Users\LOQ\Downloads\Excel Gravv.xlsx'
    data_hasil, densitas = hitung_parasnis_abs(file_path, simpan_csv=True, plot_grafik=True)
    if densitas is not None:
        print(f"Uji coba lokal berhasil. Densitas = {densitas:.3f} g/cm³")