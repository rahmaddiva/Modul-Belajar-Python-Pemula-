print("Nilai Harian :")
nilai_harian = int(input())
print("Nilai Tugas :")
nilai_tugas = int(input())
print("Nilai UTS :")
nilai_uts = int(input())
print("Nilai UAS :")
nilai_uas = int(input())

nilai_akhir = (nilai_harian * 0.1) + (nilai_tugas * 0.2) + (nilai_uts * 0.3) + (nilai_uas * 0.4)
print("Nilai akhir anda adalah:", nilai_akhir)

if nilai_akhir >= 80:
    print("Selamat, anda lulus!")
else:
    print("Maaf, anda tidak lulus.")