def max_items_dibeli(uang, daftar_barang):
    dp = [0] * (uang + 1)

    for barang in daftar_barang:
        for harga in barang['harga']:
            for uang_sisa in range(uang, harga - 1, -1):
                dp[uang_sisa] = max(dp[uang_sisa], dp[uang_sisa - harga] + 1)

    max_items = dp[uang]
    return max_items

# Contoh:
# uang_andi = 1000

uang_andi = int(input("Masukkan jumlah uang Andi: "))

daftar_barang_andi = [
    {'nama': 'Kaca_mata', 'harga': [500, 600, 700, 800]},
    {'nama': 'Baju', 'harga': [200, 400, 350]},
    {'nama': 'Sepatu', 'harga': [400, 350, 200, 300]},
    {'nama': 'Buku', 'harga': [100, 50, 150]}
]

jumlah_item = max_items_dibeli(uang_andi, daftar_barang_andi)
print(f"Jumlah uang yang dipakai: {uang_andi}")
print(f"Jumlah item yang bisa dibeli: {jumlah_item}")
