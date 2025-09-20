import requests
from bs4 import BeautifulSoup
import string

# Daftar kata terlarang
kata_terlarang = [
    "pukul", "bunuh", "tembak", "tendang", "cekik",
    "hajar", "serang", "ancam", "bantai", "tusuk",
    "culik", "keroyok", "gigit", "luka", "berdarah",
    "gasak", "habisi", "bakar", "tindas", "aniaya",
    "sabet", "tikam", "tampar", "tumbuk", "bodoh", "dongo",
    "bajingan", "goblok", "tolol", "babi", "anjing",
    "anjir", "pecundang", "malas", "perkosa", "cabul",
    "pelecehan", "sodomi", "sentuh paksa", "tahi", "asu",
    "jancuk", "cok", "bangsat", "monyet", "jing", "cangkeman",
    "babi", "lambe", "kampret", "kontol", "nyocot", "seksual",
    "sialan", "tampar"
]

def ambil_teks_dari_url(url):
    try:
        response = requests.get(url, timeout=10)
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
    teks = teks.lower()
    for p in string.punctuation:
        teks = teks.replace(p, "")
    return teks

def deteksi_kata_terlarang(teks):
    ditemukan = []
    for kata in kata_terlarang:
        if kata in teks:
            ditemukan.append(kata)
    return ditemukan

def main():
    print("\n--- HASIL ANALISIS ---")
    url = input("Masukkan URL artikel: ")
    teks = ambil_teks_dari_url(url)
    teks_bersih = bersihkan_teks(teks)
    hasil = deteksi_kata_terlarang(teks_bersih)

    if hasil:
        print("Artikel TIDAK AMAN. DITEMUKAN KATA-KATA:", ', '.join(hasil))
    else:
        print("Artikel AMAN. TIDAK DITEMUKAN KATA TERLARANG")

if __name__ == "__main__":
    main()
