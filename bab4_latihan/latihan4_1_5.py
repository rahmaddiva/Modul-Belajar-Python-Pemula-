print("Program Toko Buah SEGAR MANIS")
print("==============================")
print("\n")
# Setiap Buah yang dijual jika melebihi 5kg akan mendapat diskon kiwi 5%, mangga 2.5%, alpukat 7%, apel 10%
# Untuk kiwi dan mangga jika lebih dari 20kg akan mendapat diskon tambahan 7% dari total harga
print("Pilih Menu")
print("1. Kiwi")
print("2. Mangga")
print("3. Alpukat")
print("4. Apel")
print("\n")

pilihan = int(input("Masukkan Pilihan = "))
print("\n")
berat = float(input("Masukkan Berat (kg) = "))

match pilihan:
    case 1:
        print("Buah Kiwi")
        print("==========")
        harga = 10000
        if berat > 5:
            diskon = harga * 5 / 100
            harga = harga - diskon
        total = harga * berat 
        if berat > 20:
            diskon = harga * 7 / 100
            harga = harga - diskon
        total = harga * berat
        print("Total Harga = ", total)
    case 2:
        print("Buah Mangga")
        print("============")
        harga = 5000
        if berat > 5:
            diskon = harga * 2.5 / 100
            harga = harga - diskon
        total = harga * berat
        if berat > 20:
            diskon = harga * 7 / 100
            harga = harga - diskon
        total = harga * berat
        print("Total Harga = ", total)

    case 3:
        print("Buah Alpukat")
        print("=============")
        harga = 4000
        if berat > 5:
            diskon = harga * 7 / 100
            harga = harga - diskon
        total = harga * berat
        if berat > 10:
            print("Selamat Anda mendapatkan Payung")  
        print("Total Harga = ", total)

    case 4:
        print("Buah Apel")
        print("==========")
        harga = 9000
        if berat > 5:
            diskon = harga * 10 / 100
            harga = harga - diskon
        total = harga * berat
        if berat > 15:
            print("Selamat Anda mendapatkan Tas Jims Honey")
        print("Total Harga = ", total)
        
    case _:
        print("Maaf Pilihan tidak ada")

