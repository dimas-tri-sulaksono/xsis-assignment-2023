def hitung_gunung_lembah(urutan):
    jumlah_gunung = 0
    jumlah_lembah = 0

    ketinggian = 0
    sedang_naik = False

    for langkah in urutan:
        if langkah == 'N':
            ketinggian += 1
        elif langkah == 'T':
            ketinggian -= 1

        # Cek jika Hattori sedang di puncak gunung
        if ketinggian == 0 and langkah == 'N':
            jumlah_gunung += 1
        # Cek jika Hattori sedang di dasar lembah
        elif ketinggian == 0 and langkah == 'T':
            jumlah_lembah += 1

    return jumlah_gunung, jumlah_lembah

urutan_langkah = "NNTNNNTTTTNNTTTNTN"
jumlah_gunung, jumlah_lembah = hitung_gunung_lembah(urutan_langkah)

print(f"Jumlah Gunung: {jumlah_gunung}")
print(f"Jumlah Lembah: {jumlah_lembah}")