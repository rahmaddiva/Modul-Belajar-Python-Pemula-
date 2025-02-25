import random

print("Program Angka Acak")
print("===============")
b = "N"


while (b == "N"):
    Angka_Acak = random.randrange(1000)  # Assign a random value to "Angka_Acak"
    print("Angka Sekarang : ", Angka_Acak)
    print()
    print("Tekan Y untuk mulai pengacakan")
    print("Tekan N untuk berhenti")

    x = input()

    if x == "N":
        break

    print("Terima kasih telah menggunakan program ini")