| No | Sebelum | Sesudah | Teknik | Alasan |
|----|---------|---------|--------|--------|
| 1 | Variabel `p`, `d`, `h` tanpa makna di `per_kategori()` | `hasil`, `kategori`, `jumlah` | Rename variable | Nama jelas, mudah dibaca |
| 2 | Cek teks kosong/angka ditulis berulang tiap field | Fungsi `validasi_teks()` dan `validasi_angka()` | Extract function | Logika validasi di satu tempat |
| 3 | Kode ubah baris<->objek ditulis di banyak tempat | `Pengeluaran.ke_baris()` dan `dari_baris()` | Remove duplicate code | Format data diatur satu sumber |
| 4 | Input data langsung di dalam `main()` | Fungsi `tambah_pengeluaran()` | Extract function | `main()` lebih pendek |
