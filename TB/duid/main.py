import requests

def currency_converter(amount, from_currency, to_currency):
    # Mengirim permintaan ke API untuk mendapatkan data kurs mata uang terkini
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    
    # Mengekstrak nilai tukar mata uang
    exchange_rate = data['rates'][to_currency]
    
    # Menghitung jumlah mata uang yang dikonversi
    converted_amount = amount * exchange_rate
    
    return converted_amount

# Memasukkan input dari pengguna
amount = float(input("Masukkan jumlah uang yang akan dikonversi: "))
from_currency = input("Masukkan mata uang asal: ").upper()
to_currency = input("Masukkan mata uang tujuan: ").upper()

# Memanggil fungsi pengkonversi mata uang
result = currency_converter(amount, from_currency, to_currency)

# Menampilkan hasil konversi mata uang
print(f"{amount} {from_currency} = {result} {to_currency}")
