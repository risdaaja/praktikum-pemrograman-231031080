import os
os.system('cls')

pwd_benar = 'si23c'
a=True
limit = 3
i=0

while a:
    i+=1
    pwd = input('Masukkan password: ')
    if pwd == pwd_benar:
        print('Selamat anda berhasil logi!')
        a = False
    else:
        if i < limit:
            print('Password salah! coba lagi.')
            a = True
        else:
            print('kesempatan anda habis!')
            a = False