print("Program Kalkulator Sederhana")
print("=============================")
print("\n")
print("Pilih Menu")
print("1 . Penjumlahan")
print("2 . Pengurangan")
print("3 . Perkalian")
print("4 . Pembagian")
print("\n")
pilihan = int(input("Masukkan pilihan anda = "))
print("\n")
bilangan1 = int(input("Masukkan bilangan ke 1 = "))
bilangan2 = int(input("Masukkan bilangan ke 2 = "))

if pilihan == 1:
    print("Hasil penjumlahan adalah", bilangan1 + bilangan2)
elif pilihan == 2:
    print("Hasil pengurangan adalah", bilangan1 - bilangan2)
elif pilihan == 3:
    print("Hasil perkalian adalah", bilangan1 * bilangan2)
elif pilihan == 4:
    print("Hasil pembagian adalah", bilangan1 / bilangan2)
else:
    print("Pilihan tidak ada") 