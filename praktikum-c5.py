import os
os.system('cls')

a=True
limit=5
i=0 

while a:
    i+=1
    print(f'Menjalankan Program {limit+1-i}')
    if i==limit:
        a=False
        print('Program berhenti di sini!')
    else:
        a=True