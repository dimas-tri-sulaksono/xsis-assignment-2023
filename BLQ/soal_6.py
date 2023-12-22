def is_palindrome(kata):
    # Menghapus spasi dan mengubah menjadi huruf kecil
    kata = kata.lower().replace(" ", "")
    
    # Memeriksa apakah kata sama dengan kata yang dibalik
    return kata == kata[::-1]

# Contoh penggunaan:
kata_input = input("Masukkan sebuah kata: ")
if is_palindrome(kata_input):
    print(f"{kata_input} adalah sebuah palindrome.")
else:
    print(f"{kata_input} bukan sebuah palindrome.")