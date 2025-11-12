# Tobacco Leaf Disease Classifier

Website ini mendeteksi penyakit daun tembakau menggunakan model **MobileNetV2** dan html css dasar.

---

## Cara Instalasi

### 1. Clone Repo

```bash
git clone <repo-url>
cd ml-webapp
```

### 2. Backend (FastAPI)

```bash
cd backend
pip install -r requirements.txt
uvicorn app:app --reload --port 8000
```

### 3. Frontend

- Buka frontend/index.html di browser

### 4. Cara Menggunakan

- Pilih gambar daun tembakau

- Klik Prediksi

- Hasil prediksi beserta gambar akan muncul.
