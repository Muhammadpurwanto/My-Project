display="""
No.|  Menu                |Ukuran       |Harga  
-----------------------------------------------
1. | POPCORN CARAMEL(PC)  |Small(S)     |20.000
2. | POPCORN CARAMEL(PC)  |Medium(M)    |30.000
3. | POPCORN CARAMEL(PC)  |Large(L)     |40.000
4. | POPCORN HONEY(PH)    |Small(S)     |15.000
5. | POPCORN HONEY(PH)    |Medium(M)    |25.000
6. | POPCORN HONEY(PH)    |Large(L)     |35.000
7. | POPCORN SWEET(PS)    |Small(S)     |25.000
8. | POPCORN SWEET(PS)    |Medium(M)    |35.000
9. | POPCORN SWEET(PS)    |Large(L)     |45.000
"""
print(display)
pesanan_list=[]
ukuran_list=[]
harga_list=[]
harga_total=0
i=0
jumlah = int(input("Masukan jumlah beli: "))
while i<jumlah:
    harga=0
    input_menu = input("Masukan KODE pesanan pelanggan: ")
    input_ukuran = input("Masukan KODE Ukuran pesanan pelanggan:")
    if input_menu == "PC" or input_menu == "pc":
        if input_ukuran == "S" or input_ukuran == "s":
            harga = 20000
        elif input_ukuran == "M" or input_ukuran == "m":
            harga = 30000
        elif input_ukuran == "L" or input_ukuran == "l":
            harga = 40000
        else:
            print("Kode yang anda masukan salah!!")
    elif input_menu == "PH" or input_menu == "ph":
        if input_ukuran == "S" or input_ukuran == "s":
            harga = 15000
        elif input_ukuran == "M" or input_ukuran == "m":
            harga = 25000
        elif input_ukuran == "L" or input_ukuran == "l":
            harga = 35000
        else:
            print("Kode yang anda masukan salah!!")
    elif input_menu == "PS" or input_menu == "ps":
        if input_ukuran == "S" or input_ukuran == "s":
            harga = 25000
        elif input_ukuran == "M" or input_ukuran == "m":
            harga = 35000
        elif input_ukuran == "L" or input_ukuran == "l":
            harga = 45000
        else:
            print("Kode yang anda masukan salah!!")
    else:
        print("KODE pesanan yang anda masukan salah!!")
    pesanan_list.append(input_menu)
    ukuran_list.append(input_ukuran)
    harga_list.append(harga)
    harga_total+=harga
    i+=1

print("No. Pesanan\tUkuran\tHarga")
for i in range(jumlah):
    print(f"{i+1}   {pesanan_list[i]}\t\t{ukuran_list[i]}\t{harga_list[i]}")
print("\t  Harga Total  =",harga_total)
uang_pelanggan = int(input("Masukan uang pelanggan = "))
kembalian = uang_pelanggan-harga_total
print("\tUang kembalian =",kembalian)