import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")  # Must match .env variable name

while True:
    print("**************🌦️ Welcome to the Weather App 🌦️**************")
    print("1️⃣ Get Weather")
    print("2️⃣ Exit")
    try:
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            city = input("Enter the city name: ")
            url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
            response = requests.get(url)
            
            if response.status_code == 200:
                data = response.json()

                location = data['location']
                current = data['current']
                condition = current['condition']

                print(f"\n📍 {location['name']}, {location['country']}")
                print(f"🕒 Local Time: {location['localtime']}\n")
                print(f"🌤️ Weather: {condition['text']}")
                print(f"🌡️ Temperature: {current['temp_c']}°C (Feels like: {current['feelslike_c']}°C)")
                print(f"💧 Humidity: {current['humidity']}%")
                print(f"💨 Wind: {current['wind_kph']} kph")
                print(f"🔆 UV Index: {current['uv']}\n")
            else:
                print("❌ City not found or API error.")

        elif choice == 2:
            print("👋 Goodbye!")
            break
        
        else:
            print("⚠️ Invalid choice. Please enter 1 or 2.")

    except ValueError:
        print("⚠️ Invalid input. Please enter a number.")
