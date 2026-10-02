import json
import os
from pathlib import Path
import lmstudio as lms

IMAGE = Path("data/raw/nota-sample.jpeg")

# Ambil nama model dari environment variable
MODEL = os.environ["LM_STUDIO_MODEL"]

# Siapkan gambar
image = lms.prepare_image(str(IMAGE))

# Load model
model = lms.llm(MODEL)

# Buat chat
chat = lms.Chat()

chat.add_user_message(
    "Baca nota pada gambar dan ekstrak informasi berikut:\n"
    "- merchant\n"
    "- tanggal\n"
    "- item\n"
    "- subtotal\n"
    "- pajak\n"
    "- total\n\n"
    "Keluarkan hanya JSON valid tanpa markdown atau teks tambahan.\n"
    "Jika pajak tidak terlihat, isi dengan 0.\n"
    "Jangan mengarang informasi yang tidak terlihat pada nota."
    ,
    images=[image],
)

# Jalankan model
prediction = model.respond(chat)

# Ambil hasil response
content = prediction.content.strip()

print("Raw response:")
print(content)

# Bersihkan markdown ```json ... ```
if content.startswith("```"):
    content = content.replace("```json", "", 1)
    content = content.replace("```", "", 1)
    content = content.strip()

# Konversi response menjadi JSON
try:
    result = json.loads(content)

except json.JSONDecodeError:
    print("\nERROR: Response dari model bukan JSON yang valid.")
    print("Response model:")
    print(content)
    raise

# Pastikan folder reports tersedia
Path("reports").mkdir(parents=True, exist_ok=True)

# Simpan hasil
Path("reports/receipt.json").write_text(
    json.dumps(result, indent=2, ensure_ascii=False),
    encoding="utf-8"
)

# Tampilkan hasil
print("\nHasil ekstraksi:")
print(json.dumps(result, indent=2, ensure_ascii=False))
