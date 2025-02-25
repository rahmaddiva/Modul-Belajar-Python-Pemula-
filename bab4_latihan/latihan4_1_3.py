print("Program Menghitung Luas")
print("=======================")
print("\n")
print("Pilih Menu")
print("1. Menghitung Luas Lingkaran")
print("2. Menghitung Luas Persegi")
print("3. Menghitung Luas Segitiga")
print("\n")
pilihan = int(input("Masukkan Pilihan = "))
print("\n")

match pilihan:
    case 1:
        print("program Lingkaran")
        print("=================")
        jari = float(input("Masukkan Jari-jari = "))
        luas = 3.14 * jari * jari
        print("Luas Lingkaran = ", luas)
    case 2:
        print("Proram Persegi")
        print("===============")
        panjang = int(input("Masukkan Panjang = "))
        lebar = int(input("Masukkan Lebar = "))
        luas = panjang * lebar
        print("Luas Persegi = ", luas)
    case 3:
        print("Program Segitiga")
        print("================")
        alas = int(input("Masukkan Alas = "))
        tinggi = int(input("Masukkan Tinggi = "))
        luas = 0.5 * alas * tinggi
        print("Luas Segitiga = ", luas)
    case _:
        print("Maaf Pilihan tidak ada")
print("\n")