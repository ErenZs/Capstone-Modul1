#Daftar List Makanan Anabul
list_makanan = [
    {
     "kode barang" : "1101",
     "nama makanan" : "Whiskas",
     "stock" : 20,
     "harga" : 70000,
     "tipe makanan" : "Kering"
     },
    {
     "kode barang" : "1102",
     "nama makanan" : "Proplan",
     "stock" : 15,
     "harga" : 198000,
     "tipe makanan" : "Kering"
     },
     {
     "kode barang" : "1201",
     "nama makanan" : "Me O",
     "stock" : 30,
     "harga" : 12500,
     "tipe makanan" : "Kering"
     },
     {
     "kode barang" : "1202",
     "nama makanan" : "Life Cat",
     "stock" : 10,
     "harga" : 15000,
     "tipe makanan" : "Basah"
     },
     {
     "kode barang" : "1103",
     "nama makanan" : "Felibite",
     "stock" : 5,
     "harga" : 15500,
     "tipe makanan" : "Kering"
     },
]

def menampilkan_daftar_produk() :
    if not list_makanan:
        print("\n\n Maaf ya makanan kamu sedang habis, tidak ada tampilan produk apapun.")
    elif(pilih_menu == "1"):
        while True:
            pilihan_user= input('''
-----------------------------------
========== DAFTAR PRODUK ==========
-----------------------------------
                                    
    1.Tampilkan Seluruh Produk
    2.Tampilkan Produk Tertentu
    3.Kembali ke Menu Utama

Pilih Produk yang kamu cari [1-3]: ''')
    
            if(pilihan_user == "1"):
                judul = "Daftar Produk".center(90," ")
                print(judul)
                print("\n\n|Kode Barang\t| Nama Makanan\t\t| Stock\t| Harga\t\t| Tipe Makanan")
                for i in range(len(list_makanan)):
                    print("|{:<8}\t| {:<8}\t\t| {:<2}\t| {:<8}\t| {:<8}".format(list_makanan[i]["kode barang"],list_makanan[i]["nama makanan"],list_makanan[i]["stock"],list_makanan[i]["harga"],list_makanan[i]["tipe makanan"]))
   
            elif(pilihan_user == "2"):
                    kode_barang = input(''' Input Kode Barang Makanan Anabul : ''')
                    kode_barang = kode_barang.lower()
                    found = False
                    for product in list_makanan:
                        if kode_barang.lower() == product["kode barang"]:
                            found = True
                            print("\n\n|Kode Barang\t| Nama Makanan\t\t| Stock\t| Harga\t\t| Tipe Makanan")
                            print("|{:<8}\t| {:<8}\t\t| {:<2}\t| {:<8}\t| {:<8}".format(product["kode barang"], product["nama makanan"], product["stock"], product["harga"], product["tipe makanan"]))
                            break      
                    if not found:
                        print("\n\nProduk yang Anda cari tidak ditemukan.")
                        
            elif(pilihan_user == "3"):
                break

#Fitur Menambahkan Produk            
def menambah_produk():
    while True:
        tambah_produk = input('''
----------------------------------------
========== MENAMBAHKAN PRODUK ==========
----------------------------------------

1. Tambah produk makanan anabul
2. Kembali ke menu awal
                          
Silahkan input submenu yang akan dijalankan: ''')

        if tambah_produk == "1":
            kode_barang1 = input('''
Masukan Input Kode Produk Makanan Anabul : ''')
            kode_barang1 = kode_barang1.lower()
            kode_ada = False

            for i in range(len(list_makanan)):
                if kode_barang1 == list_makanan[i]["kode barang"]:
                    kode_ada = True
                    print("\n\nProduk yang Anda Input sudah ada ><")
                    break

            if not kode_ada:
                makanan1 = input("\nMasukan Nama Makanan Anabul : ")
                while True:
                    try:
                        stock1 = int(input("\nMasukan Stock Barang : "))
                        break
                    except ValueError:
                        print("\nStock harus dalam bentuk angka.")
                while True:
                    try:
                        harga1 = int(input("\nMasukan Harga Makanan Anabul [Rp] : "))
                        break
                    except ValueError:
                        print("\nHarga harus dalam bentuk angka")
                        
                tipe1 = input('''\nJangan lupa untuk tipe makanannya >< 
                                   \nMasukan Tipe Makanan Anabul : ''')
                produk_baru ={
                    "kode barang": kode_barang1,
                    "nama makanan": makanan1,
                    "stock": stock1,
                    "harga": harga1,
                    "tipe makanan": tipe1,
                }
                list_makanan.append(produk_baru) 
                hasil = input("Apakah Anda ingin menambahkan Produk ini {} yes/no ?: ".format(produk_baru))
                print("Makanan Anabul sudah ditambahkan")
                hasil = hasil.lower()
                if hasil != "yes":
                    list_makanan.remove(produk_baru)
                    print("Tidak ada penambahan produk")
                else:
                    continue
                    
        elif tambah_produk == "2":
            break

#Fitur Menghapus Produk
def menghapus_produk():
    if not list_makanan:
        print("\n\n Maaf makanan anabul kamu saat ini sedang habis, tidak ada produk dapat dihapus.")
    else:
        while True:             
            hapus_produk = input('''
--------------------------------------
========== MENGHAPUS PRODUK ==========
--------------------------------------

1. Hapus Produk Makanan Anabul disini:
2. Kembali ke menu awal
                          
Silahkan input submenu yang akan dijalankan: ''')         

            if hapus_produk == "1":
                hapus_produk_kode = input(''' Input Kode Barang Makanan Anabul : ''')
                hapus_produk_kode = hapus_produk_kode.lower()
                produk_ditemukan = False

                i = 0
                while i < len(list_makanan):
                    if hapus_produk_kode == list_makanan[i]["kode barang"]:
                        produk_ditemukan = True     
                        hasil1 = input("Apakah Kamu yakin untuk menghapus produk {} ini (yes/no)? ".format(hapus_produk_kode))
                        hasil1 = hasil1.lower()
                        while hasil1.lower() not in ["yes", "no"]:
                            print("Mohon masukkan 'yes' atau 'no'")
                            hasil1 = input("Apakah Kamu yakin untuk menghapus produk {} ini (yes/no)? ")
                        if hasil1.lower() == "yes":
                            del list_makanan[i]
                            print("Produk Makanan Anabul {} berhasil dihapus".format(hapus_produk_kode))
                            if len(list_makanan) == 0:
                                print("Maaf produk makanan sudah terhapus.")   
                            break
                        else:
                            print("Proses penghapusan dibatalkan.")
                            break
                    else:
                        i += 1
            
                if not produk_ditemukan: 
                   print("Kode Barang yang Anda Input tidak ditemukan.")
                
                
            elif hapus_produk == "2":
                break

#Fitur Mengupdate Produk
def mengupdate_stock_produk():
    if not list_makanan:
        print("\n\n Maaf produk Iphone kosong, Anda tidak bisa lakukan update produk")
    else:
        while True:
            update_stock = input('''
-----------------------------------------
========== UPDATE STOCK BARANG ==========
-----------------------------------------

1. Update Stock Produk disini : 
2. Kembali ke menu awal
                          
Silahkan input submenu yang akan dijalankan: ''') 
            if update_stock == "1":
                input_stock = input(''' Input Kode Barang Makanan Anabul : ''')
                input_stock = input_stock.lower()
                produk_ditemukan = False
            
                for item in list_makanan:
                    if input_stock == item["kode barang"]:
                        print("\n\n|Kode Barang\t| Nama Makanan\t\t| Stock\t| Harga\t\t| Tipe Makanan")
                        print("|{:<8}\t| {:<8}\t\t| {:<2}\t| {:<8}\t| {:<8}".format(item["kode barang"], item["nama makanan"], item["stock"], item["harga"], item["tipe makanan"]))
                        produk_ditemukan = True
                        hasil2 = input("Apakah ingin melanjutkan update stock produk anabul (yes/no)?: ")
                        hasil2 = hasil2.lower()
                        if hasil2 == "yes":
                            input_hasil = int(input("Masukkan jumlah produk anabul yang diubah: "))
                            cek_hasil = input("Apakah kode produk ({}) diupdate jadi {} (yes/no)? ".format(input_stock,input_hasil))
                            cek_hasil = cek_hasil.lower()
                            if cek_hasil == "yes":
                            
                                item["stock"] = input_hasil
                                print("Update Stock Produk Anabul berhasil")
                        break  
             
                if not produk_ditemukan:
                    print("Produk tidak ditemukan")
                
            elif update_stock == "2":
                break

#Fitur Menu
while True:
    pilih_menu = input('''
======================================                   
     Welcome and Happy Shopping
         >'Rezky Pet Shop'<
======================================
                           
Daftar Menu :
-------------                   
    1. Menampilkan Daftar Produk
    2. Menambah Produk
    3. Menghapus Produk
    4. Mengupdate Stock Produk
    5. Exit
                       
        
Masukkan angka Menu yang ingin dijalankan: ''')

    if(pilih_menu == "1"):
        menampilkan_daftar_produk()

    elif(pilih_menu == "2") :
        menambah_produk()

    elif(pilih_menu == "3") :
        menghapus_produk()
    
    elif(pilih_menu == "4") :
        mengupdate_stock_produk()

    elif(pilih_menu == "5") :
        break