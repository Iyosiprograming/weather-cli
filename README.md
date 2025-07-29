# 🌦️ Weather App (CLI) - Python

A simple command-line weather application written in Python. It fetches real-time weather data using the [WeatherAPI](https://www.weatherapi.com/) and displays the current weather, temperature, humidity, wind speed, and more!

---

## 🚀 Features

- Get current weather by city name 🌍  
- Displays temperature, humidity, wind speed, and condition ⛅  
- Easy-to-read terminal output with emojis ✨  
- Loads API key securely using `.env` file 🔐  

---

## 📦 Requirements

- Python 3.7+
- `requests`
- `python-dotenv`

Install dependencies with:

```bash
pip install -r requirements.txt
```

---

## 🔑 Setup

1. **Get your free API key** from [WeatherAPI.com](https://www.weatherapi.com/).
2. **Create a `.env` file** in the root folder:

   ```env
   API_KEY=your_api_key_here
   ```

3. **Run the app:**

   ```bash
   python weather.py
   ```

---

## 🖥️ Example Output

```text
**************🌦️ Welcome to the Weather App 🌦️**************
1️⃣ Get Weather
2️⃣ Exit
Enter your choice: 1
Enter the city name: London

📍 London, United Kingdom
🕒 Local Time: 2025-07-29 13:11

🌤️ Weather: Partly cloudy
🌡️ Temperature: 19.0°C (Feels like: 19.0°C)
💧 Humidity: 60%
💨 Wind: 12.2 kph
🔆 UV Index: 0.8
```

---

## 📁 File Structure

```
weather-app/
│
├── weather.py         # Main app
├── .env               # API key (not tracked)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 📸 Screenshot

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/767142cc-b22d-4906-a32f-63f59de362ec" />
:


---

## 📜 License

MIT License © 2025 [Iyosi](https://github.com/Iyosiprograming)
