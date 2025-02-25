print("Program Hitung")
print("==============")
bil1 = int(input("Masukkan bilangan pertama: "))
bil2 = int(input("Masukkan bilangan kedua: "))

hasil = 0 

for i in range(bil1):
    hasil = hasil + bil2
    
    for i in range(bil2):
        print(bil1, "+", end="")    
    print(bil1, "=", hasil)
