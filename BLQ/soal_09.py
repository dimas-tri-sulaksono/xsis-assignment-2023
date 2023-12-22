def generate_deret_pola(n):
    deret_pola = [i * n for i in range(1, n + 1)]
    return deret_pola

# Masukkan nilai
n = int(input("Masukkan nilai n: "))
hasil_deret = generate_deret_pola(n)
print(f"Output untuk n = {n}: {hasil_deret}")