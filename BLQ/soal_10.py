def tampilkan_pattern_karakter(nama):
    nama_split = nama.split()
    hasil_output = ""
    for kata in nama_split:
        pattern = kata[0] + "***" + kata[-1]
        hasil_output += pattern + " "
    return hasil_output.rstrip()

input_nama = input("Masukkan nama: ")
hasil_output = tampilkan_pattern_karakter(input_nama)
print("Output:", hasil_output)