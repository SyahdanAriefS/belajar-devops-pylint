"""
Modul ini memproses data berdasarkan kondisi boolean dan daftar nilai.
"""

X_VALUE = 10

def process_data(val_a, val_b, val_c, list_e, val_f):
    """
    Fungsi kalkulasi sederhana berdasarkan kondisi boolean dan validasi data.
    """
    var_l = 1
    var_o = 0

    if val_a and not val_b and val_c is None:
        try:
            print(val_a + val_b)

            result = list_e[0] + val_f + var_l + var_o
            return result
        except (IndexError, TypeError, ValueError) as error:
            print(f"Terjadi kesalahan komputasi: {error}")
            return None

    return None

if __name__ == "__main__":
    # Karena val_d dihapus, pemanggilan fungsi kini hanya menggunakan 5 argumen
    process_data(True, False, None, [2], 3)
