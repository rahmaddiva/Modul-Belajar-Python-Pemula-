print("Program Menetukan Bilangan yang Terbesar")
print("========================================")

a = int(input("masukkan bilangan pertama:"))
b = int(input("masukkan bilangan kedua:"))
c = int (input("masukkan bilangan ketiga:"))

print('\n')

if(a > b ) and (a > c):
    print("Bilangan ke 1 Paling Besar")
elif(b > a) and (b > c):
    print("Bilangan ke 2 Paling Besar")
elif(c > a) and (c > b):
    print("Bilangan ke 3 Paling Besar")
else:
    print("ada dua atau tiga masukan memiliki nilai yang sama besar")