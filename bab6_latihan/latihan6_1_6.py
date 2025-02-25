#program perhitungan pengurangan dua bilangan menggunakan perulangan while, sampai pengurangan hasilnya habis

#membaca dua bilangan
bil1 = int(input("Masukkan bilangan pertama: "))
bil2 = int(input("Masukkan bilangan kedua: "))

#menghitung hasil pengurangan bil1 - bil2 = hasil berulang kali
hasil = 0
while bil1 >= bil2:
    bil1 = bil1 - bil2
    hasil = hasil + 1

#menampilkan hasil
print("Hasil pengurangan: ", hasil)

