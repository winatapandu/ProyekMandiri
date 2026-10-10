#Modul validasi: pengecekan input dan data.
class DataError(Exception):
#Exception buatan sendiri untuk data yang tidak valid.

def validasi_teks(nilai, nama):
#Pastikan teks tidak kosong, jika kosong raise DataError.
    if not nilai or not nilai.strip():
        raise DataError(f"{nama} tidak boleh kosong")
    return nilai.strip()

def validasi_angka(nilai, nama):
#Ubah teks jadi angka. Huruf atau angka negatif ditolak.
    try:
        angka = int(nilai)
    except ValueError:  # input bukan angka
        raise DataError(f"{nama} harus berupa angka") from None
    if angka < 0:
        raise DataError(f"{nama} tidak boleh negatif")
    return angka

def validasi_baris(baris):
#Pecah baris data 'keterangan|kategori|jumlah' dan cek jumlah field-nya.
    bagian = baris.strip().split("|")
    if len(bagian) != 3:
        raise DataError("format baris salah, harus 3 field")
    return bagian

if __name__ == "__main__":
    # Pengujian lokal
    print(validasi_angka("5000", "jumlah"))
    try:
        validasi_angka("abc", "jumlah")
    except DataError as e:
        print("Error tertangkap:", e)
