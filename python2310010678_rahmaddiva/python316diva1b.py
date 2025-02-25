print("Program menghitung Gaji Karyawan PT.Pala Bapak Kau")
print("==================================================")
print("\n")

gaji = int(input("Masukkan gaji pokok = "))
print("\n")
print("Masa Kerja = 1 - 5 tahun")
masa_kerja = int(input("Masukkan masa kerja anda = "))
print("\n")
print("Status = 1. Pegawai Tetap, 2. Honorer")
status = int(input("Masukkan status anda = "))
print("\n")
print("1. Sudah menikah, 2. Belum menikah")
menikah = int(input("Masukkan status pernikahan anda = "))
print("\n")

# jika masa kerja > 5 tahun maka mendapat bonus 15% dari gaji pokok
if masa_kerja > 5:
    bonus = 0.15 * gaji
else:
    bonus = 0

# jika status pegawai tetap maka mendapat uang transport sebesar 50000 
if status == 1:
    uang_transport = 50000
else:
    uang_transport = 0

# jika sudah menikah maka mendapat uang tunjangan sebesar 10% dari gaji pokok
if menikah == 1:
    uang_tunjangan = 0.1 * gaji
else:
    uang_tunjangan = 0

# rincian gaji 
print("Rincian Gaji Anda")
print("====================================")
print("Gaji Pokok = Rp.", gaji)
print("Bonus = Rp.", bonus)
print("Uang Transport = Rp.", uang_transport)
print("Uang Tunjangan = Rp.", uang_tunjangan)
print("====================================")
total_gaji = gaji + bonus + uang_transport + uang_tunjangan
print("Total Gaji Anda = Rp.", total_gaji)
print("====================================")
print("\n")
print("Terima kasih telah menggunakan program ini")
print("Semoga hari anda menyenangkan")

