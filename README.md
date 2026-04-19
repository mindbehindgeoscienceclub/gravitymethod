1. Variabel File & Modul (Library)
- nama_file: Berisi string berupa path (lokasi) file Excel (Excel Gravv.xlsx) yang akan dibaca oleh program.
- pd, np, plt, linregress: Ini adalah variabel alias atau fungsi dari library Python yang diimpor (pandas, numpy, matplotlib.pyplot, dan fungsi dari scipy.stats).
Catatan: np diimpor tetapi tidak digunakan dalam script ini.

2. Variabel Data (DataFrame)
- df: Variabel pandas DataFrame yang menyimpan data mentah persis seperti yang dibaca dari Sheet2 pada file Excel.
- df_clean: DataFrame yang sudah dibersihkan. Variabel ini menyimpan data di mana baris yang memiliki nilai kosong (NaN) pada kolom 'FAA' dan 'Z' sudah dihapus, serta memastikan datanya bertipe numerik.

3. Variabel Kolom Data (Di dalam df_clean)
Variabel-variabel ini adalah nama kolom (Series) di dalam DataFrame yang diolah sepanjang script:
- Z: Elevasi atau ketinggian stasiun pengukuran.
- FAA: Nilai Free Air Anomaly (Anomali Udara Bebas).
- Titik: Nomor atau ID stasiun pengukuran (digunakan pada saat menyimpan ke CSV dan plot grafik).
- Sumbu_X: Variabel sumbu X untuk plot Parasnis. Dihitung dari pengali elevasi (0.04193 * Z).
- Sumbu_Y: Variabel sumbu Y untuk plot Parasnis, yang nilainya sama dengan FAA.
- Koreksi_Bouguer: Nilai koreksi Bouguer hasil perhitungan (0.04193 * rho_estimasi * Z).
- ABS_mGal: Nilai Anomali Bouguer Sederhana (ABS), dihitung dari selisih FAA dikurangi Koreksi_Bouguer.

4. Variabel Regresi & Perhitungan (Metode Parasnis)
Fungsi linregress mengeluarkan 5 output sekaligus (tuple) yang ditampung dalam variabel berikut:
- slope: Nilai kemiringan (gradien) dari garis regresi. Dalam metode Parasnis, nilai ini merepresentasikan densitas batuan rata-rata.
- intercept: Titik potong garis regresi pada sumbu Y (konstanta).
- r_value: Koefisien korelasi. Di kode ini dikuadratkan (r_value**2) untuk mendapatkan nilai R-squared (koefisien determinasi) yang menunjukkan seberapa presisi regresi tersebut.
- p_value: Nilai probabilitas signifikansi regresi (dihitung oleh fungsi, tetapi tidak dicetak/digunakan lebih lanjut).
- std_err: Standar error dari estimasi gradien (dihitung oleh fungsi, tetapi tidak dicetak/digunakan lebih lanjut).
- rho_estimasi: Variabel turunan yang mengambil nilai dari slope untuk digunakan secara eksplisit sebagai nilai densitas ($\rho$).
- garis_regresi: Array yang berisi nilai-nilai prediksi Y (berdasarkan rumus persamaan garis lurus Y = a + bX) untuk menggambarkan garis regresi linear berwarna merah pada grafik Parasnis.

5. Variabel Visualisasi (Matplotlib)
- fig: Objek figure utama (kanvas dasar) tempat grafik akan digambar.
- ax1: Objek axes (sumbu) pertama yang menampung "Grafik 1", yaitu scatter plot untuk regresi Metode Parasnis.
- ax2: Objek axes (sumbu) kedua yang menampung "Grafik 2", yaitu line plot untuk melihat profil persebaran Anomali Bouguer Sederhana (ABS) di setiap titik.

6. Define (def)
- def hitung_parasnis_abs(nama_file) : Def disini sebagai tombol pembuat mesin pengolah, dan "hitung_parasnis_abs sebagai bahan data untuk diolah dan kemudian kode-kode di baris bawahnya yang menjorok kedalam berfungsi sebagai proses kerja yang akan berlangsung.
- return : Setelah pengolahan selesai, return berfungsi untuk mengeluarkan hasilnya (berupa tabel data bersih format .CSV dan nilai densitas).
