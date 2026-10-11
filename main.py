#File utama: program Pencatat Pengeluaran Harian
from PencatatanKeuanganPribadi import fileio, processing
from PencatatanKeuanganPribadi.validasi import DataError

FILE_DATA = "data/pengeluaran.txt"
FILE_LAPORAN = "data/laporan.txt"

def muat_data():
#Baca file ke objek Dompet. Baris rusak dilewati, program tidak berhenti.
    dompet = processing.Dompet()
    for baris in fileio.baca_data(FILE_DATA):
        try:
            dompet.tambah(processing.Pengeluaran.dari_baris(baris))
        except DataError as err:
            print(f"  [!] Baris dilewati: {err}")
    return dompet

def tambah_pengeluaran():
#Input data baru, validasi, lalu menyimpan ke file.
    try:
        item = processing.Pengeluaran(
            keterangan=input("Keterangan: "),   # keyword argument
            kategori=input("Kategori  : "),
            jumlah=input("Jumlah (Rp): "))
    except DataError as err:
        print(f"  [!] Gagal: {err}")
        return
    fileio.tambah_data(FILE_DATA, item.ke_baris())
    print("  Tersimpan.")

def main():
#Menu utama.
    import os
    os.makedirs("data", exist_ok=True)
    fileio.buat_file(FILE_DATA)
    while True:
        print("\n1.Tambah 2.Tampilkan 3.Urutkan 4.Laporan 0.Keluar")
        pilihan = input("Pilih: ").strip()
        if pilihan == "1":
            tambah_pengeluaran()
        elif pilihan == "2":
            for p in muat_data().daftar:
                print(" ", p)
        elif pilihan == "3":
            for p in muat_data().urutkan(berdasarkan="jumlah"):
                print(" ", p)
        elif pilihan == "4":
            teks = processing.buat_laporan(muat_data())
            print(teks)
            fileio.tulis_laporan(FILE_LAPORAN, teks)
        elif pilihan == "0":
            print("Keluar")
            break
        else:
            print("  Pilihan tidak valid.")

if __name__ == "__main__":
    main()
