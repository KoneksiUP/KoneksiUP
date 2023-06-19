

def hapus_kontak(kontak, nama):
    for i, (kontak_nama, _) in enumerate(kontak):
        if kontak_nama == nama:
            kontak.pop(i)
            print("Kontak berhasil dihapus!")
            return
    print("Kontak tidak ditemukan!")

def tampilkan_kontak(kontak):
    if kontak:
        print("Daftar Kontak:")
        for nama, nomor in kontak:
            print("Nama:", nama)
            print("Nomor:", nomor)
            print("-----------------------")
    else:
        print("Daftar kontak anda kosong!")

def cari_kontak(kontak, nama):
    for kontak_nama, kontak_nomor in kontak:
        if kontak_nama == nama:
            print("Nama:", kontak_nama)
            print("Nomor:", kontak_nomor)
            return
    print("Kontak tidak ditemukan!")

def insertion_sort(kontak):
    for i in range(1, len(kontak)):
        current = kontak[i]
        j = i - 1
        while j >= 0 and kontak[j][0] > current[0]:
            kontak[j + 1] = kontak[j]
            j -= 1
        kontak[j + 1] = current

def main():
    kontak = []

    while True:
        print("===== KoneksiUP =====")
        print("1. Tambah Kontak")
        print("2. Hapus Kontak")
        print("3. Tampilkan Kontak")
        print("4. Cari Kontak")
        print("5. Sortir Kontak")
        print("6. Keluar")
        pilihan = input("Pilih menu (1-6): ")

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
            print("Terima kasih telah menggunakan KoneksiUP.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu (1-6) yang tersedia.")

if __name__ == "__main__":
    main()
