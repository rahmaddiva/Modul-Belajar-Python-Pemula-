print("Program Menentukan Bilangan Terkecil")
print("====================================")
bilangan1 = int(input("masukkan bilangan ke 1 ="))
bilangan2 = int(input("masukkan bilangan ke 2 ="))
bilangan3 = int(input("masukkan bilangan ke 3 ="))

if bilangan1 < bilangan2 and bilangan1 < bilangan3:
    print("Bilangan terkecil adalah", bilangan1)
elif bilangan2 < bilangan1 and bilangan2 < bilangan3:
    print("Bilangan terkecil adalah", bilangan2)
else:
    print("Bilangan terkecil adalah", bilangan3)
