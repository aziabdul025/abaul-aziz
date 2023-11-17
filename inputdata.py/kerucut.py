import math
print('=================================')                 
print("Volume dan Luas Permukaan Kerucut")
print("-------------------------------\n")

pi    = 22/7
jari   = float(input("Masukan Jari-jari Lingkaran: "))
tinggi   = float(input("Masukan Tinggi Kerucut\t: "))
pelukis = math.sqrt((jari*jari)+(tinggi*tinggi))
volume   = 1/3*pi*(jari*jari)*tinggi
luas   = pi*jari*(jari+pelukis)

print("\n-----------------Hasilnya-----------------")
print("Volume Kerucut\t = ","{:.2f}".format(volume)) 
print("Luas Permukaan Kerucut\t = ","{:.2f}".format(luas))