print("Program Membalik Kata Dari Belakang")
print("===================================")

kata = input("Tulis kata: ")

balik = ""

for i in kata:
    balik = i + balik

print("Kata yang dibalik: ", balik)