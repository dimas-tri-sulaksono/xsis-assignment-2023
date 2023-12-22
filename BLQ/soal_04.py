def cek_prima(angka):
    if angka < 2:
        return False
    for i in range(2, int(angka**0.5) + 1):
        if angka % i == 0:
            return False
    return True

def tampilkan_prima_pertama(n):
    bilangan_prima = []
    angka = 2
    while len(bilangan_prima) < n:
        if cek_prima(angka):
            bilangan_prima.append(angka)
        angka += 1
    return bilangan_prima

# Input nilai n
n = int(input("Masukkan nilai: "))

# Tampilkan n bilangan prima pertama
prima_pertama = tampilkan_prima_pertama(n)
print(f"{n} bilangan prima pertama: {prima_pertama}")