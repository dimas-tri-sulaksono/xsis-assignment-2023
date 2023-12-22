def nilai_minimal_maksimal_deret(deret_angka):
    if len(deret_angka) < 4:
        return None  # Deret harus memiliki setidaknya 4 komponen untuk dijumlahkan

    deret_angka.sort()  # Mengurutkan deret angka

    minimal = float('inf')  # Inisialisasi dengan nilai tak terhingga
    maksimal = float('-inf')  # Inisialisasi dengan nilai tak terhingga negatif

    for i in range(len(deret_angka) - 3):
        jumlah = deret_angka[i] + deret_angka[i+1] + deret_angka[i+2] + deret_angka[i+3]
        minimal = min(minimal, jumlah)
        maksimal = max(maksimal, jumlah)

    return minimal, maksimal

# Contoh penggunaan:
deret_angka_input = input("Masukkan deret angka (gunakan spasi sebagai pemisah): ")
deret_angka = [int(angka) for angka in deret_angka_input.split()]

hasil_minimal, hasil_maksimal = nilai_minimal_maksimal_deret(deret_angka)

if hasil_minimal is not None:
    print(f"Deret Angka (Setelah Diurutkan): {deret_angka}")
    print(f"Nilai Minimal dari Penjumlahan 4 Komponen: {hasil_minimal}")
    print(f"Nilai Maksimal dari Penjumlahan 4 Komponen: {hasil_maksimal}")
else:
    print("Deret harus memiliki setidaknya 4 komponen untuk dijumlahkan.")