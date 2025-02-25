print("Program Jual Disc")
print("=================")
beli = int(input("Total Pembelian= "))

match beli:
    case beli if 0 <= beli <= 100:disc = 100
    case beli if 1001 <= beli <= 10000:disc = 500
    case beli if 10001 <= beli <= 30000:disc = 2000

    case _:
        print("Maaf Persediaan tidak mencukupi")
print("\n")
print("Jumlah Pembelian = Rp.", beli)
print("Diskon = Rp.", disc)
print("Jumlah yang di bayar : Rp.", beli-disc)
print("=================")