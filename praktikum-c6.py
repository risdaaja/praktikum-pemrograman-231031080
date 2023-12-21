import os
os.system('cls')


a=True

while a:
    pilih=input('apakah ingin melanjutkan? [y/n]')
    if pilih =='y':
        print('Terimakasih!')
        a=False
    elif pilih== 'n':
        print('Sampai jumpa lagi:)')
        a=False
    else:
        print('jangan aneh deh!:(')