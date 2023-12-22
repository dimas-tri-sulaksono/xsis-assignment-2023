def suit_game(jarak_awal, suit_a, suit_b):
    posisi_a = 0
    posisi_b = jarak_awal
    i = 0

    while posisi_a != posisi_b:
        if suit_a[i] == 'G':
            posisi_a += 2
        elif suit_a[i] == 'B':
            posisi_a -= 1

        if suit_b[i] == 'G':
            posisi_b += 2
        elif suit_b[i] == 'B':
            posisi_b -= 1

        i += 1

        if i == len(suit_a) or posisi_a <= 0 or posisi_b <= 0:
            break

    if posisi_a == posisi_b:
        return "Draw"
    elif posisi_a > posisi_b:
        return "A"
    else:
        return "B"

jarak_awal = 2
suit_a = "GGG"
suit_b = "KKB"

hasil_game = suit_game(jarak_awal, suit_a, suit_b)
print(f"Pemenang: {hasil_game}")