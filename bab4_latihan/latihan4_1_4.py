print("Program Sederhana Kalkulator")
print("============================")
print("\n")
print("Pilih Menu")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("\n")
pilihan = int(input("Masukkan Pilihan = "))
print("\n")
match pilihan:
    case 1:
        print("Program Penjumlahan")
        print("===================")
        bil1 = int(input("Masukkan Bilangan 1 = "))
        bil2 = int(input("Masukkan Bilangan 2 = "))
        hasil = bil1 + bil2
        print("Hasil Penjumlahan = ", hasil)
    case 2:
        print("Program Pengurangan")
        print("===================")
        bil1 = int(input("Masukkan Bilangan 1 = "))
        bil2 = int(input("Masukkan Bilangan 2 = "))
        hasil = bil1 - bil2
        print("Hasil Pengurangan = ", hasil)
    case 3:
        print("Program Perkalian")
        print("=================")
        bil1 = int(input("Masukkan Bilangan 1 = "))
        bil2 = int(input("Masukkan Bilangan 2 = "))
        hasil = bil1 * bil2
        print("Hasil Perkalian = ", hasil)
    case 4:
        print("Program Pembagian")
        print("=================")
        bil1 = int(input("Masukkan Bilangan 1 = "))
        bil2 = int(input("Masukkan Bilangan 2 = "))
        hasil = bil1 / bil2
        print("Hasil Pembagian = ", hasil)
    case _:
        print("Maaf Pilihan tidak ada")
print("\n")
