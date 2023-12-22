def lilin_pertama_habis_meleleh(panjang_lilin_awal):
    fibonacci = [1, 1]
    while fibonacci[-1] <= max(panjang_lilin_awal):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    waktu_meleleh = [1] * len(panjang_lilin_awal)

    for i, panjang in enumerate(panjang_lilin_awal):
        waktu = 0
        for fib in reversed(fibonacci):
            while panjang >= fib:
                panjang -= fib
                waktu += 1
        waktu_meleleh[i] = waktu

    return waktu_meleleh.index(min(waktu_meleleh)) + 1

panjang_lilin_awal = [3, 3, 9, 6, 7, 8, 23]
hasil = lilin_pertama_habis_meleleh(panjang_lilin_awal)

print(f"Lilin pertama yang habis meleleh adalah lilin ke-{hasil}")