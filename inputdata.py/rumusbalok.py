print('--------------------------------------------')
print('              RUMUS BALOK                   ')
print('============================================')
  
panjang = float(input('\033[94mInput panjang balok\t: '))
lebar = float(input('\033[92mInput lebar balok\t: '))
tinggi = float(input('\033[93mInput tinggi balok\t: '))
volume = panjang * lebar * tinggi
 
luas = 2*(panjang*lebar) + 2*(panjang*tinggi) + 2*(lebar*tinggi)
 
print('\033[91mLuas permukaan balok\t= ',round(luas,2))
print('\033[95mvolume\t= ', volume)

