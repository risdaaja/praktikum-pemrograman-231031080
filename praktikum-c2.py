print("Nama : Risda")
print("Nim : 231031080")
print("Prodi : sistem informasi")
print("Tanggal lahir : 20-10-2005")

#Operasi aritmatika
a=0
print ("Nilai a =",a)
a=80
a+=1
print ("Nilai a+=1 akan menjadi",a)
a=80
a-=1
print ("Nilai a-=1 akan menjadi",a)
a=80
a*=2
print ("Nilai a*=2 akan menjadi",a)
a=80
a/2
print ("Nilai a/=2 akan menjadi",a)
a=80
a%=2
print ("Nilai a%=2 akan menjadi",a)
a=80
a//=2
print ("Nilai a//=2 akan menjadi",a)
a=80
a**=2
print ("Nilai a**=2 akan menjadi",a)
#OR
b=True
print ("Nilai b=",a)
b|=False
print ("Nilai b|=False",b)
b|=False
print ("Nilai b|=False",b)
b|=False
print ("Nilai b|=False",b)
#AND
b=True
print ("Nilai b =",b)
b&=False 
print ("Nilai b&=False akan menjadi",b)
b=False
print ("Nilai b =",b)
b&=False
print ("Nilai b&=False akan menjadi",b)
#XOR
b=True
print ("Nilai b =",b)
b^=False
print ("Nilai b^=False akan menjadi",b)
b=False
print ("Nilai b =",b)
b^=False
print ("Nilai b^=False akan menjadi",b)
#Shifting 
c=0b0100
print ("Nilai c=", format(c, '04b'))
c>>=1
print ("Nilai c >>=1 akan menjadi", format (c, '04b'))
c=0b0100
c<<=1
print ("Nilai c  <<=1 akan menjadi", format(c, '04b'))

a =0
b =5
print (' ================== Besar dari 13 ')
hasil = a >5
print (a ,'> 5 adalah ', hasil )
hasil = b >5
print (b ,'> 5 adalah ', hasil )

print (' ================== Kecil dari 5 ')
hasil = a <5
print (a ,'< 5 adalah ', hasil )
hasil = b <5
print (b ,'< 5 adalah ', hasil )

print (' ================== Besar atau sama dari 5 ')
hasil = a >=5
print (a ,' >= 5 adalah ', hasil )
hasil = b >=5
print (b ,' >= 5 adalah ', hasil )

print (' ================== Besar atau sama dari 5 ')
hasil = a <=5
print (a ,' <= 5 adalah ', hasil )
hasil = b <=5
print (b ,' <= 5 adalah ', hasil )

print (' ================== Sama dengan 5 ')
hasil = a ==5
print (a ,'== 5 adalah ', hasil )
hasil = b ==5
print (b ,'== 5 adalah ', hasil )

print (' ================== Tidak sama dengan 5 ')
hasil = a !=5
print (a ,'!= 5 adalah ', hasil )
hasil = b !=5
print (b ,'!= 5 adalah ', hasil )

print (' ============= NOT ============= ')
a = True
c = not a
print ('a adalah ',a )
print (' ------c = not a- - - -- - - NOT ')
print ('c adalah ',c )

print (' ============= OR ============= ')
a = True
b = True
c = a or b
print (a ,'OR ',b ,'menjadi ',c )

a = True
b = False
c = a or b
print (a ,'OR ',b ,'menjadi ',c )

a = False
b = True
c = a or b
print (a ,'OR ',b ,'menjadi ',c )

a = False
b = False
c = a or b
print (a ,'OR ',b ,'menjadi ',c )

print (' ============= AND ============= ')
a = True
b = True
c = a and b
print (a ,'AND ',b ,'menjadi ',c )

a = True
b = False
c = a and b
print (a ,'AND ',b ,'menjadi ',c )

a = False
b = True
c = a and b
print (a ,'AND ',b ,'menjadi ',c )

a = False
b = False
c = a and b
print (a ,'AND ',b ,'menjadi ',c )

print (' ============= XOR ============= ')
a = True
b = True
c = a ^ b
print (a ,'^',b ,'menjadi ',c )

a = True
b = False
c = a ^ b
print (a ,'^',b ,'menjadi ',c )

a = False
b = True
c = a ^ b
print (a ,'^',b ,'menjadi ',c )

a = False
b = False
c = a ^ b
print (a ,'^',b ,'menjadi ',c )

print (' ======================= IN ')
nama_lengkap = ' Bacharuddin Jusuf Habibie '
test = 'a'
cek = test in nama_lengkap
print ( test +' terdapat di '+ nama_lengkap +' adalah '+ str( cek ) )

test = 'rud '
cek = test in nama_lengkap
print ( test +' terdapat di '+ nama_lengkap +' adalah '+ str( cek ) )

test = 'bac '
cek = test in nama_lengkap
print ( test +' terdapat di '+ nama_lengkap +' adalah '+ str( cek ) )

print (' ======================= NOT IN ')
nama_lengkap = ' Bacharuddin Jusuf Habibie '
test = 'a'
cek = test not in nama_lengkap
print ( test +' tidak terdapat di '+ nama_lengkap +' adalah '+str ( cek) )

test = 'rud '
cek = test not in nama_lengkap
print ( test +' tidak terdapat di '+ nama_lengkap +' adalah '+str ( cek) )

test = 'bac '
cek = test not in nama_lengkap
print ( test +' tidak terdapat di '+ nama_lengkap +' adalah '+str ( cek) )


#TUGAS
#operator logika
#not, or, and, xor

a=True
b=False
print('\n============NAND============')
hasil=not (a and a)
print(a,'nand',a,'adalah =',hasil)
hasil=not (a and b)
print(a,'nand',b,'adalah =',hasil)
hasil=not (b and a)
print(b,'nand',a,'adalah =',hasil)
hasil=not (b and b)
print(b,'nand',b,'adalah =',hasil)

print('\n============NOR============')
hasil=not (a or a)
print(a,'nor',a,'adalah =',hasil)
hasil=not (a or b)
print(a,'nor',b,'adalah =',hasil)
hasil=not (b or a)
print(b,'nor',a,'adalah =',hasil)
hasil=not (b or b)
print(b,'nor',b,'adalah =',hasil)
 
print('\n============NXOR============')
hasil=not (a ^ a)
print(a,'nxor',a,'adalah =',hasil)
hasil=not (a ^ b)
print(a,'nxor',b,'adalah =',hasil)
hasil=not (b ^ a)
print(b,'nxor',a,'adalah =',hasil)
hasil=not (b ^ b)
print(b,'nxor',b,'adalah =',hasil)

#OPERATOR MEMBERSHIP
print('\n=========== IN ============')
nama ='RISDA'
test ='SD'
cek = test in nama
print(test,'ada di',nama,'adalah=',cek)
test ='DS'
cek = test in nama
print(test,'ada di',nama,'adalah=',cek)

test1='A'
test2='I'
test3='U'
test4='E'
test5='O'
cek =test1 in nama
print(test1,'ada di',nama,'adalah=',cek)
cek=test2 in nama
print(test2,'ada di',nama,'adalah=',cek)
cek=test3 in nama
print(test3,'ada di',nama,'adalah=',cek)
cek=test4 in nama
print(test4,'ada di',nama,'adalah=',cek)
cek=test5 in nama
print(test5,'ada di',nama,'adalah=',cek)

print('\n=========== NOT IN ============')
cek =test1 not in nama
print(test1,'tidak di',nama,'adalah=',cek)
cek=test2 in nama
print(test2,'tidak di',nama,'adalah=',cek)
cek=test3 in nama
print(test3,'tidak di',nama,'adalah=',cek)
cek=test4 in nama
print(test4,'tidak di',nama,'adalah=',cek)
cek=test5 in nama
print(test5,'tidak di',nama,'adalah=',cek)
