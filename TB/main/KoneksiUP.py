def tambah_kontak(kontak, nama, nomor):
    status = True
    kontak_baru = {
        'nama': nama,
        'nomor': nomor,
        'status': status
    }
    kontak.append(kontak_baru)
    print("Kontak berhasil ditambahkan!")

def hapus_kontak(kontak, nama):
    for i in range(len(kontak)):
        if kontak[i]['nama'] == nama:
            kontak.pop(i)
            print("Kontak berhasil dihapus!")
    return None

def tampilkan_kontak(kontak):
    print("\nDaftar kontak: ")
    for data in kontak:
        if data['status'] != False:
            nama = data['nama']
            nomor = data['nomor']
            print("=======================")
            print(f"Nama: {nama}")
            print(f"Nomor: {nomor}")
            print("=======================")
            
def cari_kontak(kontak, nama):
    print("Data kontak:")
    for data in kontak:
        if data['nama'] == nama:
            nama = data['nama']
            nomor = data['nomor']
            print(f"Nama: {nama}")
            print(f"Nomor: {nomor}")
            print("=======================")
    
def insertion_sort(kontak):
    for i in range(1, len(kontak)):
        current = kontak[i]
        j = i - 1
        while j >= 0 and kontak[j]['nama'] > current['nama']:
            kontak[j + 1] = kontak[j]
            j -= 1
        kontak[j + 1] = current

def blokir_kontak(kontak, daftar_blokir, nama):
    for i in range(len(kontak)):
        if kontak[i]['nama'] == nama:
            kontak[i]['status'] = False
            if kontak[i]['nama'] == nama and kontak[i]['status'] == False:
                nama_kontak_blokir = {
                    'nama': kontak[i]['nama'],
                    'nomor': kontak[i]['nomor']
                }
                daftar_blokir.append(nama_kontak_blokir)
                print("Kontak berhasil diblokir!")
            else:
                print("Nama tidak ditemukan!")
    return None

def unblokir_kontak(kontak, daftar_blokir, nama):
    for i in range(len(daftar_blokir)):
        if daftar_blokir[i]['nama'] == nama:
            print("Kontak berhasil diunblokir!")
            daftar_blokir.pop(i)
            for i in range(len(kontak)):
                if kontak[i]['nama'] == nama:
                    kontak[i]['status'] = True
                    return None
        else:
            print("Nama tidak ditemukan!")
    return None

def main():
    kontak = []
    daftar_blokir = []

    while True:
        print("\n===== KoneksiUP =====")
        print("1. Tambah Kontak")
        print("2. Hapus Kontak")
        print("3. Tampilkan Kontak")
        print("4. Cari Kontak")
        print("5. Sortir Kontak")
        print("6. Blokir Kontak")
        print("7. Unblokir Kontak")
        print("8. Keluar")
        pilihan = input("Pilih menu (1-8): ")
        if pilihan == "1":
            nama = input("Masukkan nama kontak: ")
            nomor = input("Masukkan nomor telepon: ")
            tambah_kontak(kontak, nama, nomor)
        elif pilihan == "2":
            nama = input("Masukkan nama kontak yang ingin dihapus: ")
            hapus_kontak(kontak, nama)
        elif pilihan == "3":
            tampilkan_kontak(kontak)
        elif pilihan == "4":
            nama = input("Masukkan nama kontak yang ingin dicari: ")
            cari_kontak(kontak, nama)
        elif pilihan == "5":
            insertion_sort(kontak)
            print("Kontak berhasil disortir secara otomatis!")
        elif pilihan == "6":
            nama = input("Masukkan nama kontak yang ingin diblokir: ")
            blokir_kontak(kontak, daftar_blokir, nama)
        elif pilihan == "7":
            nama = input("Masukkan nama kontak yang ingin diunblokir: ")
            unblokir_kontak(kontak, daftar_blokir, nama)
        elif pilihan == "8":
            print("Terima kasih telah menggunakan KoneksiUP.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu (1-8) yang tersedia.")

main()
