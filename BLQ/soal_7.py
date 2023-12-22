from collections import Counter

def hitung_mean(deret_angka):
    return sum(deret_angka) / len(deret_angka)

def hitung_median(deret_angka):
    sorted_deret_angka = sorted(deret_angka)
    n = len(sorted_deret_angka)
    if n % 2 == 0:
        median = (sorted_deret_angka[n//2 - 1] + sorted_deret_angka[n//2]) / 2
    else:
        median = sorted_deret_angka[n//2]
    return median

def hitung_modus(deret_angka):
    counter = Counter(deret_angka)
    max_frequency = max(counter.values())
    modus = [key for key, value in counter.items() if value == max_frequency]
    modus.sort()
    return modus

# Input deret angka dengan pemisah spasi
deret_input = input("Masukkan deret angka (gunakan spasi sebagai pemisah): ")
deret_angka = [int(angka) for angka in deret_input.split()]

mean = hitung_mean(deret_angka)
median = hitung_median(deret_angka)
modus = hitung_modus(deret_angka)

print(f"Deret Angka: {deret_angka}")
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Modus: {modus}")
