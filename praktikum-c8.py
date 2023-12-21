import os
import random as rd
os.system ('cls')

warna = ['merah','putih','hitam']
com = rd.choice(warna)
a = True

while a:
    pilih = input('Masukkan Pilihan ['merah'],['putih'],['hitam']: ')
    if pilih == com:
        print(f'Pilihan anda benar yaitu {pilih}')
        a = True
    else:
        print('Tebakan anda salah! coba lagi.')

#Tugas : buat program tebak angka 1 sampi 10 dengan batas kesempatan 3 kali. berikan pesan "kesempatan anda tersisa x kali"