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
