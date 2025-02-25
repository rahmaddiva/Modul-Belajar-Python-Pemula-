hasil = 0

while True:
    print()
    print("Program Perhitungan Menggunakan Perulangan")
    print()
    bil1 = int(input("Masukkan bilangan pertama: "))
    bil2 = int(input("Masukkan bilangan kedua: "))
    
    if bil1 > bil2:
        hasil = bil1 - bil2
    else:
        hasil = bil1 + bil2
    print()
    print("Hasil perhitungan adalah: ", hasil)
    print()
    tanya = input("Apakah anda ingin mengulang lagi? (Y/N): ")
    if tanya == "N":
        break


    
