print("Program menghitung Gaji Karyawan PT.Pala Bapak Kau")
print("==================================================")
print("\n")

# input data
nama = input("Masukkan nama anda = ")
nik = input("Masukkan NIK anda = ")
print("Masa Kerja = 1 - 7 tahun")
masa_kerja = int(input("Masukkan masa kerja anda = "))
print("Status Karyawan = 1. Pegawai Tetap, 2. Kontrak")
status = input ("Masukkan status karyawan anda = ")
print("Status Hubungan = 1. Sudah menikah, 2. Belum menikah")
menikah = input("Masukkan status hubungan anda = ")
gaji = int(input("Masukkan gaji pokok = "))
print("\n")

# jika masa kerja > 5 tahun maka mendapat bonus 20% dari gaji pokok
if masa_kerja > 5:
    bonus = 0.2 * gaji
else:
    bonus = 0

# jika status pegawai tetap maka mendapat uang transport sebesar 50000 
if status == "Pegawai tetap":
    uang_transport = 50000
else:
    uang_transport = 0

# jika sudah menikah maka mendapat uang tunjangan sebesar 10% dari gaji pokok
if menikah == "Sudah menikah":
    uang_tunjangan = 0.1 * gaji
else:
    uang_tunjangan = 0

# rincian gaji 
print("Rincian Gaji Anda")
print("====================================")
print("Nama Karyawan = ", nama)
print("NIK Anda = ", nik)
print("Masa Kerja = ", masa_kerja, "tahun")
print("Status Karyawan = ", status)
print("Status Hubungan = ", menikah)
print("Gaji Pokok = Rp.", gaji)
print("Bonus = Rp.", bonus)
print("Uang Transport = Rp.", uang_transport)
print("Uang Tunjangan = Rp.", uang_tunjangan)
print("====================================")
total_gaji = gaji + bonus + uang_transport + uang_tunjangan
print("Total Gaji Bersih = Rp.", total_gaji)
print("====================================")
print("\n")
print("Terima kasih telah menggunakan program ini")
print("Semoga hari anda menyenangkan")

