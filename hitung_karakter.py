def count_characters(teks):
    jumlah = 0

    for karakter in teks:
        if karakter.islower() or karakter.isdigit():
            jumlah += 1

    return jumlah


teks_contoh = "Latihan BTPN di 2026"
hasil = count_characters(teks_contoh)

print("Teks Asli:", teks_contoh)
print("Karakter yang dihitung: a, t, i, h, a, n, d, i, 2, 0, 2, 6")
print("Jumlah karakter:", hasil)