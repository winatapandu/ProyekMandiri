#Modul testing: pengujian dengan library unittest.
import unittest
from .processing import Pengeluaran, Dompet, hitung_rata_rata, buat_record
from .validasi import DataError

class TestPengeluaran(unittest.TestCase):
    def setUp(self):
        self.d = Dompet()
        self.d.tambah(buat_record("Bakso", kategori="Makanan", jumlah=12000))
        self.d.tambah(buat_record("Bensin", kategori="Transport", jumlah=30000))

    def test_total(self):
        self.assertEqual(self.d.total(), 42000)

    def test_urutkan(self):
        self.assertEqual(self.d.urutkan()[0].keterangan, "Bensin")

    def test_filter_kategori(self):
        self.assertEqual(len(self.d.filter_kategori("makanan")), 1)

    def test_rata_rata(self):
        self.assertEqual(hitung_rata_rata(10, 20, 30), 20)

    def test_jumlah_negatif_ditolak(self):
        with self.assertRaises(DataError):
            Pengeluaran("Test", "Lain", -100)

    def test_baris_bolak_balik(self):
        p = Pengeluaran.dari_baris("Kopi|Minuman|8000")
        self.assertEqual(p.ke_baris(), "Kopi|Minuman|8000")

if __name__ == "__main__":
    unittest.main()
