def hitung_pembayaran(makanan_harga, pembayaran_alergi):
    total_harga = sum(makanan_harga)
    pajak = 0.10 * total_harga
    service = 0.05 * total_harga
    total_biaya = total_harga + pajak + service

    pembayaran_per_orang = total_biaya / len(makanan_harga)

    # Mengurangkan biaya untuk orang yang membayar lebih murah (alergi ikan)
    pembayaran_per_orang -= pembayaran_alergi

    return pembayaran_per_orang

makanan_harga = [42000, 50000, 30000, 70000, 30000]
pembayaran_alergi = 42000  # Harga makanan yang mengandung ikan

pembayaran_per_orang = int(hitung_pembayaran(makanan_harga, pembayaran_alergi))

print(f"Total biaya yang harus dibayar masing-masing teman: {pembayaran_per_orang}")