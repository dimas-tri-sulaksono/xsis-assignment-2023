from datetime import datetime

def hitung_tarif_parkir(masuk, keluar):
    # Mengubah string tanggal dan waktu menjadi objek datetime
    masuk_waktu = datetime.strptime(masuk, "%d %b %Y | %H:%M:%S")
    keluar_waktu = datetime.strptime(keluar, "%d %b %Y | %H:%M:%S")

    # Menghitung selisih waktu dalam jam
    selisih_waktu = keluar_waktu - masuk_waktu
    selisih_jam = selisih_waktu.total_seconds() / 3600

    # Ketentuan tarif parkir
    tarif_per_jam = 1000
    tarif_8_jam_pertama = 8 * tarif_per_jam
    tarif_24_jam_8_jam_berikutnya = 15000

    # Menghitung tarif parkir berdasarkan ketentuan
    if selisih_jam <= 8:
        tarif = int(selisih_jam * tarif_per_jam)

        # Jika selisih waktu kurang dari 1 jam
        if tarif < 1000: tarif = 1000
    
    elif 8 < selisih_jam <= 24:
        tarif = tarif_8_jam_pertama

    elif (selisih_jam % 24) <= 8:
        if (selisih_jam % 24) < 1:
            tarif = int(tarif_24_jam_8_jam_berikutnya * (selisih_jam // 24) + tarif_per_jam)    
        else:
            tarif = int(tarif_24_jam_8_jam_berikutnya * (selisih_jam // 24) + (selisih_jam % 24) * tarif_per_jam)    

    elif 8 < (selisih_jam % 24) <= 24:
        tarif = int(tarif_24_jam_8_jam_berikutnya * (selisih_jam // 24) + tarif_8_jam_pertama)
    
    return tarif, selisih_waktu

# Contoh:
masuk_parkir = "27 Jan 2019 | 00:00:00"
keluar_parkir = "28 Jan 2019 | 06:00:00"

tarif, selisih_waktu = hitung_tarif_parkir(masuk_parkir, keluar_parkir)
print(f"Selisih waktu: {selisih_waktu}")
print(f"Tarif parkir: {tarif} IDR")