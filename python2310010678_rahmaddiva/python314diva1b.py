print("Program menghitung luas")
print("========================")
print("\n")
print("pilih Menu")
print("1 . Luas Lingkaran")
print("2 . Luas Persegi")
print("3 . Luas Segitiga")
print("\n")
pilihan = int(input("Masukkan pilihan anda = "))
print("\n")

if pilihan == 1:
    print("program lingkaran")
    print("=================")
    jari = int(input("Masukkan jari-jari = "))
    luas = 3.14 * jari * jari
    print("Luas lingkaran adalah", luas)
elif pilihan == 2:
    print("program persegi")
    print("================")
    panjang = int(input("Masukkan panjang = "))
    lebar = int(input("Masukkan lebar = "))
    luas = panjang * lebar
    print("Luas persegi adalah", luas)
elif pilihan == 3:
    print("program segitiga")
    print("=================")
    alas = int(input("Masukkan alas = "))
    tinggi = int(input("Masukkan tinggi = "))
    luas = 0.5 * alas * tinggi
    print("Luas segitiga adalah", luas)
else:
    print("Pilihan tidak ada")