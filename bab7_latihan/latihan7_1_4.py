def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    return a / b

while True: 
    print()
    print("Program Perhitungan Menggunakan Function")

    bil1 = int(input("Masukkan Bilangan Pertama : "))
    bil2 = int(input("Masukkan Bilangan Kedua : "))
    print()

    print(bil1, "+", bil2, "=", tambah(bil1, bil2))
    print(bil1, "-", bil2, "=", kurang(bil1, bil2))
    print(bil1, "*", bil2, "=", kali(bil1, bil2))
    print(bil1, "/", bil2, "=", bagi(bil1, bil2))
    print()
    ulang = input("Apakah Anda Ingin Mengulang (y/t) : ")
    if ulang == "t":
        break
    else:
        continue
    