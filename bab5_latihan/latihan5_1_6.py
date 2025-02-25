print("Program Menampilkan Bintang")
print("============================")

bintang = int(input("Masukkan jumlah bintang: "))
print()

for i in range(bintang):
    for j in range(bintang):
        print("*", end="")
    print()

