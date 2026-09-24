"""
Modul ini berisi fungsi dasar untuk menjumlahkan dua nilai.
"""

def hitung_jumlah(nilai_a, nilai_b):
    """
    Menjumlahkan dua angka, mencetak, dan mengembalikan hasilnya.
    """
    hasil = nilai_a + nilai_b
    print(hasil)
    return hasil

if __name__ == "__main__":
    hitung_jumlah(1, 2)
