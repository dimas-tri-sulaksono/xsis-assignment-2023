def generate_deret_pola(deret, n):
    panjang_deret = len(deret)
    if n == 1:
        return deret[1:] + [deret[0]]
    else:
        return deret[n:] + deret[:n]

def input_deret():
    deret_input = input("Masukkan deret angka (pisahkan dengan spasi): ")
    return [int(angka) for angka in deret_input.split()]

# deret_input_user = [3, 9, 0, 7, 1, 2, 4]
deret_input_user = input_deret()

n1 = 3
hasil_deret1 = generate_deret_pola(deret_input_user, n1)
print(f"n = {n1}: {hasil_deret1}")

n2 = 1
hasil_deret2 = generate_deret_pola(deret_input_user, n2)
print(f"n = {n2}: {hasil_deret2}")
