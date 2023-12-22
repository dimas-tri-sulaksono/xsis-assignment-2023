def find_walk_jump_sequence(track):
    st = 0
    sequence = []

    for i, cell in enumerate(track):
        if cell == 'X':
            # Player must walk to build stamina
            sequence.append('W')
            st += 1
        elif cell == 'O':
            # Player must jump to cross the hole
            if st >= 2:
                sequence.append('J')
                st -= 2
            else:
                return "FAILED"
        elif cell == '_':
            # Player can choose to walk or jump, prefer walking
            if st > 0:
                sequence.append('J')
                st -= 2
            else:
                sequence.append('W')
                st += 1

    return sequence

# Contoh
lintasan_1 = "X_ _ _ _ O _ _ _ Finish"
lintasan_2 = "X O _ _ _ _ O _ _ _ Finish"

hasil_1 = find_walk_jump_sequence(lintasan_1.split())
hasil_2 = find_walk_jump_sequence(lintasan_2.split())

print(f"Lintasan 1: {' '.join(hasil_1)}")
print(f"Lintasan 2: {' '.join(hasil_2)}")
