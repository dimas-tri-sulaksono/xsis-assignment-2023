from datetime import datetime, timedelta

def hitung_denda(nama_buku, durasi_peminjaman, tanggal_peminjaman, tanggal_pengembalian):
    # Mendefinisikan tarif denda per hari
    tarif_denda = 100

    # Konversi tanggal peminjaman dan pengembalian menjadi objek datetime
    tanggal_peminjaman = datetime.strptime(tanggal_peminjaman, "%d %B %Y")
    tanggal_pengembalian = datetime.strptime(tanggal_pengembalian, "%d %B %Y")

    # Menghitung selisih hari
    selisih_hari = (tanggal_pengembalian - tanggal_peminjaman).days

    # Mendapatkan durasi peminjaman buku berdasarkan nama buku
    index_buku = ["A", "B", "C", "D"].index(nama_buku)
    durasi_peminjaman_buku = durasi_peminjaman[index_buku]

    # Menghitung denda jika terlambat mengembalikan
    denda = max(0, selisih_hari - durasi_peminjaman_buku) * tarif_denda

    return denda

# Kasus a
nama_buku_a = "A"
durasi_peminjaman_a = [14, 3, 7, 7]
tanggal_peminjaman_a = "28 February 2016"
tanggal_pengembalian_a = "7 March 2016"

denda_a = hitung_denda(nama_buku_a, durasi_peminjaman_a, tanggal_peminjaman_a, tanggal_pengembalian_a)
print(f"Denda untuk buku {nama_buku_a}: {denda_a} IDR")

# Kasus b
nama_buku_b = "B"
durasi_peminjaman_b = [14, 3, 7, 7]
tanggal_peminjaman_b = "29 April 2018"
tanggal_pengembalian_b = "30 May 2018"

denda_b = hitung_denda(nama_buku_b, durasi_peminjaman_b, tanggal_peminjaman_b, tanggal_pengembalian_b)
print(f"Denda untuk buku {nama_buku_b}: {denda_b} IDR")
