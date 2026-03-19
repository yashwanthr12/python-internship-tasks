import requests

API_KEY = "Paste the api key"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url)
    data = response.json()

    if data["cod"] != 200:
        print("City not found")
    else:
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]

        print("Weather Information")
        print("City:", city)
        print("Temperature:", temperature, "°C")
        print("Condition:", condition)
        print("Humidity:", humidity, "%")

except Exception as e:
    print("Error occurred:", e)