from datetime import datetime as datetime, timedelta
import os
import requests


from twilio.rest import Client


BASE_URL ="https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "b9730caa166b753b108d41a1c922ee91"
CITY = "Chicoutimi"

url = BASE_URL+"appid="+API_KEY+"&q="+CITY
print (url)

response = requests.get(url).json()

temp_c = str(response['main']['temp'] - 273.15)
feel_temp_c = str(response['main']['feels_like'] - 273.15)
humidity = str(response['main']['humidity'])
description = str(response['weather'][0]['description'])
wind_speed = str(response['wind']['speed'])



account_sid = 'AC17edf098792d89f24d5308f808f59a85'
auth_token = 'a104cb9d07478452d77282af87294ab3'
client = Client(account_sid, auth_token)

send_when = datetime.utcnow() + timedelta(minutes=61)

message = client.messages.create(
                     messaging_service_sid = 'MG083c7b9ddac633e6986ceed073cbf5dc',
                     body= description + 'Temp:'+ temp_c + 'Feels like' + feel_temp_c,
                     from_='+19856038576',
                     to='+91 70202 49770',
                     schedule_type = 'fixed',
                     send_at=send_when.isoformat() + 'Z',
                 )

print(message.sid)
print("done")

#print(f"{description}")
#print(f"Temperature: {temp_c:.2f} °C")
#print(f"Feels like {feel_temp_c:.2f} °C")
#print(f"Humidity: {humidity} %")
#print(f"Wind speed: {wind_speed} m/s")

print("done")
