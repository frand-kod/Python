async function uploadImage() {
  const fileInput = document.getElementById("fileInput");
  const file = fileInput.files[0];

  if (!file) {
    alert("Pilih gambar dulu!");
    return;
  }

  // --- Kirim ke backend untuk prediksi ---
  const formData = new FormData();
  formData.append("file", file);

  // Optional: tampilkan loading sementara
  const resultDiv = document.getElementById("result");
  resultDiv.innerHTML = `<p>⏳ Sedang memproses...</p>`;

  const res = await fetch("http://127.0.0.1:8000/predict", {
    method: "POST",
    body: formData,
  });

  const data = await res.json();

  // --- Tampilkan hasil prediksi + gambar ---
  const imageURL = URL.createObjectURL(file);
  resultDiv.innerHTML = `
    <h3>Hasil Prediksi:</h3>
    <img src="${imageURL}" alt="Gambar Prediksi" width="300" style="margin-top:10px; border:1px solid #ccc; border-radius:8px;">
    <p><strong>Kelas:</strong> ${data.predicted_class}</p>
    <p><strong>Kepercayaan:</strong> ${data.confidence}%</p>
  `;
}
