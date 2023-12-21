import os
import random as rd
os.system('cls')

angka = ['1','2','3','4','5','6','7','8','9','10']
com = rd.choice (angka)
limit = 3
i = 0
a= True

while a:
    i += 1
    pilih = input ('Masukkan pilihan [1,2,3,4,5,6,7,8,9,10]:\n')
    if pilih == com:
        print (f'Wahh pilihan kamu benar!! {pilih}')
        a= False
    else:
        if i < limit:
            print ('Owhh tidak tebakan kamu salah. Ayo coba lagiii')
            print (f'Yahh kesempatan kamu tersisa {limit-i} kali:)')
            a=True
        else:
            print ('Maaf kesempatan kamu sudah habis:)')
            a = False