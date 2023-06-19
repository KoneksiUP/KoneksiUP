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
