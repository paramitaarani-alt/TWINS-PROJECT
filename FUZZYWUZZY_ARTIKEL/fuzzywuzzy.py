from PIL import Image
import pytesseract
from rapidfuzz import fuzz, process
import cv2
import os

# Path ke tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
os.environ['TESSDATA_PREFIX'] = r'C:\Program Files\Tesseract-OCR\tessdata'

# Daftar kata kasar (bisa kamu kembangkan sendiri)
kata_kekerasan = [
   "pukul", "bunuh", "tembak", "tendang", "cekik",
    "hajar", "serang", "ancam", "bantai", "tusuk",
    "culik", "keroyok", "gigit", "luka", "berdarah",
    "gasak", "habisi", "bakar", "tindas", "aniaya",
    "sabet", "tikam", "tampar", "tumbuk", "bodoh", "dongo"
    "bajingan", "goblok", "tolol", "babi", "anjing", 
    "anjir", "pecundang", "malas", "perkosa", "cabul", 
    "pelecehan", "sodomi", "sentuh paksa", "tahi", "asu",
    "jancuk", "cok", "bangsat", "monyet", "jing", "cangkeman","babi", 
    "lambe", "kampret", "kontol", "nyocot", "seksual", "sialan", "tampar"
]

# Fungsi pendeteksi fuzzy
def deteksi_unsur_kekerasan(teks):
    teks_kecil = teks.lower().split()
    for kata in teks_kecil:
        if len(kata) <= 2:
            continue  # abaikan kata pendek seperti "am"
        for kata_kasar in kata_kekerasan:
            skor = fuzz.ratio(kata, kata_kasar)
            print(f"{kata} vs {kata_kasar} = {skor}")  # DEBUGGING
            if skor >= 80:
                return True, kata
    return False, None

# Load gambar dan OCR
path_gambar = input("Masukkan path atau nama file gambar (misal: gambar.jpg): ")

# Load gambar dan OCR
img = Image.open(path_gambar)
hasil_ocr = pytesseract.image_to_string(img, lang='ind')
print("Hasil OCR:", hasil_ocr)


# Analisis
mengandung, kata_ditemukan = deteksi_unsur_kekerasan(hasil_ocr)
if mengandung:
    print(f"Mengandung unsur kekerasan! Ditemukan kata: {kata_ditemukan}")
else:
    print("Tidak mengandung unsur kekerasan.")

import requestsfrom bs4 import BeautifulSoup
import string
#Daftar kata terlarang
kata_terlarang = [
   "pukul", "bunuh", "tembak", "tendang", "cekik",
    "hajar", "serang", "ancam", "bantai", "tusuk",
    "culik", "keroyok", "gigit", "luka", "berdarah",
    "gasak", "habisi", "bakar", "tindas", "aniaya",
    "sabet", "tikam", "tampar", "tumbuk", "bodoh", "dongo"
    "bajingan", "goblok", "tolol", "babi", "anjing", 
    "anjir", "pecundang", "malas", "perkosa", "cabul", 
    "pelecehan", "sodomi", "sentuh paksa", "tahi", "asu",
    "jancuk", "cok", "bangsat", "monyet", "jing", "cangkeman","babi", 
    "lambe", "kampret", "kontol", "nyocot", "seksual", "sialan", "tampar"
]

def ambil_teks_dari_url(url):
    try:
        response = request.get(url, timeout=10)
        if response.status_code != 200:
            print("Gagal mengambil halaman. Kode:", response.status_code)
            return "" 
        soup = BeautifulSoup(response.text, "html.parser")
        paragraf = soup.find_all('p')
        return ' '.join([p.get_text() for p in paragraf])
    except Exception as e:
        print("Terjadi kesalahan:", e)
        return ""
    
def bersihkan_teks(teks):
    teks = teks.lower
    for p in string.punctuation:
