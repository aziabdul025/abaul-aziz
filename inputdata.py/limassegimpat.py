import math
print('--------------------------------------------')
print('            LIMAS SEGIEMPAT                 ')
print('============================================')

tinggi=int(input("Masukan Tinggi            : "))
sisi=int(input("Masukan Panjang sisi Alas : "))

Sisi_miring = math.sqrt((sisi*0.5) * (sisi*0.5)+(tinggi*tinggi))
Segi_Tiga = 0.5*sisi * Sisi_miring

hasil_Luas = (sisi*sisi) + (4*Segi_Tiga)
hasil_Volume = (1/3) * (sisi*sisi) * tinggi

print ("Luas Limas   =  ", round(hasil_Luas))
print ("Volume Limas = ", round(hasil_Volume))
