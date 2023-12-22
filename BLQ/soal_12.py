def bubble_sort(deret_angka):
    n = len(deret_angka)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if deret_angka[j] > deret_angka[j + 1]:
                deret_angka[j], deret_angka[j + 1] = deret_angka[j + 1], deret_angka[j]

def input_deret():
    deret_input = input("Masukkan deret angka (pisahkan dengan spasi): ")
    return [int(angka) for angka in deret_input.split()]

def tampilkan_deret(deret):
    print("Output:", end=" ")
    for angka in deret:
        print(angka, end=" ")

deret_input_user = input_deret()

# Menggunakan Bubble Sort
bubble_sort(deret_input_user)

# Menampilkan deret yang telah diurutkan
tampilkan_deret(deret_input_user)