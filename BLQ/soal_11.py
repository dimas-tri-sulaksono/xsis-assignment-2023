def tampilkan_pattern_karakter(string):
    string = string[::-1]  # Membalikkan string
    for char in string:
        pattern = "***" + char + "***"
        print(pattern.center(3))

input_string = input("Masukkan satu kata: ")
tampilkan_pattern_karakter(input_string)