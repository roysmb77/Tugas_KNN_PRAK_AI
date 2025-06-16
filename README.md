# Klasifikasi Bunga Iris menggunakan KNN

Aplikasi web untuk mengklasifikasikan jenis bunga iris menggunakan algoritma K-Nearest Neighbors (KNN).

## Fitur

- Input pengukuran sepal dan petal
- Prediksi jenis bunga iris
- Visualisasi probabilitas prediksi
- Tampilan responsif dan modern

## Teknologi yang Digunakan

- Python 3.9
- Flask
- Scikit-learn
- Plotly
- HTML/CSS

## Cara Menjalankan Lokal

1. Clone repository ini
2. Buat virtual environment:
   ```
   python -m venv .venv
   ```
3. Aktifkan virtual environment:
   - Windows: `.venv\Scripts\activate`
   - Linux/Mac: `source .venv/bin/activate`
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Jalankan aplikasi:
   ```
   python app.py
   ```
6. Buka browser dan akses `http://localhost:5000`

## Deployment

Aplikasi ini dapat di-deploy di Railway dengan mengikuti langkah-langkah berikut:

1. Buat akun di Railway
2. Hubungkan repository GitHub
3. Railway akan otomatis mendeteksi konfigurasi dan melakukan deployment

## Struktur Proyek

```
.
├── app.py              # Aplikasi Flask
├── train_model.py      # Script untuk melatih model
├── requirements.txt    # Dependensi Python
├── Procfile           # Konfigurasi Railway
├── runtime.txt        # Versi Python
├── static/            # File statis (CSS)
├── templates/         # Template HTML
└── model/            # Model yang telah dilatih
``` 