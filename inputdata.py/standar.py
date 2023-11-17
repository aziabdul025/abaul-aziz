nilai = int(input('Inputkan nilai\t\t: '))
nilai_sikap = input('Inputkan nilai sikap\t: ')
nilai_ulangan =int(input('Inputkan nilai ulangan\t: '))

if nilai > 75 and nilai_sikap == 'A' or 'B' and nilai_ulangan > 60:
    print('Anda lulus')
else:
    print('Anda tidak lulus')

