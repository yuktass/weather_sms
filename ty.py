import datetime as dt
import requests


from twilio.rest import Client

BASE_URL ="https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "b9730caa166b753b108d41a1c922ee91"
CITY = "Chicoutimi"

url = BASE_URL+"appid="+API_KEY+"&q="+CITY
print (url)

response = requests.get(url).json()

temp_c = response['main']['temp'] - 273.15
feel_temp_c = response['main']['feels_like'] - 273.15
humidity = response['main']['humidity']
description = response['weather'][0]['description']
wind_speed = response['wind']['speed']

print (description)

account_sid = 'AC17edf098792d89f24d5308f808f59a85'
auth_token = 'badc269eddac42e48151da2882ce19d6'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body= '{}',
                     from_='+19856038576',
                     to='+14317266122'
                 )

print(message.sid)
print("done")

print(f"{description}")
print(f"Temperature: {temp_c:.2f} °C")
print(f"Feels like {feel_temp_c:.2f} °C")
print(f"Humidity: {humidity} %")
print(f"Wind speed: {wind_speed} m/s")

print("done")

print("hello")