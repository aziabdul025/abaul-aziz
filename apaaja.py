print("Program Python Hitung Volume dan Luas Permukaan Bola")
print("---------------ekorkode.com---------------\n")

pi    = 22/7
jari   = float(input("Masukan Jari-jarinya : "))
volume   = 4/3*pi*(jari*jari*jari)
luas   = 4*pi*(jari*jari)

print("\n-----------------Hasilnya-----------------")
print("Volume Bola =","{:.3f}".format(volume)) 
print("Luas Permukaan Bola =","{:.3f}".format(luas))

