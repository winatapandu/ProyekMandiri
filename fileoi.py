#Modul fileio: baca / tulis / tambah file.
def buat_file(path):
#Mode 'x': buat file data pertama kali.
#Jika file sudah ada (FileExistsError), data lama dibiarkan aman.
    try:
        with open(path, "x") as f:
            f.write("# keterangan|kategori|jumlah\n")
        return True
    except FileExistsError:
        return False

def tambah_data(path, baris):
#Mode 'a': tambah satu data baru di akhir file.
    with open(path, "a") as f:
        f.write(baris + "\n")

def baca_data(path):
#Mode 'r': baca file baris per baris (iteratif).
    hasil = []
    try:
        with open(path, "r") as f:
            for baris in f:
                if baris.strip() and not baris.startswith("#"):
                    hasil.append(baris.strip())
    except FileNotFoundError:
        print("File data belum ada, silakan tambah data dulu.")
    return hasil

def tulis_laporan(path, teks):
#Mode 'w': tulis laporan (isi lama ditimpa agar selalu terbaru).
    with open(path, "w") as f:
        f.write(teks)
