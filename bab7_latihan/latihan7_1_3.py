def A_pangkat_N_Positif(A, N):
    hasil = A**N
    print("Hasil dari ", A, " pangkat ", N, " adalah ", hasil)
    return hasil

def A_pangkat_N_Negatif(A, N):
    hasil = A**N
    print("Hasil dari ", A, " pangkat ", N, " adalah ", hasil)
    return hasil

def A_pangkat_N_Nol(A, N):
    hasil = A**N
    print("Hasil dari ", A, " pangkat ", N, " adalah ", hasil)
    return hasil

A = int(input("Masukkan Nilai A : "))
N = int(input("Masukkan Nilai N : "))

if N > 0:
    A_pangkat_N_Positif(A, N)
elif N < 0:
    A_pangkat_N_Negatif(A, N)
else:
    A_pangkat_N_Nol(A, N)

