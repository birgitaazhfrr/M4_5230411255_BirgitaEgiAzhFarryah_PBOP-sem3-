class Debitur:
    def __init__(self, nama, ktp, limit):
        self.nama = nama
        self.ktp = ktp
        self.limit = limit

class Pinjaman:
    def __init__(self, debitur, jumlah, bunga, bulan, angsuran):
        self.debitur = debitur
        self.jumlah = jumlah
        self.bunga = bunga
        self.bulan = bulan
        self.angsuran = angsuran

daftar_debitur = [
    Debitur("Gita", "1234", 50000000),
    Debitur("Munchin", "5678", 2100000),
    Debitur("Jiro", "9012", 1200000),
    Debitur("Sasa", "0234", 2200000),
    Debitur("alin", "3456", 2000000),
    Debitur("jado", "6789", 3000000),
    Debitur("Minji", "4567", 1000000),
    Debitur("apin", "5678", 2500000),
    Debitur("senja", "6789", 2300000),
    Debitur("shuizuka", "7890", 1700000),
    Debitur("mail", "8901", 1500000),
    Debitur("lolly", "9012", 1900000),
    Debitur("sakura", "0012", 7000000),
    Debitur("beby", "0013", 4500000),
]

daftar_pinjaman = [
    Pinjaman("Bimo", 3000000, 2, 7, 125000),
    Pinjaman("Mila", 5000000, 3, 10, 121000),
    Pinjaman("Mimo", 2000000, 4, 12, 210000),
    Pinjaman("Ciput", 1500000, 5, 5, 190000),
    Pinjaman("Hahun", 1700000, 6, 6, 120000),
    Pinjaman("Aceng", 2100000, 7, 9, 115000),
    Pinjaman("Maung", 1200000, 8, 11, 173000),
    Pinjaman("Maxi", 1900000, 9, 12, 123000),
    Pinjaman("Nana", 2300000, 10, 9, 124000),
    Pinjaman("Naoko", 1100000, 2, 12, 125000),
    Pinjaman("Bundel", 1800000, 3, 10, 135000),
    Pinjaman("Bleki", 2700000, 4, 24, 141000),
]

def tampilkan_menu():
    print("=============== Aplikasi Admin Pinjol ===============")
    print("1. Kelola Debitur")
    print("2. Pinjaman")
    print("0. Keluar")
    pilihan = input("Masukan Pilihan : ")
    return pilihan

def kelola_debitur():
    while True:
        print("=============== Kelola Debitur ===============")
        print("1. Tampilkan Semua Debitur")
        print("2. Cari Debitur")
        print("3. Tambah Debitur")
        print("0. Kembali")
        sub_menu = input("Masukan Pilihan Sub Menu : ")
        
        if sub_menu == '1':
            print("=============== Daftar Debitur ===============")
            print("{:<15} {:<10} {:<15}".format("Nama Debitur", "No KTP", "Limit Pinjaman"))
            for debitur in daftar_debitur:
                print("{:<15} {:<10} Rp.{:<15,.0f}".format(debitur.nama, debitur.ktp, debitur.limit))
            

        elif sub_menu == '2':
            ktp = input("Masukkan No KTP: ")
            found = False
            for debitur in daftar_debitur:
                if debitur.ktp == ktp:
                    print(f"Nama: {debitur.nama}, Limit: Rp.{debitur.limit:,.0f}")
                    found = True
                    break
            if not found:
                print("Debitur tidak ditemukan.")
            

        elif sub_menu == '3':
            nama = input("Masukkan Nama: ")
            ktp = input("Masukkan No KTP: ")
            limit = int(input("Masukkan Limit Pinjaman: "))
            daftar_debitur.append(Debitur(nama, ktp, limit))
            print("Debitur berhasil ditambahkan!")
            

        elif sub_menu == '0':
            break

def menu_pinjaman():
    while True:
        print("=============== Menu Pinjaman ===============")
        print("1. Tambah Pinjaman")
        print("2. Tampilkan Pinjaman")
        print("0. Kembali")
        sub_menu = input("Masukan Pilihan Sub Menu : ")

        if sub_menu == '1':
            debitur = input("Masukkan Nama Debitur: ")
            jumlah = int(input("Masukkan Jumlah Pinjaman: "))
            bunga = int(input("Masukkan Bunga (%): "))
            bulan = int(input("Masukkan Lama Pinjaman (Bulan): "))
            angsuran = (jumlah * (1 + bunga / 100)) / bulan
            daftar_pinjaman.append(Pinjaman(debitur, jumlah, bunga, bulan, angsuran))
            print("Pinjaman berhasil ditambahkan!")
            

        elif sub_menu == '2':
            print("=============== Daftar Pinjaman ===============")
            print("{:<15} {:<15} {:<10} {:<10} {:<15}".format("Nama Debitur", "Pinjaman", "Bunga", "Bulan", "Angsuran(Bln)"))
            for pinjaman in daftar_pinjaman:
                print("{:<15} Rp.{:<15,.0f} {:<10}% {:<10} Rp.{:<15,.0f}".format(pinjaman.debitur, pinjaman.jumlah, pinjaman.bunga, pinjaman.bulan, pinjaman.angsuran))
           

        elif sub_menu == '0':
            break

while True:
    pilihan = tampilkan_menu()
    
    if pilihan == '1':
        kelola_debitur()
    elif pilihan == '2':
        menu_pinjaman()
    elif pilihan == '0':
        print("Keluar dari program...")
        break