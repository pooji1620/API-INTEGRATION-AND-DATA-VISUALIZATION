import requests
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

# OpenWeatherMap API Key (Replace with your actual key)
API_KEY = "990dc73be3409ee67e61dbc04f3612ca"
CITY = "Usa"

# API URL
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

try:
    # Fetch data with a timeout of 10 seconds
    response = requests.get(URL, timeout=10)
    response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
    data = response.json()
    
    # Check if API returned valid data
    if "list" not in data:
        print("Invalid response from API. Check your API key or city name.")
        exit()

    # Extract weather data
    dates = []
    temps = []
    humidity = []

    for item in data['list']:
        dt = datetime.datetime.fromtimestamp(item['dt'])
        dates.append(dt)
        temps.append(item['main']['temp'])
        humidity.append(item['main']['humidity'])

    # Create a visualization dashboard
    plt.figure(figsize=(12, 5))

    # Temperature Plot
    plt.subplot(1, 2, 1)
    plt.plot(dates, temps, marker='o', color='b', label='Temperature (°C)')
    plt.xlabel("Date-Time")
    plt.ylabel("Temperature (°C)")
    plt.title(f"Temperature Trend in {CITY}")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)

    # Humidity Plot
    plt.subplot(1, 2, 2)
    sns.lineplot(x=dates, y=humidity, marker='o', color='g', label='Humidity (%)')
    plt.xlabel("Date-Time")
    plt.ylabel("Humidity (%)")
    plt.title(f"Humidity Trend in {CITY}")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

except requests.exceptions.Timeout:
    print("Request timed out! Check your internet connection or try again later.")
except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
