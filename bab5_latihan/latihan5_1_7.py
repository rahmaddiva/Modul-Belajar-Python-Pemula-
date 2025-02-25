print("Program Bintang Miring Kanan")
print("================")   

bintang = int(input("Masukkan jumlah bintang: "))
print()

for i in range(bintang):
    for j in range(i):
        print(" ", end="")
    for k in range(bintang):
        print("*", end="")
    print()




