#Modul processing: perhitungan dan analisis pengeluaran.
from .validasi import validasi_teks, validasi_angka, validasi_baris

class Pengeluaran:
    """Satu catatan pengeluaran."""

    def __init__(self, keterangan, kategori, jumlah):
        self.keterangan = validasi_teks(keterangan, "Keterangan")
        self.kategori = validasi_teks(kategori, "Kategori")
        self.jumlah = validasi_angka(jumlah, "Jumlah")

    def ke_baris(self):
#Ubah objek jadi satu baris teks untuk disimpan ke file.
        return f"{self.keterangan}|{self.kategori}|{self.jumlah}"

    @classmethod
    def dari_baris(cls, baris):
        """Buat objek dari satu baris teks file."""
        return cls(*validasi_baris(baris))

    def __str__(self):
        return f"{self.keterangan} ({self.kategori}): Rp{self.jumlah}"

class Dompet:
#Kumpulan pengeluaran beserta analisisnya.

    def __init__(self):
        self.daftar = []

    def tambah(self, item):
#Tambah pengeluaran ke daftar.
        assert isinstance(item, Pengeluaran), "item harus bertipe Pengeluaran"
        self.daftar.append(item)

    def total(self):
#Hitung total semua pengeluaran.
        return sum(p.jumlah for p in self.daftar)

    def urutkan(self, berdasarkan="jumlah"):
#Urutkan dari terbesar, memakai lambda sebagai key sorted().
        return sorted(self.daftar, key=lambda p: getattr(p, berdasarkan), reverse=True)

    def filter_kategori(self, kategori):
#Ambil pengeluaran pada kategori tertentu (filter + lambda).
        return list(filter(lambda p: p.kategori.lower() == kategori.lower(), self.daftar))

    def per_kategori(self):
#Hitung total pengeluaran untuk tiap kategori.
        hasil = {}
        for p in self.daftar:
            hasil[p.kategori] = hasil.get(p.kategori, 0) + p.jumlah
        return hasil

def hitung_rata_rata(*args):
#Rata-rata dari sejumlah angka (*args).
    return round(sum(args) / len(args)) if args else 0

def buat_record(keterangan, **kwargs):
#Buat Pengeluaran dengan atribut bervariasi (**kwargs); default kategori 'Lainnya'.
    data = {"kategori": "Lainnya", "jumlah": 0}
    data.update(kwargs)
    return Pengeluaran(keterangan, **data)

def buat_laporan(dompet):
#Susun teks laporan pengeluaran.
    rata = hitung_rata_rata(*[p.jumlah for p in dompet.daftar])
    baris = ["=== LAPORAN PENGELUARAN ===",
             f"Total     : Rp{dompet.total()}",
             f"Rata-rata : Rp{rata}", "Per kategori:"]
    for kat, jml in dompet.per_kategori().items():
        baris.append(f"  - {kat}: Rp{jml}")
    return "\n".join(baris) + "\n"

if __name__ == "__main__":
    # Pengujian lokal + library statistics (pengujian global)
    import statistics
    data = [10000, 20000, 30000]
    assert hitung_rata_rata(*data) == round(statistics.mean(data))
    d = Dompet()
    d.tambah(buat_record("Makan siang", kategori="Makanan", jumlah=15000))
    print(buat_laporan(d))
