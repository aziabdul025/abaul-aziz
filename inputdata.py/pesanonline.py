data_product = {
    1:"Laptop",
    2:"Computer",
    3:"Monitor",
    4:"KeyBoard",
    5:"Mouse",
}
daftar_harga = {
    1: 5000000,
    2: 2000000,
    3: 600000,
    4: 150000,
    5: 50000,
}

dict_trx = {}
metode_pembayaran = {
    1:"Transfer Bank",
    2:"Dana",
    3:"Shoppee",
    4:"Ovo",
    5:"MiniMarket",
}
print("=========== List Product ===========")
for x in data_product :
    print("Id Product:", x, "\tNama Product:", data_product[x], "\tHarga Product:", daftar_harga[x])
pilih_id = int(input("Pilih Id Product: "))
if pilih_id in data_product :
    pilih_beli = input('ingin beli (Y/N): ')
    if pilih_beli == 'y' or pilih_beli == 'Y':
        nama_penerima    = input('Nama Penerima    : ')
        alamat_penerima  = input('Alamat Penerima  : ')
        telepone         = input('No HandPhone     : ')
        kurir_pengiriman = input('Kurir Pengiriman : ')
        dict_trx = {
            'Nama Penerima': nama_penerima,
            'Alamat Penerima': alamat_penerima,
            'No HandPhone': telepone,
            'Kurir Pengiriman': kurir_pengiriman,
            'Product Id': pilih_id,
        }
        print('=========== Metode Pembayaran ===========')
        for i in metode_pembayaran:
            print('Id : ', i, '\tMetode Pembayaran : ', metode_pembayaran[i])
        pilih_metode = int(input('Pilih Id Metode Pembayaran: '))
        if pilih_metode in metode_pembayaran:
            print('Nama Penerima     : ', dict_trx['Nama Penerima'])
            print('Alamat Penerima   : ', dict_trx['Alamat Penerima'])
            print('No HandPhone      : ', dict_trx['No HandPhone'])
            print('Kurir Pengiriman  : ', dict_trx['Kurir Pengiriman'])
            print('Nama Produk       : ', data_product[pilih_id])
            print('Harga             : ', daftar_harga[pilih_id])
            print('Metode Pembayaran : ', metode_pembayaran[pilih_metode])
            konfirmasi = input('Apakah Anda yakin ingin melakukan pembayaran ini? (Y/N) ')
            if konfirmasi == 'y' or konfirmasi == 'Y':
                print('Anda sudah berhasil melakukan pembayaran ini')
            else:
                pass
        else:
            print('Id Metode pembayaran tidak tersedia')
    else:
        pass
else:
    print('Id Product tidak tersedia')
