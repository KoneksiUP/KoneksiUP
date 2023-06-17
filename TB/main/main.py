import subprocess

# Daftar file yang tersedia
available_files = ["TB\main\kontak.py", "TB\main\cuaca.py", "TB\main\duid.py"]

# Tampilkan pilihan file yang tersedia
print("Pilih file yang akan dijalankan:")
for i, file in enumerate(available_files):
    print(f"{i + 1}. {file}")

# Minta input pengguna untuk memilih nomor file
choice = input("Masukkan nomor file: ")

# Validasi input pengguna
if not choice.isdigit() or int(choice) <= 0 or int(choice) > len(available_files):
    print("Pilihan tidak valid.")
else:
    # Jalankan file yang dipilih
    selected_file = available_files[int(choice) - 1]
    subprocess.call(['python', selected_file])
