import os
nama_list=[]
no_list=[]
harga_list=[]

os.system('cls')
jml_kontrakan = int(input("masukan jumlah kontrakan = "))
harga = int(input("Masukan harga kos per bulan = "))

def hitung():
    global jml_kotor
    global biaya_semua_air
    global jml_bersih
    global gaji_penjaga
    jml_kotor = len(nama_list) * harga       

    biaya_air_per_kos = int(input("Masukan biaya air per kos = "))
    biaya_semua_air = biaya_air_per_kos * len(nama_list)

    gaji_penjaga = int(input("Masukan gaji penjaga = "))
    jml_bersih = (jml_kotor - biaya_semua_air) - gaji_penjaga

def display():
    os.system('cls')
    print(f"NO.|{'Nama':<12}|{'No.Kontrakan':<12}| Harga ")
    print(40*'-')
    for i in range(len(nama_list)):
        print(f"{i+1}  |{nama_list[i]:<12}|{no_list[i]:^12}|{harga_list[i]}")
        print(40*'-')

def display2():
    global berhenti
    print("Jumlah pendapatan kotor  =",jml_kotor)
    print("Total biaya air tiap kos =",biaya_semua_air)
    print("Gaji penjaga \t\t =",gaji_penjaga)
    print("Jumlah pendapatan bersih =",jml_bersih)
    berhenti=True

def lanjut():
    is_lanjut = input("Apakah masih ada yang ngontrak (y/n)??")
    if is_lanjut == "n":
        print('sudah tidak ada lagi yang mengontrak')
        hitung()
        display()
        display2()
        
    elif is_lanjut == 'y':
        pass
    else:
        print("Huruf yang anda inputkan salah, coba lagi!!")  
        lanjut()

def cek_nama():
    global nama
    nama = input("masukan nama pengontrak = ")
    if nama in nama_list:
        print("nama sudah ada")
        cek_nama()

def cek_nomor():
    global harga
    global no
    no = int(input("masukan nomer kontrakan = "))

    if no in no_list:
        print("no sudah ada yang ngisi")
        cek_nomor()
    else:
        pass
    if no >= 1 and no <= jml_kontrakan:
        pass
    else:
        print(f"masukan nomer 1 sampai {jml_kontrakan}")  
        cek_nomor()

def tambah():
    if no >= 1 and no <= jml_kontrakan:
        nama_list.append(nama)
        no_list.append(no)
        harga_list.append(harga)
        display()
    else:
        pass

berhenti=False
while True:
    cek_nama()            
    cek_nomor()
    tambah()


    if len(nama_list)==jml_kontrakan:
        print("kontrakan sudah penuh")
        hitung()
        display()
        display2()

    if berhenti==True:
        break
    else:
        lanjut()
        if berhenti==True:
            break
        
print("PROGAM SELESAI")

