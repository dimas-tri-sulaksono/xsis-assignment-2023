from datetime import datetime

def ubah_format_waktu(waktu_input):
    try:
        waktu_12_jam = datetime.strptime(waktu_input, "%I:%M:%S %p")
        waktu_24_jam = waktu_12_jam.strftime("%H:%M:%S")
        return waktu_24_jam
    except ValueError:
        print("Format waktu tidak valid. Pastikan format sesuai dengan 'hh:mm:ss AM/PM'.")
        return None

def input_waktu():
    while True:
        waktu_input = input("Masukkan waktu dalam format 'hh:mm:ss AM/PM': ")
        hasil_ubah = ubah_format_waktu(waktu_input)
        if hasil_ubah:
            return hasil_ubah

# Penggunaan fungsi input_waktu
waktu_24_jam = input_waktu()
print(f"Waktu dalam format 24 jam: {waktu_24_jam}")