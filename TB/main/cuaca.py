import requests
import json

def get_weather(api_key, city):
    base_url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    response = requests.get(base_url)
    weather_data = json.loads(response.text)
    return weather_data

def main():
    api_key = "89459012bef54833b2450712231506"  # Ganti dengan API key Weather API Anda
    city = input("Masukkan nama kota: ")
    weather_data = get_weather(api_key, city)
    
    if "error" not in weather_data:
        location = weather_data["location"]["name"]
        main_weather = weather_data["current"]["condition"]["text"]
        temperature = weather_data["current"]["temp_c"]
        humidity = weather_data["current"]["humidity"]
        wind_speed = weather_data["current"]["wind_kph"]
        
        print(f"Cuaca saat ini di {location}:")
        print(f"Kondisi cuaca: {main_weather}")
        print(f"Suhu: {temperature}°C")
        print(f"Kelembaban: {humidity}%")
        print(f"Kecepatan angin: {wind_speed} kph")
    else:
        print("Data cuaca tidak ditemukan.")

if __name__ == "__main__":
    main()
