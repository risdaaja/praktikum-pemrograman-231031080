import os

os.system("cls")


#Fungsi Rekursif factorial dengan perulangan
def faktorial(nilai):
    if nilai<=1:
        return 1
    else:
        return nilai*faktorial(nilai-1)


#Program Utama
for i in range(11):
    print('%2d ! = %d' % (i,faktorial(i)))
print()
 
 #Perbaikan
 # Fungsi Rekursif factorial dengan perulangan
def faktorial(nilai):
    if nilai <=1:
        return 1
    else:
        return nilai*faktorial(nilai-1)

nilai = int(input("masukan nilai:"))

# Program Utama
print(f" Hasil Faktorial dari 0 sampai {nilai}:")
for i in range(nilai + 1):
    print(f"{i}! = {faktorial(i)}")
print()