import os
nama_pengontrak = []

os.system('cls')
jml_kontrakan = int(input("masukan jumlah kontrakan = "))
harga_per_bulan = int(input("Masukan harga kos per bulan = "))

def hitung():
    global jml_kotor
    global biaya_semua_air
    global jml_bersih
    global gaji_penjaga
    jml_kotor = len(nama_pengontrak) * harga_per_bulan       

    biaya_air_per_kos = int(input("Masukan biaya air per kos = "))
    biaya_semua_air = biaya_air_per_kos * len(nama_pengontrak)

    gaji_penjaga = int(input("Masukan gaji penjaga = "))
    jml_bersih = (jml_kotor - biaya_semua_air) - gaji_penjaga

def display():
    os.system('cls')
    print(f"NO.|{'Nama':<12}|{'No.Kontrakan':<12}| Harga ")
    print(40*'-')
    for index,data in enumerate(nama_pengontrak):
        print(f"{index+1}  |{data[0]:<12}|{data[1]:^12}|{harga_per_bulan}")
        print(40*'-')

def display2():
    print("Jumlah pendapatan kotor  =",jml_kotor)
    print("Total biaya air tiap kos =",biaya_semua_air)
    print("Gaji penjaga \t\t =",gaji_penjaga)
    print("Jumlah pendapatan bersih =",jml_bersih)

def lanjut():
    is_lanjut = input("Apakah masih ada yang ngontrak (y/n)??")
    if is_lanjut == "n":
        print('sudah tidak ada lagi yang mengontrak')
        hitung()
        display()
        display2()
        global berhenti
        berhenti = True  
        
    elif is_lanjut == 'y':
        pass
    else:
        print("Huruf yang anda inputkan salah, coba lagi!!")  
        lanjut()

def cek_nama():
    global pengontrak
    pengontrak = input("masukan nama pengontrak = ")
    for nama1 in nama_pengontrak:        
        if pengontrak == nama1[0]:
            print("nama sudah ada")
            cek_nama()

def cek_nomor():
    global nomer_kontrakan
    nomer_kontrakan = int(input("masukan nomer kontrakan = "))
    for nomor1 in nama_pengontrak:
        if nomer_kontrakan==nomor1[1]:
            print("Nomor sudah ada yang ngisi")
            cek_nomor()

    if nomer_kontrakan >= 1 and nomer_kontrakan <= jml_kontrakan:
        pengontrak_baru=[pengontrak,nomer_kontrakan]        
        nama_pengontrak.append(pengontrak_baru)
        display()
    else:
        print(f"masukan nomer 1 sampai {jml_kontrakan}")  
        cek_nomor()

i=1

while True:
    berhenti=False

    cek_nama()                  

    cek_nomor()

    if i==jml_kontrakan:
        print("kontrakan sudah penuh")
        hitung()
        display()
        display2()
        break 

    lanjut()
    if berhenti == True:
        break
    i +=1
print("PROGAM SELESAI")

    







''
