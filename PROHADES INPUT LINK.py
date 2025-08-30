import pytesseract
from PIL import Image
import os
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
kata_kekerasan = {
    "pukul", "bunuh", "tembak", "tendang", "cekik",
    "hajar", "serang", "ancam", "bantai", "tusuk",
    "culik", "keroyok", "gigit", "luka", "berdarah",
    "gasak", "habisi", "bakar", "tindas", "aniaya",
    "sabet", "tikam", "tampar", "tumbuk", "bodoh", "dongo"
    "bajingan", "goblok", "tolol", "babi", "anjing", 
    "anjir", "pecundang", "malas", "perkosa", "cabul", 
    "pelecehan", "sodomi", "sentuh paksa", "tahi", "asu"
    "jancuk", "cok", "bangsat", "monyet", "jing", "cangkeman","babibabi", 
    "lambemu"
}

def deteksi_dari_gambar(path_gambar):
    try:
        gambar = Image.open(path_gambar)

        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        teks = pytesseract.image_to_string(gambar, lang='ind')

        print("=== Hasil OCR ===")
        print(teks)
        
        kata_input = teks.lower().split()
        hasil = []

        for kata in kata_input:
            kata_bersih = ''.join(char for char in kata if char.isalnum())
            if kata_bersih in kata_kekerasan:
                hasil.append(kata_bersih)

        return hasil

    except Exception as e:
        print("Terjadi kesalahan:", e)
        return []

if __name__ == "__main__":
    print("=== Deteksi Kekerasan dari Gambar ===")
    path_gambar = input("Masukkan path ke file gambar: ")
    
    if not os.path.exists(path_gambar):
        print("❌ File gambar tidak ditemukan.")
    else:
        hasil = deteksi_dari_gambar(path_gambar)
        if hasil:
            print("\n⚠️ Terdapat unsur kekerasan pada kata-kata berikut:")
            for kata in hasil:
                print(f"- {kata}")
        else:
            print("\n✅ Tidak ditemukan unsur kekerasan.")