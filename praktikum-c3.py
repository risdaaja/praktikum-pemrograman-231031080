nama = 'risda'
nim  = '231031080'
meet = 'praktikum 3 (string)'
prodi= 'Sistem informasi C'
email= 'risrisda95@gmail.com'
ttl='20-10-2005'
alamat= 'jl. liu buloe'
asal= 'pinrang'
hobi= 'fotografer'
tinggi= '152'
sp=40
print('-'*sp)
print(nama.upper().center(sp))
print(nim.center(sp))
print('\n'*2)
print(meet.rjust(sp))
print(prodi.rjust(sp))
print(email.lower().rjust(sp))
print('-'*sp)

print(f'''\tHalo, nama saya {nama} dengan NIM {nim} dari prodi {prodi}, ini adalah file {meet}. Terima Kasih.\n''')

print(f'''Biodata saya, 
Nama\t: {nama.upper()}
NIM\t: {nim}
prodi\t: {prodi}
TTL\t: {ttl}
Alamat\t: {alamat}
Asal\t: {asal}
Hobi\t: {hobi}
Tinggi\t: {tinggi}cm
''')


stat1 = 'duFort Frankel Sir Issac'
up = stat1.split(" ")
print(up[-1]," ".join(up[0:3]))
# Issac duFort Frankel Sir

stat2 = 'duFort Frankel Sir Issac'
up2 = stat2.split(" ")
print(f'{up2[0][0]}{up2[1][0]}{up2[2][0]} {up2[3]}')
# d F S Issac
 
stat3 = 'duFort Frankel Sir Issac'
up3 = stat3.split(" ")
print(f'{up3[0]} {up3[1][0]}{up3[2][0]}{up3[3][0]}')
# duFort F S I

stat4 = 'duFort Frankel Sir Issac'
up4 = stat4.split(" ")
print(f'{up4[3][0]} {stat4[0:6]} {stat4[7:14]} {stat4[15:18]}')
# I duFort Frankel Sir

stat5 = 'duFort Frankel Sir Issac'
up5 = stat5.split(" ")
print(f'{up5[-1]} {up5[0][0]} {up5[1][0].upper()} {up5[2][0].upper()}')
# Issac d F S

stat6 = 'duFort Frankel Sir Issac'
up5 = stat6.upper().split(" ")
print(f'{up5[-1].upper()} {up5[0][0]} {up5[1][0].upper()} {up5[2][0].upper()}')
# ISSAC D F S

stat7 = '#duFort Frankel Sir Issac$'
up7=stat7.strip('#$')
print(up7)
# duFort Frankel Sir Issac

stat8 = '#duFort-Frankel-Sir-Issac$'
up8 = stat8.split("-")
print(f'{up8[0].strip("#")} {up8[1]} {up8[2]} {up8[3].strip("$")}')
# duFort Frankel Sir Issac

stat9 = '#duFort@ ^Frankel* (Sir( (Issac$'
a = stat9.strip("#$")
b = a.replace("@","")
c = b.replace("^","")
d = c.replace("*","")
e = d.replace("(","")
f = e.replace("("," ")
g = f.replace("(","")
print(g)
# duFort Frankel Sir Issac

stat10 = '#duFort@-^Frankel*-(Sir(-(Issac$'
a=stat10.strip("#$")
b=a.replace("@-^"," ")
c=b.replace("*-("," ")
d=c.replace("(-("," ")
print(d.upper())
# DUFORT FRANKEL SIR ISSAC
