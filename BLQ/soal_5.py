def tampilkan_fibonacci_pertama(n):
    fibonacci = [0, 1]
    while len(fibonacci) < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci[:n]

# Input nilai n
n = int(input("Berapa angka fibonacci yang ingin ditampilkan? "))

# Tampilkan n bilangan Fibonacci pertama
fibonacci_pertama = tampilkan_fibonacci_pertama(n)
print(f"{n} bilangan Fibonacci pertama: {fibonacci_pertama}")