import os
os.system('clear')

nim = ('2','3','1','0','3','1','0','8','0')

print(nim)  

print('item indeks 0 (pertama)',nim[0])
print('item indeks 1 (kedua)',nim[1])

print(f'item indeks 0 (pertama) {nim[0]}')
print(f'item indeks 1 (kedua) {nim[1]}')
print(f'item indeks terakhir {nim[len(nim)-1]}')
print(f'item indeks terakhir {nim[-1]}')
print(f'item indeks (pertama) {nim[-len(nim)]}')

data = ['risda',2023,'Aktif']
nilai= [90,89,93,97]

print('Nama: '+ data[0])
print('angkatan:', data[1])
print('status: '+ data[2])

print(f'{data[0]} ''status kuiah:', data[2])
# >> risda status kuliah: Aktif
print(f'Data terbesar nilai adalah: {max(nilai)}')
# >> Data terbesar nilai adalah: 97
print(f'Data terkecil nilai adalah: {min(nilai)}')
# >> Data terkecil nilai adalah: 80
rataan = sum(nilai)/len(nilai)
print(f'Rata-rata nilai adalah: {rataan}')
# >> Rata-rata nilai adalah: 92.25
print(f'Jumlah nilai {data[0]} adalah: {len(nilai)}')
# >> Jumlah nilai mahasiswa adalah: 4

data = [['Risda',2023,'Aktif'],
        [90,89,93,97],
        [20,22],
        ['S1-Reguler','Ganjil']]

matkul = ['Agama islam',
          'pancasila',
          'wawasan cinta iptek dan imtaq',
          'pengantar teknologi informasi',
          'pengantar program',]
matkul.append('bahasa indonesia')
matkul.append('sains terpadu')
matkul.append('kalkulus dasar')
sks = [2,2,2,3,3]
sks.append('2')
sks.append('3')
sks.append('3')
print(matkul,sks)
print()
# Daftar Mata kuliah
print(f'Mata kuliah 1: {matkul[0]} dengan {sks[0]} sks')
# Mata kuliah 1: Matkul1 dengan jumlah 2 sks
print(f'Mata kuliah 2: {matkul[1]} dengan {sks[1]} sks')
# Mata kuliah 2: Matkul2 dengan jumlah 3 sks
print(f'Mata kuliah 3: {matkul[2]} dengan {sks[2]} sks')
# Mata kuliah 3: Matkul3 dengan jumlah 2 sks
print(f'Mata kuliah 4: {matkul[3]} dengan {sks[3]} sks')
# Mata kuliah 4: Matkul4 dengan jumlah 3 sks
print(f'Mata kuliah 5: {matkul[4]} dengan {sks[4]} sks')
# Mata kuliah 5: Matkul5 dengan jumlah 3 sks
print(f'Mata kuliah 6: {matkul[5]} dengan {sks[5]} sks')
# Mata kuliah 6: Matkul6 dengan jumlah .. sks
print(f'Mata kuliah 7: {matkul[6]} dengan {sks[6]} sks')
# Mata kuliah 7: Matkul7 dengan jumlah .. sks
print(f'Mata kuliah 8: {matkul[7]} dengan {sks[7]} sks')
# Mata kuliah 8: Matkul8 dengan jumlah .. sks
print()
print(data[0][0])
print(data[-1][0])
print(data[2][0:])

print (f"nama mahasiswa: {data[0][0]}")
#Nama mahasiswa: Risda
print (f"Inisial Risda: {data[0][0][0][0][0]}")
#Inisial Risda : R
nim_int = int(''.join(map(str,nim)))
print(f'NIM {data[0][0]}: {nim_int}')
#Nim Risda : 231031080

#Inisial 