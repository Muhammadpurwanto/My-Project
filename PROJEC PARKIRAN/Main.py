import os
os.system('cls')
print('            STRUK PARKIR RUMAH SAKIT                  \n')


jam = int(input("Masukan lama parkiran/jam \t\t: "))
jenis_kendaraan = input("Masukan jenis kendaraan[MOTOR/MOBIL] \t: ")

if jenis_kendaraan == "MOTOR" or jenis_kendaraan == "motor":
    if jam <= 3:
        harga = 3000
    elif jam >= 4 and jam <=5:
        harga = 5000
    else:
        harga = 10000
        
elif jenis_kendaraan == "MOBIL" or jenis_kendaraan == "mobil":
    if jam <= 3:
        harga = 5000
    elif jam >= 4 and jam <=5:
        harga = 10000
    else:
        harga = 15000
else:
    print("Anda salah menginputkan jenis kendaraan!!")

print(50*"=")
print("Anda memarkirkan jenis kendaraan\t:",jenis_kendaraan)
print("Lama parkir anda\t\t\t:",jam," jam")
print(f"Harga yang anda bayar\t\t\t: {harga}")
uang = int(input("Masukan uang pelanggan \t\t\t: "))
uang_kembalian = uang - harga
print("Uang kembalian pelanggan adalah\t\t:",uang_kembalian)
print(50*"=")


print("\n       TERIMAKASIH TELAH BERKUNJUNG")
print("             SEMOGA LEKAS SEMBUH")


        



