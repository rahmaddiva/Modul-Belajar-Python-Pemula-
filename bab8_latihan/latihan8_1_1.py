def calculate_final_score(tugas, uts, uas):
    return (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)

def main():
    print("Program Nilai Mahasiswa")
    print("#######################")
    
    jumlah_mahasiswa = int(input("Masukkan Jumlah Data Mahasiswa: "))
    
    data_mahasiswa = []
    
    for i in range(jumlah_mahasiswa):
        print("\nENTRY NILAI UJIAN MAHASISWA")
        print("---------------------------")
        
        nama = input("Masukkan Nama: ")
        nilai_tugas = float(input("Masukkan Nilai Tugas: "))
        nilai_uts = float(input("Masukkan Nilai UTS: "))
        nilai_uas = float(input("Masukkan Nilai UAS: "))
        
        nilai_akhir = calculate_final_score(nilai_tugas, nilai_uts, nilai_uas)
        
        data_mahasiswa.append({
            "nama": nama,
            "tugas": nilai_tugas,
            "uts": nilai_uts,
            "uas": nilai_uas,
            "nilai_akhir": nilai_akhir
        })
    
    print("\nLAPORAN UJIAN MAHASISWA")
    print("-----------------------")
    print("No  Nama    Tugas  UTS   UAS   Nilai Akhir")
    
    for i, mahasiswa in enumerate(data_mahasiswa):
        print(f"{i + 1}  {mahasiswa['nama']}    {mahasiswa['tugas']}  {mahasiswa['uts']}  {mahasiswa['uas']}  {mahasiswa['nilai_akhir']:.1f}")

if __name__ == "__main__":
    main()
