def is_pangram(kalimat):
    abjad = set("abcdefghijklmnopqrstuvwxyz")
    kalimat_lower = kalimat.lower()

    for huruf in abjad:
        if huruf not in kalimat_lower:
            return False

    return True

# Contoh kasus:
kalimat1 = "Sphinx of black quartz, judge my vow"
kalimat2 = "Brawny gods just flocked up to quiz and vex him"
kalimat3 = "Check back tomorrow; I will see if the book has arrived."

print(f'"{kalimat1}" adalah pangram: {is_pangram(kalimat1)}')
print(f'"{kalimat2}" adalah pangram: {is_pangram(kalimat2)}')
print(f'"{kalimat3}" adalah pangram: {is_pangram(kalimat3)}')
