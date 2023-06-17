from datetime import datetime

def print_menu():
    print("\nProgram Todo List!")
    print("1. Tambahkan tugas")
    print("2. Tampilkan semua tugas")
    print("3. Urutkan tugas berdasarkan jam")
    print("4. Cari tugas")
    print("5. Keluar")


def add_task(tasks):
    task_name = input("Masukkan nama tugas: ")
    task_time = input("Masukkan jam (HH:MM): ")
    tasks.append((task_name, task_time))
    print("Tugas berhasil ditambahkan!")


def show_tasks(tasks):
    if len(tasks) == 0:
        print("Belum ada tugas yang ditambahkan.")
    else:
        print("Daftar Tugas:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task[0]} (Jam: {task[1]})")


def sort_tasks(tasks):
    sorted_tasks = sorted(tasks, key=lambda x: datetime.strptime(x[1], "%H:%M"))
    print("Tugas berhasil diurutkan berdasarkan jam.")
    return sorted_tasks


def search_task(tasks):
    keyword = input("Masukkan kata kunci: ")
    results = []
    for task in tasks:
        if keyword.lower() in task[0].lower():
            results.append(task)
    if len(results) == 0:
        print("Tidak ditemukan tugas yang sesuai.")
    else:
        print("Hasil pencarian:")
        for i, task in enumerate(results, start=1):
            print(f"{i}. {task[0]} (Jam: {task[1]})")


def main():
    tasks = []
    while True:
        print_menu()
        choice = input("Pilih menu (1-5): ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            show_tasks(tasks)
        elif choice == '3':
            tasks = sort_tasks(tasks)
        elif choice == '4':
            search_task(tasks)
        elif choice == '5':
            print("Terima kasih telah menggunakan Todo List. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang sesuai.")


if __name__ == "__main__":
    main()
