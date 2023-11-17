print('--------------------------------------------')
print('             PRISMA SEGITIGA                ')
print('============================================')
luas_alas = float(input("Masukkan Luas Alas\t: "))
tinggi = float(input("Masukkan Tinggi Limas\t: "))
sisi = float(input("Masukkan Sisi Limas\t: "))

volume = 1/3 * luas_alas * tinggi * sisi

print ("Volume Prisma adalah\t= %d" %volume)

luas_alas = float(input("Masukkan Luas Alas\t: "))
jumlah_sisi_tegak = float(input("Masukkan Sisi Tegak\t: "))

luas = luas_alas + jumlah_sisi_tegak

print("Luas Prisma adalah\t= %d" %luas)
print('--------------------------------------------')          