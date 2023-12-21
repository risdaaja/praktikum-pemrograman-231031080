#LATIHAN 3
nama = input("nama karyawan :")
pendapatan = int(input("pendapatn karyawan :"))

#Cetak kembali nama karyawan dengan menggunakan fungsi print
print(f"nama karyawan :", nama)

#Cetak kembali pendapatan karyawan dengan menggunakan fungsi print
print(f"pendapatan karyawan :", pendapatan)

#periksa pendapatan
if pendapatan >1000:
    print("status : Berhak")
else: 
    print("status : Tidak Berhak")