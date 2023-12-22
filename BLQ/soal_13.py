# Comment baris ini jika tidak ingin menggunakan input
def hitung_sudut_jarum_jam(jam, menit):

# Uncomment baris ini jika ingin menggunakan input
# def hitung_sudut_jarum_jam():
    try:
        # Uncomment baris jam & menit jika ingin menggunakan input 
        # jam = float(input("Masukkan jam (format 0-12): "))
        # menit = float(input("Masukkan menit (format 0-59): "))

        # Validasi input
        if not (0 <= jam <= 12 and 0 <= menit <= 59):
            return "Input waktu tidak valid."

        # Hitung sudut jarum jam
        sudut_jam = (jam % 12) * 30 + (menit / 60) * 30
        sudut_menit = menit * 6

        sudut_terkecil = abs(sudut_jam - sudut_menit)
        return int(min(sudut_terkecil, 360 - sudut_terkecil))

    except ValueError:
        return "Input tidak valid. Masukkan angka."

# Uncomment dua garis di bawah ini untuk menggunakan input
# sudut = hitung_sudut_jarum_jam()
# print(f"Sudut terkecil yang dibentuk oleh kedua jarum jam: {sudut} derajat")

# Comment baris di bawah jika ingin menggunakan input
print(hitung_sudut_jarum_jam(3, 0))    # Output: 90
print(hitung_sudut_jarum_jam(5, 30))   # Output: 15
print(hitung_sudut_jarum_jam(2, 20))   # Output: 50