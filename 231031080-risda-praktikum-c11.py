import os

os.system("cls")

nilai=5
def hitung_faktorial(nilai):
    #Mencari Faktorial dengan input
     if nilai>2:
        return nilai*hitung_faktorial(nilai-1)
     return 2


#Program Utama mulai di sini
faktorial=hitung_faktorial(nilai)
print(f'Nilai Faktorial dari {nilai}! = {faktorial}')

#Perbaikan
nilai = int(input("Masukkan nilai yang akan dihitung faktorialnya: "))

def hitung_faktorial(nilai):
    #Mencari Faktorial dengan input
    if nilai>1:
        return nilai*hitung_faktorial(nilai-1)
    return 1
faktorial = hitung_faktorial(nilai)
# Cetak hasil
print(f'Nilai Faktorial dari {nilai}! = {faktorial}')