print('\033[92m======================')
print('\033[4mRumus Limas Segi Empat\033[0')
print('\033[92m----------------------')
l1 = int(input('\033[94ml1:'))
l2 = int(input('l2:'))
l3 = int(input('l3:'))
l4 = int(input('l4:'))
l5 = int(input('l5:'))
T  = int(input('\033[95mTinggi :'))
Luas_Alas = int(input('Luas Alas:'))
Luas    = l1 + l2 + l3 + l4 + l5
Volume  = 1/3 * Luas_Alas * T
print('\033[93mLuas     : ',str(Luas),'cm2')
print('Volume   :',str(Volume),'cm3')