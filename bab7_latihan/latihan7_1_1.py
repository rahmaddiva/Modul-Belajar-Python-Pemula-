def Operasi_hitung(A,B,C):
    C = A + B
    print()
    print("Hasil Penjumlahan Adalah : ", C)
    C = A - B
    print("Hasil Pengurangan Adalah : ", C)
    C = A * B
    print("Hasil Perkalian Adalah : ", C)
    C = A / B
    print("Hasil Pembagian Adalah : ", C)

A = int(input("Masukkan Bilangan Pertama : "))
B = int(input("Masukkan Bilangan Kedua : "))
C = 0
Operasi_hitung(A,B,C)

