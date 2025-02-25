print("Program Menghitung Jumlah & Rata Rata sejumlah data nilai cacah data tidak diketahui dengan pasti pembacaan data dihentikan dengan data sentinel, data sentinel berupa sembarang bilangan negatif")

#inisialisasi variabel  
jumlah = 0
banyak = 0
nilai = 0
#pembacaan nilai
nilai = int(input("Masukkan nilai: "))

#perulangan pembacaan nilai
while nilai >= 0:
    jumlah = jumlah + nilai
    banyak = banyak + 1
    nilai = int(input("Masukkan nilai: "))
#perhitungan rata-rata
if banyak != 0:
    rata = jumlah / banyak
    print("Jumlah Data: ", jumlah)
    print("Nilai Rata-rata: ", rata)
else:
    print("Tidak ada data yang dimasukkan")

#output
print("Selesai")